#  Chapter 1 Notes

#  Single line comment  - not part of the code

'''
Multi-line comment
If you need to say more
Use this type of comment
'''

print("Hello World")

print("8 + 5 / 3")
print(8 + 5 / 3)

print("Francis", "Parker")  # print multiple items separated by commas
print("Francis", "W.", "Parker")  # Python automatically inserts a space
print("Your Score:", 5 + 8)


# Escape Codes
print("I want to print quotes \" but I can't")  # escape means ignore next character

# \t (tab) and \n (new line)
print("First: Aaron\t\tLast: Lee")
print("First Line\nSecond Line\nThird Line")

# Assignment Operator

# create a variable x
x = 5  # variable on left, value on the right
print(x)

y = 8
print(x + y)

z = x + y
print(z)

name = "Zoey"
print(name)

print(name, "is", z + 2)

# iteration (adding to yourself)
x = x + 1
print(x)

# shortcut iteration
x += 1
print(x)


# Variables and naming

# case specific
x = 1
X = 2
print(x)

# naming conventions
# - use lower case
# - snake_case for multiple words
# - no special characters (underscores allowed)
# - no spaces
# - numbers are okay, but cannot start the name

eight_ball = 8
#8ball = 8

tax_percentage = 0.11
#tax% = 0.11

# Constants use all caps
SCREEN_WIDTH = 700


# Math Operators
# +, - *, /
x = 5 + 3 - 2 * 10 / 5
print(x)

# floor operator //
# returns the value from division and chops off the remainder
x = 5 // 4
print(x)
x = 10 // 3
print(x)

# exponent operator **
y = 3 ** 2  # squared
print(y)
y = 3 ** 0.5  # sqrt
print(y)

# modulus operator %
# return the value of the remainder
z = 5 % 3
print(z)
z = 897458793458790345789 % 2
print(z)
z = 13 % 5
print(z)

# PEMDAS Rules Apply
avg = (4 + 5 + 9 + 3) / 4
print(avg)

#  Not allowed in Programming, but okay in math
# x = 5y  # Wrong
x = 5 * y  # :)
# x = 5(3 + 2) # Wrong
x = 5 * (3 + 2)  # :)

# Spacing
x=8*(4/3+2)  #  legal, but improper
x = 8 * (4 / 3 + 2)  # legal and proper
x     =8       *   (4/3      + 2)  # equivalent, but awful

#  Importing libraries
import math
print(math.cos(3))
print(math.pi)

#  Make a calculator
r = 5
area = math.pi * r ** 2
print(area)

# User input
input("Press Enter to Continue: ")  # waits for user input

my_number = input("Enter a number: ")
#  my_number = int(my_number)  # int() changes value to integer
my_number = float(my_number)  # float() changes to decimal/float
print(my_number ** 2)


# area of circle calculator
print("Area of circle calculator")
r = float(input("Enter the radius: "))  # python functions work inside out
area = math.pi * r ** 2
print("The area of your circle is:", area)

print("end of program")


