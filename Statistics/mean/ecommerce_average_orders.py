import statistics as st


print("E-commerce: Average Order Value (AOV)")
transactions = []


def addTransactions():
    total_transactions = int(input("No. of total transactions: "))
    for i in range(1, total_transactions + 1):
        transaction_amount = int(input(f"Enter amount of Order # {i}: "))
        i += 1
        transactions.append(transaction_amount)


addTransactions()

print(transactions)
aov = st.mean(transactions)

print(f"The average Transaction amount is: {aov}")
