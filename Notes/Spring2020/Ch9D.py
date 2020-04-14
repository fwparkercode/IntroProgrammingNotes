# Chapter 9 - FUNctions

# functions help organize our code
# and are repeatable
import math


def say_hi():
    print("Hello")

say_hi()


# functions can also take parameters / arguments
def say_hi2(name):
    print("Hello", name)

say_hi2("Ben")


# return a value
def area_circle(radius):
    area = math.pi * radius ** 2
    return area

print(area_circle(5))


# volume cylinder
def volume_cylinder(height, radius):
    volume = math.pi * radius ** 2 * height
    return volume

print("Volume can", volume_cylinder(6, 2))
print("Volume six pack", volume_cylinder(6, 2) * 6)


# improved volume cylinder
def volume_cylinder(height, radius):
    volume = area_circle(radius) * height
    return volume

print("Volume can", volume_cylinder(6, 2))
print("Volume six pack", volume_cylinder(6, 2) * 6)


# return multiple values
def sum_product(n1, n2):
    total = n1 + n2
    product = n1 * n2
    return total, product

print(sum_product(3, 5))  # multiple returned items are in a tuple
print(sum_product(3, 5)[0])  # index the tuple to get individual values
print(sum_product(3, 5)[1])

# pythonic way of returning multiple items
tot, prod = sum_product(8, 10)
print(tot)
print(prod)


# return and capture
def double_me(n):
    return n * 2

x = 5
x = double_me(x)  # the only way to change a global variable using a function
print(x)


# SCOPE - one of the most misunderstood concepts for new programmers
# The scope of a variable is where it can be ACCESSED and where it is ALIVE
# It is ALIVE where it was born.

# global variables are to the far left and can be SEEN anywhere, but cannot be changed in the local scope.
# local variables can only be SEEN inside the function (where they were born).

def f():
    x = 20


print(x)  # the local variable can not be seen globally.  (this just prints the value of the global x)


# We cannot chagne a global variable in the local space (but we can see it)
y = 3  # global variable

def g():
    print(y ** 2)  # we can see the global y and use it
    # y += 1  # we cannot change a global variable locally

g()


# if we want to change a global variable with a function
def h(z):
    return z ** 2

z = 5
z = h(z)  # returned and capture
print(z)





