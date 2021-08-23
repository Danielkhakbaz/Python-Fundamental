import collections

candidates = []

votes = int(input("Enter the total votes: "))

for _ in range(votes):
    candidate = input("Enter your candidate: ")

    candidates.append(candidate)

collection = collections.Counter(candidates)

collection_most_common = collection.most_common()

counter = sorted(collection_most_common)

for index, value in enumerate(counter):
    print(f"{value[0]}: {value[1]}")
