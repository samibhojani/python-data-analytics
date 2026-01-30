import numpy as np


users = int(input("No. of Users: "))
battery_drainage_calculation = []

for l in range(1, users + 1):
    battery_drain_per_hour = int(input("Battery drained per hour: "))
    battery_drainage_calculation.append(battery_drain_per_hour)

Q3 = np.percentile(battery_drainage_calculation, 75)


print(
    f"The heaviest 25% of users from {users} users, lose more than {Q3}% battery per hour.")
