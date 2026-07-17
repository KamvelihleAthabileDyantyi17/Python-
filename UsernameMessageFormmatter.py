first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()
bio = input("Enter a short bio about yourself: ").strip()

#Count and display the number of characters in the bio using len()
bio_length = len(bio)
print(f"Your bio has {bio_length} characters.")

#Replace any occurrence of ‘I am’ in the bio with ‘I’m’ using .replace()
bio = bio.replace("I am", "I'm")

print(f"I am: {first.title()} {last.title()} and my bio is: {bio}")

