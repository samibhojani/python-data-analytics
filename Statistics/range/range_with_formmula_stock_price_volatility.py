import random

company_name = input("Company Name: ")
total_days = 7
prices = []

for day in range(1, total_days + 1, 1):
    add_stock_price = random.randint(132, 245)
    prices.append(add_stock_price)
    print(f"stock closed today at: {add_stock_price}")

data_range = max(prices) - min(prices)

print(
    f"Daily Price Volatility Range of {company_name} company stock in a week are: {data_range}")
