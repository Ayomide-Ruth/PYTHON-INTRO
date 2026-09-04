rom quiz_data import get_questions
import random, datetime

quiz_questions = get_questions()

print(quiz_questions)

print("=" * 40)
random.shuffle(quiz_questions)
print(quiz_questions)

questions_only = []
answers_only = []
user_response = []

for question in quiz_questions:
    print(question[0])
    questions_only.append(question[0])
    answers_only.append(question[1])

print(questions_only)
print(answers_only)

def ask(question):
    response = input(f"{question}:")
    return response
    print(response)  


while True:
    for quiz in questions_only:
        answer = ask(quiz)
        user_response.append(answer)
        #print(answer)

    break