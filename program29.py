class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload - operator (distance between two points)
    def __sub__(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

    # Overload >= operator (compare distance from origin)
    def __ge__(self, other):
        return (self.x**2 + self.y**2) >= (other.x**2 + other.y**2)


# Taking input from user
try:
    x1 = float(input("Enter x coordinate of P1: "))
    y1 = float(input("Enter y coordinate of P1: "))
    x2 = float(input("Enter x coordinate of P2: "))
    y2 = float(input("Enter y coordinate of P2: "))

    # Create objects
    P1 = Point(x1, y1)
    P2 = Point(x2, y2)

    # Distance between points
    print("Distance between P1 and P2:", P1 - P2)

    # Compare distance from origin
    if P1 >= P2:
        print("P1 is farther or equal from origin than P2")
    else:
        print("P2 is farther from origin than P1")

except ValueError:
    print("Invalid input! Please enter numeric values.")
