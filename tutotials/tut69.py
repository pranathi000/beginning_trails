print("THE TOPIC IS ABOUT SETTERS AND PROPERTY DECORATORS..")
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


hindusthani_supporter = employee("hindusthani", "supporter")
# nikhil_raj_pandey = employee("nikhil", "raj")

print(hindusthani_supporter.explain())
print(hindusthani_supporter.email)

hindusthani_supporter.fname = "US"

print(hindusthani_supporter.email)
hindusthani_supporter.email = "this.that@codewithharry.com"

print(hindusthani_supporter.email) #this  output



del hindusthani_supporter.email
# output cant delete attribute.
print(hindusthani_supporter.email)


# there is much thing that should be learnt through this code.
# firstly, print(hindusthani_supporter.email()) after email bracket is very important. other wise when the code is compiled
# you may get some type of unknown message.
# secoondly, we can also write the code without brackets. but we have to provide a command for that.
# @property must be used above the  email constructor...
#  so that u can easily get the desired out put without the brackets.
















