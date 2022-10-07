# OOPS
"""
Oject oriented programming(oop) and it is all about creating objects.

An object is a group of interrelated variables and functions. These variables are often referred to as properties of the object and the function.

Functions are referred to as a behaviour of the object.

If we consider a car as an object, then its property would be: color, model, price, brand etc...
"""

#===============================================================

import datetime
class Person:
    def __init__(self, name, surname, dob, address, phone, email):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.address = address
        self.phone = phone
        self.email = email
    def age(self):
        today = datetime.date.today()
        age = today.year - self.dob.year
        if today < datetime.date(today.year, self.dob.month, self.dob.day):
            age -= 1
            return age
        
person = Person('Jerry', 'Candy', datetime.date(1995, 10, 26), 'no:3 amsterdam', '9080502147', 'raajthiya@gmail.com')

print(person.name)
print(person.surname)
print(person.age())
print(person.address)
print(person.phone)
print(person.email)


