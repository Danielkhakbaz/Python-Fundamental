import random

NUMBER = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

shots = 10 if difficulty == "easy" else 5

for shot in range(shots):
    print(f"You have {shots} attempts remaining to guess the number.")

    guess = int(input("Make your guess: "))

    if guess == NUMBER:
        print("GOT IT!")

        quit()
    elif guess > NUMBER:
        print("HIGH")
    else:
        print("LOW")

    shots -= 1
