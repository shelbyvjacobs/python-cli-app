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
    def add(self):
        print("Fill in these fields to create a new contact.")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        phone_number = input("Phone Number: ")
        new_contact = Contact(first_name = first_name, last_name = last_name, phone_number = phone_number)
        print("Your contact has been saved!")
        new_contact.save()

contact_book = ContactBook()
contact_book.add()
