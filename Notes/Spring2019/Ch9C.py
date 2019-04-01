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
    y += 1  # not allowed to change a global here
    return y

print(g())



