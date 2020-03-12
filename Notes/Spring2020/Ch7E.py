# Lists

# data types
import random

my_string = "Hello"
my_int = 4
my_float = 3.4
my_bool = True

my_list = ["Hello", 4, 3.4, True]
my_tuple = (9, 8, 3, 2)  # immutable list

# Indexing a list
my_list = [6, 9, 3, 2, 1, 7]

print(my_list)
print(my_list[0])  # index 0 is the first item in the list
print(my_list[3])  # fourth one in the list (prints 2)
# print(my_list[6])  # IndexError: list index out of range

my_grocery = ["spam", "eggs", "Python", "milk"]

print(my_grocery)
print(my_grocery[1])

# iterate through a list
# Using a FOR EACH loop
for item in my_grocery:
    print(item)

# Using an INDEX VARIBLE loop
for i in range(len(my_grocery)):
    print(my_grocery[i])


# len function - returns the length of the list
print(len(my_grocery))

# Adding to a list (append)
my_grocery.append("Frosted Flakes")  # append method to add to end of list
print(my_grocery)


# Tuple - immutable (unchanging list)
RED = (255, 0, 0)
# RED.append("Hello")  # cannot append to a tuple (it's immutable)
print(RED[0])
# RED[0] = 0  # can't do this (it's immutable)
print(RED)

my_grocery[2] = "Froot Loops"  # can do this with a list
print(my_grocery)


# When to use FOR EACH, and when to use INDEX VARIBLE

# FOR EACH loop works with a copy of the object
# item is a COPY of the value inside the list
for item in my_grocery:
    item = "Captain Crunch"
    print(item)

print(my_grocery)

# INDEX VARIABLE loop is speaking directly to the list
for i in range(len(my_grocery)):
    my_grocery[i] = "Captain Crunch"  # must use index to change a value

print(my_grocery)



my_list = [5, 9, 1, 4, 2]
# print the squares of each number

for number in my_list:
    print(number ** 2)

print(my_list)


for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 2

print(my_list)


# 2d lists
my_list = [4, [6, 8, 2], [1, 9, [7, 5]], 3]
print(my_list[0])  # print the number 4
print(my_list[3])  # print the number 3
print(my_list[1])  # print the list [6, 8, 2]
print(my_list[1][1])  # print the number 8
print(my_list[1][2])  # print the number 2
print(my_list[2][1])  # print the number 9
print(my_list[2][2][1])  # print the number 5

# sum a list
my_list = [20, 45, 35, 5, 25, 70]
total = 0

for number in my_list:
    total += number

print(total)

# make a list of 100 single die rolls
my_rolls = []

for i in range(100):
    die = random.randrange(1, 7)
    my_rolls.append(die)

print(my_rolls)

# make a list of 100 two die rolls
# add them as [die1, die2]
my_rolls = []

for i in range(100):
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    my_rolls.append([die1, die2])

print(my_rolls)


# find out how many sevens you rolled by going back through the list