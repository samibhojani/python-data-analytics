import numpy as np

customers = []
spendings = []

total_customers = int(input("Total Customers: "))
for t in range(1, total_customers + 1):
    add_customer = input(f"Enter name of customer # {t}: ")
    customers.append(add_customer)
    add_spendings = int(input(
        f"Enter total amount spent of {add_customer} (customer#{t}): "))
    spendings.append(add_spendings)

spendings.sort()

Q1 = np.percentile(spendings, 25)
Q3 = np.percentile(spendings, 75)

IQR = Q3 - Q1

UF = Q3 + (1.5 * IQR)
LF = Q1 - (1.5 * IQR)

outliers = []
for x in spendings:
    if x >= UF:
        outliers.append(x)
vip_customers = {}

print(f"VIP/Whale customers spent: {outliers} PKR.")
