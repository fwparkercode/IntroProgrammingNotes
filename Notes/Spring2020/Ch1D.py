#  Chapter 1 - Create a Custom Calculator

#  Print function
print("Hello World")  #  A string is a piece of text with quotes around it
print('hello')  # single and double quotes are equivalent but must match

print("8 + 5")
print(8 + 5)  #  this is an integer, not a string

print("Hello", "World")  # multiple items, space is inserted automatically
print("Francis", "W", "Parker")
print("8 + 5 =", 8 + 5)
print("Score:", 8394)

# Escape Codes  (back slash)
print("printing quotes \" is tricky")  # "Escapes" then next character

# Special Codes
print("FIRST\tMIDDLE\tLAST")   # \t inserts a tab into your string
print("Francis\tWayland\tParker")

print("One\nTwo\nThree")  # \n inserts a return carriage (enter)
print("Ode\n\tTo\n\t\tCode")

# Comments
# I am a single line comment
'''
I am a 
multi
line 
comment
'''

# Assignment Operator (it's just the equal sign)
# variable on the left = value on the right
x = 5  # the variable named 'x' has been assigned a value of 5
print("x =", x)
x = 6
print("x =", x)
x = x + 1  # we can do this in programming, not in math
print("x =", x)
x += 1  # does the same thing
print("x =", x)


# Variables
# variables are named using snake_case
# not camelCase or PascalCase or kebab-case etc.

# Improper variable names
Bob = "Bob"  # no uppercase
X = 5  # no uppercase

# Illegal variable names
# 8ball = 8   # cannot START with a number
# tax% = 0.10  # no special characters
# mr lee = "teacher"  # no spaces
# first.name = "aaron"  # no dot notation (yet)

# Good names
bob = "Bob"
x  = 5
eight_ball = 8
ball8 = 8
mr_lee = "teacher"
first_name = "aaron"

# Math Operators
# +, -, *, /
x = 3 + 2 - 5 * 8 / 2
print(x)

# floor division //
# division that chops off the remainder
x = 3 // 2
print(x)

# power **
print(2 ** 3)
print(16 ** 0.5)

# modulus %
# division that only gives us the remainder
print(9 % 5)
print(7 % 3)
print(524789523497803524897 % 3)

# Operator spacing (space on either side of EVERY operator)
x=5+3-2/(6**0.5)//4  # please don't do this
x         =5+3-2          /(  6**     0.5)   //4  # please don't do this
x = 5 + 3 - 2 / (6 ** 0.5) // 4  # please do this

# Order of operations - PEMDAS rules apply


# Importing libraries (adds functionality to our code)
import math

print(math.pi)
print(math.cos(math.pi))  # trig is in radians
print(math.e)


#  Custom calculator

# simple calculator without inputs
# area of circle
radius = 5
area_circle = math.pi * radius ** 2
print(area_circle)

# Input function
# input()  # this just pauses the program waiting for input and RETURN from user
# input("Press any key to continue: ")  # the input function can use a prompt (string)
# my_input = input("Type something and hit Return")  # returns a string that you can assign
# print("You typed", my_input)
# print("End of program")

# Data Types
my_string = "Hello"  # strings are just text
my_int = -3  # integers are counting numbers (negative, zero, positive)
my_float = 3.5  # floats are decimal numbers

# Casting (switching between data types)
x = int("5")  # the string "5" is converted to integer 5
print(x ** 2)

x = float("5.5")  # string to float conversion
print(x)

x = int(5.5)
print(x)


# Improved Calculator
print("Area of Circle Calculator")
radius = float(input("Enter the radius of the circle"))
#radius = float(radius)
area_circle = math.pi * radius ** 2
print("Area:", area_circle)


# Make your own MPG calculator (mpg = miles / gallons)
print("\nMPG Calculator")
miles = float(input("Enter the miles"))
gallons = float(input("Enter the gallons"))

mpg = miles / gallons

print("MPG:", mpg, "miles/gallon")



# Concatenation (smooshing together the strings)
percentile = 89.8
print(str(percentile) + "%")

first = "Francis"
last = "Parker"
print(first + last)












