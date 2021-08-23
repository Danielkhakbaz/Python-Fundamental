import random
from words import WORD_LIST
from art import STAGES, LOGO

lives = 6
word = []
CHOOSEN_WORD = random.choice(WORD_LIST)

print(LOGO)

for _ in enumerate(CHOOSEN_WORD):
    word.append("_")

while lives != 0:
    if "_" not in word:
        print("You win!")

        quit()

    guess = input("Guess a letter: ").lower()

    if guess in word:
        print(f"You've already guessed {guess}.")

        lives -= 1

    for index, number in enumerate(CHOOSEN_WORD):
        if guess == CHOOSEN_WORD[index]:
            word[index] = guess

    if guess not in CHOOSEN_WORD:
        lives -= 1

        print(
            f"You guessed {guess}, That's not in the word.\nYou lose a life.\nNow you have {lives} lives.")

    print(word)
    print(STAGES[lives])

print("You lost!")
