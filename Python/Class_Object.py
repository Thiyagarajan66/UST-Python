#All classes have fucntion _init_(), which is always executed when the class is being initiated.

#When we can use _init_() function to assign values to object properties or other operations that are necessary to perform when the object is being created

#Self parameter is the reference to the current instance of the class and is used to access class variable.
"""
class myclass:       
    "DocString"
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    def myfucn1(self):
     print(self.var1)
     print(self.var2)"""
#=========================================================================================================================================

#create an emplyee class

class Employee:
    def __init__(self, name, empid):  # __init__() funtion is used to assign values
        self.name = name
        self.empid = empid

    def greet(self):  #Self parameter is the reference to the current instance of the class and is used to access class variable.
        print("Thanks for joining rhe zxh company {} !!".format(self.name))

#Create an emplyee object
emp1 = Employee("Thiya", 193775)   #Create an employee object
print('Name:', emp1.name)
print('Employee ID:', emp1.empid)
emp1.greet()

#create another object with new emplyoee

emp2 = Employee("jerry", 261095)
print('Name: ', emp2.name)
print('Employee ID:', emp2.empid)
emp2.greet()

emp1.country = 'INDIA'
print(emp1.country)


#modify the values
emp1.name = 'candy'
print(emp1.name)


#Delete the object properties
del (emp1.empid)
#This will be given the error -Attribute error
emp1.empid  #After deletion the Object properties we try to access the property, it will throw the attribute error

#delete an Object
del emp1

#This will give the name errror
emp1   #after deletion the object we try to access the emp1 it will throw the name error


    
