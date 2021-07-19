from questions_and_answers import QUESTIONS_AND_ANSWERS


def correct():
    global score
    score = 0

    score += 1

    return "Correct!"


def incorrect():
    return "Incorrect!"


print("! Welcome to my Computer Quiz Game !")

playing = input(
    "Do you want to play? Type 'y' for playing and 'n' to pass: ").lower()

if playing != "y":
    quit()

print("OK! Let's play!")

for QUESTION_AND_ANSWER in QUESTIONS_AND_ANSWERS:
    answer = input(QUESTION_AND_ANSWER["question"]).lower()

    if answer == QUESTION_AND_ANSWER["answer"]:
        print(correct())
    else:
        print(incorrect())

print(f"You got {score} Questions right!")
