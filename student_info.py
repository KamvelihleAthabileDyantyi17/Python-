# 1. Collect inputs and convert the number types immediately
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favouritenumber = float(input("Enter your favourite number: "))

# 2. Display formatted greeting using an f-string
fullname = f"{name} {surname}"
print(f"Welcome, {fullname}!")

# 3. Display name in Uppercase and title case
print(f"Uppercase: {fullname.upper()}")
print(f"Title Case: {fullname.title()}")

# 4. Calculate and display age in months
age_in_months = age * 12
print(f"Your age in months is: {age_in_months}")

# 5. Round the favourite number to 2 decimal places
rounded_number = round(favouritenumber, 2)
print(f"Your rounded favourite number is: {rounded_number}")

# 6. Print the data type of each collected value
print("--- Data Types ---")
print(type(name))
print(type(surname))
print(type(age))
print(type(favouritenumber))