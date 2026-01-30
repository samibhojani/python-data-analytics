product_ids = []

for i in range(1, 20):
    i = 1000 + i
    product_ids.append(i)

for j in range(1, 10):
    j = 1000 + j
    product_ids.append(j)

print(product_ids)

for k in range(1, 5):
    k = 1000 + j
    product_ids.append(k)

print(product_ids)

frequency = {}
for item in product_ids:
    frequency[item] = frequency.get(item, 0) + 1

mode_best_seller_products = max(frequency, key=frequency.get)

print(f"Best Seller Product IDs: {mode_best_seller_products}")
