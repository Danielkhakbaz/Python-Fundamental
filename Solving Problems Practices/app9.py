import collections

words = []

sentence = input("Enter the sentece: ").lower()

words = sentence.split(" ")

counter = collections.Counter(words)

print(f"{counter.most_common()[0][0]}: {counter.most_common()[0][1]}")
print(f"{counter.most_common()[1][0]}: {counter.most_common()[1][1]}")
print(f"{counter.most_common()[2][0]}: {counter.most_common()[2][1]}")
