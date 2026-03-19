students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    
    student = {"name": name, "marks": marks}
    students.append(student)

print(students)

for student in students:
    if student["marks"] > 90:
        print("Above 90:", student["name"])
    elif student["marks"] > 80:
        print("Above 80:", student["name"])
    elif student["marks"] > 70:
        print("Above 70:", student["name"])
