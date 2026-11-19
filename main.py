from contact_manager import Contact, ContactService


def main():

    manager = ContactService()

    while True:

        print("\n======================================")
        print("       CONTACT MANAGEMENT SYSTEM")
        print("======================================")
        print("\nWhat would you like to do?")
        print("--------------------------------------")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Exit")
        print("--------------------------------------")

        choice = input(
            "\nEnter option number : "
        ).strip().lower()

        # Accept both numbers and names
        options = {
            "add contact": "1",
            "add": "1",
            "delete contact": "2",
            "delete": "2",
            "search contact": "3",
            "search": "3",
            "view all contacts": "4",
            "view": "4",
            "exit": "5"
        }

        choice = options.get(choice, choice)

        # Add Contact
        if choice == "1":

            print("\n===== ADD NEW CONTACT =====")

            try:
                name = input("Enter contact name: ")
                email = input("Enter email address: ")
                phone = input("Enter phone number: ")
                address = input("Enter address: ")

                contact = Contact(
                    name, email, phone, address
                )

                manager.add_contact(contact)

            except ValueError as error:
                print("\nError:", error)

        # Delete Contact
        elif choice == "2":

            print("\n===== DELETE CONTACT =====")

            email = input("Enter email of contact to delete: ")
            manager.delete_contact(email)

        # Search Contact
        elif choice == "3":

            print("\n===== SEARCH CONTACT =====")

            name = input("Enter contact name to search: ")
            manager.search_contact(name)

        # View All Contacts
        elif choice == "4":

            print("\n===== ALL CONTACTS =====")

            manager.list_contacts()

        # Exit
        elif choice == "5":

            print("\nThank you for using Contact Management System!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid option!")
            print("Please enter 1-5 or a valid option name.")


if __name__ == "__main__":
    main()