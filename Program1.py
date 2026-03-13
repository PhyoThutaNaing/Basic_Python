# Accept two numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Calculations
sum_result = a + b
diff_result = a - b
prod_result = a * b
quot_result = a / b
rem_result = a % b

# Printing results with their data types
print("Sum:", sum_result, "Type:", type(sum_result))
print("Difference:", diff_result, "Type:", type(diff_result))
print("Product:", prod_result, "Type:", type(prod_result))
print("Quotient:", quot_result, "Type:", type(quot_result))
print("Remainder:", rem_result, "Type:", type(rem_result))
