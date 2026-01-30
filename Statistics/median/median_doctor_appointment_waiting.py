import statistics

extra_waited_time = []

print("Appointments extra waiting analysis")

print("---------PATIENT WATING EXTRA TIME AFTER BOOKING AN APPOINTMENT---------")
doctor = input("Enter Doctor Name: ")
count_of_patients_waited_extra = int(
    input("Total no. of scheduled patients waited in queue: "))

for patient in range(1, count_of_patients_waited_extra, 1):
    add_waited_time = int(
        input(f"Extra wait time of patient # {patient} (in minutes) is: "))
    extra_waited_time.append(add_waited_time)

median_extra_waited_time = statistics.median(extra_waited_time)

print(
    f"Average extra waited time of patients: {median_extra_waited_time:.0f} minutes.")
