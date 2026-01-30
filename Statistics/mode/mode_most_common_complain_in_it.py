import statistics
import random

it_domain = ['Network', 'Hardware', 'Software']
total_issues = 3000
user_tickets = []
for issue in range(1, total_issues + 1, 1):
    add_ticket = random.choice(it_domain)
    user_tickets.append(add_ticket)

mode_most_common_issues_in_domain = statistics.mode(user_tickets)

print("IT COMPLAINTS ANALYSIS")
print(f"Total tickets: {total_issues}")
for i in range(1, 5+1):
    print("running analysis...")


print(
    f"ANALYSIS RESULT: Most tickets raised by {total_issues} users in IT are of : {mode_most_common_issues_in_domain} domain.")
