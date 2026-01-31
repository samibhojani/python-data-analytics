
print("Finance: Fraudulent Credit Card Charges \nIdentifying transactions that are significantly higher than a customer's usual spending habits.")

transactions = [10, 15, 20, 12, 18, 25, 14, 5000]
print(f"Transactions history: {transactions}")
for k in range(0, 5):
    print("Running Analysis. . .")


transactions.sort()
n = len(transactions)

q1 = transactions[n//4]
q3 = transactions[(3*n)//4]
iqr = q3 - q1
upper_fence = q3 + (1.5 * iqr)

outliers = []

for x in transactions:
    if x > upper_fence:
        outliers.append(x)

print(f"Potential fraudulent transactions: {outliers}")
