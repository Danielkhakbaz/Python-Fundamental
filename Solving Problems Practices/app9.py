import collections

words = []

sentence = input("Enter the sentence: ").lower()

words = sentence.split(" ")

counter = collections.Counter(words)

for index, value in enumerate(counter):
    print(
        f"{counter.most_common()[index][0]}: {counter.most_common()[index][1]}")
