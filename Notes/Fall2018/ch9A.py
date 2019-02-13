# Chapter 9 - FUNctions

# Why use functions:
# Make code repeatable
# Organize your code

def hi(name):
    print("Hello", name)

# def means define
# name of function is hi.  Follows normal naming rules (snake_case)
# parentheses contain the parameters of the function

# this is the call to the function
hi("Mr. Lee")
hi("computer")



import math

def volume_cylinder(height, radius):
    """
    Calculate the volume of a cylinder
    :param height: float height of cylinder
    :param radius: float radius of cylinder
    :return: volume
    """
    volume = math.pi * radius ** 2 * height
    #print(volume)
    return volume

volume_cylinder(5, 3)

# returning values from the function
# use return statement to send values back to your program

print(volume_cylinder(5, 3))
vol = volume_cylinder(3, 8)  # return and capture the value
print(vol * 6)



# Scope - the most misunderstood thing in programming.
# scope is where is a variable (or object) alive.
# (where can it be used, and where can it be seen)

x = 5  # this is a global variable (all the way to the left)
# global variables can be seen everywhere.  Can't be changed everywhere

def f1():
    x = 10  # I am a local variable.  I exist only inside the function

f1()
print(x)



y = 21

def f2():
    print(y)

f2()


# if we want to change something with a function, we must return and capture
z = 10

def f3(z):
    z += 1  # local z
    return z

z = f3(z)  # return value from f3 and assign it to the global z
print(z)


# Functions can call functions
def f4():
    print("Hello")
    f5()

def f5():
    print("Goodbye")

f4()


# Returning multiple items

def double_triple(n):
    double = n * 2
    triple = n * 3
    return double  # you only get one return, then it exits the function
    return triple

print(double_triple(5))

def double_triple(n):
    double = n * 2
    triple = n * 3
    return double, triple  # returns a tuple

print(double_triple(5))

double, triple = double_triple(5)  # python specific "special power"
print(double)
print(triple)






# LOW STRESS EXAMPLES (DO NOT COPY, THEY ARE IN YOUR CHAPTER)


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
    x = x + 1  # local varialbe x

x = 3 # global
a(x)

print(x) # global


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



print("Example 10")
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



def hi():
    print("Hello")

hi()

# Write a function that returns the total and the average.  Return and print both.

def total_avg(any_list):
    total = 0
    for num in any_list:
        total += num
    average = total / len(any_list)
    return total, average

my_list = [4, 5, 6, 3, 5]
total, average = total_avg(my_list)
print(total)
print(average)


print(int(input("Hello")))








