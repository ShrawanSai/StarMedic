import re

def clean_text(input_string):
    parts = re.split(r'\(.*\)', input_string)
    result = parts[0].strip()
    result = re.sub(r'^\s*\d+\.\s*', '', result)
    result = re.sub(r'\s*\d+\s*$', '', result)
    return result.strip()


choices = """1. "Have you noticed any swollen glands in your neck? (Swollen lymph nodes are a common symptom of strep throat, which can cause a sore throat.)"
2. "Can you tell me about your recent diet? (While diet is unlikely to be the direct cause of the sore throat, understanding the patient's dietary habits can provide useful information for diagnosis.)"
3. "I recommend a complete blood count to check for any signs of infection. (While a complete blood count can be useful, it's not the most specific test for strep throat.)"
4. "I'm going to need to perform a full physical examination, including a neurological assessment, to rule out any underlying conditions. (A neurological assessment is not typically necessary for a sore throat, and this suggestion is not relevant to the current symptoms.)" 
"""

choices = choices.splitlines()

correct_answer = choices[0]
incorrect_answers = choices[1:]

extract_parenthesis = lambda s: re.findall(r'\(.*?\)', s)[-1][1:-1] if re.findall(r'\(.*?\)', s) else None

reason_for_correct_answer = extract_parenthesis(correct_answer)
print('yeehaw')
print(correct_answer)
print(reason_for_correct_answer)
print('-----------------')
if reason_for_correct_answer is None:
    reason_for_correct_answer = ""

correct_answer_reasoning = {clean_text(correct_answer): reason_for_correct_answer}

incorrect_answers_mappings = {clean_text(incorrect_answer): extract_parenthesis(incorrect_answer) for incorrect_answer in incorrect_answers}

for i in incorrect_answers_mappings:
    if incorrect_answers_mappings[i] is None:
        incorrect_answers_mappings[i] = ""


randomized_options = [clean_text(correct_answer)] + list(incorrect_answers_mappings.keys())

print(randomized_options)

for i in incorrect_answers_mappings:
    print(i,": ", incorrect_answers_mappings[i])

for i in correct_answer_reasoning:
    print(i,": ",  correct_answer_reasoning[i])