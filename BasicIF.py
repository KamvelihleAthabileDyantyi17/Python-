age = int(input("Enter your age: "))
section_pass =input("Do you have a section pass? (yes/no): ").strip().lower()

if age >= 18:
    print("You are an adult. ")
else:
    print("You are a minor. ")

if section_pass ==yes:
    print("You have a section pass. ")
else:
    print("You do not have a section pass. ")