import collections

candidates = []

votes = int(input("Enter the total votes: "))

for _ in range(votes):
    candidates.append(input("Enter your candidate: "))

counter = sorted(collections.Counter(candidates).most_common())

for index, value in enumerate(counter):
    # print(f"{value[index]}: {value[index + 1]}")
    print(f"{value[0]}: {value[1]}")
