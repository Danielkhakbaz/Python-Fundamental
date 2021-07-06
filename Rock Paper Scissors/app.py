import random
from rockPaperScissor_art import rock, paper, scissors

def show_the_hand(choose):
    """Return a image due to its condition"""
    if choose == 0:
        return rock
    elif choose == 1:
        return paper
    elif choose == 2:
        return scissors

def detect_the_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("DRAW!")
    elif computer_choice == 2 and user_choice == 0:
        print("YOU WIN!")
    elif computer_choice == 0 and user_choice == 2:
        print("YOU LOSE!")
    elif computer_choice > user_choice:
        print("YOU LOSE!")
    elif computer_choice < user_choice:
        print("YOU WIN!")
    else:
        print("YOU ENTERED AN INVALID NUMBER!")

user_choice = int(input("What do you choose? Type 0 for Rocks, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

print(f"User's choice:\n{show_the_hand(user_choice)}")
print(f"Computer's choice:\n{show_the_hand(computer_choice)}")

detect_the_winner(user_choice, computer_choice)