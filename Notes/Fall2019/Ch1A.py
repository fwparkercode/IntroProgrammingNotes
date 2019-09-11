# Chapter 1 - Create a Calculator

print("Hello")  # strings (text) are inside quotes
print("5 + 3")  # this is also a string
print(12378)  # we can print numbers too (no quotes)
print(5 + 3)  # we can do math inside the print statement

# Printing Multiple Items
print("Francis", "Parker")  # automatically adds a space between
print("Francis", "Wayland", "Parker")
print("5 + 3 =", 5 + 3)

# Escape Codes (backslash \)
# the backslash "escapes" the following character.  Tells python to ignore it as code.
print("Mr. Lee said \"Hi\" to the students.")

# tab \t (just like hitting the tab key)
print("First\tMiddle\tLast")
print("Francis\tWayland\tParker")


# return or newline \n (like hitting return or enter)
print("line1\nline2\nline3")
print("Programming\n\tis\n\t\tfun")
print("c:\\new_folder\\this_file")


# Comments
# Single line comment
'''
Multi
Line
Comment
'''

# Assignment Operator (equal sign)
x = 5  # variable name is x.  x is assigned a value of 5.

print(x)
print(x + 1)

x = 10  # we can change value using assignment operator

print(x)
print("x =", x)

x + 5  # Python runs this line, but it doesn't change anything
print("x =", x)

x = x + 5  # legal in code, not in math class
print("x =", x)

x += 5  # coding shorthand
print("x =", x)


# Variables
x = 1
X = 2
print(x)  # all names are case sensitive

# in python we use snake_case, not camelCase, or PascalCase, or kebab-case
# be descriptive on the naming of variables

first_name = "Aaron"
eight_ball = 8
tax_percentage = 0.11

'''
first name = "Aaron"  # spaces are not allowed
8ball = 8  # cannot start with a number (numbers are allowed though
tax% = 0.11  # no special characters other than _
'''

PI = 3.14  # this is a constant (CAPITALIZE CONSTANTS)


#  Operators (math)

y = 3 + 5 - 2  # addition and subtraction
print(y)

z = 2 * 4 / 2  # multiplication and division
print(z)

a = 3 ** 2  # power of (3^2)
print(a)

b = 3 // 2  # floor division.  Removes everything after decimal.  Rounds down.
print(b)

d = 7 % 4  # modulus.  Returns the remainder after division.
print(d)


#  Writing out equations
#x = 3y  # legal in math, not in programming  (be explicit)
x = 3 * y

#x = 2 (4 / 3)
x = 2 * (4 / 3)

# Spacing
x=9*2-4/(3-1)**2  # legal but improper
x    =     9*    2        -4/(     3-1)   **   2  # legal but improper
x = 9 * 2 - 4 / (3 - 1) ** 2  # legal and proper

# PEMDAS
avg = 4 + 5 + 3 / 3
avg = (4 + 5 + 3) / 3  # correct


# Libraries (normally written at top)
import math

print(math.pi)
print(math.cos(math.pi / 2))  # works in radians


# continued 9/10/19
# CUSTOM EQUATIONS

# area of a circle
radius = 5
area = math.pi * radius ** 2
print(area)

# improved
print()
print("\nArea of Circle Calculator")
radius = float(input("Enter the radius: "))  # waits for user to hit enter and "records" value
area = math.pi * radius ** 2
print("Area:", area)


# Degrees to radians
print()
print("Degrees to Radians Calculator")
degrees = float(input("Enter degrees: "))
radians = degrees * (math.pi / 180)
print(degrees, "degrees =", radians, "radians")
