import random


print("DELIVERY TIME PER QUARTILE")

delivery_time_in_days = []

total_delivered_orders = int(input("Total delivered orders: "))
for o in range(1, total_delivered_orders + 1):
    add_deliverytime = random.randint(1, 7)
    delivery_time_in_days.append(add_deliverytime)

delivery_time_in_days.sort()
n = len(delivery_time_in_days)

Quartile1 = delivery_time_in_days[n // 4]
Quartile2 = delivery_time_in_days[(2 * n) // 4]
Quartile3 = delivery_time_in_days[(3 * n) // 4]


for p in range(0, 5):
    print(
        f"Runniny analysis for {total_delivered_orders} delivered orders.....")


print(
    f"ANALYSIS RESULT: 25% of orders arrive within {Quartile1} days, 50% orders arrive within {Quartile2} days and 75% arrive within {Quartile3} days.")
