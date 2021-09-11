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

harry = employee("harry", 255, "instructor")
larry = employee("larry", 350, "player")
karan = employee.from_str("karan-480-student")

harry.change_leaves(34)


print(karan.printgood("pranathi"))
print(employee.printgood("pranathi"))
print(karan.no_of_leaves)
print(karan.printdetails())