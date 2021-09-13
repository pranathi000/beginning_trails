print("HURREY! I have reached 60 vedios in code with harry python")

class employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"the name is {self.name}. salary is {self.salary}, and the role is {self.role}."

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
          return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("This is good " + string)
class programmer(employee):
    no_of_holidaypackages = 45

    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages
    def printprog(self):
         return f"the programmer's name is {self.name}. salary is {self.salary}, and the role is {self.role}.The languages are {self.languages}"

harry = employee("harry", 255, "instructor")
larry = employee("larry", 350, "player")
karan = employee.from_str("karan-480-student")

tom = programmer("subham", 555, "programmer", ["python"])
jerry = programmer("jerry", 456, "programmer", ["python", "c++"])
harry.change_leaves(34)


print(tom.printprog())
print(tom.printdetails())
print(jerry.printdetails())
print(tom.no_of_holidaypackages)