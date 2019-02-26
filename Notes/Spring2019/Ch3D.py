# Chapter 3 - Quiz games and IF statements

# IF statements are used for comparison
# They are gatekeepers to blocks of code.

#name = input("Enter your name: ")
name = "Me"


if name == "Aaron":
    print("Hello!")

# if (condition):
     # stuff to do

# Conditional Operators
# > greater than
# >= greater than or equal to
# < less than
# <= less tahn or equal to
# == equal to
# != not equal to

a = 3
b = 4
c = 4
d = 5

if a < b:
    print("a less than b")

if a > b:
    print("a greater than b")

if b >= c:
    print("b greater or equal to c")

if c >= d:
    print("c greater or equal to d")

if b == c:
    print("b equal to c")

if b != c:
    print("b not equal to c")

# common mistake (= instead of ==)
#if b = c:
    #print("can't write it this way!")

#if b == c
    #print("need a colon")

# Indentation
print("Code to the far left will ALWAYS run")
if 3 > 4:
    print("indented code might run")

print("As soon as you unindent, you are back to the global line")
    #print("you cannot reindent")

if 10 > 5:
    print("This will print")
    print("so will this")
    print("me too")

# AND and OR (Compound Statements)
a = 3
b = 4
c = 4
d = 5

if a < b and c < d:
    print("both are true")

if a > b and c < d:
    print("BOTH ARE TRUE")

if b == c or c > d:
    print("one or both are true")

if a > b or c > d:
    print("ONE OR BOTH ARE TRUE")


if (a > b or c > d) and b == c:
    print("This is a compound statement")

# Boolean Values
my_int = 5
my_float = 5.4
my_string = "Hello"
my_bool = True

print(my_bool)
print(5 > 2)
print(b == d)
my_bool = 3 < 10
print(my_bool)

if 0:
    print("Zero is always False")
if 879234:
    print("Anything other than zero is True")
if "Hi":
    print("Strings are always true")


name = "Linda"

if name == "Bob" or "Mary":
    # this is a common error
    print("Hi Bob or Mary")


# Else statements
# catchall.  Happens if the IF statement is NOT triggered.

x = 5
if x < 3:
    print("This")
else:
    print("That")


# elif statement (ELSE IF)

temp = -1

if temp > 90:
    print("It is hot")
elif temp > 70:
    print("It is warm outside")
elif temp > 50:
    print("It is cool outside")
elif temp < 10:
    print("You are in Chicago")
else:
    print("It is not hot")


# school = input("Where do you go to school? ")
school = "Parker"
# school = school.upper()
# school = school.lower()
print(school)

if school.upper() == "PARKER" or school.upper() == "FWP" or school.upper() == "FRANCIS PARKER" or school.upper() == "FRANCIS W. PARKER":
    print("Yay! I go there too.")
elif school.lower() == "latin":
    print("Good for you.")
else:
    print("I hear", school, "is a fine institution.")


score = 0

print("\n\nQuestion 1:")
print("A.  Chicago")
print("B.  Springfield")
print("C.  Rockford")
print("D.  Peoria")
print("E.  Wadsworth")

answer = input("What is the capital of Illinois? ")

if answer.upper() == "B" or answer.upper() == "SPRINGFIELD":
    print("Correct")
    score += 1
elif answer.upper() == "E":
    print("Seriously?")
else:
    print("No.  The answer was Springfield.")

print()

print("Question 2:")
print("What is 2 + 2? ")
answer = float(input("Your answer: "))

if answer == 4:
    print("You are correct!")
    score += 1
else:
    print("Missed that one.")

print("\nYou scored", str(score / 2 * 100) + "%")













