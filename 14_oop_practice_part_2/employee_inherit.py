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


class extemployee(employee):

    def __init__(self, name, age, company, salary, phone, hobbies):
        super().__init__(name, age, company, salary)
        self.phone = phone
        self.hobbies = hobbies
        self.calctax()

    def printinfo(self):
        super().printinfo()
        print("-----------------------------------------")
        print("PHONE     : ", self.phone)
        print("HOBBIES   : ", self.hobbies)

    def calctax(self):
        tax1 = 0
        tax2 = 0
        tax3 = 0
        tax4 = 0
        if(self.salary <= 250000):
            tax1 = 0
        elif(self.salary > 250000 and self.salary <= 500000):
            tax1 = (self.salary - 250000) * 0.05
        elif(self.salary > 500000 and self.salary <= 1000000):
            tax1 = 12500
            tax2 = (self.salary - 500000) * 0.1
        elif(self.salary > 1000000 and self.salary <= 1500000):
            tax1 = 12500
            tax2 = 50000
            tax3 = (self.salary - 1000000) * 0.2
        elif(self.salary > 1500000 ):
            tax1 = 12500
            tax2 = 50000
            tax3 = 100000
            tax4 = (self.salary - 1500000) * 0.3
        self.tax = tax1 + tax2 + tax3 + tax4
        

    def calchike(self, hikepct):
        self.salary = self.salary + self.salary * (hikepct/100)
        self.calctax()

    def setsalary(self, newsalary):
        self.salary = newsalary
        self.calctax()

    def updatephone(self, newphone):
        self.phone = newphone

    def updatehobbies(self, action, value):
        if(action == 'clear'):
            self.hobbies = []
        elif(action == 'add'):
            self.hobbies.append(value)
        elif(action == "remove"):
            if(value in self.hobbies):
                self.hobbies.remove(value)


# --------------------------------------------------------------------------
ep = employee('anil', 35, 'corecard', 1300000)
e = extemployee('anil', 35, 'corecard', 1300000, '9987673646', ['Cricket'])
e.printinfo()
print()
e.setsalary(2000000)
e.printinfo()
print()
e.calchike(17) 
e.printinfo()
print()
e.updatehobbies('add', 'Cooking')
e.printinfo()
print()
e.updatehobbies('remove', 'Cricket')
e.printinfo()
print()
e.updatehobbies('clear', '')
e.printinfo()
print()
e.updatephone('9777744445')
e.printinfo()
print()

# ---------------------------------------------------------------

print('POLYMORPHISM')

print('with ep')
x = ep
x.printinfo()

print()
print('with e')
x = e
x.printinfo()