# def func1(name, age):
#     print(name, age)
#     return func1
# #Function that takes two arguments, name and age, and print their value.

# func1("Hollie",26)

# def func2(*args):
#     for i in args:
#         print(i)

# #Function that accepts any number of arguments and prints them
# func2(50,2000,122,2)

# def calculation(a,b):
#     return a+b, a-b

# add_sub = calculation(2,3)
# print(add_sub)

# def show_employee(name, salary=9000):
#     print("Name:", name, "salary:", salary)
#     return name, salary
# #= provides a default value if there is no argument passed
# show_employee("Ben", 12000)
# show_employee("Jessa",)

# def outer_calc(a,b):
#     def inner_calc(a,b):
#         return a + b
#     calc = inner_calc(a,b)
#     return calc + 5

# result = outer_calc(5,5)
# print(result)
#Create an outer function that will accept two parameters, a and b
#Create an inner function that will calculate the addition of a and b
#Outer function will add 5 into addition and return it

# def sum(num):
#     if num:
#     # call same function by reducing number by 1
#         return num + sum(num-1)
#     else:
#         return 0
    
# res = sum(10)
# print(res)

#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

# def display_student(name, age):
#     print(name, age)

# show_student = display_student

# show_student("Emma", 26)

# print(list(range(4, 30, 2)))
# #Generate a Python list of all the even numbers between 4 to 30

# x = [4, 6, 8, 24, 12, 2]
# print(max(x))