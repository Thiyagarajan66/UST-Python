# Inheritence
"""
1) Inheritence is the powerfull feature in object oriented prohramming.

2) Inheritence provides the code resuablility in the program, because we can use the existing class.

3) (Super class / Parent classs/ Base class) To create a new class(subclass/ child class/ derived class) instead of creating it from the scratch.

4) The child class inherits the data definitions and methods from the parent class which facilitates the reuse of feautres already available .
   Child class can add few more definitions or redefine base class method. """
#=====================================================================================================================================

class Person:     #ParentClass
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name: {}'.format(self.name))
        print('age: {}'.format(self.age))
        print('gender: {}'.format(self.gender))


#Child Classs1

class student(Person):
    def __init__(self, name, age, gender, stuid, fees):
        Person.__init__(self, name, age,gender,)
        self.stuid = stuid
        self.fees = fees

    def StudentInfo(self):
        print('Student ID: {}'.format(self.stuid))
        print('Fees: {}'.format(self.fees))

#Child Classs2

class Teacher(Person):
    def __init__(self, name, age, gender, empid, salary):
        Person.__init__(self, name, age, gender)
        self.empid = empid
        self.salary = salary
    def TeacherInfo(self):
        print('EmplyeeID: {}'.format(self.empid))
        print('Salary: {}'.format(self.salary))
    
stu_obj = student('Candy', 25, 'Male', 12345, 10000)
print('Student details: ')
print('---------------------------------')
stu_obj.PersonInfo()        #PersonInfo method present in parent class and it will be accessible
stu_obj.StudentInfo()    









    
    
        
        
    
