import random

feedback = ""
low = 1

high = int(input("Enter the maximum number inside your mind: "))

while feedback != "c":
    guessed_number = random.randint(low, high)

    feedback = input(
        f"Is {guessed_number} too high(H), too low(L) or correct(C)? ").lower()

    if feedback == "h":
        high = guessed_number - 1
    elif feedback == "l":
        low = guessed_number + 1

print(f"Yaay, Your number was {guessed_number}.")
