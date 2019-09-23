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


# IF ELIF (ELSE IF) ELSE

# ELSE will always run if no other condition met
'''
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You are", age, "and cannot vote until you are 18")

temp = int(input("Enter the temperature in degrees F: "))
if temp > 100:
    print("It is crazy hot outside")
elif temp > 80:
    print("it is hot outside.  Great day for the beach.")
elif temp > 60:
    print("it is so nice out")
elif temp > 30:
    print("it is cool outside")
else:
    print("It is freezing out here")


# Case Insensitivity
print("Francis Parker")
print("Francis Parker".upper())  # makes it all CAPS
print("Francis Parker".lower())  # makes it all lowercase

name = "Aaron Lee"
print(name.upper())


school = input("Where do you go to school? ")

if school.lower() == "parker" or school.upper() == "FWP" or school.lower() == "francis parker":
    print("Yay, I go there too!")
elif school.upper() == "LATIN":
    print("Good for you.")
else:
    print("Great, I hear", school, "is a fine institution.")

'''
# QUIZ QUESTION

score = 0

print()
print("Question 1")
answer = float(input("What is 2 + 2? "))

if answer == 2 + 2:
    print("Correct")
    score += 1
else:
    print("Sorry, the answer is 4.")

print()
print("Question 2")
print("What is the capital of Illinois?")
print("\tA. Peoria")
print("\tB. Chicago")
print("\tC. Springfield")
print("\tD. Sandwich")

answer = input("Enter your choice: ")

if answer.lower() == "c" or answer.lower() == "springfield":
    print("Correct.")
    score = score + 1
elif answer.upper() == "B" or answer.upper() == "CHICAGO":
    print("Wrong, but it should be.  The correct answer is Springfield.")
else:
    print("Incorrect.  The answer is Springfield.")

print()
print("Congratulations, you scored", score, "out of 2.")
print("You scored", str(score / 2 * 100) + "%")

