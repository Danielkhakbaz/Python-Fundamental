import random
from art import logo

user_cards = []
computer_cards = []

print(logo)

for _ in range(2):
    user_cards.append(random.randint(1, 10))
    computer_cards.append(random.randint(1, 10))

print(f"Your cards: {user_cards}")
print(f"Computer's first card: {computer_cards[0]}")