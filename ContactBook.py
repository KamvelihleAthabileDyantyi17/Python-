# The main list that will hold all our contact dictionaries
contacts = []

def add_contact():
    # 1. Ask for the 3 pieces of info
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    # 2. Package them into a dictionary
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    # 3. Add the dictionary to our list
    contacts.append(new_contact)
    print("Contact added successfully!")

def search_contact(search_name):
    # Loop through the list to check every dictionary one by one
    for contact in contacts:
        if contact["name"] == search_name:
            return contact  # We found them! Return the dictionary
            
    return None  # The loop finished and we didn't find them

def delete_contact(delete_name):
    # Use our search function to find the dictionary
    contact_to_delete = search_contact(delete_name)
    
    if contact_to_delete != None:
        contacts.remove(contact_to_delete)
        print("Contact deleted!")
    else:
        print("Contact not found.")

def view_all():
    # Check if the list is completely empty first
    if len(contacts) == 0:
        print("Your contact list is empty.")
    else:
        # Loop through and print each one
        for contact in contacts:
            print(f"Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")

# --- Main Program Menu ---
while True:
    print("\n1. Add a contact")
    print("2. Search for a contact")
    print("3. Delete a contact")
    print("4. View all contacts")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_contact()
        
    elif choice == '2':
        name = input("Enter name to search for: ")
        result = search_contact(name)
        
        if result != None:
            print(f"Found: {result['name']}, Phone: {result['phone']}, Email: {result['email']}")
        else:
            print("Contact not found.")
            
    elif choice == '3':
        name = input("Enter name to delete: ")
        delete_contact(name)
        
    elif choice == '4':
        view_all()
        
    elif choice == '5':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice, please try again.")