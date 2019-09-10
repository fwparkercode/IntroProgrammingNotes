# Chapter 1 - Create a Calculator

print("Hello")  # strings go inside quotes

# Printing results of expressions
print("3 + 2")
print(3 + 2)  # no quotes

# Printing multiple items
print("3 + 2 =", 3 + 2)  # separated by commas
print("Francis", "Parker")  # adds a space in between each item

# Escape codes
# backslash "escapes" the next character.  Python treats that character as text
print("I need to print a double quote \", how do you do it?")

# tab escape code, just like hitting the tab key
print("First\tMiddle\tLast")
print("Francis\tWayland\tParker")

# return escape code, just like hitting the enter/return key
print("line1\nline2\nline3")
print("Programming\n\tis\n\t\tfun")

print("file at c:\\this folder\\new folder")

# Comments
# this is a single line comment

'''
This is a multi
line comment
Very useful for troubleshooting
print("code inside any comment will not run")
'''

# Assignment Operator
# the equal sign

# Only one way to create a variable
x = 5  # the variable named x is given a value of 5
print("x")
print(x)
print("x =", x)

print(x + 1)
print(x + x)
print(x)

x = 10  # this changes the value of x
print(x)

x + 1
print(x)

x = x + 1  # you can do this in coding, not in math class
# x + 5 = 3 # this is legal in math, but not in code
print(x)

# Python uses snake_case for variable naming
# Other languages might use camelCase or PascalCase or kebab-case

# Rules for variable naming
# no special characters except _
# snake case with no capitalization
# numbers are ok, but cannot be first character

# first name = "Bob"  # no spaces
first_name = "Bob"  # that's better

# 8ball = 8  # cannot start with number
eight_ball = 8  # fixed

# tax% = 0.11  # no special characters
tax_percentage = 0.11  # fixed


# Math Operators

x = 4 + 5 - 2  # addition and subtraction
y = 3 * 2 / 4  # multiplication and division

# floor division (//) divides and chops off decimal remainder
z = 5 // 3
print(z)

# modulus (%) divides and returns only the remainder
a = 7 % 4
print(a)

# power (**)
b = 3 ** 3
print(b)

#  These do not work in code (works in math class)
#c = 5x
c = 5 * x  # fixed

#d = 5 (x + 2)
d = 5 * (x + 2)

# Operator spacing
x=3*2/(8-3)**2  # works but is improper
x        =3*        2/   (   8  -3 ) **    2    # works but is improper
x = 3 * 2 / (8 - 3) ** 2  # works and is proper

# PEMDAS Applies!  Be explicit


# Importing libraries
import math
print(math.pi)
print(math.cos(math.pi / 2))




# Custom calculators

# user input
#input()  # waits for user response

#name = input("What is your name? ")  # also accepts a prompt
#print("Hello", name, "how are you today?")

# find the area of a circle
#radius = input("Enter the radius: ")
#radius = float(radius)

radius = float(input("Enter the radius: "))
area = math.pi * radius ** 2
print(area)


