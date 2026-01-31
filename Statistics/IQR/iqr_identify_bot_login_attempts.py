import numpy as np
import random

print("-------------- BOT LOGIN DETECTION -------------")

login_attempts = [324, 245, 50]
users = int(input("Enter no. of users"))

for u in range(0, users, 1):
    attempts = random.randint(1, 5)
    login_attempts.append(attempts)

login_attempts.sort()

Q1 = np.percentile(login_attempts, 25)
Q3 = np.percentile(login_attempts, 75)

IQR = Q3 - Q1
lower_fence = Q1 - (1.5 * IQR)
upper_fence = Q3 + (1.5 * IQR)


outliers = []
for o in login_attempts:
    if o <= lower_fence or o >= upper_fence:
        outliers.append(o)
outliers.sort()

print(f"Suspicious login activity detected! login attempts: {outliers}")
print(f"Normal user attempt range: {IQR}")
