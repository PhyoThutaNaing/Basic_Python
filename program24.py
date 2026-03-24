Cel = [34.56, 23.67, 45.67, 67, 34]

print("Temperature in Celsius:", Cel)

Fer = list(map(lambda x: round((x * 1.8) + 32, 2), Cel))

print("Temperature in Fahrenheit:", Fer)
