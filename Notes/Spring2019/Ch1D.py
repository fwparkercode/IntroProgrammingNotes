#  Chapter 1 Notes


print("Hello World")

# printing text
print("Hi")  # strings (text) are in quotes
print("Yo")

# print multiple items
print("Francis", "Parker")  # separate by commas (comma adds a space)
print("my number is", 8)

# printing numbers
print(10)  # this is an integer (counting number positive, negative or zero)
print(3.14)  # this is a float (decimal number)
print(5 + 4)
print(5 * (3 + 4))
print("3 + 4")

# Escape codes
print("\"To be or not to be\" --Bill")  # backslash tells python the next character is not code

# \t tab
print("Aaron\tLee")

# \n new line
print("First\nSecond\nThird")
print("First\n\tSecond\n\t\tThird")

print("The file is stored in C:\\\\new folder\\this")

# comments
# single line comment
print("hi")  # single line comments can go at end of code

# multiline comment (uses triple quotes)
'''
Each line is part
of the comment
Useful for troubleshooting
'''

# Assignment Operator (the equal sign)
x = 5  # variable, assignment operator, value in that order
print(x)
x = 6  # we can overwrite variable values
print(x)
x = 5 + 4
print(x)
x = x + 1  # increments x by 1
print(x)
x += 1  # coder way to write the increment (adds 1)
print(x)
x -= 2  # subtract two from self
print(x)

# Variables (the thing to the left of the assignment operator)
# naming rules
# Python uses snake_case variable naming
# Other languages may use camelCase.

# variable names must start with a lower case letter
my_variable = 6  # use THIS one
My_variable = 7  # improper

# numbers are allowed, but CANNOT be at beginning
# 8ball = 8  # NOT THIS
eight_ball = 8  # USE THIS
ball8 = 8  # OR THIS

# special characters are not allowed
# tax% = 0.05  # NO!!!
tax_percentage = 0.05

# spaces are not allowed
# first name = "Me"  # NO!!
first_name = "Me"
# first.name = "Me"  # NO dot notation yet

# ALL CAPS IS FOR CONSTANTS
PI = 3.141592  # All caps means don't change me

#  MATH OPERATORS (+, -, *, /, **, //, %)
x = 5 + 4 - 9 * 3 / 6
print(x)

x = 2 ** 8  # 2^8
print(x)

x = 5 // 3  # floor operator (chops off everything after decimal)
print(x)

x = 7 % 3  # remainder after division  Modulus or modulo
print(x)
x = 17 % 6
print(x)
print(9384578957938 % 2)  # this finds if something is even or odd

# Operator spacing
x=5+3-2*(3/4)  # this works, but is ugly
x    =  5+   3 -2      *(3     /4)  # this works, but is ugly
x = 5 + 3 - 2 * (3 / 4)  # should look like this
print(x)

# Trig and math
import math  # should be at top of file
print(math.e)
print(math.pi)
print(math.cos(math.pi / 2))


# CUSTOM CALCULATORS

# Area of circle
print("\n\nArea of Circle Calculator")
radius = float(input("Radius: "))  # float is a decimal number
area = math.pi * radius ** 2
print("Area:", area)

# input function
'''
input("Press any key to continue: ")  # prompt goes inside the input
age = input("Enter your age: ")  # always records a string
print("You are", age, "years old.")
print("Next year, you will be", int(age) + 1)  # int() function changes the string to number

guess = int(input("What number am I thinking of?: "))  # python works inside out
print("I was thinking of 10, you guessed", guess)
print("end of program")
'''


# Warm up
# Make a speed calculator in miles per hour
# (speed = distance / time)

print("\n\nSpeed Calculator:")
distance = float(input("Enter the miles: "))
time = float(input("Enter the time in minutes: "))
time = time / 60
speed = distance / time
print("Your speed is:", speed, "mph")










