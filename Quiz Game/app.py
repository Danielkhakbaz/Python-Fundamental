from questions_and_answers import QUESTIONS_AND_ANSWERS


def correct():
    """Return a string which is 'Correct!' to show the user that he got the right answer! and also this function adds the score variable's value based on correct answers"""
    global score
    score = 0

    score += 1

    return "Correct!"


def incorrect():
    """Return a string which is 'Correct!' to show the user that he did not get the right answer!"""

    return "Incorrect!"


print("! Welcome to my Computer Quiz Game !")

playing = input(
    "Do you want to play? Type 'y' for playing and 'n' to pass: ").lower()

if playing != "y":
    quit()

print("OK! Let's play!")

for QUESTION_AND_ANSWER in QUESTIONS_AND_ANSWERS:
    answer = input(QUESTION_AND_ANSWER.get("question")).lower()

    if answer == QUESTION_AND_ANSWER.get("answer"):
        print(correct())
    else:
        print(incorrect())

print(f"You got {score} Questions right!")
