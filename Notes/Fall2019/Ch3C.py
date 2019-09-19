# Chapter 3 - If Statements

a = 1
b = 1

if a < b:
    print("a is less than b")

if a > b:
    print("a is greater than b")


# check equality
if a == b:
    print("a is equal to b")

if a <= b:
    print("a less than or equal to b")

if a >= b:
    print("a greater than or equal to b")


# Indentations
# 4 space indent is proper Python
# Python cares about white space
'''
 x = 3 # space is not allowed, indent level error
y = 4
'''

if a == 1:
    print("a equal to 1")
    print("all code under indent level will run")

print("this code runs too")
#    print("Cannot reindent your code")


# Compound IF statements using AND/OR
a = 1
b = 2
c = 2
d = 3

# AND means that BOTH must be true
if a < b and a < d:
    print("a less than b AND a less than d")

if a > b and a < d:
    print("this is not true")

if a < b and d:  # this is a trap!
    print("This is not written correctly")

# OR means that EITHER must be true
if a > b or a < d:
    print("one or both is true")

if b == c or d > a:
    print("both are true")

# You can even combine statements
if (b == c or c > d) and (b > a and d > a):
    print("checks 4 different conditions")


# Boolean variable
my_int = 87  # counting numbers positive and negative
my_float = 4.783  # decimal numbers (more precise)
my_string = "Hello World"
my_bool = True  # can also be False

# boolean can be True or False only.
a = True
if a:
    print("a is True")

if not a:
    # this is a handy way to check for False
    print("a is not True")

a = 3 > 2
if a:
    print("a is True!")

# anything other than a False or a zero is evaluated as True
a = 9
if a:
    print("a is True????")

if "Aaron Lee":
    print("strings are always True")

if 0:
    print("zeroes are False")

if False:
    print("False is False (of course)")


# leads to this trap
a = 1
b = 2
c = 3

if b > a and c:
    print("b is greater and a and c")  # this is wrong


# Else and Else If
'''
temp = float(input("Enter the temperature: "))

if temp > 90:
    print("it is hot")
elif temp > 80:
    print("it's nice out")
elif temp > 70:
    print("Beautiful Chicago weather")
elif temp > 40:
    print("It is cool")
elif temp > 20:
    print("Brrr")
else:
    print("Chiberia")



guess = int(input("What number am I thinking of? (0-9)"))
correct_number = 6

if guess == correct_number:
    print("You are a mind reader")
elif guess == correct_number + 1 or guess == correct_number - 1:
    print("Oh, so close!  The number was", correct_number)
else:
    print("Sorry, the number was", correct_number)
'''

#  Multiple choice question
print("What is the capital of Illinois?\n")

print("\tA.  Chicago")
print("\tB.  Springfield")
print("\tC.  Peoria")
print("\tD.  Rockford\n")

answer = input("Your answer: ")

if answer.upper() == "B" or answer.lower() == "springfield":
    print("Correct!")
elif answer.upper() == "A" or answer.lower() == "chicago":
    print("It should be.")
else:
    print("Sorry, the correct answer is Springfield")


#  Case insensitive
first = "Francis"
last = "Parker"

print(first)
print(first.lower())
print(first.upper(), last.lower())

school = input("What school do you go to?")

if school.lower() == "francis parker" or school.upper() == "FWP" or school.lower() == "parker":
    print("Yay!  I go there too.")
elif school.lower() == "latin":
    print("Sorry")
else:
    print("Great! I hear", school, "is a fine institution.")
