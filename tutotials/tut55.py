class employee:
    no_of_leaves = 10
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"name is {self.name}.salary is {self.salary} and role is {self.role}."


harry = employee("harry", 455, "instructor")
# rohan = employee()

# harry.name = "harry"
# harry.salary = 455
# harry.role = "instructor"
#
# rohan.name = "rohan"
# rohan.salary = 500
# rohan.role = "student"

print(harry.salary)



print("THIS IS MY PRACTICE.")
class teacher:
    no_of_leaves= 10
    def __init__(self, name, salary, age, religion, gender):
        self.name = name
        self.salary = salary
        self.age = age
        self.religion = religion
        self.gender = gender
    def printdetails(self):
        return f"The name of the teacher is {self.name}. \nThe Teacher gets a salary of {self.salary} every month. \nThe teachers age is {self.age} and the teacher belongs to {self.religion} religion. \nThe sex of the teacher is {self.gender}."
venu = teacher("venu", 20000, 36, "Hindu", "male")
bhargavi = teacher("bhargavi", 25000, 30, "Hindu", "Female")

print(venu.printdetails())

print(bhargavi.printdetails())

