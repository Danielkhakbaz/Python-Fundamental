from resources import resources

is_on = True

while is_on:
    choice = input("What would you like? (espresso, latte, cappuccino): ")

    if choice == "off":
        is_on = False

    if choice == "report":
        print(f"""Water: {resources.get("water")}ml
Milk: {resources.get("milk")}ml
Coffee: {resources.get("coffee")}g
Money: ${0}""")