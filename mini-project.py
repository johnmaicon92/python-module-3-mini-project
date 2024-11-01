"""
Introduction
Welcome to the Contact Management System project! In this project, you will apply your Python programming skills to create a functional command-line-based application that simplifies the management of your contacts. You will be able to add, edit, delete, and search for contacts, all while reinforcing your understanding of Python dictionaries, file handling, user interaction, and error handling.



Project Requirements

Your task is to develop a Contact Management System with the following features:

1- User Interface (UI):
Create a user-friendly command-line interface (CLI) for the Contact Management System.
Display a welcoming message and provide a menu with the following options:
Welcome to the Contact Management System! 
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file *BONUS*
8. Quit

2- Contact Data Storage:
Use nested dictionaries as the main data structure for storing contact information.
Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
Store contact details within the inner dictionary, including:
Name
Phone number
Email address
Additional information (e.g., address, notes).

3- Menu Actions:
Implement the following actions in response to menu selections:
Adding a new contact.
Editing an existing contact's information (name, phone number, email, etc.).
Deleting a contact.
Searching for a contact and displaying their details.
Displaying a list of all contacts.
Exporting contacts to a text file in a structured format.
Importing contacts from a text file and adding them to the system. * BONUS

4- User Interaction:
Utilize input() to enable users to select menu options and provide contact details.
Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.


5- Error Handling:
Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.


6- GitHub Repository:
Create a GitHub repository for your project.
Create a clean and interactive README.md file in your GitHub repository.
Include clear instructions on how to run the application and explanations of its features.
"""


import re

class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}

    def display_menu(self):
        print("\nWelcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")

    def validate_phone(self, phone):
        pattern = r'^\d{3}-\d{3}-\d{4}$'
        return re.match(pattern, phone) is not None

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def format_phone(self, phone):
        """Format the phone number to 'XXX-XXX-XXXX'."""
        digits = ''.join(filter(str.isdigit, phone))  # Keep only digits
        if len(digits) == 10:
            return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
        else:
            return None

    def add_contact(self):
        identifier = input("Enter a unique identifier (contact name or email): ").capitalize()
        if identifier in self.contacts:
            print("Contact already exists.")
            return
        name = input("Enter name: ").title()

        phone = input("Enter phone number (digits only): ")
        formatted_phone = self.format_phone(phone)
        while formatted_phone is None:
            print("Invalid phone number. Please enter 10 digits.")
            phone = input("Enter phone number (digits only): ")
            formatted_phone = self.format_phone(phone)

        email = input("Enter email address: ")
        while not self.validate_email(email):
            print("Invalid email address format.")
            email = input("Enter email address: ")

        additional_info = input("Enter additional information (address, notes): ")

        self.contacts[identifier] = {
            'Name': name,
            'Phone': formatted_phone,
            'Email': email,
            'Additional Info': additional_info
        }
        print("Contact added successfully.")

    def edit_contact(self):
        identifier = input("Enter the unique identifier of the contact to edit: ").title()
        if identifier not in self.contacts:
            print("Contact not found.")
            return
        print("Current details:", self.contacts[identifier])
        
        name = input("Enter new name (leave blank to keep current): ").title()
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email address (leave blank to keep current): ")
        additional_info = input("Enter new additional information (leave blank to keep current): ")

        if name:
            self.contacts[identifier]['Name'] = name
        if phone:
            self.contacts[identifier]['Phone'] = phone
        if email:
            self.contacts[identifier]['Email'] = email
        if additional_info:
            self.contacts[identifier]['Additional Info'] = additional_info

        print("Contact updated successfully.")

    def delete_contact(self):
        identifier = input("Enter the unique identifier of the contact to delete: ").title()
        if identifier in self.contacts:
            del self.contacts[identifier]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def search_contact(self):
        identifier = input("Enter the unique identifier of the contact to search: ").title()
        if identifier in self.contacts:
            print("Contact details:", self.contacts[identifier])
        else:
            print("Contact not found.")

    def display_all_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for identifier, details in self.contacts.items():
            print(f"Identifier: {identifier}, Details: {details}")

    def export_contacts(self):
        try:
            with open('contacts.txt', 'w') as file:
                for identifier, details in self.contacts.items():
                    file.write(f"{identifier}|{details['Name']}|{details['Phone']}|{details['Email']}|{details['Additional Info']}\n")
            print("Contacts exported successfully to contacts.txt.")
        except Exception as e:
            print(f"An error occurred while exporting contacts: {e}")

    def import_contacts(self):
        try:
            with open('contacts.txt', 'r') as file:
                for line in file:
                    identifier, name, phone, email, additional_info = line.strip().split('|')
                    self.contacts[identifier] = {
                        'Name': name,
                        'Phone': phone,
                        'Email': email,
                        'Additional Info': additional_info
                    }
            print("Contacts imported successfully from contacts.txt.")
        except Exception as e:
            print(f"An error occurred while importing contacts: {e}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option (1-8): ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.edit_contact()
            elif choice == '3':
                self.delete_contact()
            elif choice == '4':
                self.search_contact()
            elif choice == '5':
                self.display_all_contacts()
            elif choice == '6':
                self.export_contacts()
            elif choice == '7':
                self.import_contacts()
            elif choice == '8':
                print("Goodbye!")
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    cms = ContactManagementSystem()
    cms.run()


