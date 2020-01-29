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
