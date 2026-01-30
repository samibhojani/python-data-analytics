print("Real Estate: Average Price per Square Foot")

real_estate_company = input("Company Name: ")
total_properties = int(
    input(f"No. of properties listed in {real_estate_company}: "))
prices_per_sqft = []

for i in range(1, total_properties + 1):
    price_of_property = int(
        input(f"Price of property {i} per square feet is: "))
    prices_per_sqft.append(price_of_property)

mean = sum(prices_per_sqft) / len(prices_per_sqft)
print(
    f"Average cost per sq ft of a propery in {real_estate_company} is: ${int(mean)}")
