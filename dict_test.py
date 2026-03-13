# Create the dictionary
car = {"brand" : "Ford" , "model" : "Mustang"
, "year" : 2024}# Print the model

print(car["model"])
# Add a color key
car["color"] = "red" 
# Remove the brand key
car.pop("model")

print(car)

for i in car:
    print(i)
    print(car[i])


for i in car.values():
    print(i)
