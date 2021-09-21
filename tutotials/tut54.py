
print("THIS TOPIC IS ABOUT OOPS LECTURE 2")
class employee:
    no_of_leaves = 10
    pass

harry = employee()
rohan = employee()

harry.name = "harry"
harry.salary = 455
harry.role = "instructor"

rohan.name = "rohan"
rohan.salary = 500
rohan.role = "student"

print(harry.salary)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(employee.no_of_leaves)

employee.no_of_leaves = 6
print(rohan.no_of_leaves)
print(harry.no_of_leaves)
print(employee.no_of_leaves)
print(rohan.__dict__)
rohan.no_of_leaves = 7
print(rohan.no_of_leaves)
print(harry.no_of_leaves)
print(employee.no_of_leaves)
print(rohan.__dict__)

print("THIS IS MY PRACTICE")
class teacher:
    no_of_leaves = 3
    pass

srilatha = teacher()
chandrika = teacher()
venu = teacher()

print(chandrika.no_of_leaves)
print(venu.no_of_leaves)
print(srilatha.no_of_leaves)

venu.no_of_leaves = 5
print(venu.no_of_leaves)
print(srilatha.no_of_leaves)
print(chandrika.no_of_leaves)

srilatha.no_of_leaves = 4
print(venu.no_of_leaves)
print(srilatha.no_of_leaves)
print(chandrika.no_of_leaves)

chandrika.no_of_leaves = 2
print(venu.no_of_leaves)
print(srilatha.no_of_leaves)
print(chandrika.no_of_leaves)
print(venu.__dict__)