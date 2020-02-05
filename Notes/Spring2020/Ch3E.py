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

# Compond IF statement
if (a < b and b < c) or (d == e and e > a):
    print("You can check lots of things at once")

# Special python only math trick
if a < b < c:
    print("Only in Python")

