n = 100
total = 0

for i in range(0, n+1, 2):
    print(i, end=" / ")
    total+=i

print("\nTotal of even is ", total)
    
for i in range(1, n+1, 2):
    print(i, end=" / ")
    total+=i

print("\nTotal of odd is ", total)
