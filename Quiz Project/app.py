from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

import time

start_time = time.time()

question_bank = []

for q_a in question_data:
    question_bank.append(Question(q_a.get("question"), q_a.get("answer")))

qb = QuizBrain(question_bank)

while qb.still_has_questions():
    print(qb.next_question())

print("- + - + - + - + - + - + - + - + - + ")
print("You've completed the Quiz!")
print(f"Your final score was: {qb.correct_answers}/{len(question_bank)}")

print("--- %s seconds ---" % (time.time() - start_time))