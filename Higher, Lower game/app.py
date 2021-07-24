import random
from art import LOGO, VS_LOGO
from data import DATA

score = 0
chose_person = {}
other_person = {}


def set_players(first_selected, second_selected, choice):
    """Return a Tuple of both choose person and not choose person"""
    if choice == "a":
        chose_person = first_selected
        other_person = second_selected
    elif choice == "b":
        chose_person = second_selected
        other_person = first_selected

    return chose_person, other_person


print(LOGO)

while True:
    first_selected = random.choice(DATA)
    second_selected = random.choice(DATA)

    print(f"Compare A: {first_selected.get('name')}, a {first_selected.get('description')} and from {first_selected.get('country')}.")
    print(VS_LOGO)
    print(f"Against B: {second_selected.get('name')}, a {second_selected.get('description')} and from {second_selected.get('country')}.")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    chose_person, other_person = set_players(
        first_selected, second_selected, choice)

    if chose_person.get("follower_count") > other_person.get("follower_count"):
        score += 1

        print(f"You're right! Current Score: {score}")
    else:
        print(f"Sorry, That's wrong! Final Score: {score}")

        quit()
