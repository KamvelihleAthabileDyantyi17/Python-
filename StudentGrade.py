learner_name = input("Enter your name: ")
geo = float(input("Enter your Geography grade: "))
math = float(input("Enter your Math grade: "))
physics = float(input("Enter your Physics grade: "))

average = (geo + math + physics) / 3

# 1. Figure out the letter grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# 2. Print the main report card
print(f"\n--- REPORT CARD FOR {learner_name.upper()} ---")
print(f"Average: {average:.2f}%")
print(f"Grade: {grade}")

# 3. Simple Pass/Fail check printed directly
if average >= 50:
    print("Status: Pass")
else:
    print("Status: Fail")

# 4. Simple Intervention check printed directly
if geo < 40:
    print("Flag: Geography needs intervention")
if math < 40:
    print("Flag: Math needs intervention")
if physics < 40:
    print("Flag: Physics needs intervention")