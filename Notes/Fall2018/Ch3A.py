# Chapter 3 - Quiz Games and If Statements

# Basic Comparison

a = 4
b = 5
c = 5
d = 6

if a < b:
    print("a < b")

if d > b:
    print("d > b")

if b >= c:
    print("b >= c")

if a == b:
    print("a equal to b")

b = 5  # Assignment operator
b == 5  # Comparison operator

if a != b:
    print("a not equal to b")

# Indentation
if a == 4:
    print("First")
    print("Second")

print("Third")  # global indent level all the way left

# indent levels must match
# cannot reindent

# Compound Statement
a = 4
b = 5
c = 5
d = 6

# AND STATEMENT
# Both have to be true
if a < b and b <= c:
    print("both are true")

if a < b <= c:  # this is only available in Python
    print("both are true")

# OR STATEMENT
# One or both are true
if d < a or c > a:
    print("One or both are true")

# COMPOUND IF/AND
if (d < a or c > a) and b <=c:
    print("All this is true")

# Boolean Variables
# True or False
x = False
print(x)

y = 10 > 9
print(y)

# the number zero and False are the only two boolean Falses
# Anything else (characters, strings, etc. are True)
z = 0
if z:
    print("z is true")

z = "A"
if z:
    print("A is true!")

a = 5
b = 5
c = b == a
print(c)

# Else and Else If (elif)

#temp = float(input("What is the temperature in Farenheit?"))
temp = 100

if temp > 90:
    print("It is hot!")
elif temp < 30:
    print("It is cold outside!")
else:
    print("It is not hot outside.")

grade = 85

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("Fun")

# only one IF and one ELSE (else is optional)
# As many ELIF as you want (each has its own condition)
# if none of the IF or ELIF are true, the ELSE will always trigger

# Text comparison
#password = input("Enter the secret password: ")
password = "parker123"

if password == "parker123":
    print("Correct!")
else:
    print("You are forbidden!!!")


# Case insensitive text

#school = input("Where do you go to school? ")
school = "Parker"

if school.upper() == "PARKER" or school.upper() == "FRANCIS PARKER" or school.lower() == "francis w. parker" or school.upper() == "FWP" or school.lower() == "francis wayland parker":
    print("Yay!  I go there too.")
elif school.lower() == "latin":
    print("Oh.")
else:
    print("I hear", school, "is a fine institution.")






# Make a multiple choice question
score = 0

print("\nWhat is the capital of Illinois?\n\tA. Chicago\n\tB. Springfield\n\tC. Carbondale\n\tD. Evanston\n")

answer = input("Your Answer: ")

if answer.upper() == "A" or answer.upper() == "CHICAGO":
    print("Do you even live here?")
elif answer.lower() == "b":
    print("Correct!!  Nice job.")
    score += 1
elif answer.upper() == "C":
    print("Wrong!  The answer is Springfield.")
elif answer.upper() == "D":
    print("Incorrect.  Springfield is the answer.")
else:
    print("That is an invalid choice.")

# Math Problem
print()
print("What is 17 squared?")

answer = float(input("Your answer: "))

if answer == 17 ** 2:
    print("You are a math genius!!")
    score += 1
else:
    print("Incorrect, the answer is", 17 ** 2)

print("Your final score was", str(round(score / 3 * 100, 1)) + "%")

