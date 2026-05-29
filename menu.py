contacts = []
def show_menu():
    print("CONTACT BOOK MENU")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
def add_contact():
    print("Add New Contact")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully")
def view_contacts():
    print("Contact List")
    if not contacts:
        print("No contacts available.")
        return
    for index, contact in enumerate(contacts, start=1):
        print(f"Contact {index}")
        print(f"Name    : {contact["name"]}")
        print(f"Phone   : {contact["phone"]}")
        print(f"Email   : {contact["email"]}")
        print(f"Address : {contact["address"]}")
def search_contact():
    print("Search Contact")
    search = input("Enter Name or Phone Number: ").lower
    found = False
    for contact in contacts:
        if search in contact["name"].lower() or search in contact["phone"]:
            print("Contact Found")
            print(f"Name    : {contact["name"]}")
            print(f"Phone   : {contact["phone"]}")
            print(f"Email   : {contact["email"]}")
            print(f"Address : {contact["address"]}")
            found = True
    if not found:
        print("Contact not found.")
def update_contact():
    print("Update Contact")
    phone = input("Enter Phone Number of contact to update: ")
    for contact in contacts:
        if contact["phone"] == phone:
            print("Enter New Details")
            contact["name"] = input("New Name: ")
            contact["phone"] = input("New Phone Number: ")
            contact["email"] = input("New Email: ")
            contact["address"] = input("New Address: ")
            print("Contact updated successfully!")
            return
    print("Contact not found.")
def delete_contact():
    print("Delete Contact")
    phone = input("Enter Phone Number of contact to delete: ")
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully")
            return
    print("Contact not found")
while True:
    show_menu()
    choice = input("\nEnter your choice (1-6): ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice! Please try again.")