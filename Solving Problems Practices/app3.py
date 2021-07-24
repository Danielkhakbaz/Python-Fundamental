VOWELS = ["a", "A", "e", "E", "o", "O", "u", "U", "i", "I"]

sentence = list(input("Enter the sentence: "))

for index, letter in enumerate(sentence):
    if letter in VOWELS:
        sentence[index] = "."

print("".join(sentence).lower())
