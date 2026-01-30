import statistics
import random

print("Marketing: Most Common Customer Feedback")

ratings = []
customer_count = 1000

for r in range(1, customer_count + 1, 1):
    add_ratings = random.randint(1, 5)
    ratings.append(add_ratings)

mode_of_ratings = statistics.mode(ratings)

print(
    f"The most common feedback/ratings given by {customer_count} customers: {mode_of_ratings} stars.")
