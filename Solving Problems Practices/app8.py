total = 0
transaction = ""
transactions = []
balance = []
totals = []

while transaction != "-1":
    transaction = input(
        "Enter the transaction with the value, Type 'D' for DEPOSIT and 'W' for withdrawal and then value(EX: D 200): ")

    if transaction != "-1":
        transactions.append(transaction)

for transaction in transactions:
    specifics = transaction.split(" ")
    balance.append(specifics)

for value in balance:
    if value[0] == "W":
        value[1] = int(value[1]) * -1
    else:
        totals.append(value[1])

    total += int(value[1])

print(f"The Total is {total}.")
