import statistics
import random

vehicles = ['bus', 'van', 'uber', 'bykea', 'own-bike', 'own-car']
employee_count = 500
mode_of_transport = []

print("MOST FREQUENT TRANSPORT USED BY EMPLOYEES")
print(f"Total number of employees: {employee_count}")

print(
    f"VEHICLES USED BY EMPLOYEES: \n {vehicles[0]} \n {vehicles[1]} \n {vehicles[2]} \n {vehicles[3]} \n {vehicles[4]} \n {vehicles[5]}")

for employee in range(1, employee_count + 1, 1):
    add_emp_mode_of_transport = random.choice(vehicles)
    mode_of_transport.append(add_emp_mode_of_transport)

mode_most_used_transport_by_employees = statistics.mode(mode_of_transport)

print(
    f"ANALYSIS RESULT: The most common mode of transport used by {employee_count} employees is: {mode_most_used_transport_by_employees}")
