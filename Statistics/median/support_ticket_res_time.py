import statistics


print("Customer Support: Median Ticket Response time")

hours = []

support_executive_name = input("Customer support person: ")
total_tickets = int(
    input(f"no. of tickets resolved by {support_executive_name} are: "))

for ticket in range(1, total_tickets + 1,):
    add_ticket_resolution_hours = int(
        input(f"time taken to resolve ticket # {ticket}: "))
    hours.append(add_ticket_resolution_hours)

median_of_ticket_res_time = statistics.median(hours)

print(
    f"Median customer ticket resolution time is: {median_of_ticket_res_time} hours.")
