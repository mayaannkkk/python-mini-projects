student_data = {}
Number_of_students = int(input("Enter number of students:"))
list_of_students = input(f"Enter name of {Number_of_students} students with space:").split()

# Taking input of student marks
for i in range(Number_of_students):
    marks = list(map(int, input("Enter 5 subject marks (0-100) separated by space: ").split()))
    while len(marks)!=5:
        print("Please enter exactly 5 subject marks")
        marks = list(map(int, input("Enter 5 subject marks (0-100) separated by space: ").split()))
    student_data[list_of_students[i]] = marks

#Total marks by each student
total_marks_by_each_student = []
for value in student_data.values():
    total_marks_by_each_student.append(sum(value))

# This block of code calculating number of fail students
count = 0
for i in range(len(total_marks_by_each_student)):
    if total_marks_by_each_student[i] < 200:
        count = count + 1
print(f"No of fail student out of {Number_of_students} is:", count)

# Average marks by each student
for name, marks in student_data.items():
    average = sum(marks) / len(marks)
    print(f"{name}'s average marks is:{average}")

# Topper of the class
topper_index = total_marks_by_each_student.index(max(total_marks_by_each_student))
topper_name = list_of_students[topper_index]
print(f"Topper of the class is:{topper_name}")


print(f"Total marks by students is:{total_marks_by_each_student}")
print(f"Name of student with their marks is:{student_data}")
