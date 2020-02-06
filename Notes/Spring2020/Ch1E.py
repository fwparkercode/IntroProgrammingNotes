#  Chapter 1 - Create a Calculator


# Printing Text
print("Hello World")  # Strings go inside quotes (single or double)
print('hello world')  # strings are just pieces of text
print("2 + 5")  # It prints any character or string
print(2 + 5)  # prints results of expressions
print("Hello", "Class")  # printing multiple items (comma adds a space)
print("Francis", "W", "Parker")
print("Score =", 50 + 10)

# Escape Codes
# Any character can be "escaped" using a backslash
# escaped characters are not treated as code by Python
print("Printing a quote \" is hard")
print("printing a backslash \\too")

# special codes
print("Printing\nreturn\ncarriages")  # \n is the same as hitting enter/return
print("Printing\ttabs\tis\tfun")  # \t is a tab
print("First\n\tSecond\n\t\tThird")

# Comments
# I am a single line comment
'''
I am a multi
line
comment
'''

# comment out
# multiple lines
# using shortcut Command+/


# Assignment Operator (equal sign)
x = 5  # the variable x has been assigned a value of 5
print("x =", x)
x = 6  # value is overwritten
print("x =", x)
x = x + 1  # can't do this in math
print("x =", x)
x + 2  # no effect
print("x =", x)
# x + 1 = y  # works in math, not in programming

# coding shortcut
x += 1  # add to yourself
print("x =", x)
x += 10
print("x =", x)

# Variables
# Python uses snake_case
# different from camelCase, PascalCase or kebab-case

# illegal variable names
# 8ball = 8  # variable names cannot START with numbers
# tax% = 0.11  # variable names cannot have special characters !@#$%^&*()
# first name = "Aaron"  # no spaces
# first.name = "Aaron"  # no dot notation

# improper
Bob = "Bob"
firstName = "Bob"

# These are okay
eight_ball = 8
ball8 = 8
tax_percentage = 0.11
first_name = "Bob"
SCREEN_WIDTH = 1000  # all caps indicates this is a constant that should not be changed
# names are case specific and should be explicit

# Math operators
# +, -, *, /
x = 3 + 4 - 2 * 5 / 3
print(x)

# Floor division //
# drops the remainder after division
x = 5 // 3
print(x)

# Power **
x = 2 ** 3
print(x)
x = 16 ** 0.5  # square root
print(x)

# Modulus %
x = 7 % 4
print(x)
x = 4523789234897 % 2  # check for an even or odd
print(x)


# This works in math, but not here
y = 3
# x = 5y
# x = 5(y)
x = 5 * y  # This is the way!
print(x)


# Operator Spacing
x=5*(3+2-1/2)**2  # works but is improper
x                      =5*(3+2              -1/2      )**2  # works but is improper
x = 5 * (3 + 2 - 1 / 2) ** 2  # space before and after every OPERATOR
print(x)

# PEMDAS COUNTS

# Math library
import math
print(math.pi)
print(math.cos(0.5))  # radians



# Custom equations

# area of a circle
radius = 5
area_circle = math.pi * radius ** 2
print(area_circle)


# The input function
import math
radius = float(input("Enter the radius: "))  # input statement returns only strings (text)
area_circle = math.pi * radius ** 2
print(area_circle)


# input function returns a string
# float("5.0")  # converts a string to a float (decimal number)
# int("5")  # converts to integer (counting number, positive or negative)


#  MPG calculator
print()  # prints a blank line
print("MPG Calculator")
miles = float(input("Enter the miles travelled: "))
gallons = float(input("Enter the gallons used: "))

mpg = miles / gallons
print(mpg, "MPG")


#  Volume of a cube
print("\nVolume of Cube Calculator")
length = input("Enter the length of one face: ")
length = float(length)

volume = length ** 3
print("\nCubic volume:", volume)


# round function
x = 2 / 3
x = round(x, 2)  # rounded to two digits
print(x)

# concatenation (squashing two strings together with a +)
print("Francis", "W", "Parker")
print("Francis" + "W" + "Parker")

percentage = round(67 / 489 * 100, 2)
print(str(percentage) + "%")

