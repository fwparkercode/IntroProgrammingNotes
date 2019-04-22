# Chapter 1 - Custom Calculator


a = False
a = not a
print(a)

# Printing strings
print("Hello World")

# Printing multiple items
print("Francis", "Parker")

# Printing numbers and results
print(3.14)  # float (decimal number)
print(3)  # integer (counting number, positive or negative)
print(5 + 7)
3 + 4

# Escape codes ("escapes" the next character after the backslash)
print(
    "\"We live in an embryonic democracy\" --Frank")  # I want to print a quote "We live in an embryonic democracy" --Frank

#  tab \t
print("1\t2\t3")
#  return \n or \r
print("First\n\tSecond\n\t\tThird")
print("The file is stored in C:\\\\new_folder\\this")

# Comments
# This is a single line comment - It is not part of my code.
print("Hi")  # single line comments can be at end of line of code

# Assignment Operators
x = 5  # the equal sign IS the assignment operator
# 5 = x # this is no good.  variable goes on left, value on right
# x + 5 = 6  # this is no good.  works in math class
x = 6 - 5  # this works

# Variables and naming
# numbers are allowed, but not at start of name
eight_ball = 8
# 8ball = 8
ball8 = 8  # this is legal

# no spaces
first_name = "Me"
# first name = "Me"

# no special characters
tax_percentage = 0.05
# tax% = 0.05

last_name = "Lee"
# last.name = "Lee"

# No capitalization (allowed, but not Pythonic)
John = "name"  # legal, but improper
john = "name"

# ALL CAPS for constants
PI = 3.14159265  # ALL CAPS by convention, not mandatory

# case sensitive language
x = 5
X = 6
print(x)

# variables can be changed
x = 6  # overwrites the previous value
print(x)
x = x + 1  # not proper in math, but okay in programming
print(x)

# fancy programmers way to write it...
x += 1  # increment
print(x)
x += 5
print(x)

# Math Operators (+, -, *, /, **, //, %)
y = 5 + 6 - 3 * 8 / 2
print("y =", y)

#  ** is power (2 ** 3 = 8)
y = 2 ** 8
print(y)

# // floor operator (chops off the decimal)
y = 5 // 3
print(y)

# % modulus (returns the remainder from division)
print(234897 % 3)
print(7 % 4)
print(12 % 2)

# Spacing
y = 3 + 5 / 3 * (8 + 2)
print(y)

# you can do it in math, but not in programming
y = 5 * (3 + 2)  # not y = 5(3 + 2)
# y + 1 = 4

# PEMDAS (use it)

# Inputs  (commented out because it's annoying)

#input()  # waits for user input
print("End")

#input("Enter your name: ")  # you can add a prompt

#age = input("Enter your age: ")  # capture the value
#print("You are", age, "years old.")

#print(int(age) + 1)  # cast it as an integer


# libraries and imports
import math
print(math.pi)
print(math.cos(math.pi))
print(math.e)

# concatenation (adding strings)
a = "Francis"
b = "Parker"

print(a + " " + b)  # sticks them together with concatenation


# Custom Equations

import math
print("\nArea of Circle Calculator")
radius = float(input("Enter the radius: "))
area = math.pi * radius ** 2
print("Area:", area)


# Kinetic Energy
print()
print("Kinetic Energy Calculator")
mass = float(input("Enter the mass in kg: "))
velocity = float(input("Enter the velocity in m/s: "))
ke = 0.5 * mass * velocity ** 2
print("Kinetic Energy:", str(ke) + "J")
