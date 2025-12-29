# Get 3 numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find and print min and max
min_value = min(num1, num2, num3)
max_value = max(num1, num2, num3)

print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
