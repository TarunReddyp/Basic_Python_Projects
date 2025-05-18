def contact_book():
    contacts = {}

    while True:
        print("\n--- Contact Book ---")
        print("1. Add new contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ").strip()
            phone = input("Enter contact phone number: ").strip()
            contacts[name] = phone
            print(f"Contact '{name}' added.")
        elif choice == '2':
            if not contacts:
                print("Your contact book is empty.")
            else:
                print("--- Contacts ---")
                for name, phone in contacts.items():
                    print(f"Name: {name}, Phone: {phone}")
        elif choice == '3':
            search_name = input("Enter the name to search for: ").strip()
            if search_name in contacts:
                print(f"Name: {search_name}, Phone: {contacts[search_name]}")
            else:
                print(f"Contact '{search_name}' not found.")
        elif choice == '4':
            delete_name = input("Enter the name to delete: ").strip()
            if delete_name in contacts:
                del contacts[delete_name]
                print(f"Contact '{delete_name}' deleted.")
            else:
                print(f"Contact '{delete_name}' not found.")
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    contact_book()