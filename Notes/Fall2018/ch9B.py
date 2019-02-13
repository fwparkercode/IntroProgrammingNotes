# Chapter 9 - FUNctions (we put the fun in functions)

# functions help organize our code
# functions are repeatable


def area_triangle(base, height):
    print("Area =", base * height / 2)


area_triangle(5, 10)  # call of the function
area_triangle(6.4, 8.3)


# Functions

def hi():
    """
    Say hi to the user
    :return:
    """
    print("Hello")

hi()  # call to the function


def hi_there(name):
    print("Hello", name)

hi_there("Mr. Lee")



# Returned values

import math

def volume_cylinder(height, radius):
    """
    Calculate the volume of a cylinder
    :param height: float height of cylinder
    :param radius: radius of the cylinder
    :return: volume
    """
    volume = math.pi * radius ** 2 * height
    return volume

volume_cylinder(5, 3)  # calls to functions are "replaced" by the returned value
print(volume_cylinder(5, 3))
print(volume_cylinder(6, 2) * 6)  # volume of a six pack of soda


# Returning and capturing values

def add_two_numbers(n1, n2):
    return n1 + n2

print(add_two_numbers(2, 3))
my_sum = add_two_numbers(2, 3)  # captured the returned value into a new variable
print(my_sum)

# Scope - Perhaps the most misunderstood concept by new programmers
# Variable scope is where the variable is ALIVE and where it can be ACCESSED

# global variables can be SEEN anywhere
# local variables can be SEEN inside the function only

def f():
    x = 10  # this is a local variable

f()  # call the function
# print(x)  # cannot print a local variable in the global space


# We can SEE global variables inside functions
y = 10

def f2():
    print(y)

f2()



# We cannot change a global variable in the local space (local scope)
z = 11

def f3():
    # z += 1
    print(z)

f3()


# If we want to change a value, we need to return and capture
a = 5

def f4(a):
    a += 1
    return a

print(a)  # prints 5
a = f4(a)
print(a)  # prints 6, function added one


# Returning multiple items

def double_triple(n):
    double = n * 2
    return double  # function stops at the first return
    triple = n * 3
    return triple

def double_triple(n):
    double = n * 2
    triple = n * 3
    return double, triple  # returns a tuple of len 2

print(double_triple(5)[1])  # you can then index the tuple



# Example 1
def a():
    print("A")


def b():
    print("B")


def c():
    print("C")


a()




print("Example 2")
def a():
    b()
    print("A")
 
def b():
    c()
    print("B")
 
def c():
    print("C")
 
a()


print("Example 3")
def a():
    print("A")
    b()
 
def b():
    print("B")
    c()
 
def c():
    print("C")
 
a()


print("Example 4")
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

print("Example 5")
def a(x):
    print("A start, x =",x)
    b(x + 1)
    print("A end, x =",x)
 
def b(x):
    print("B start, x =",x)
    c(x + 1)
    print("B end, x =",x)
 
def c(x):
    print("C start and end, x =",x)
 
a(5)


print("Example 6")
def a(x):
    x = x + 1
 
x = 3
a(x)
 
print(x)




print("Example 7")
def a(x):
    x = x + 1
    return x
 
x = 3
a(x)
 
print(x)




print("Example 8")
def a(x):
    x = x + 1
    return x
 
x = 3
x = a(x)
 
print(x)


print("Example 9")
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


print("Example 11")
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y
 
x = 10
y = 20
z = a(x, y)
 
print(z)



print("Example 12")

def a(x, y):
    x = x + 1
    y = y + 1
    return x, y
 
x = 10
y = 20
x2, y2 = a(x, y) # Most computer languages don't support this
 
print(x2)
print(y2)




print("Example 13")

def a(my_data):
    print("function a, my_data =  ", my_data)
    my_data = 20
    print("function a, my_data =  ", my_data)
 
my_data = 10
 
print("global scope, my_data =", my_data)
a(my_data)
print("global scope, my_data =", my_data)



print("Example 14")

def a(my_list):
    print("function a, list =  ", my_list)
    my_list = [10, 20, 30]
    print("function a, list =  ", my_list)
 
my_list = [5, 2, 4]
 
print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)



print("Example 15")
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



my_list = [4, 5, 6]


def total_avg(any_list):
    total = 0
    for num in any_list:
        total += num
    avg = total / len(any_list)
    return total, avg


total, avg = total_avg(my_list)
print(total, avg)
print(total_avg(my_list))











