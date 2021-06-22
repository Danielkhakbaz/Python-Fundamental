import random

password_list = []
password = ""

words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
         "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
words_number = int(
    input("How many words would you like in your password? "))
numbers_number = int(input("How many numbers would you like? "))
symbols_number = int(input("How many symbols would you like? "))

if numbers_number + symbols_number <= words_number:
    for word in range(abs(words_number - (symbols_number + numbers_number))):
        password_list += random.choice(words)
    for number in range(numbers_number):
        password_list += random.choice(numbers)
    for symbol in range(symbols_number):
        password_list += random.choice(symbols)

    random.shuffle(password_list)

    for word in password_list:
        password += str(word)

    print(f"Here is your Password: {password}")
else:
    print("Get out of here ASAP!!!")
