#  Chapter 1 Notes

#  Single line comment  - not part of the code

"""
Multi-line comment
If you need to say more
Use this type of comment
"""

# Printing
print("Hello World")  # print a string, strings have quotes around them
print(3 + 4)  # can print numbers (and do math inside the print statement)
print("3 + 4")  # this is a string

print("Francis", "Parker")  # separated by space, with a \n at end
print("Francis", "Wayland", "Parker")
print("High Score:", 1000 + 200)

first = "Francis"
last = "Parker"
print(first, last)

# Escape Codes (backslash)
print("I want to print a quote \", but it doesn't work")
# backslash means ignore the next character (it is not code)

# tab and new line (\t and \n)
print("Aaron\tMikel\tLee")
print("First\nSecond\nThird")
print("First\n\tSecond\n\t\tThird")



#  Assignment Operators (only way to change a variable
x = 10  # the variable "x" is assigned a value of 10
y = 5  #variable name on left, value on right
print(x)
print(x, y)
print(x + y)

z = x + y
print(z)
print("z =", z)

# Increment
z = z + 1  # can't do this in math, but you can in programming
print(z)

# shorthand increment
z += 2
print(z)

# Variables
X = 1
x = 2
print(X)  # python is case specific

# naming rules
# - should be all lower case
# - should use snake_case
# - cannot use special characters (underscore is okay)
# - cannot start with a number (okay to use numbers)
# - cannot use spaces

eight_ball = 8
#  8ball = 8

tax_percent = 0.09
#  tax% = 0.09

# constants are in ALL_CAPS
PI = 3.1415926
RED = (255, 0, 0)

# MATH OPERATORS (+, -, /, *, //, **, %)
x = 5
# y = 5x  # This is illegal
y = 5 * x  # this works instead
# y = 5(3 + x)  # also illegal
y = 5 * (3 + x)

z = 3 + 4 - 2 * 8 / 2  # PEMDAS rules apply

# Floor division (//)
# divides two numbers and chops off the remainder.
a = 14 // 4
print(a)

# Exponent (**)
b = 3 ** 2  # square
print(b)
c = 5 ** 0.5 # sqrt
print(c)

# Modulus (%)
# returns the remainder from division
d = 7 % 3
print(d)
e = 13 % 7
print(e)
f = 8 % 2
print(f)

# Spacing
x=5+2*(4/3)**2  # Ugly
x    =    5    +  2 *  (4 / 3) **      2  # hard to read
x = 5 + 2 * (4 / 3) ** 2


# Math Library
import math  # import statement pulls in a library (this one is called math)
print(math.pi)
print(math.cos(math.pi))

# Make a calculator
r = 5
area = math.pi * r ** 2
print(area)

# User input
input("Press Return to Quit")  # input function, takes in one parameter (prompt)

# we can also grab the value of the input
name = input("What is your name?")
print("Hello", name, ", my name is Python.")

x = input("Enter a number: ")
x = float(x)
print(x ** 2)

# Improved area of circle
r = float(input("Enter the radius of the circle: "))
area = math.pi * r ** 2
print("The area of the circle is:", area)


