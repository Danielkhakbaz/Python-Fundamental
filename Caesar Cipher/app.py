from alphabet import alphabet
from art import logo

again = "yes"


def encrypt_and_decrypt(message, shift_number):
    """Return a coded string based on the user's want"""
    code = ""

    for letter in message:
        code += alphabet[alphabet.index(
            letter) + shift_number] if choice == "encode" else alphabet[alphabet.index(letter) - shift_number]

    return code


print(logo)

while (again == "yes") or (not "no"):
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

    if (choice != "encode") and (choice != "decode"):
        break

    message = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number: "))

    print(
        f"Here is the {choice}d result: {encrypt_and_decrypt(message, shift_number)}.")

    again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
