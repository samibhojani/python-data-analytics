import numpy as np

print("-------------- Manufacturing: Defective Product Size ------------ \n Analysis: Finding parts that were cut incorrectly and don't meet quality standards.")

sizes = [10.1, 10.2, 10.1, 10.0, 10.2, 12.5, 9.9, 8.2]
print("Product Sizes: ", sizes)

for i in range(0, 5):
    print("Running Defect Detection Analysis...")

Q1 = np.percentile(sizes, 25)
Q3 = np.percentile(sizes, 75)

IQR = Q3 - Q1

# find upper fence with the formula UF = Q3 + 1.5(IQR)
UF = Q3 + (1.5 * IQR)


# find upper fence with the formula UF = Q3 + 1.5(IQR)
LF = Q1 - (1.5 * IQR)

outliers = []
for o in sizes:
    if o <= LF or o >= UF:
        outliers.append(o)

print(f"RESULT: Defective sizes to be discarded: {outliers}")
