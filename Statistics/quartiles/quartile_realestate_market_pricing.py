import numpy as np
import random
print("Real Estate Categorization based on: Market Pricing")

business = input("Enter estate agency name: ")
city = input("Enter city name: ")
total_property = int(
    input(f"Enter total no. of properties owned by {business} in {city}: "))
price_range = [100000, 250000, 500000, 1000000, 2500000, 5000000,
               750000, 10000000, 50000000, 100000000]


properties = []
for r in range(1, total_property + 1):
    add_price = random.choice(price_range)
    properties.append(add_price)

Q1_budget_home_price = np.percentile(properties, 25)
Q2_luxury_home_price = np.percentile(properties, 50)
Q3_eliteclass_price = np.percentile(properties, 75)


for p in range(0, 5):
    print(
        f"Running property price range analysis of {total_property} properties of {business} in {city}....")

print(
    f"ANALYSIS RESULT: \n Budget homes are below {Q1_budget_home_price} PKR, \n Luxury homes are above {Q2_luxury_home_price} PKR, \n Elite class homes are above {Q3_eliteclass_price} PKR")
