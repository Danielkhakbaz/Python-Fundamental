import random

number = random.randint(1, 100)

def check_answer(guess, number):
    if guess == number: 
        got_it_right = True
    else:
        got_it_right = False


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

shots = 10 if difficulty == "easy" else 5

print(number)

print(f"You have {shots} attempts remaining to guess the number.")

for shot in range(1, shots + 1):
    guess = int(input("Make your guess: "))

    print(check_answer(guess, number))
