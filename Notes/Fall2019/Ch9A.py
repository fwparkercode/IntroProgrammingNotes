# Chapter 9 - Functions are fun
import math
import random

# Functions make code repeatable
# Functions help us organize code.


# Defining a function
def say_hi(name):
    """
    Just says hi to the user
    :param name:
    :return:
    """
    print("Hello", name)


# call to the function (with parameters)
say_hi("Mr. Lee")
say_hi("Ryan")



# Area of a circle function
def area_circle(radius):
    """
    Calculates and prints area of circle
    :param radius:
    :return:
    """
    area = math.pi * radius ** 2
    print("Area =", area)

# Volume of cylinder
def vol_cylinder(radius, height):
    """
    Calculates and prints volume of a cylinder
    :param radius:
    :param height:
    :return:
    """
    area = math.pi * radius ** 2
    volume = area * height
    print(volume)


area_circle(5)
vol_cylinder(5, 10)
print(area_circle(5)) # this prints None because nothing is returned


# Returning values from a function
def area_circle2(radius):
    """
    Calculates and returns area of circle
    :param radius:
    :return: area
    """
    area = math.pi * radius ** 2
    return area # sends the value back to the function call

def vol_cylinder2(radius, height):
    """
    Calculates and returns volume of cylinder
    :param radius:
    :param height:
    :return:
    """
    area = area_circle2(radius)
    volume = area * height
    return volume


print(area_circle2(5))
print(vol_cylinder2(5, 10))


# Variable Scope
# confusing topic

# Scope Example 1
def f():
    x = 20  # local variable

f()
# print(x)  # trying to print the local variable in global scope


# Scope Example 2
y = 5  # global

def g():
    print(y)  # you can see a global variable in local space

g()


# Scope Example 3

z = 12

def h():
    # z += 1  # you can see global, but can't change locally
    print(z)

h()


# Scope rules for Python
# look at where the variable was born to determine global vs. local
# Global variables can be seen but not changed locally.
# Local variables cannot be seen (or changed) at all globally.




# Return and Capture
def double_me(n):
    """
    Doubles the number n
    :param n:
    :return:
    """
    return n * 2

print(double_me(2))
x = 2
x = double_me(x)  # capture the returned value
print(x)


# Multiple returns
# The first return ends the function

def sum_product(n1, n2):
    """return the sum and product of n1 and n2"""
    return n1 + n2
    return n1 * n2  # this line never reached


# Returning multiple items
def sum_product(n1, n2):
    """return the sum and product of n1 and n2"""
    sum = n1 + n2
    product = n1 * n2
    return sum, product  # returns a tuple


print(sum_product(5, 4))
print(sum_product(3, 6)[1])  # tuple can be indexed

sum, product = sum_product(5, 7)  # pythonic way of doing it.\
print(sum, product)




