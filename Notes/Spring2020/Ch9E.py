# Chapter 9 - FUNctions

# functions help us organize our code
# make code repeatable
import math
import random


def hi():
    print("Hello!")

hi()


# using parameters
def hey_you(time_of_day, name):
    print("Good", time_of_day, name)

hey_you("morning", "G Awesome")
hey_you("afternoon", "Gabriela")


# area of a circle

def area_circle(radius):
    area = math.pi * radius ** 2
    print("Area circle:", area)

area_circle(5)
area_circle(7)

# it's repeatable
for r in range(100):
    area_circle(r)


# returned values
def area_circle(radius):
    area = math.pi * radius ** 2
    return area

print(area_circle(5))
print("Area circle:", area_circle(7))


def volume_cylinder(height, radius):
    volume = area_circle(radius) * height
    return volume

print(volume_cylinder(5, 3))

# maybe I wanted to calculate the volume of a six pack
print(6 * volume_cylinder(6, 2))




# Returning AND capturing a value
def add_two_numbers(n1, n2):
    total = n1 + n2
    return total

print(add_two_numbers(2, 3))
my_sum = add_two_numbers(10, 5)  # return and capture
print(my_sum)

# Return multiple values
def product_sum(n1, n2):
    total = n1 + n2
    product = n1 * n2
    return product, total

print(product_sum(4, 5))  # returns multiple values as tuple
print(product_sum(4, 5)[1])  # only the product which is index zero


# SCOPE
# often misunderstood by new programmers
# Variable scope is where the variable is ALIVE and where it can be ACCESSED
# If you want to know where a varialbe is alive, look at where it was born

# global variables can be SEEN anywhere
# local variables can be SEEN only inside the function

def f():
    x = 10  # this variable is LOCAL

f()
# print(x)  # local variables cannot be SEEN in the global scope




y = 5  # this is GLOBAL

def f2():
    print(y)  # global can be SEEN locally

f2()




z = 11

def f3():
    # z += 1  # cannot change a global variable in the local scope (can only SEE it)
    print(z)

f3()


# "Rules for scope"
# We can see GLOBAL variables in the LOCAL scope but cannot change them
# We cannot see or change LOCAL variables in the GLOBAL scope


# RETURN AND CAPTURE (how we get around some scope issues)
def double_me(x):
    return x * 2  # return

x = 5
x = double_me(x)  # capture in global scope
print(x)


# make a function that returns a list of five random numbers from 1 to 6

def yahtzee_roll():
    roll_list = []
    for i in range(5):
        roll = random.randrange(1, 7)
        roll_list.append(roll)
    return roll_list

for i in range(100000):
    my_roll = yahtzee_roll()
    if my_roll == [6, 6, 6, 6, 6]:
        print("WINNER!")
