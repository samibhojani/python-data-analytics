import statistics

house_prices = []

print("Real Estate: Median House Price")
total_listed_houses = int(input("No. of houses listed in your name: "))

for house in range(1, total_listed_houses + 1):
    add_price = int(input(f"Enter price of house # {house}: "))
    house_prices.append(add_price)

median_house_price = statistics.median(house_prices)

print(f"Median Price is: {median_house_price}")
