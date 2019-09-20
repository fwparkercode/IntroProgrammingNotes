# Chapter 3 - If Statements

if 10 > 5:
    print("The condition is true")

if 3 < 0:
    print("This condition is true also")  # NOPE


a = 1
b = 2
c = 2

if a <= b:
    print("a is less than or equal to b")

if b >= a:
    print("b is greater than or equal to a")

if b >= c:
    print("b is greater than or equal to c")

if a == b:
    print("a is equal to b")

if b == c:
    print("b is equal to c")

if a != c:
    print("a is NOT equal to c")


# Indentation
# x = 5  # produces an error.  indent level matters
#print(x)

if a == 1:
    print("This prints")
    print("This too")

print("anything on the far left always executes")

#    print("You cannot reindent")


# AND and OR statements
a = 1
b = 2
c = 2
d = 3

# for AND, both have to be True
if a < b and a < c:
    print("a is less than b AND a is less than c")

# for OR, one or both can be True
if a > d or b == c:
    print("a greater than d OR b equal to c")

# you can also make COMPOUND IF statements
if (a < b and b == c) or (a > b and d < b):
    print("Python checks all the conditions")

# Special in PYTHON
if a < b <= c:
    print("a < b <= c")

#  Boolean variables
my_int = 867  # counting numbers
my_float = 343.89 # decimals (more precise)
my_str = "Hello World"  # text
my_bool = True  # True or False

my_bool = 8 > 4
print(my_bool)
my_bool = 9 == 8
print(my_bool)

if my_bool:
    print("It's True")

if not my_bool:
    print("not my_bool")


# Nested IF statements
a = 10
b = 12
c = 14

if b > a:
    print("b > a")
    if c > b:
        print("c > b")
        print("This code will only be reached if both nested statements are True")


# Everything can be evaluated as a Boolean True or False
# Only False and 0 are evaluated as False
if "Aaron Lee":
    print("Aaron Lee is True??")

if 4 * 8:
    print("Numbers are True")

if 0 * 8:
    print("Except for zero")

if False:
    print("False is always False")

# Common error
a = 7

if a == 6 or 8:
    print("One of these is True")
    # It's a TRAP!

#  ELIF (ELSE IF) and ELSE
'''
temp = float(input("Enter the temp: "))

if temp > 100:
    print("It is crazy hot outside")
elif temp > 90:
    print("It is really hot")
elif temp > 50:
    print("It's so nice")
elif temp > 30:
    print("It's getting cold")
elif temp > 0:
    print("BRRR!")
else:
    print("Chiberia")


# Case Insensitive Text
name = "Francis Parker"
print(name)
print(name.lower())
print(name.upper())

school = input("What school do you go to? ")

if school.lower() == "parker" or school.upper() == "FWP" or school.lower() == "francis parker":
    print("Yipee!  I go there too.")
elif school.upper() == "LATIN":
    print("Good for you.")
elif school == "":
    pass
else:
    print("Great, I hear that", school, "is a fine institution.")

'''
# Quiz Questions

print()
print("Question 1")
print("What is 24 squared?")
answer = int(input("Your answer: "))

if answer == 24 ** 2:
    print("You pass math!")
else:
    print("You should know this!, it's", 24 ** 2)

print()
print("Question 2")
print("Who is the narrator of Moby Dick")
print("\tA. Herman Melville")
print("\tB. Ahab")
print("\tC. Ishmael")
print("\tD. Moby")

answer = input("Your Answer: ")

if answer.lower() == "c" or answer.lower() == "ishmael":
    print("You are correct!")
elif answer.lower() == "d" or answer.upper() == "MOBY":
    print("That's the whale!  It was Ishmael.")
else:
    print("Incorrect.  It was Ishmael")





