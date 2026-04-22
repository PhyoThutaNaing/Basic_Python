class Student:
    def __init__(self, name, roll, physics, chemistry, maths):
        self.name = name
        self.roll = roll
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    def average(self):
        return (self.physics + self.chemistry + self.maths) / 3


name = input("Enter name: ")
roll = input("Enter roll: ")

physics = float(input("Enter Physics: "))
chemistry = float(input("Enter Chemistry: "))
maths = float(input("Enter Maths: "))

# Simple validation (no exception)
if 0 <= physics <= 100 and 0 <= chemistry <= 100 and 0 <= maths <= 100:
    s = Student(name, roll, physics, chemistry, maths)

    print("Name:", s.name)
    print("Average:", s.average())
else:
    print("Marks should be between 0 and 100")
