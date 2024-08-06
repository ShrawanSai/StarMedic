import google.generativeai as genai
from dotenv import load_dotenv
import os
import re
from actor import Actor
from game_options import OptionsLLM
from disease_reasoning import DiseaseReasoning
from fetch_dataset import get_random_disease
import random
import streamlit as st
import warnings
import time


warnings.filterwarnings("ignore")
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class SituationMaster:

  def __init__(self, patient_details, disease):
    
    if 'disease' not in st.session_state or st.session_state.disease is None:
      st.session_state.patient_details = patient_details
      st.session_state.patient_name = patient_details["name"]
      st.session_state.patient_specie = patient_details["specie"]
      st.session_state.patient_description = patient_details["description"]

      st.session_state.disease = disease
      (st.session_state.disease_name, st.session_state.symptoms, st.session_state.treatment_plan, st.session_state.major_tests_scan_results, st.session_state.other_info) = st.session_state.disease
      st.session_state.diesease_found = False
      st.session_state.score = 0
      st.session_state.attempts = 0
      st.session_state.tps_found = 0

    # Initate all initializations from the session state
    self.patient_details = st.session_state.patient_details
    self.patient_name = st.session_state.patient_name
    self.patient_specie = st.session_state.patient_specie
    self.patient_description = st.session_state.patient_description
    self.disease = st.session_state.disease
    self.disease_name = st.session_state.disease_name
    self.symptoms = st.session_state.symptoms
    self.treatment_plan = st.session_state.treatment_plan
    self.major_tests_scan_results = st.session_state.major_tests_scan_results
    self.other_info = st.session_state.other_info
    
    self.diesease_found = st.session_state.diesease_found
    self.score = st.session_state.score
    self.attempts = st.session_state.attempts
    self.tps_found = st.session_state.tps_found

    if 'actorllm' not in st.session_state or st.session_state.actorllm is None:
            st.session_state.actorllm = Actor(self.patient_name, self.patient_specie, self.patient_description)
    self.actorllm = st.session_state.actorllm

    if 'drllm' not in st.session_state or st.session_state.drllm is None:
        st.session_state.drllm = DiseaseReasoning(self.disease_name, self.symptoms, self.treatment_plan, self.major_tests_scan_results, self.other_info)
    self.drllm = st.session_state.drllm

    if 'optionsllm' not in st.session_state or st.session_state.optionsllm is None:
        st.session_state.optionsllm = OptionsLLM(self.disease_name, self.symptoms, self.treatment_plan, self.major_tests_scan_results, self.other_info)
    self.optionsllm = st.session_state.optionsllm

    
    self.initialize_session_state()

  def initialize_session_state(self):
    if 'last_message' not in st.session_state:
        st.session_state.last_message = None
    if 'selected_option' not in st.session_state:
        st.session_state.selected_option = None
    if 'response' not in st.session_state:
        st.session_state.response = None
    if 'correct_answer_reasoning' not in st.session_state:
        st.session_state.correct_answer_reasoning = None
    if 'incorrect_answers_mappings' not in st.session_state:
        st.session_state.incorrect_answers_mappings = None
    if 'randomized_options' not in st.session_state:
        st.session_state.randomized_options = None
    if 'initialized' not in st.session_state:
        st.session_state.initialized = False
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []


  def patient_says(self, message):
    drllm_response = self.drllm.ask(message)
    time.sleep(1)
    actorllm_response, dr_response = self.actorllm.talk(drllm_response)
    return actorllm_response, dr_response

  def clean_text(self, input_string):
    parts = re.split(r'\(.*\)', input_string)
    result = parts[0].strip()
    result = re.sub(r'^\s*\d+\.\s*', '', result)
    result = re.sub(r'\s*\d+\s*$', '', result)
    return result.strip()

  def extract_option_reasoning(self, choices):
    choices = choices.splitlines()

    correct_answer = choices[0]
    incorrect_answers = choices[1:]

    extract_parenthesis = lambda s: re.findall(r'\(.*?\)', s)[-1][1:-1] if re.findall(r'\(.*?\)', s) else None

    reason_for_correct_answer = extract_parenthesis(correct_answer)
    if reason_for_correct_answer is None:
      reason_for_correct_answer = ""
    if self.disease_name.lower() in reason_for_correct_answer.lower():
      reason_for_correct_answer = reason_for_correct_answer.replace(self.disease_name.lower(), "XXX disease")
      reason_for_correct_answer = reason_for_correct_answer.replace(self.disease_name.capitalize(), "XXX disease")
    correct_answer_reasoning = {self.clean_text(correct_answer): reason_for_correct_answer}

    incorrect_answers_mappings = {self.clean_text(incorrect_answer): extract_parenthesis(incorrect_answer) for incorrect_answer in incorrect_answers}

    for i in incorrect_answers_mappings:
      if incorrect_answers_mappings[i] is None:
        incorrect_answers_mappings[i] = ""
      if self.disease_name.lower() in incorrect_answers_mappings[i].lower():
        incorrect_answers_mappings[i] = incorrect_answers_mappings[i].replace(self.disease_name.lower(), "XXX disease")
        incorrect_answers_mappings[i] = incorrect_answers_mappings[i].replace(self.disease_name.capitalize(), "XXX disease")

    randomized_options = [self.clean_text(correct_answer)] + list(incorrect_answers_mappings.keys())
    random.shuffle(randomized_options)

    return randomized_options, correct_answer_reasoning, incorrect_answers_mappings

  def start_game_streamlit(self):
    st.title("Medical Diagnosis Game")
    st.header(f"Patient Name: {self.patient_name}")
    st.subheader("Your score: " + str(st.session_state.score))
    if st.session_state.diesease_found:
      st.subheader("Disease Found: " + self.disease_name)
    if not st.session_state.initialized:
        st.session_state.initialized = True
        st.session_state.last_message = "Hello. What seems to be the problem?"
        st.session_state.response, st.session_state.dr_response = self.patient_says(st.session_state.last_message)
        choices = self.optionsllm.ask(st.session_state.response, self.drllm.get_history())
        st.session_state.randomized_options, st.session_state.correct_answer_reasoning, st.session_state.incorrect_answers_mappings = self.extract_option_reasoning(choices)
        st.session_state.conversation_history.append(f"<span style='color:blue;'><strong>You:</strong> 🩺 : {st.session_state.last_message}</span>")
        st.session_state.conversation_history.append(f"<span style='color:green;'><strong>Patient:</strong> 🤒 : {st.session_state.response}</span>")
        if st.session_state.dr_response:
            st.session_state.conversation_history.append(f"<span style='background-color:lightgray; color:black;'><strong>{st.session_state.dr_response}</strong></span>")

    col1, col2, col3 = st.columns([2, 0.1, 3])

    with col1:
        if st.session_state.dr_response:
            if "FOUND DISEASE" in st.session_state.dr_response:
                st.session_state.diesease_found = True
                st.session_state.score += 500
            if "FOUND TP" in st.session_state.dr_response:
                st.session_state.tps_found += 1
                st.session_state.score += 100
            if st.session_state.diesease_found:
                st.success("Disease Found!")
            if st.session_state.tps_found >= 2 and st.session_state.diesease_found:
                st.success("Winner! You have found the disease and the treatment plans!")
            if st.session_state.score >1000:
                st.success("Winner! You have found the disease and the treatment plans!")
            st.markdown(f"<span style='background-color:lightgray; color:black;'><strong>{st.session_state.dr_response}</strong></span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color:green;'><strong>Patient:</strong> 🤒 : {st.session_state.response}</span>", unsafe_allow_html=True)

        selected_option = st.radio("Choose your response:", st.session_state.randomized_options, key='options_radio')

        if st.button("Submit", key='submit_button'):
            input_message = selected_option
            st.markdown(f"<span style='color:blue;'><strong>You:</strong> 🩺 : {input_message}</span>", unsafe_allow_html=True)

            if input_message in st.session_state.correct_answer_reasoning:
                feedback = f"<span style='background-color:yellow; color:black;'>Correct! {st.session_state.correct_answer_reasoning[input_message]}</span>"
                prompt_for_drllm = input_message + "\n" + st.session_state.correct_answer_reasoning[input_message]
                st.session_state.score += 10
                st.markdown(feedback, unsafe_allow_html=True)
            else:
                correct_answer = list(st.session_state.correct_answer_reasoning.keys())[0]
                correct_reasoning = st.session_state.correct_answer_reasoning[correct_answer]
                feedback = f"<span style='background-color:yellow; color:black;'>That is not exactly right! {st.session_state.incorrect_answers_mappings[input_message]}</span>"
                correct_feedback = f"<span style='background-color:orange; color:black;'>The correct answer was: {correct_answer}. {correct_reasoning}</span>"
                st.markdown(feedback, unsafe_allow_html=True)
                st.markdown(correct_feedback, unsafe_allow_html=True)
                prompt_for_drllm = input_message + "\n" + st.session_state.incorrect_answers_mappings[input_message]

            # Update the conversation history
            st.session_state.conversation_history.append(f"<span style='color:blue;'><strong>You:</strong> 🩺 : {input_message}</span>")
            st.session_state.conversation_history.append(feedback)
            if 'correct_feedback' in locals():
                st.session_state.conversation_history.append(correct_feedback)

            # Update the session state with the latest message
            st.session_state.last_message = prompt_for_drllm
            st.session_state.response, st.session_state.dr_response = self.patient_says(st.session_state.last_message)

            # Generate new options based on the updated state
            choices = self.optionsllm.ask(st.session_state.response, self.drllm.get_history())
            st.session_state.randomized_options, st.session_state.correct_answer_reasoning, st.session_state.incorrect_answers_mappings = self.extract_option_reasoning(choices)

            # Update conversation history with the patient's new response
            if st.session_state.dr_response:
                st.session_state.conversation_history.append(f"<span style='background-color:lightgray; color:black;'><strong>{st.session_state.dr_response}</strong></span>")
            st.session_state.conversation_history.append(f"<span style='color:green;'><strong>Patient:</strong> 🤒 : {st.session_state.response}</span>")

            # Clear radio button selection to allow for new options to be selected
            st.session_state.selected_option = None

            # Rerun the app to refresh the state
            st.experimental_rerun()

    with col3:
        st.subheader("Conversation History")
        for message in st.session_state.conversation_history:
            st.markdown(message, unsafe_allow_html=True)





