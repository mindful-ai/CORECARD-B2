'''
    name 
    age
    company
    salary
    tax
    hike

    printinfo, calctax, calchike
'''

class employee:

    # Class variable
    empCount = 0

    # Data
    def __init__(self, name, age, company, salary):
        self.name = name
        self.age = age
        self.company = company
        self.salary = salary
        self.tax = 0
        self.hike = 0
        employee.empCount += 1 

    # Methods

    def printinfo(self):
        print("NAME     : ", self.name)
        print("AGE      : ", self.age)
        print("COMPANY  : ", self.company)
        print("-----------------------------------------")
        print("GROSS SALARY : ", self.salary)
        print("TAX          : ", self.tax)
        print("-----------------------------------------")
        print("NET SALARY   : ", self.salary - self.tax)

    def calctax(self, taxpct):
        self.tax = self.salary * (taxpct/100)

    def calchike(self, hikepct):
        self.salary = self.salary + self.salary * (hikepct/100)

    def setsalary(self, salary):
        pass

# -------------------------------------------------------------------

emp = employee("Anil", 30, "Infosys", 1500000)
emp.printinfo()
print()
emp.calctax(17)
emp.printinfo()
print()
emp.calchike(10)
emp.calctax(17)
emp.printinfo()

emp1 = employee("Sunil", 30, "Infosys", 1500000)
emp2 = employee("Ajay", 30, "Infosys", 1500000)

print("Number of employees : ", emp.empCount)