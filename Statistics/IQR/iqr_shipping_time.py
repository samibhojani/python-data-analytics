import numpy as np

days = [2, 3, 3, 4, 5, 5, 6, 30]  # 30 is an outlier
days.sort()
n = len(days)

q1 = days[n // 4]
q3 = days[(3 * n) // 4]
iqr = q3 - q1

Q1 = np.percentile(days, 25)
Q3 = np.percentile(days, 75)
IQR = Q3 - Q1

print(f" RESULT BY MANUAL FORMULA: Standard shipping window (IQR): {iqr} days")
print(f" RESULT BY LIBRARY_NUMPY: Standard shipping window (IQR): {iqr} days")
