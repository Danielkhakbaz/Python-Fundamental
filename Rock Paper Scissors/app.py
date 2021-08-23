import random
from rockPaperScissor_art import ROCK, PAPER, SCISSORS


def show_the_hand(choose: int) -> str:
    """
    Return a image based on the user's choice(0 for rock, 1 for paper and 2 for scissors).

    Parameters:
    choose (num): A number which we asked user to enter

    Returns
    str: The right image based on the user's choice
    """

    if choose == 0:
        return ROCK
    elif choose == 1:
        return PAPER
    elif choose == 2:
        return SCISSORS


def detect_the_winner(user_choice: int, computer_choice: int) -> str:
    """
    Return a string for specifying the situation of the game(Draw, Win and Lose).

    Parameters:
    user_choice (num): a Number user entered based on their intrest between 0 and 2
    computer_choice (num): a Number which was maufactored randomly with random module

    Returns
    str: a String that shows us the final result of the game
    """

    if user_choice == computer_choice:
        return "DRAW!"
    elif (computer_choice == 2) and (user_choice == 0):
        return "YOU WIN!"
    elif (computer_choice == 0) and (user_choice == 2):
        return "YOU LOSE!"
    elif computer_choice > user_choice:
        return "YOU LOSE!"
    elif computer_choice < user_choice:
        return "YOU WIN!"
    else:
        return "YOU ENTERED AN INVALID NUMBER!"


user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

computer_choice = random.randint(0, 2)

print(f"User's choice:\n{show_the_hand(user_choice)}")
print(f"Computer's choice:\n{show_the_hand(computer_choice)}")

print(detect_the_winner(user_choice, computer_choice))
