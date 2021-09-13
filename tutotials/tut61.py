print("THIS VEDIO IS ALL ABOUT MULTIPLE INHERITANCE.\nWHICH IS ONE OF THE IMPORTANT PART IN OOPS!!")

class employee:
    var = 8
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

class player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name= name
        self.game = game

    def printdetails(self):
        return f"The name is {self.name} and the game is {self.game}."

class coolprogrammer(employee, player):
    # var = 10
    language = "c++"

    def printlanguage(self):
        print(self.language)

harry = employee("harry", 255, "instructor")
larry = employee("larry", 350, "player")

tinku = player("tinku", ["cricket"])

minku = coolprogrammer("minku", 8000, "coolprog")
# det = minku.printdetails()
# minku.printlanguage()
# print(det)
print(minku.var)

# print(harry.var)
# print(tinku.var)