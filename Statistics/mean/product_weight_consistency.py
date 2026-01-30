import statistics

print("Quality Control: Product Weight Consistency")

# Sample weights of boxes in grams
products_batch = []

weights = [502, 498, 505, 490, 501, 499]
for i in weights:
    product_name = input("Name of the product: ")
    products_batch.append(product_name)
    print(f"{product_name}'s weight is: {i}")


mean_weight = statistics.mean(weights)

print(f"Average batch weight: {mean_weight}g")
