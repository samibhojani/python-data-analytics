import statistics

total_tickets_in_a_day = int(input("Total tickets managed today: "))
latency = []

for i in range(1, total_tickets_in_a_day + 1):
    response_time = int(input(f"Response time of ticket # {i}: "))
    latency.append(response_time)

average_response_time = statistics.mean(latency)
print(
    f"Average response time for a ticket in minutes: {average_response_time} minutes")
