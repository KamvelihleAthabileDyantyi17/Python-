num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

# 1. Do the safe math first
cal1 = round(num1 + num2, 2)
cal2 = round(num1 - num2, 2)
cal3 = round(num1 * num2, 2)

# 2. Print the safe math
print(f"Addition: {cal1}")
print(f"Subtraction: {cal2}")
print(f"Multiplication: {cal3}")

# 3. NOW we check for zero BEFORE we ever try to divide
if num2 == 0:
    print("Division: Error: Division by zero is not allowed.")
else:
    # This ONLY runs if num2 is NOT zero!
    cal4 = round(num1 / num2, 2)
    print(f"Division: {cal4}")