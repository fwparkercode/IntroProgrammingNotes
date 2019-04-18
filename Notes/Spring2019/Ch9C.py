# Chapter 9 - Functions

# Functions are a programmers best friend
# - Makes code easy to read
# - Makes code reusable  (DRY - Don't Repeat Yourself)
import math


def hello_world():
    print("Hello World")

# DEF "defines" the function
# hello_world is the name of the function (normal naming rules apply)
# parentheses hold the PARAMETERS for the function (this one has none)

# A function is a set of instructions.
# to call the function, we need to include the CALL code.
hello_world()
hello_world()


# area of a circle

r = 5
area = math.pi * r ** 2
print(area)

# make a function out of it.
def area_circle(radius):
    area = math.pi * radius ** 2
    print(area)

area_circle(10)


# make a function for the volume of a cylinder
def volume_cylinder(radius, height):
    area = math.pi * radius ** 2
    volume = area * height
    print(volume)

volume_cylinder(9, 10)


# find the volume of a six pack of soda (r = 2 and height = 6)
# return the value to my program to do this
def volume_cylinder(radius, height):
    area = math.pi * radius ** 2
    volume = area * height
    return volume  # sends the value back to the CALL in the program

print(volume_cylinder(2, 6) * 6)


# Return AND capture a value
def cube(number):
    return number ** 3

print(cube(3))
captured_value = cube(4)  # captures the value to use in your program
print(captured_value)
captured_value +=1
print(captured_value)


# make a function which RETURNS the average of three numbers
# call the function and print the result

def average(a, b, c):
    avg = (a + b + c) / 3
    return avg

print(average(2, 3, 4))


# SCOPE
# if you want to know where a variable lives, look where it was born.
# Built-in > Global > Local(inside def)

def f():
    x = 10  # this is a local variable

f()
#print(x) # causes error because you cannot access a local variable in the global scope


# The previous is different than this
x = 5 # this is a global variable

def f():
    x = 10
    return x

x = f()
print(x)


# We can see, but cannot change a global variable in the local scope
y = 10

def g():
    #y += 1  # not allowed to change a global here
    return y

print(g())


# Summarizing the scoping rules
# - Functions can "see" global variables but they cannot change them
# - Local variables cannot be seen in the global scope


# Returning multiple items

def double_triple(number):
    return number * 2, number * 3

print(double_triple(4))
print(double_triple(4)[0])

double, triple = double_triple(13)  # Python is unusual in allowing this
print(double, triple)


#  Make a function that takes a string as a parameter and
# returns the number of e's in the text (upper and lower case)


my_text = '''Those three lines of code don't really pop out as obviously drawing a tree! If we have multiple trees or complex objects, it starts getting hard to understand what is being drawn.

By defining a function we can make the program easier to read. To define a function, start by using the def command. After the def command goes the function name. In this case we are calling it draw_tree. We use the same rules for function names that we use for variable names.

Following the function name will be a set of parentheses and a colon. All the commands for the function will be indented inside. See the example below:'''

def number_e(text):
    e = 0
    for char in text:
        if char.lower() == "e":
            e += 1
    return e

print(number_e(my_text))


# FROM CHAPTER

# Example 1
def a():
    print("A")


def b():
    print("B")


def c():
    print("C")


a()


# Example 2
def a():
    b()
    print("A")


def b():
    c()
    print("B")


def c():
    print("C")


a()


# Example 3
def a():
    print("A")
    b()


def b():
    print("B")
    c()


def c():
    print("C")


a()


# Example 4
def a():
    print("A start")
    b()
    print("A end")


def b():
    print("B start")
    c()
    print("B end")


def c():
    print("C start and end")


a()


# Example 5
def a(x):
    print("A start, x =", x)
    b(x + 1)
    print("A end, x =", x)


def b(x):
    print("B start, x =", x)
    c(x + 1)
    print("B end, x =", x)


def c(x):
    print("C start and end, x =", x)


a(5)


# Example 6
def a(x):
    x = x + 1


x = 3
a(x)

print(x)


# Example 7
def a(x):
    x = x + 1
    return x


x = 3
a(x)

print(x)


# Example 8
def a(x):
    x = x + 1
    return x


x = 3
x = a(x)

print(x)


# Example 9
def a(x, y):
    x = x + 1
    y = y + 1
    print(x, y)


x = 10
y = 20
a(y, x)


# Example 10
def a(x, y):
    x = x + 1
    y = y + 1
    return x
    return y


x = 10
y = 20
z = a(x, y)

print(z)


# Example 11
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y


x = 10
y = 20
z = a(x, y)

print(z)


# Example 12
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y


x = 10
y = 20
x2, y2 = a(x, y)  # Most computer languages don't support this

print(x2)
print(y2)


# Example 13
def a(my_data):
    print("function a, my_data =  ", my_data)
    my_data = 20
    print("function a, my_data =  ", my_data)


my_data = 10

print("global scope, my_data =", my_data)
a(my_data)
print("global scope, my_data =", my_data)




