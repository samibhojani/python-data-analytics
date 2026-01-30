import statistics

print("Environmental Science: Average Daily Temperature")

# Daily max temperatures in Celsius for one week
temp_by_day = {"mon": 28, "tue": 31, "wed": 29,
               "thu": 33, "fri": 30, "sat": 27, "sun": 26}
print(temp_by_day)
temp = [temp_by_day["mon"], temp_by_day["tue"], temp_by_day["wed"],
        temp_by_day["thu"], temp_by_day["fri"], temp_by_day["sat"], temp_by_day["sun"]]
print(f"Temperature on monday {temp_by_day['mon']}")
print(f"Temperature on tuesday {temp_by_day['tue']}")
print(f"Temperature on wednesday {temp_by_day['wed']}")
print(f"Temperature on thu {temp_by_day['thu']}")
print(f"Temperature on friday {temp_by_day['fri']}")
print(f"Temperature on saturday {temp_by_day['sat']}")
print(f"Temperature on sunday {temp_by_day['sun']}")

avg_temp = statistics.mean(temp)

print(f"Mean weekly temperature: {avg_temp:.1f}°C")
# :.1f = one float point/value.
