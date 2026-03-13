L = ["pen", "ball", "eraser", "pen", "band", "pen", "pencil", "ball"]

max_count = L.count(L[0])
most_item = L[0]

for i in range(len(L)):
    c = L.count(L[i])

    if c > max_count:
        max_count = c
        most_item = L[i]

print("Most occurring item is:", most_item)
print("Quantity:", max_count)
