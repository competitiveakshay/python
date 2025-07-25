#Create a student report card program. Use variables for student name, three subject marks, calculate total and average, then display a formatted report using f-strings.

student_name = "Akshay Gaur"
maths = 85
science = 90
english = 78
total_marks = maths + science + english
average = (total_marks)/3
round_average = round(average, 2)

print("=== STUDENT REPORT CARD ===")
print(f"Student name: {student_name}")
print(f"Maths: {maths}, Science: {science}, English: {english}")
print(f"Total Marks: {total_marks}")
print(f"Average: {round_average}")
