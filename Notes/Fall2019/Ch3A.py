# Chapter 3 - IF Statements

a = 1
b = 2

# Greater than and Less Than (> <)
if a < 10:
    print("a is less than 10")

if b > a:
    print("b greater than a")

# Equality
if a == 1:
    print("a is equal to 1")

if a != 2:
    # ! represents the NOT statement
    print("a is not equal to 2")

if b >= 2:
    print("b greater than or equal to 2")

if a <= 1:
    print("a is less than or equal to 1")

# common errors (single equal, and no colon)
'''
if a = 1:
    print("a equal 1")

if a == 1
    print("a equal 1")
'''

# Indentation
'''
# this produces indent error
 x = 5
print(x)
'''

a = 1
b = 2
c = 2
d = 3

if a == 1:
    print("this will print")
    print("so will this")

print("everything to the far left will execute")
#    print("You cannot reindent")


# Using AND/OR
# AND - BOTH have to be True
if a == 1 and b == c:
    print("a equal 1 AND b equal c")

if b == c and a > 3:
    print("b equal c AND a less than 3")

# OR - ONE or BOTH can be True
if b == c or a > 1000:
    print("b equal c OR a greater than 1000")

if b > c or a > 1000:
    print("b greater than c OR a greater than 1000")

# Compound statements
if (a == 1 and b == c) or (b > c or a > 1000):
    print("Python can do multiple checks for one IF")

# Nested IF statements
if b == c:
    print("b equal c")
    if c > 1:
        print("This will only print if both are True")
    if c > 10:
        print("c is greater than 10")


# BOOLEAN variables
my_int = 4378
my_float = 4.98
my_str = "Hello World"
my_bool = False

print(my_bool)

if my_bool:
    print("my_bool is True")

if not my_bool:
    print("not my_bool")

x = 4 > 7
print(x)

y = 4 != 8
print(y)

# ONLY zero and False evaluate as False.  Everything else is True
if 7:
    print("7 is True")
if "Aaron Lee":
    print("Aaron Lee is True")
if 0:
    print("zeroes are False")
if False:
    print("False is False")

# common error
if a > c or d:
    print("Written incorrectly")
    print("It's a trap!")