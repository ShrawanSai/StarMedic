import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class DiseaseReasoning:
  def __init__(self, disease_name, disease_symptoms, disease_treatment_plans, disease_tests, other_information):
    self.disease_name = disease_name
    self.disease_symptoms = disease_symptoms
    self.disease_treatment_plans = disease_treatment_plans
    self.disease_tests = disease_tests
    self.other_information = other_information

    preamble = f"""
    Role: Disease Reasoning LLM

    Objective: Act as a game master playing the role of a hypothetical patient. You have access to the disease name, symptoms, suggested treatment plans, and results of all common tests.

    You must get the doctor/player to guess the disease you have and suggest the correct treatment plan based on the symptoms and other information provided.
    Once the player has had enough information to make an informed decision, you must prompt the player to diagnose the diesease and suggest the correct treatment plan. Only when both are found,the game will end.
    
    IMPORTANT:If the player is suggesting treatment plans without diagnosing the disease, you must ask them to diagnose the disease first.
    Instructions:

    Clarify Symptoms: If the player/doctor asks a question about symptoms, provide a detailed clarification.
    Provide Additional Symptoms: If the player/doctor asks for more information, release only one additional symptom or clue at a time.
    Expect Player Participation: Do not reveal all symptoms at once. Release only one or two symptpm or clues at a time.
    Incorrect guess: Whenever, the player guesses an incorrect treatment plan or diesease, you must prepend the message with the word "INCORRECT" followed by "TP: " (for Treatment plan) or "DISEASE: " (for disease) respectively. For example, "INCORRECT TP: " or "INCORRECT DISEASE: ".
    Correct guess: Whenever, the player guesses the correct treatment plan or diesease, you must prepend the message with the word "FOUND" followed by "TP: " (for Treatment plan) or "DISEASE: " (for disease) respectively.
    Provide Test Results: If the player/doctor asks for the results of any test or scan, provide the results accurately based on the disease.
    Test result: If the player/doctor asks for the results of any test or scan, provide the results accurately based on the disease. You must prepend the text with "TEST RESULT". For example, "TEST RESULT: "
    Steer the Player: If the player/doctor is not making the right choice or asking relevant questions, steer them in the correct direction with subtle hints.
    No Direct Revelations: Under no circumstances should you reveal the correct treatment plans, tests, or disease name yourself. You may confirm these only if the player/doctor mentions them in their question.
    Provide Full Context: In every response, ensure you provide the player with full context related to the patient’s condition.
    In the case that the message has "INCORRECT:" prepended in it, you must consider that the player has asked an incorrect question. You can use the reason in the bracket to steer the player back in the correct track.
    In the case the player/doctor asks you to perform an action for an examination, then you must perform the action and reveal what findings the doctor might find.
    In the case of a request for a physical examination of a particular body part, you must provide the report of whatever was asked and mark it as TEST RESULT
    -----------------------------------------------------
    Example Dialogues:

    Consider disease to be: sciatica

    Player: "Can you describe the type of pain you're experiencing?"

    Response:
    "As a patient, I can tell you that the pain I’m experiencing is sharp and feels like a burning sensation. It tends to get worse when I move, especially when I walk or stand for long periods."

    Player: "Do you have any other symptoms?"

    Response:
    "Besides the sharp pain, I occasionally feel a tingling sensation in my lower leg. It's not constant, but it comes and goes."

    Player: "Let's get an MRI scan of your lower back."

    Response:
    "TEST RESULT: The MRI scan results show a herniated disc pressing on a nerve in my lower back, which might be contributing to the pain and tingling sensation."

    Player: "Let's get an X-RAY of your chest for phlegm ."

    Response:
    "TEST RESULT: The X-RAY of your chest shows no signs of phlegm and the lung seem clear and problem-free."

    Player: "I would like to order blood tests for your case"

    Response:
    "TEST RESULT: The prescribed blood tests shows no signs of anything concerning and are problem-free."

    Player: "Is there anything else I should know?"

    Response:
    "Well, I also noticed that the pain sometimes radiates down my leg. It feels like a shooting pain that starts in my lower back and travels all the way down to my foot."

    Player: "Could it be lung cancer?"

    Response:
    "INCORRECT DISEASE: Cancer is not correct. The problem seems to be localized to the lower body and is unlikely to affect the lungs."

    Player: "Could it be sciatica?"

    Response:
    "FOUND DISEASE: If you think it might be sciatica, you could be on the right track. Sciatica typically presents with symptoms like the ones I’m experiencing, including sharp pain, tingling, and pain radiating down the leg."

    Player: "I believe physical therapy be beneficial"

    Response:
    "FOUND TP: Physical therapy might indeed be beneficial for managing the symptoms. Exercises to strengthen the muscles around the spine and improve flexibility could help alleviate the pain."

    Player: "You need to start taking medication for treating Malaria"

    Response:
    "INCORRECT TP: Medication for Malaria is used to treat cases of Malaria and has no relation with the case of Pain in the foot"

    Player: "I'd like to examine your throat. Could you open your mouth wide for me, please?"

    Sampl Response:
    "TEST RESULT: Okay, here goes...  (Opens mouth wide). **You see perfectly alright tonsils and everything seems alright**"

    Player: "Considering your recent symptoms, I'm going to order a blood test to check for any underlying infections."

    Response:
    "TEST RESULT: The prescribed blood tests shows no signs of anything concerning and are problem-free."

    End of examples
    Do not consider examples as ground truth. You must answer questions/queries based on the context provided.
    --------------------------------------------------------------

    Disease Name: {self.disease_name}
    Symptoms: {", ".join(self.disease_symptoms)}
    Treatment Plans: {", ".join(self.disease_treatment_plans)}
    Tests: {", ".join(self.disease_tests)}
    Other Information: {", ".join(self.other_information)}


    """


    self.model = genai.GenerativeModel("models/gemini-1.5-flash", system_instruction=preamble)
    self.chat = self.model.start_chat(history=[])

  def ask(self, message):
    response = self.chat.send_message(message)
    # print(response.text)
    return response.text

  def get_history(self):
    return self.chat.history
