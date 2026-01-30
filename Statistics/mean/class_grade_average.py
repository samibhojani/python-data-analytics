import statistics

students = []
grades = []
class_name = "VIII-O"


total_students = int(input(f"Total no. of students in class {class_name}: "))

print(f"Total students in class is: {total_students}")

for i in range(1, total_students):
    student_name = input(f"Student # {i}'s Name: ")
    students.append(student_name)
    student_grade = int(input(f"{student_name}'s grade is: "))
    if student_grade >= 0 and student_grade <= 100:
        grades.append(student_grade)
    else:
        print("Invalid input")

class_avg_grade = statistics.mean(grades)
print(f"Class average score: {class_avg_grade:.2f}%")
