students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    
    student = {"name": name, "marks": marks}
    students.append(student)

print(students)
