A = input("Enter the binary number: ")

count0 = A.count('0')
count1 = A.count('1')

if count0 == 1 or count1 == 1:
    print("YES")
else:
    print("NO")
