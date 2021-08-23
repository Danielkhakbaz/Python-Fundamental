import random
from art import LOGO, VS_LOGO
from data import DATA

score = 0
choosen_person = {}
other_person = {}


def set_players(first_selected: dict, second_selected: dict, choice: str) -> tuple:
    """
    Return a Tuple of both choosed instagram user and not choosed instagram user.

    Parameters: 
    first_selected (dict): a Directory of a randomly choosen instagram user as the first user
    second_selected (dict): a Directory of a randomly choosen instagram user as the second user
    choice (str): a Choice that the user make depending on their knowledge

    Returns
    tup: a Tuple of both choosen instagram user and not choosen instagram user
    """

    choosen_person = first_selected if choice == "a" else second_selected
    other_person = second_selected if choice == "a" else first_selected

    return choosen_person, other_person


print(LOGO)

while True:
    first_selected = random.choice(DATA)
    second_selected = random.choice(DATA)

    print(f"Compare A: {first_selected.get('name')}, a {first_selected.get('description')} and from {first_selected.get('country')} with {first_selected.get('follower_count')} followers.")
    print(VS_LOGO)
    print(f"Against B: {second_selected.get('name')}, a {second_selected.get('description')} and from {second_selected.get('follower_count')} with {second_selected.get('follower_count')} followers.")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    choosen_person, other_person = set_players(
        first_selected, second_selected, choice)

    if choosen_person.get("follower_count") > other_person.get("follower_count"):
        score += 1

        print(f"You're right! Current Score: {score}")
    else:
        print(f"Sorry, That's wrong! Final Score: {score}")

        quit()
