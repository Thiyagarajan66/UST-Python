#Multi_Level_Inheritance

class Person:   #ParentClass
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name:  {}'.format(self.name))
        print('Age:  {}'.format(self.age))
        print('Gender:  {}'.format(self.gender))

class employee(Person):   #Child Class
    def __init__(self, name, age, gender, empid, salary):
        Person.__init__(self, name, age, gender)
        self.empid = empid
        self.salary = salary

    def employeeInfo(self):
        print('EmpId:  {}'.format(self.empid))
        print('Salary:  {}'.format(self.salary))


class Fulltime(employee):    #Grand Child Class
    def __init__(self, name, age, gender, empid, salary, experience):
        employee.__init__(self, name, age, gender, empid, salary)
        self.experience = experience

    def FulltimeInfo(self):
        print('experience:  {}'.format(self.experience))


class Contract(employee):     #Grand Child Class
    def __init__(self, name, age, gender, empid, salary, ContractExpiry):
        employee.__init__(self, name, age, gender, empid, salary)
        self.ContractExpiry = ContractExpiry

    def ContractInfo(self):
        print('ContractExpiry:  {}'.format(self.ContractExpiry))


print('Contract Employee details:')
print('**************************')
Contract_obj = Contract('Thiya', 26, 'Male', 1234, 32234, '31-12-22')
Contract_obj.PersonInfo()
Contract_obj.employeeInfo()
Contract_obj.ContractInfo()

print('FullTime Employee details:')
print('**************************')
FullTime_obj = Fulltime('Thiya', 26, 'Male', 1234, 32234, '5yoe')
FullTime_obj.PersonInfo()
FullTime_obj.employeeInfo()
FullTime_obj.FulltimeInfo()
