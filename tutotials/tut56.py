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
harry = employee("harry", 255, "instructor")
larry = employee("larry", 350, "player")

harry.change_leaves(34)

print(harry.no_of_leaves)

print("THIS IS MY PRACTICE.")

class jobs:
    no_of_vacancies = 22

    def __init__(self, name, study, creed):
        self.name = name
        self.study = study
        self.creed = creed

    def printdetails(self):
        return f"the job holder name is {self.name}, and their study is {self.study}. their creed is {self.creed}."
    @classmethod
    def change_vacancies(cls, new_vacancies):
        cls.no_of_vacancies = new_vacancies
sumathi = jobs("sumathi", "btech", "female")

jobs.change_vacancies(44)
print(jobs.no_of_vacancies)
print(sumathi.printdetails())
print(sumathi.no_of_vacancies)