# Chapter 9 - Functions are fun
import math
import random

# Functions make code repeatable
# Functions help us organize code.


# Defining a function
def say_hi(name):
    print("Hello", name)


# call to the function (with parameters)
say_hi("Mr. Lee")
say_hi("Ryan")


# Area of a circle function
def area_circle(radius):
    area = math.pi * radius ** 2
    print("Area =", area)

# Volume of cylinder
def vol_cylinder(radius, height):
    area = math.pi * radius ** 2
    volume = area * height
    print(volume)


area_circle(5)
vol_cylinder(5, 10)
print(area_circle(5)) # this prints None because nothing is returned


# Returning values from a function
def area_circle2(radius):
    area = math.pi * radius ** 2
    return area # sends the value back to the function call

def vol_cylinder2(radius, height):
    area = area_circle2(radius)
    volume = area * height
    return volume


print(area_circle2(5))
print(vol_cylinder2(5, 10))
