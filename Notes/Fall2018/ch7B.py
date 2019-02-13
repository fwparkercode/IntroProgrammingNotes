# Chapter 7 - Lists (Arrays)

# Data types (bool, int, float, string)
# New Data Types (list, tuple)

my_list = [11, 21, 31, 41, 51]
# values are 11, 21, 31, 41, 51
# indices are 0, 1, 2, 3, 4

# use indices to address individual elements of an array/list
print(my_list[0])  # we always start counting at 0 in programmin!
print(my_list[4])  # prints 51
print(my_list[4] + my_list[3])
print(my_list)

# we can change a list
my_list = [11, 21, 31, 41, 61]
print(my_list)

# we can change individual items in a list by using the index and assignment operator (=)
my_list[0] = 12
print(my_list)

my_list[1] += 10
print(my_list)

# do not go beyond the end of the list (IndexError: list index out of range)
# print(my_list[5])

grocery_list = ["eggs", "spam", "milk", "cereal"]

# Method 1 - iterate through a list using a for loop
for item in grocery_list:
    print("eat more", item)


my_list = [11, 12, 13, 14]

# Method 2 - iterate through a list using the "index variable loop" method.
print(len(my_list))  # len returns the number of items in the list

for i in range(len(my_list)):
    print(my_list[i])

# Method 1 only uses a copy of the item.  Method 2 talks directly to the list.

#  Method 1 - uses a copy
for number in my_list:
    number += 1
    print(number)
print(my_list)

# Method 2 - uses the index
for i in range(len(my_list)):
    my_list[i] += 1
    print(my_list[i])
print(my_list)


# Adding items to a list using the append method.
my_list.append("hi")
print(my_list)


# Lists of lists  (using 2d list indices)
my_list2d = [[20, 21], [35, 45], [88, 89, 90], [3, [4, 5], ["Hi", "There"]]]
print(my_list2d[0])
print(my_list2d[0][1])  # prints 21
print(my_list2d[1][0]) # print 35
print(my_list2d[2][2]) # print 90
print(my_list2d[3])
print(my_list2d[3][2][0])  # prints "Hi"


# Tuple -  The less capable cousin of the list
# tuple is an immutable list (you cannot change it)
my_tuple = (255, 255, 0)
#  my_tuple[0] = 0  # can't do this
print(my_tuple)


# Roll 5 dice.  Store the values in a list.
import random
rolls_list = []

for die in range(5):
    roll = random.randrange(1, 7)
    rolls_list.append(roll)

print(rolls_list)

# sum the 5 dice

# Method 1
total = 0
for roll in rolls_list:
    total += roll

print("Total:", total)

# Method 2 (index variable loop)
total = 0
for i in range(len(rolls_list)):
    total += rolls_list[i]

print("Total:", total)

# find the average of the five die
print("Average:", total / len(rolls_list))


# Yahtzee roller

rolls_needed = []
for sim in range(100):

    done = False
    total_rolls = 0

    while not done:
        rolls_list = []
        total_rolls += 1

        for die in range(5):
            roll = random.randrange(1, 7)
            rolls_list.append(roll)

        print(rolls_list)

        if rolls_list[0] == rolls_list[1] and rolls_list[0] == rolls_list[2] and rolls_list[0] == rolls_list[3] and rolls_list[0] == rolls_list[4]:
            done = True
            print("YAHTZEE!! on roll number", total_rolls)
    rolls_needed.append(total_rolls)

print("Avg rolls", sum(rolls_needed)/len(rolls_needed))



#  modifying a list (must use method 2)
my_list = [1, 2, 3, 4, 5]

for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 2

print(my_list)


# String Slicing
# a string is really just a list of characters

my_text = "Francis W. Parker"

# Accessing from the left side
print(my_text[0])  # strings can be indexed
print(my_text[4])# prints c

# Accessing from the right side
print(my_text[-2])  # print the e

# Accessing multiple characters
print(my_text[4:7])#  print "cis"
print(my_text[8:12])#  print "W. P"
print(my_text[:4])  #  print "Fran"
print(my_text[14:])# print "ker"
print(my_text[-3:])














