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
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        # alternative for these three lines in the form of one line command.
          return cls(*string.split("-"))

harry = employee("harry", 255, "instructor")
larry = employee("larry", 350, "player")
karan = employee.from_str("karan-480-student")

harry.change_leaves(34)


print(karan.salary)
print(karan.no_of_leaves)
print(karan.printdetails())


print("THIS IS MY PRACTICE.")
class teachers:
    no_of_leaves = 4

    def __init__(self, aname, acreed, astudy):
        self.name = aname
        self.creed = acreed
        self.study = astudy

    def printdetails(self):
        return f"the name is {self.name}, the creed is {self.creed}, and the study is {self.study}."
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))

kumar = teachers.from_str("kumar-male-btech")
kumar.change_leaves(8)
print(kumar.no_of_leaves)
print(kumar.printdetails())
print(kumar.creed)
