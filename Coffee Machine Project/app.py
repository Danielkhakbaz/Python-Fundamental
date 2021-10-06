from resources import resources
from menu import MENU

is_on = True
is_it_sufficient = []
menu = ["espresso", "latte", "cappuccino"]

while is_on:
    choice = input("What would you like? (espresso, latte, cappuccino): ")

    if (choice == "off") or (choice not in menu) and (choice != "report"):
        is_on = False

    if choice == "report":
        print(
            f"Water: {resources.get('water')}ml\nMilk: {resources.get('milk')}ml\nCoffee: {resources.get('coffee')}g\nMoney: ${0}")

    if choice in menu:
        ingredients = list(MENU.get(choice).get('ingredients').keys())

        for item_ingredient in ingredients:
            is_it_sufficient.append(resources.get(item_ingredient) >= MENU.get(
                choice).get('ingredients').get(item_ingredient))

        # Check the ingredients if they are sufficient to make different type of coffee
        for item_menu in ingredients:
            if all(is_it_sufficient):
                resources[item_menu] = resources.get(
                    item_menu) - MENU.get(choice).get('ingredients').get(item_menu)
            else:
                print(f"Sorry there is not enough {item_menu.capitalize()}.")

                is_on = False
