class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 =  "I am insides class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "special"
class B (A):
    classvar1 = " I am in class B"
    def __init__(self):
        # super().__init__()
        self.var1 =  "I am insides class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        print(super().classvar1)

a = A()
b = B()

# print(b.classvar1)
# # print(b.classvar2)
# print(a.classvar1)

print(b.special, b.var1, a.var1, b.classvar1)

#     super method can only be used after the def__init__.
# otherwise it may alter all the sequence.



print("THIS IS MY PRACTICE.")


class A:
    classvar1 = "I am shalini . I am in 10th A section."
    def __init__(self):
        self.var1 = "I am inside 10th A ."
        self.classvar1 = "I am a friend of malini."
        self.teacher = "vinod"

class B(A):
    classvar1 = "I am pallavi . I am in 10th B section."
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside 10th B ."
        self.classvar1 = "I am a friend of supriya."
a = A()
b = B()

print(a.classvar1, a.var1)
print(b.classvar1, b.var1)
print(a.classvar1, b.var1)
print(b.classvar1, a.var1)