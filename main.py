from peewee import *

db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()

db.create_tables([Contact])

print("Hello! Welcome to your contact book!")

class ContactBook:
    def menu(self):
        print("\nMAIN MENU")
        response = input("\nAdd a contact: A\nSearch contacts: S\nView all contacts: V\n\n")
        if response == "A":
            self.add()
        elif response == "S":
            self.search()
        elif response == "V":
            self.view()
        else:
            print("Sorry, that's not an option. Please select a valid option.")
            self.menu()
    def add(self):
        print("\nADD A CONTACT")
        print("\nFill in these fields to create a new contact.\n")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        phone_number = input("Phone Number: ")
        new_contact = Contact(first_name = first_name, last_name = last_name, phone_number = phone_number)
        print("\nYour contact has been saved! Returning to main menu.\n")
        new_contact.save()
        self.menu()
    def search(self):
        print("\nSEARCH CONTACTS")
        search = input("\nEnter their first name: ")
        result = Contact.select().where(Contact.first_name.contains(search)).get()
        print(f"\n{result.first_name} {result.last_name}\n{result.phone_number}\n")
        self.navigate()
    def view(self):
        print("\nCONTACTS")
        for all_contacts in Contact.select():
            print(f"\n{all_contacts.first_name} {all_contacts.last_name}\nPhone Number: {all_contacts.phone_number}")
        self.navigate()
    def navigate(self):
        response = input("\nReturn to the main menu: M\nExit contact book: Q\n")
        if response == "M":
            self.menu()
        elif response == "Q":
            return
        else:
            print("\n\nSorry, that's not an option. Please enter a valid option.")
            self.navigate()


contact_book = ContactBook()
contact_book.menu()
