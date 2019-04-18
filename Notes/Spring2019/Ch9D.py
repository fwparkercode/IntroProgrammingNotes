# Chapter 9 - FUNctions

# Functions are our friends
# - makes our code easy to read
# - make our code reusable
import math


def hello(name):
    '''
    Prints hello to the user
    :param name:
    :return:
    '''
    print("Hello", name)

# def means define
# hello is the name of my function (normal snake case rules)
# parentheses are required (may contain parameters)
# don't forget the colon.

hello("Dolly")  # call to the function


# Area of a circle

def area_circle(radius):
    area = math.pi * radius ** 2
    print(area)

area_circle(5)
for i in range(10):
    area_circle(i)  # reusable code


# Volume of a cylinder

def volume_cylinder(radius, height):
    volume = math.pi * radius ** 2 * height
    print(volume)

volume_cylinder(10, 10)


# Volume of a six pack (radius = 2, height = 6)
# Use a return to send the answer back to the CALL

def volume_cylinder(radius, height):
    '''
    Calculate the volume of a cylinder and returns the answer
    :param radius:
    :param height:
    :return: volume
    '''
    volume = math.pi * radius ** 2 * height
    return volume

print(volume_cylinder(2, 6))  # one can of soda
print(volume_cylinder(2, 6) * 6) # 6 sodas

# RETURN and CAPTURE
vol_6pack = volume_cylinder(2, 6) * 6
print(vol_6pack)
print("Case:", 4 * vol_6pack)


# FUNCTIONS calling functions (simplify previous functions)

def area_circle(radius):
    area = math.pi * radius ** 2
    return area

def volume_cylinder(radius, height):
    volume = area_circle(radius) * height
    return volume

print(volume_cylinder(2, 6))


# Function that returns the square root and cube root
# You can return more than one thing

def roots(number):
    square_root = number ** 0.5
    cube_root = number ** (1 / 3)
    return square_root, cube_root

print(roots(16))
print(roots(9)[0])
print(roots(27)[1])

x, y = roots(18)
print(x, y)


# SCOPE
# Python has relatively simple scoping rules
# Built in > global > local
# built in variables are Python wide
# global variables are far left (no indent)
# local variables live inside functions


# Rule: local variables cannot be seen in the global scope.
def f():
    a = 1

#print(a)  # local variables are not alive in the global space (this won't work)



# Rule: global variables can be SEEN locally (inside function)
b = 78

def g():
    print(b)

g()


# Rule: global variables can NOT be changed locally (inside function)
c = 11

def h():
    #c += 1  # this is illegal (can't change it here)
    print(c)

h()


# EXAMPLES FROM THE WEBSITE (Do not copy)

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
print()


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
print()


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
print()


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
print()


# Example 6
def a(x):
    x = x + 1


x = 3
a(x)

print(x)
print()


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


# Example 14
def a(my_list):
    print("function a, list =  ", my_list)
    my_list = [10, 20, 30]
    print("function a, list =  ", my_list)


my_list = [5, 2, 4]

print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)


# Example 15
# New concept!
# Covered in more detail in Chapter 12
def a(my_list):
    print("function a, list =  ", my_list)
    my_list[0] = 1000
    print("function a, list =  ", my_list)


my_list = [5, 2, 4]

print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)