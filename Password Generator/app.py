import random
from password_characters import WORDS, NUMBERS, SYMBOLS

password_list = []
password = ""

print("Welcome to the PyPassword Generator!")
words_number = int(
    input("How many words would you like in your password? "))
numbers_number = int(input("How many numbers would you like? "))
symbols_number = int(input("How many symbols would you like? "))

if numbers_number + symbols_number <= words_number:
    for word in range(abs(words_number - (symbols_number + numbers_number))):
        password_list += random.choice(WORDS)
    for number in range(numbers_number):
        password_list += random.choice(NUMBERS)
    for symbol in range(symbols_number):
        password_list += random.choice(SYMBOLS)

    random.shuffle(password_list)

    for word in password_list:
        password += str(word)

    print(f"Here is your Password: {password}")
else:
    print("Get out of here ASAP!!!")
