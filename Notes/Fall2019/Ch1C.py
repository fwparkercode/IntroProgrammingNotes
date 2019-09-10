# Chapter 1 - Create a Custom Calculator

# Started 9/9/19
# Printing
print("Hello World")  # printing a string
print(5)  # printing an integer
print(1.23) # printing float (decimal)

# Printing results of equations
print(5 + 3)

# Printing multiple items
print("Francis", "Wayland", "Parker")  # automatically puts space in between each
print("5 + 3 =", 5 + 3)

# Escape Codes
# backslash (above return) \
# tells Python to ignore the next character as code
print("Mr. Lee said \"hi\" to the class")

# tab \t
print("First\tMiddle\tLast")
print("Francis\tWayland\tParker")

# new line (return/enter) \n
print("first\nsecond\nthird")

print("Programming\n\tis\n\t\tfun")
print("file located at c:\\new_folder\\this_file")


# Comments
# I am a single line comment
'''
I am a 
multi
line
comment
Sometimes I am handy for troubleshooting
'''

#  Assignment Operator (equal sign)
# the only way to assign a value to a variable name
x = 5  # variable name is x.  Assigned a value of 5.
print(x)
print(x + 10)
print(x)
x + 10  # has no effect
print(x)

x = x + 10  # you can use the variable itself when assigning value
print(x)

x += 10  # does the same thing
print(x)


# Variables
x = 5
X = 6
print(x)  # python is case sensitive

# python uses snake_case, not camelCase, PascalCase, or kebab-case.
first_name = "Francis"  # correct snake_case
# first name = "Francis"  # illegal (no spaces allowed)
# first.name = "Francis"  # illegal (no dots)

eight_ball = 8  # correct
# 8ball = 8  # illegal cannot start with a number
ball8 = 8  # this could also be correct



# Continued 9/10/19
tax_percentage = 0.11
# tax% = 0.11  # illegal, no special characters

# CONSTANTS
PI = 3.14  # constants are written with all caps



# Math Operators
x = 3 + 5 - 2  # addition and subtraction
y = 4 * 3 / 4  # multiplication and division
print(x, y)

# floor operator //   division that chops off the decimal remainder
print(5 / 3)
print(5 // 3)
print(2 // 3)

# power **
print(3 ** 2)
print(2 ** 8)  # 2^8

# modulus %   returns the remainder after division
print(13 % 5)
print(4237689 % 2)  # odd/even check
print(7 % 5)


# These do not work in coding
# x = 3y
x = 3 * y  # correct
# x = 5(y - 1)
x = 5 * (y - 1)  # correct


# Spacing
x=3*y-8/(6+2)  # legal but not pretty
x   =  3*    y-   8/(   6+   2)  # legal but hideous
x = 3 * y - 8 / (6 + 2)  # PEP-8 proper

# PEMDAS used just like math


# Importing libraries
import math

print(math.pi)
print(math.cos(math.pi / 2))  # works in radians



