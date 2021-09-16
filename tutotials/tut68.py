# print("ABSTRACT BASE CLASS AND @ABSTRACTMETHOD")
# # from abc import ABCMeta, abstractmethod
# from abc import  ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def pruntarea(self):
#         return 0
#
# class rectangle:
#     type = "rectangle"
#     sides = 4
#     def __init__(self):
#         self.length = 6
#         self.breadth = 7
#     def printarea(self):
#         return self.length * self.breadth
#
# rect1 = rectangle()
# print(rect1.printarea()

print("this or that we can use any of the above or below mentioned methods.")


from abc import ABCMeta, abstractmethod
# from abc import  ABC, abstractmethod
class shape(metaclass = ABCMeta):
    @abstractmethod
    def pruntarea(self):
        return 0

class rectangle:
    type = "rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
    def printarea(self):
        return self.length * self.breadth

rect1 = rectangle()
print(rect1.printarea())



