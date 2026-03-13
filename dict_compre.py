cube = {x : x**3 for x in range(6)}
print(cube)

print("")

print("Alias")
cube2 = cube
print(cube2)

print("")

print("Copy")
cube3=cube2.copy()
print(cube3)

