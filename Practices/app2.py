sentence_length = 0

sentence = input("Enter the sentence: ")

for letter in sentence:
    if letter != " ":
        sentence_length += 1

print(f"There are {sentence_length} letters in this sentence!")
