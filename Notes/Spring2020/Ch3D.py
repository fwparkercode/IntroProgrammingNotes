#  Conditions and IF statements

a = 1
b = 2
c = 3
d = 3

# Basic comparison
if b > a:
    print("b > a")
    print("This prints too.")

if c >= d:
    print("c >= d")

if c == d:
    print("c == d (equal)")

if c != b:
    print("c != b (not equal)")

# Indentation
# Indents set aside blocks of code (used to group code)
if a == 1:
    print("This")
print("and this")
    # print("and not this")  #reindent not allowed

print("This will ALWAYS run")


# Using AND/OR
if a < b and b < c:
    print("Both are True")

if a < b or d < a:
    print("One or both are True")


if a < b < c:
    print("This only works in python")
    print("Guido van Rossum is a mathematician")

# this is not correct
if d < b or c:
    print("This doesn't do what you think")


# Boolean variables
x = True
y = False
z = a < b

print(x, y, z)

if x:
    print("x is True")

if not y:
    # equivalent of if y != True
    print("y is False")

game_over = False

if not game_over:
    print("keep playing")


# EVERYTHING is True (except 0 and False)
if 1:
    print("1 is True")

if "Hello World":
    print("Strings are True")

if False or 0:
    print("This is not True")

# That's why this code doesn't work
if d < b or c:
    print("This doesn't do what you think")


# ELSE and ELSE IF (elif)
# one and only one IF/ELIF/ELSE will trigger (first one)

temperature = 0

if temperature > 90:
    print("It is hot")
elif temperature > 70:
    print("It is warm")
elif temperature > 40:
    print("It is cool")
elif temperature > 20:
    print("It is cold")
else:
    # catchall
    print("It is Chicago")


# Text comparison
name = "Bob"

if name == "Bob":
    print("Hi Bob")
else:
    print("Where is Bob?")


if "Z" > "A":
    print("Z comes after A alphabetically")

if "Z" > "a":
    print("lower case comes after Upper")

if "apple" > "ant":
    print("if the first letter is tie, go to next one")


# Case inspecific comparisons
name = input("Enter your name: ")

if name.upper() == "AARON":
    print("That's my name too")

# .upper() and .lower() methods
print("Francis".upper())
print("Parker".lower())


# Monday, 2/10




# Short Answer or Fill in Blank
score = 0  # track the number of correct answers

print("Question 1")
answer = input("What school do you go to?")

if answer.upper() == "PARKER" or answer.lower() == "fwp" or answer.upper() == "FRANCIS PARKER" or answer.upper() == "FRANCIS W. PARKER":
    print("Yay! I go there too")
    score += 1  # increment by 1
elif answer.upper() == "LATIN":
    print("Oh, good for you.")
else:
    print("I hear that", answer, "is a fine institution.")



# Math Question
print("\n\nQuestion 2")
answer = float(input("What is 25 squared?"))

if answer == 25 ** 2:
    print("Correct!")
    score += 1
else:
    print("Sorry, the answer was", 25 ** 2)


# Multiple Choice
print("\n\nQuestion 3")
print("What is the capital of Illinois?")

print("\tA. Springfield")
print("\tB. Chicago")
print("\tC. Peoria")
print("\tD. Rockford")

answer = input("Enter your choice: ")

if answer.lower() == "a" or answer.upper() == "SPRINGFIELD":
    print("Correct!")
    score += 1
elif answer.upper() == "B" or answer.upper() == "CHICAGO":
    print("Do you even live here?")
else:
    print("Incorrect.  The answer was Springfield.")

print("\n\nYou got", score, "out of", 3, "correct.")
print("You got",score / 3 * 100 ,"percent.")

percent = score / 3 * 100
print(str(percent) + "%")  # concatenation of two strings




# Additional help
print()  # prints blank line
print("\n")  # two blank lines
















