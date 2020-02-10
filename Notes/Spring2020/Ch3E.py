# Chapter 3 - If Statements (Quiz Game)

# Basic Comparisons
a = 1
b = 2
c = 3
d = 4
e = 4

if b > a:
    print("b > a")

if a > b:
    print("a > b")

if b < c:
    print("b < c")

if b >= a:
    print("b >= a")

if d >= e:
    print("d >= e")

if d == e:
    print("d == e (equal to)")

if a != b:
    print("a != b (not equal to)")

a == 2  # commmon mistake (this does not change a)

# Indentation
if a == 1:
    print("a is one.  this prints")
    print("this too")
    print("and this")

#  this always prints because it is on the global line (all the way left)
print("this will always print")

#  Indentation levels must match  (this code is broken)
# if a == 1:
#     print("a is one.  this prints")
#         print("this too")
#     print("and this")


# You cannot reindent (this code is broken)
# if a == 1:
#     print("a is one.  this prints")
# print("this too")
#     print("and this")

# Compound conditions
# AND (both conditions must be True)
if a < b and a < c:
    print("Both are true")

# OR (either one or both must be True)
if a < b or a > c:
    print("Both are true")

# must ask two independent questions/conditions
if e < a or b:
    print("This doesn't do what you think")


# BOOLEAN (True or False)
game_over = True

if game_over:
    print("YOU LOSE!")

# using the not statement
game_over = False
if not game_over:
    print("You haven't lost yet")

x = True
y = False

if x and y:
    print("both are True")

# Compound IF statement
if (a < b and b < c) or (d == e and e > a):
    print("You can check lots of things at once")

# Special python only math trick
if a < b < c:
    print("Only in Python")


# More with Boolean variables
x = True
y = a > b
print(y)

z = d == e
print(z)

if 1:
    print("1 is True")

if 0:
    print("0 is False")  # does not print


# Everything is True except False and 0
if "Hello World":
    print("Strings are ALL True")


# common error
if a > b or c:
    print("This is checking to see if c is True")


# Else and Else If (elif)
# Only one If elif can execute.
# If no If elif are True, the else will always run

temperature = 10

if temperature > 90:
    print("It is hot outside")
elif temperature > 70:
    print("It is warm outside")
elif temperature > 40:
    print("It is cool outside")
elif temperature > 20:
    print("It is cold outside")
else:
    print("You are in Chicago")


# Text comparisons
name = input("Enter your name: ")
if name == "Aaron":
    print("That's my name too.")

# Text is alphabetical (according to ascii table)
if "A" > "B":
    print("A is greater than B")  # does not print

if "B" > "a":
    print("B is greater than a")  # does not print

if "apple" > "ant":
    print("If the first character is a tie, it goes to next")

# Case insensitive comparisons
# .upper() and .lower()
name = "Francis"
print(name.upper())
print(name.lower())
print(name)


name = input("Enter your name: ")
if name.upper() == "AARON":
    print("That's my name too.")


# Nesting If statements
if b > a:
    print("b > a")
    if d > a:
        print("d > a")





# Multiple choice question
score = 0
total_questions = 2

print("Question #1")
print("What is the capitol of Illinois?")

print("\tA) Chicago")
print("\tB) Springfield")
print("\tC) Peoria")
print("\tD) Rockford")

answer = input("Your answer: ")

if answer.upper() == "B" or answer.upper() == "SPRINGFIELD":
    print("Correct")
    score += 1  # increment the score
elif answer.upper() == "A":
    print("Do you even live here?")
else:
    print("Incorrect")

print("\n")

# Fill in blank / short answer
answer = input("Where do you go to school?")

if answer.lower() == "parker" or answer.upper() == "FRANCIS PARKER" or answer.upper() == "FRANCIS W PARKER" or answer.upper() == "FRANCIS W. PARKER" or answer.upper() == "FWP":
    print("Yay! I go there too.")
    score += 1
elif answer.upper() == "LATIN":
    print("Good for you.")
    score -= 1000000
else:
    print("I hear", answer, "is a fine institution.")


print("You got", score, "out of", total_questions, "correct.")

percent = score / total_questions * 100
print("You scored", str(percent) + "%.")