if __name__ == "__main__":


  def get_random_patient():
      patients = [
          {
              "name": "Elara Vendarian",
              "specie": "Naboo",
              "description": """Elara Vendarian, a Naboo from the Star Wars world, despite her impressive intellect and self-assured demeanor, is a challenging patient when it comes to medical visits. When visiting a doctor, she tends to overanalyze her symptoms, often diagnosing herself before the medical professionals have a chance. Her confidence can come across as dismissive or even condescending, as she believes she knows best about her own health.

  When Elara is injured or in pain, her usually composed facade crumbles. She becomes extremely sensitive and vocal about her discomfort, frequently expressing her distress with dramatic flair. Small injuries feel catastrophic to her, and she doesn't hesitate to make her suffering known. Her pain tolerance is notably low, and she requires a great deal of reassurance and gentle handling from the medical staff.

  During periods of depression, Elara's usual confidence is replaced with a profound sense of vulnerability. She becomes introspective and withdrawn, struggling with feelings of inadequacy and self-doubt. Her sharp mind turns against her, as she fixates on her perceived failures and weaknesses. In these moments, she needs compassionate care and patience, as her typical resilience is overshadowed by her emotional turmoil.

  Overall, Elara's interactions with healthcare providers are marked by a mix of intellectual assertiveness and emotional fragility. Her high sensitivity to pain and tendency to vocalize her discomfort require a delicate balance of firm guidance and empathetic support from the medical team."""
          },
          {
              "name": "Taryn Raeth",
              "specie": "Corellian",
              "description": """Taryn Raeth, a Corellian from the Star Wars universe, is a practical and straightforward individual. As a patient, Taryn is cooperative but has a tendency to downplay symptoms, often considering them trivial. This can lead to delayed diagnoses as he prefers to 'tough it out' rather than seek immediate medical attention.

  When in pain, Taryn tries to maintain his composure and often uses humor as a coping mechanism. He has a moderate pain tolerance but is not overly expressive about his discomfort. He appreciates clear and direct communication from medical staff and values efficiency in his treatment.

  During periods of depression, Taryn becomes unusually quiet and reserved, retreating into himself. He struggles with asking for help and tends to isolate himself. In these times, he benefits from a proactive approach by healthcare providers, who can offer consistent support and encouragement.

  Overall, Taryn's interactions with healthcare providers are generally positive, as long as his tendency to minimize symptoms is addressed. He values professionalism and appreciates a no-nonsense approach to his care."""
          },
          {
              "name": "Liora Melane",
              "specie": "Alderaanian",
              "description": """Liora Melane, hailing from Alderaan, carries the grace and poise typical of her people. However, she is also known for her meticulous nature and a strong preference for understanding every detail of her medical care. As a patient, Liora is highly engaged and asks numerous questions, seeking to be an active participant in her treatment plan.

  In times of pain, Liora remains composed but is very precise about describing her symptoms. She has a high pain tolerance and prefers to endure discomfort silently rather than show vulnerability. She respects medical expertise but needs thorough explanations to feel comfortable with her care.

  When depressed, Liora becomes withdrawn and can appear aloof. She internalizes her struggles and finds it hard to open up, even to those closest to her. Supportive and gentle coaxing is required from her healthcare team to help her express her feelings and accept help.

  Liora's interactions with healthcare providers are marked by her desire for thorough understanding and clear communication. She appreciates a collaborative approach and values detailed, patient-centered care."""
          },
          {
              "name": "Dax Tenor",
              "specie": "Human",
              "description": """Dax Tenor, a human from the bustling cityscape of Coruscant, is a dynamic and assertive individual. In medical settings, Dax can be impatient and demanding, often pushing for quick solutions and immediate results. His confidence sometimes borders on arrogance, making him a challenging patient for healthcare providers.

  When in pain, Dax is very vocal and insistent on immediate relief. He has a low pain threshold and is not hesitant to express his discomfort. He prefers aggressive treatment options and quick fixes, often questioning and challenging medical advice.

  During depressive episodes, Dax's usually vibrant personality dims significantly. He becomes irritable and withdrawn, struggling with feelings of frustration and helplessness. In these times, he needs a firm yet compassionate approach to help him navigate his emotions and engage in his treatment.

  Dax's interactions with healthcare providers require a balance of assertiveness and empathy. He responds well to clear, decisive communication and appreciates a proactive approach to his care."""
          },
          {
              "name": "Mira Talon",
              "specie": "Togruta",
              "description": """Mira Talon, a Togruta from the planet Shili, is a resilient and independent individual. In medical situations, Mira tends to be stoic and prefers to handle her discomfort privately. She has a high pain tolerance and rarely complains, even when experiencing significant symptoms.

  When in pain, Mira remains calm and composed, often underreporting her level of discomfort. She values traditional healing methods and prefers natural remedies whenever possible. She respects medical professionals but is somewhat skeptical of invasive procedures and medications.

  During periods of depression, Mira becomes introspective and seeks solitude. She struggles with expressing her emotions and can appear detached. She benefits from a patient and understanding approach, with healthcare providers who respect her need for space while offering consistent support.

  Mira's interactions with healthcare providers are characterized by her preference for non-invasive treatments and her high level of independence. She appreciates a respectful and considerate approach to her care, with an emphasis on holistic and natural methods."""
          }
      ]

      patient = random.choice(patients)
      patient_details = {
          "name": patient["name"],
          "specie": patient["specie"],
          "description": patient["description"]
      }

      return patient_details

  # Example usage
  patient_details = get_random_patient()
  # print(random_patient)

  disease = get_random_disease()

  situation1 = SituationMaster(patient_details, disease)

  st.set_page_config(page_title="Medical Diagnosis Game")
  situation1.start_game_streamlit()
