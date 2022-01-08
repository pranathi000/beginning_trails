numbers = ["3", "34", "64"]

numbers = list(map(int, numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers[2])
#
# def s(a):
#     return a*a

# num = [2,3,4,5,6,7,8,9]
# square = list(map())
# print(square)

num = [2,3,4,5,6,7,8,9]
square = list(map(lambda x: x*x, num))
print(square)

# def s(a):
#     return  a*a*a

num = [2,3,4,5,6,7,8,9]
cube = list(map(lambda x: x*x*x, num))
print(cube)

# map function is completed.
