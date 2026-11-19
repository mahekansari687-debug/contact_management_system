from .utils import validate_email, format_phone


class Contact:
    def __init__(self, name, email, phone, address):

        if not name.strip():
            raise ValueError("Name cannot be empty.")

        if not validate_email(email):
            raise ValueError("Invalid email format.")

        phone = format_phone(phone)

        if len(phone) < 10 or len(phone) > 15:
            raise ValueError("Phone number must contain 10 to 15 digits.")

        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def display(self):
        print("\n----------------------------")
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone:", self.phone)
        print("Address:", self.address)
        print("----------------------------")