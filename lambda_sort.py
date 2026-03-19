L = [(1, "Yellow"), (2, "Red"), (3, "White"), (4, "Green")]

L.sort()

L.sort(key=lambda L:L[1])

print(L)
