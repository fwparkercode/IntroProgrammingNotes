# Chapter 3 - Quiz Games and IF Statements

a = 4
b = 5
c = 5
d = 6

# Basic comparisons
if a < b:
    print("a is less than b")

if a > b:
    print("a is greater than b")

# Comparison operators
# <, >, <=, >=, ==, !=
# less than, greater than, less than or equal, greater or equal, equal, not equal

if b >= c:
    print("b is greater than or equal to c")  # YES

if b >= d:
    print("b is greater than or equal to d")  # NO

if b == c:
    print("b and c are equal")  # YES

if b != c:
    print("b and c are NOT equal")  # NO

# Common error (use = instead of ==)
#if b = c:
    #print("b and c are equal")

# Indentation (python uses 4 spaces to indent; let PyCharm do this for you!)

if 10 > 20:
    print("This is true")

print("This will always print")  # all the way to left
    #print("you cannot reindent")

if 3 < 4:
    print("watch your indents")
     #print("this won't work")

# AND and OR statements

a = 4
b = 5
c = 5
d = 6

if a < b and c < d:
    print("both are true")

if a < b and c > d:
    print("both are true!!")

if a < b or c > d:
    print("either (or both) is true")

if a > b or c < b:
    print("either is true!!")

# if a > b or > c:

if a > b > c:
    print("This is legal in python (and unusual in programming)")

# Compound statements
if (a > b and b < c) or (a > c or c < d):
    print("now we are checking 4 conditions")


# Boolean Variables (True or False)

my_int = 5
my_float = 5.32
my_string = "Hello"
my_boolean = True
my_boolean = False
my_boolean = 5 > 3
print(my_boolean)

if True:
    print("True statements trigger the code inside IF statements")

if not a > b:
    # not checks the opposite
    print("a greater than b")

# anything not False or 0 evaluates as True
if 3:
    print("3 is evaluated as True")

if False:
    print("False and zero are the only things NOT true")

if 0:
    print("False and zero are the only things NOT true")

if 0.0000001:
    print("This is true")

if "Hi":
    print("All strings are true too")

if a > b or c:
    print("c is always true")

#  Else and Else If chains
#  Else is the catchall.  If you reach the else statement it will always run the code.

#temperature = float(input("What is the temperature in F? "))
temperature = 100

if temperature > 110:
    print("It is crazy hot outside")
elif temperature > 90:
    print("It is hot outside")
elif temperature > 70:
    print("It is warm outside")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is not hot outside")

# Case insensitive comparisons

first = "Francis"
last = "Parker"

print(first.upper())
print(last.lower())

#name = input("Enter your name: ")
name = "Linda"

if name.upper() == "LINDA":
    print("Hello Linda")
else:
    print("You don't belong here.")



# Make a multiple choice question

print("A.  Chicago")
print("B.  Rockford")
print("C.  Springfield")
print("D.  Boston")

answer = input("What is the capital of Illinois? ")

if answer.upper() == "C" or answer.lower() == "springfield":
    print("Correct")
elif answer.upper() == "A":
    print("Do you even live here? ")
else:
    print("Incorrect")


# Math question
answer = float(input("What is: 4 * 8 / 2 + 12 ** 2 ? "))
if answer == 4 * 8 / 2 + 12 ** 2:
    print("Correct")
else:
    print("Incorrect")


# Short answer
answer = input("What time does this class end?")
if answer == "11:15":
    print("Correct")
else:
    print("Incorrect")

answer = input("Where do I go to school?")
if answer.upper() == "FRANCIS W. PARKER" or answer.upper() == "FRANCIS PARKER" or answer.upper() == "PARKER" or answer.upper() == "FWP":
    print("I go there too")
elif answer.upper() == "LATIN":
    print("I hear that is a fine institution")
else:
    print("Good for you")



