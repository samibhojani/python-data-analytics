load_times = []  # 4.5s is a slow outlier

attempts = int(input("No. of attempts: "))

for attempt in range(1, attempts + 1, 1):
    add_load_time = float(
        input(f"Add load time of attempt {attempt} in seconds: "))
    load_times.append(add_load_time)

load_times.sort()
n = len(load_times)

if n % 2 == 0:
    median = (load_times[n//2 - 1] + load_times[n//2]) / 2
else:
    median = load_times[n//2]

print(f"Median of Server Load Time of all attempts: {median:.1f} seconds")
