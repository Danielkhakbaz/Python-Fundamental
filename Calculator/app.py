OPERATORS = ["+", "-", "*", "/"]

again = "y"


def calculate(first_number: float, operation: str, second_number: float) -> float:
    """
    Calculate the numbers based on the operation which user entered.

    Parameters: 
    first_number (num): The first number which is going to be calculated
    operation (str): The operation that user enter based on their needs
    second_number (num): The second number which is going to be calculated

    Returns
    num: The result of the operated numbers
    """

    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number


first_number = int(input("Enter the first number: "))

while again == "y":
    for operator in OPERATORS:
        print(operator)

    operation = input("Pick an operation: ")

    if operation not in OPERATORS:
        break

    second_number = int(input("Enter the second number: "))

    print(f"{first_number} {operation} {second_number} = {calculate(first_number, operation, second_number)}")

    again = input(
        f"Type 'y' to continue calculating with {calculate(first_number, operation, second_number)}, or type 'n' to stop the calculator: ").lower()

    if again == "y":
        first_number = calculate(first_number, operation, second_number)

if again == "n":
    quit()

print("You entered an unvalid choice!")
