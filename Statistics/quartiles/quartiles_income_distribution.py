import numpy as np
import random

company_name = input("Company Name: ")
employees_count = int(input("Total employee: "))
salary_range = [33000, 50000, 75000, 90000, 115000, 150000, 180000, 200000, 220000,
                260000, 290000, 310000, 335000, 370000, 395000, 425000, 440000, 485000, 500000]
salary_dist = []

for e in range(1, employees_count + 1):
    add_salary_range = random.choice(salary_range)
    salary_dist.append(add_salary_range)

Q1 = np.percentile(salary_dist, 25)
Q2 = np.percentile(salary_dist, 50)
Q3 = np.percentile(salary_dist, 75)


print(f"{company_name} INCOME QUARTILE: \n Q1 = {Q1} \n Q2 = {Q2} \n Q3 = {Q3} ")
