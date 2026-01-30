import statistics

company = input("Company's name: ")
days = int(input("Days Count: "))

stock_closing = []
for i in range(0, days):
    closing_price = int(input(f"closing pricing of {company} on day {i}: "))
    stock_closing.append(closing_price)


stock_closing_average = statistics.mean(stock_closing)
print(
    f"average of closing price of {company} of last {days} days is: {stock_closing_average:.2f}")
