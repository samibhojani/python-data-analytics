import statistics
import random

blood_groups = ['A+', 'O+', 'B-', 'A+', 'O+', 'O+', 'AB+']
total_patients = 10000
patients_blood_group = []

for bg in range(1, total_patients + 1, 1):
    add_patient_blood_group = random.choice(blood_groups)
    patients_blood_group.append(add_patient_blood_group)

mode_for_most_common_blood_groups = statistics.mode(patients_blood_group)

print(f"The most common Blood Group among {total_patients} patients is: ")
