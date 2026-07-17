# 1 & 2. Ask for the password and clean up spaces
password = input("Enter your password: ").strip()

# 3. Grab the first and last letters using indexing
first_letter = password[0]
last_letter = password[-1]

# 4. Print the hint using an f-string and force the letters to UPPERCASE
print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}")