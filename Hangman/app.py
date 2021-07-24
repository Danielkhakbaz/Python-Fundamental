import random
from words import WORD_LIST
from art import STAGES, LOGO

lives = 6
word = []
choosen_word = random.choice(WORD_LIST)

print(LOGO)

for _ in range(len(choosen_word)):
    word.append("_")

while lives != 0:
    if "_" not in word:
        quit()

    guess = input("Guess a letter: ").lower()

    if guess in word:
        print(f"You've already guessed {guess}.")

    for number in range(len(choosen_word)):
        if guess == choosen_word[number]:
            word[number] = guess
    if guess not in choosen_word:
        lives -= 1
        print(
            f"You guessed {guess}, That's not in the word.\nYou lose a life.\nNow you have {lives} lives.")

    print(word)
    print(STAGES[lives])

if lives == 0:
    print("You lost!")
