import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
word = []
choosen_word = random.choice(word_list)

print(logo)

for _ in range(len(choosen_word)):
    word.append("_")

while lives != 0:
    if "_" not in word:
        break

    guess = input("Guess a letter: ")

    for number in range(len(choosen_word)):
        if guess == choosen_word[number]:
            word[number] = guess
    if guess not in choosen_word:
        lives -= 1
        print(f"You guessed {guess}, That's not in the word.\nYou lose a life.\nNow you have {lives} lives.")

    print(word)
    print(stages[lives])

if lives == 0:
    print("You lost!")