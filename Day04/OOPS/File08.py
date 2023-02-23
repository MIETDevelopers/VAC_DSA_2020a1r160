""""
write a program on: you are given a class named Access where there are certain members, named= [name, age, phone, address, email].
Write a program to change your phone number and email in a second class named NoAccess by inheriting the properties of class Access,
and access privilage should only be restricted to the class Access to change other details than phone and email
"""
class Access:
    def __init__(self, name, age, phone, address, email):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.email = email
    
    def change_phone(self, new_phone):
        self.phone = new_phone
    
    def change_email(self, new_email):
        self.email = new_email


class NoAccess(Access):
    def __init__(self, name, age, phone, address, email):
        super().__init__(name, age, phone, address, email)
    
    def change_phone(self, new_phone):
        print("Not access to change number")
    
    def change_email(self, new_email):
        print("Not access to change mail")

person1 = Access('Raju', 30, '1234567890', '69, Jammu', 'raju@example.com')
person1.change_phone('0987654321')
person1.change_email('raju@mail.com')

print(f"Name: {person1.name}, Age: {person1.age}, Phone: {person1.phone}, Address: {person1.address}, Email: {person1.email}")

person2 = NoAccess('Tanmay', 25, '9876543210', '10, Jammu', 'tanmay@example.com')
person2.change_phone('1111111111')
person2.change_email('tanmay@mail.com')
print(f"Name: {person2.name}, Age: {person2.age}, Phone: {person2.phone}, Address: {person2.address}, Email: {person2.email}")