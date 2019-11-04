# Chapter 9 - FUNctions
import math

# functions help us organize code
# functions are reusable

# print the area of circle
import random


def area_circle(radius):
    area = math.pi * radius ** 2
    print(area)


area_circle(5)  # call to function


# RETURN area of circle
def area_circle(radius):
    area = math.pi * radius ** 2
    return area


print(area_circle(10))


# print volume cylinder
def volume_cylinder(radius, height):
    volume = area_circle(radius) * height
    return volume

print(volume_cylinder(5, 10))

# Return and capture
volume = volume_cylinder(3, 5)
print(volume * 6)  # volume of a six pack



# Variable Scope
# confusing for most students

# Scoping example 1

def f():
    x = 5  # this is a local variable

f()
# print(x)  # this fails.  x only exists inside the function


# Scoping example 2
y = 10

def g():
    print(y)  # we can see global variables in the local scope


g()


# Scoping example 3
z = 1

def h():
    # z += 1  # You cannot change a global variable locally
    print(z)


h()


# Scoping rules
# a variable lives where it was born
# global variables can be seen, but not changed locally
# local variables can not be seen or changed globally (or in other functions)

# Return and capture

a = 1

def add_one(a):
    a += 1  # add to local variable
    return a  # return local variable

a = add_one(a)
print(a)


#  Multiple returned items

def square_cube(n):
    square = n ** 2
    cube = n ** 3
    return square, cube

print(square_cube(3))  # returns a tuple (immutable)
print(square_cube(3)[1])  # prints the cube only
answer = square_cube(3)
print("square:", answer[0])


# Multiple returns
def coin_toss():
    if random.randrange(2) == 0:
        return "Heads"
    else:
        return "Tails"

print(coin_toss())