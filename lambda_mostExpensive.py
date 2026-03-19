price = {"pen": 10, "pencil": 5, "book": 50, "eraser": 20}

expensive = max(price, key=lambda i: price[i])

print("Expensive item:", expensive)
