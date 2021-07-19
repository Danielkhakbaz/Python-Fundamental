import random
from art import logo

choice = "y"
game_is_over = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

user_cards = []
dealer_cards = []

for _ in range(2):
    user_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

print(logo)
print(f"Your cards: {user_cards} -> {sum(user_cards)}")
print(f"Dealer's first card: {dealer_cards[0]}")

while (not game_is_over) and (choice == "y"):
    choice = input(
        "Type 'y' to get another card, type 'n' to pass on it: ").lower()

    if choice == "y":
        user_cards.append(random.choice(cards))

        print(f"Your cards: {user_cards} -> {sum(user_cards)}")

        if sum(user_cards) > 21:
            print("! LOSE !")
            break
    else: