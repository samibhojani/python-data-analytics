import random


print("Quality Control: Manufacturing Precision")

product_count = int(input("Total products: "))

bolt_length = []
for b in range(1, product_count + 1, 1):
    add_bolt_length = random.uniform(9.98, 10.99)
    bolt_length.append(add_bolt_length)

data_range = max(bolt_length) - min(bolt_length)

for i in range(1, 5+1):
    print("Runnning Analysis....")

print(f"Manufacturing Tolerance range: {data_range:.2f}")
