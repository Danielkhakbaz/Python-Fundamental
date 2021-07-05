import random
from rockPaperScissor_art import rock, paper, scissors

def show_the_hand(choose):
    if choose == 0:
        return rock
    elif choose == 1:
        return paper
    elif choose == 2:
        return scissors

choose = int(input("What do you choose? Type 0 for Rocks, 1 for Paper or 2 for Scissors: "))

print(f"User's choice:\n{show_the_hand(choose)}")
print(f"Computer's choice:\n{show_the_hand(random.randint(0, 2))}")