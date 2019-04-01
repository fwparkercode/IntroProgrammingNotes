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

def f():
    a = 1

print(a)




