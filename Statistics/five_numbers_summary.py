import numpy as np
# import seaborn as sns


arr = np.array([-100, -50, -40, -39, 2, 3, 4, 6, 7, 8, 9, 12,
               13, 16, 17, 23, 25, 27, 34, 37, 201, 300, 500, 100000,])

# finding Q1 and Q3 with numpy - np.percentile(dataArray, percentileValue)
Q1 = np.percentile(arr, 25)
Q3 = np.percentile(arr, 75)

# Finding IQR with formula IQR = Q3 - Q1
IQR = Q3 - Q1

print(f"Array (arr) = {arr} \n Q1 = {Q1} \n Q3 = {Q3} \n IQR = {IQR}")

# find upper fence with the formula UF = Q3 + 1.5(IQR)
UF = Q3 + (1.5 * IQR)


# find upper fence with the formula UF = Q3 + 1.5(IQR)
LF = Q1 - (1.5 * IQR)

print(f"Upper fence = {UF} \n Lower fence = {LF}")

# create new list - that has outliers removed from arr
l = []
outliers = []
for o in arr:
    if o >= LF and o <= UF:
        l.append(o)
    elif o <= LF or o >= UF:
        outliers.append(o)
    else:
        print("end...")

list_with_outliers = np.array(outliers)
list_after_removing_the_outlier = np.array(l)

print("Data array = ", arr)
print("Outliers are = ", list_with_outliers)
print("Final list = ", list_after_removing_the_outlier)


# sns.boxplot(x=arr)
# this is seaborn somehow not working, so i'll check it again when i'm learning seaborn complete.
