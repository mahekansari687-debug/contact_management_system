class ContactService:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        for existing in self.contacts:
            if existing.email.lower() == contact.email.lower():
                print("Contact with this email already exists!")
                return

        self.contacts.append(contact)
        print("Contact added successfully!")

    def delete_contact(self, email):
        for contact in self.contacts:
            if contact.email.lower() == email.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return

        print("Contact not found!")

    def search_contact(self, name):
        found = False

        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                contact.display()
                found = True

        if not found:
            print("Contact not found!")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts available!")
            return

        print("\n===== ALL CONTACTS =====")

        for contact in self.contacts:
            contact.display()