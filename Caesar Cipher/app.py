from alphabet import ALPHABET
from art import LOGO

again = "yes"


def encrypt_and_decrypt(message, shift_number):
    """
    Convert the plain text to a coded text with the use of shift_number.

    Parameters:
    message (str): The text that is going to be coded
    shift_number (num): A number of moving characters in our coded text

    Returns:
    str: A coded string based on the user's want
    """

    code = "".join([ALPHABET[ALPHABET.index(
        letter) + shift_number] if choice == "encode" else ALPHABET[ALPHABET.index(letter) - shift_number] for letter in message if letter])

    return code


print(LOGO)

while again == "yes":
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

    if (choice != "encode") and (choice != "decode"):
        break

    message = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number: "))

    print(
        f"Here is the {choice}d result: {encrypt_and_decrypt(message, shift_number)}.")

    again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no': ").lower()

if again == "no":
    quit()

print("You entered a unvalid choice!")
