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









