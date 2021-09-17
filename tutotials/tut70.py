print("OBJECT INTROSPECTION......")
class employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}."
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set. p\Please set it using setter!"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None # n should be capital N
        self.lname = None


skillf = employee("skill", "f")
# print(skillf.email)
print(type(skillf))
print(type("this is book"))
print(id("this is book"))
print(id("this is book"))
print(id("this is book, pen, pencil"))
o = "this is a book"
print(dir(o))
p = "skillf"
print(dir(p))

import inspect
print(inspect.getmembers(skillf))
# google search : inspect modules for more info.





# kisi bhi object ke baare me jaan na ki vo kis class se aaya
# hai , kis type ka hai, kaise store ho raha
# hai, iske baake me jaan ne ko kehte hai onj introspection.




















