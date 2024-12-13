import json

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact():
    view_contacts()
    index = int(input("Enter the index of the contact to edit: ")) - 1
    if 0 <= index < len(contacts):
        contacts[index]["name"] = input("Enter new name: ")
        contacts[index]["phone"] = input("Enter new phone number: ")
        contacts[index]["email"] = input("Enter new email address: ")
        print("Contact edited successfully!")
    else:
        print("Invalid index.")

def delete_contact():
    view_contacts()
    index = int(input("Enter the index of the contact to delete: ")) - 1
    if 0 <= index < len(contacts):
        del contacts[index]
        print("Contact deleted successfully!")
    else:
        print("Invalid index.")

def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)
    print("Contacts saved to file.")

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
        print("Contacts loaded from file.")
    except FileNotFoundError:
        contacts = []

load_contacts()

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Save Contacts")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        save_contacts()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")