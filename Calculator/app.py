OPERATORS = ["+", "-", "*", "/"]

to_be_continue = True


def calculate(first_number, operation, second_number):
    """Returns the result of operated numbers"""
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number


first_number = int(input("Enter the first number: "))

while to_be_continue:
    for operator in OPERATORS:
        print(operator)

    operation = input("Pick an operation: ")

    second_number = int(input("Enter the second number: "))

    print(f"{first_number} {operation} {second_number} = {calculate(first_number, operation, second_number)}")

    if input(f"Type 'y' to continue calculating with {calculate(first_number, operation, second_number)}, or type 'n' to start a new calculation: ").lower() == "y":
        first_number = calculate(first_number, operation, second_number)
    else:
        to_be_continue = False
