import random
from art import LOGO

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

choice = "y"
user_cards = []
dealer_cards = []


def game_detector():
    """
    Show the result of the game based on the cards.

    Returns:
    str: The situation of the game as a string
    """

    if sum(user_cards) == sum(dealer_cards):
        return "! DRAW !"
    elif (sum(dealer_cards) > 21) or (sum(user_cards) > sum(dealer_cards)) or (sum(user_cards) == 21):
        return "! WIN !"
    elif (sum(user_cards) < sum(dealer_cards)) or (sum(dealer_cards) == 21):
        return "! LOSE !"


for _ in range(2):
    user_cards.append(random.choice(CARDS))
    dealer_cards.append(random.choice(CARDS))

print(LOGO)
print(f"Your cards: {user_cards} -> {sum(user_cards)}")
print(f"Dealer's first card: {dealer_cards[0]}")

while choice == "y":
    if sum(user_cards) == 21:
        print("! BLACKJACK !")

        quit()

    choice = input(
        "Type 'y' to get another card, type 'n' to pass on it: ").lower()

    while (choice == "y") or (choice == "n"):
        if choice == "y":
            user_cards.append(random.choice(CARDS))

            print(f"Your cards: {user_cards} -> {sum(user_cards)}")

            if sum(user_cards) > 21:
                print("! LOSE !")

                quit()
            elif sum(user_cards) == 21:
                print("! BLACKJACK !")

                quit()
        else:
            while sum(dealer_cards) < 17:
                dealer_cards.append(random.choice(CARDS))

            print(f"Dealer's cards: {dealer_cards}")

            print(game_detector())

            quit()

    print("You entered an unvalid choice!")
