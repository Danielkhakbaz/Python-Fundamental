import random
from art import logo

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
choice = "y"
game_is_over = False
user_cards = []
dealer_cards = []


def game_detector():
    """Return the result of the game based of the cards"""
    if sum(user_cards) == sum(dealer_cards):
        return "! DRAW !"
    elif (sum(dealer_cards) > 21) or (sum(user_cards) > sum(dealer_cards)) or (sum(user_cards) == 21):
        return "! WIN !"
    elif (sum(user_cards) < sum(dealer_cards)) or (sum(dealer_cards) == 21):
        return "! LOSE !"


for _ in range(2):
    user_cards.append(random.choice(CARDS))
    dealer_cards.append(random.choice(CARDS))

print(logo)
print(f"Your cards: {user_cards} -> {sum(user_cards)}")
print(f"Dealer's first card: {dealer_cards.get[0]}")

while (not game_is_over) and (choice == "y"):
    if sum(user_cards) == 21:
        print("! BLACKJACK !")
        break

    choice = input(
        "Type 'y' to get another card, type 'n' to pass on it: ").lower()

    if choice == "y":
        user_cards.append(random.choice(CARDS))

        print(f"Your cards: {user_cards} -> {sum(user_cards)}")

        if sum(user_cards) > 21:
            print("! LOSE !")
            break
        elif sum(user_cards) == 21:
            print("! BLACKJACK !")
            break
    else:
        while sum(dealer_cards) < 17:
            dealer_cards.append(random.choice(CARDS))

        print(f"Dealer's cards: {dealer_cards}")

        print(game_detector())
