# Chapter 3 - Quiz Games and If Statements

a = 4
b = 5
c = 5
d = 6

if a < b:
    print("a is less than b")

if a > b:
    print("a is greater than b")

if a <= b:
    print("a <= b")

if b >= c:
    print("b >= c")

if b == c:
    print("b is equal to c")

# assignment operator
x = 5

# comparison
x == 5

if b != c:
    print("b and c are not equal")

# Most common errors
'''
if 10 < 5
    print("Wrong")

if 5 = 4:
    print("Also wrong")
'''

# Indentation
x = 9

if x == 9:
    print("First")

print("Second")
print("Third")

# 4 space indents
# blocks of code must all line up
# if you unindent, you cannot reindent

#  Compound Condition statements

a = 1
b = 2
c = 2
d = 3

# AND compound
# Both have to be true
if a < b and b <= c:
    print("both are true")
if a < b <= c:
    print("simplified version")  # python simplification

# OR compound
# Either statement is true
if a < b or c > d:
    print("one or both of these is true")

# Link ANDs and ORs together to do any condition
if a < b and (a < b or c > d):
    print("It's all true")

# Boolean Variables
x = False

if x:
    print("x is True")

y = 5 > 2
print(y)

a = 3
b = 3
c = b == a
print(c)

print("A" > "B")
print("Apple" > "Banana")
print("apple" > "Banana")

# Else and Else If (elif)

# ELIF statement is a linked condition (chain of IF statements)
# ELIF can only follow an IF chain
# ELSE can only be at the end of an IF chain
# only one statement in the chain can execute their code

#temp = float(input("What is the temperature in degrees Farenheit?"))
temp = 80

if temp > 100:
    print("It is crazy hot outside.")
elif temp >= 80:
    print("It is hot outside.")
elif temp >= 60:
    print("It is nice outside.")
elif temp >= 40:
    print("It is cool outside.")
elif temp >= 20:
    print("It is chilly outside.")
else:  #catch all
    print("Chiberia.")


# Text comparisons and case insensitivity

print("Aaron")
print("Aaron".upper())  # .upper() method converts entire string to upper case
print("Aaron".lower())  # .lower() method converts to all lower

#  school = input("What school do you go to?")
school = "parker"

if school.upper() == "PARKER" or school.upper() == "FRANCIS PARKER" or school.lower() == "fwp" or school.upper() == "FRANCIS W. PARKER":
    print("Go Colonels!!")
elif school.lower() =="latin":
    print("Oh.")
else:
    print("I hear", school, "is a fine institution.")





# Multiple Choice Question

score = 0

print("\nWho was the first king of Spain?")
print("\tA. Ferdinand I\n\tB. Ferdinand II\n\tC. Charles I\n\tD. Alejandro I\n")

answer = input("Your answer: ")

if answer.upper() == "C":
    print("Correct!")
    score += 1
elif answer.upper() == "B":
    print("That doesn't even make sense!")
else:
    print("Incorrect.  The answer was Charles I")


# Math Question
print("What is 15 squared?")
answer = int(input("Your answer: "))

if answer == 15 ** 2:
    print("You are a math genius.")
    score += 1
else:
    print("Incorrect, the answer is", 15 ** 2)

# print("Your score is", score, "out of", 2)
print("Your score is", str(round(score / 2 * 100, 1)) + "%")


