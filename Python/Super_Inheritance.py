#Super built in function that allow us to access the methods of the base class

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name:  {}'.format(self.name))
        print('Name:  {}'.format(self.age))
        print('Name:  {}'.format(self.gender))

class student(Person):
    def __init__(self, name, age, gender, stuid, fees):
        super().__init__(name, age, gender)
        self.stuid = stuid
        self.fees = fees

    def studentInfo(self):
        super().PersonInfo()
        print('Student ID: {}'.format(self.stuid))
        print('Student ID: {}'.format(self.fees))

        
stu_obj = student('Candy', 26, 'Male', 787687, 89758765)
stu_obj.studentInfo()
        
