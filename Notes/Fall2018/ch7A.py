# Chapter 7 - Lists

my_list = [10, 20, 30] # this list stores 3 integers

# prints the whole list
print(my_list)

# we can also address individual elements of a list
print(my_list[0])  # like all things programming, we count 0, 1, 2
print(my_list[2])  # the 2 here is the "index" of the list.

# You can use the index to change your list
my_list[0] = 15
print(my_list)

grocery_list = ["milk", "eggs", "cereal", "spam", 2]  # python allows mixing variable types

# you can read through a list with a for loop
# iterating through a list
for item in grocery_list:
    print(item)

# lists can even contain other lists (list of lists)
my_list2 = [[100, 200], [300, 400], [500, 600, 700]]
# use multiple indices to address individual elements of the list/array
print(my_list2[0][1])  # prints the second item from the first list
print(my_list2[2][2])  # print 700


my_list3 = [11, 21, 31, 41, 51]
# There is a second way to iterate through a list. (index variable loop)

# len function returns the length of the list
print(len(my_list3))

for i in range(len(my_list3)):
    print(my_list3[i])

# This method is more complex, but more capable.

# when we iterate the first way, we are working with a copy
for number in my_list3:
    number += 1
    print(number)

print(my_list3)  # the list did not change

# when we index the variable, we are working directly with the list
for i in range(len(my_list3)):
    my_list3[i] += 1
    print(my_list3[i])

print(my_list3)

# Tuples
# tuple is a less capable cousin to the list
my_tuple = (255, 255, 0)
print(my_tuple[0])  # you can index tuples the same as a list

# you can iterate, same as a list
for n in my_tuple:
    print(n)

# only difference is that a tuple is immutable (unchanging)
# my_tuple[0] = 0  # this is illegal (TypeError)


# Adding to a list
grocery_list = []

# append to the list
grocery_list.append("spam")
grocery_list.append("eggs")
print(grocery_list)

# add items in a loop
for i in range(3):
    #item = input("Enter an item: ")
    item = "spam"
    grocery_list.append(item)
print(grocery_list)

# roll a die 100 times and store it in a list
import random
my_rolls = []

for roll in range(100):
    my_rolls.append(random.randrange(1, 7))

print(my_rolls)

# how many 6's
sixes = 0
for roll in my_rolls:
    if roll == 6:
        sixes += 1
print(sixes, "Sixes")
print(1 / 6)



# Totaling the numbers in a list
my_list = [19, 25, 24, 30, 42]

# Method 1 - Better for this task
total = 0
for number in my_list:
    total += number

print(total)

# Method 2 - Can also be used (index variable loop)
total = 0
for i in range(len(my_list)):
    total += my_list[i]

print(total)

# Find the average
print(total / len(my_list))

# square all of the numbers in the list
for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 2
    # alternate way to write
    # my_list[i] **= 2

print(my_list)


# YAHTZEE!

count_list = []

for j in range(10):
    done = False
    count = 0
    while not done:
        roll_list = []
        count += 1
        for i in range(5):
            roll = random.randrange(1, 7)
            roll_list.append(roll)

        if roll_list[0] == roll_list[1] and roll_list[0] == roll_list[2] and roll_list[0] == roll_list[3] and roll_list[0] == roll_list[4]:
            print("YAHTZEE! in", count, "rolls")
            done = True
            count_list.append(count)

    print(roll_list)

print("Average number of rolls:", sum(count_list) / len(count_list))

# String Slicing
my_text = "Francis W. Parker"

# Use the index to address character
print(my_text[0])  # Print the "F"
print(my_text[6])  # print the "s"

# Accessing characters from the right
print(my_text[-1])  #  print the "r"
print(my_text[-6])  # print the "P"

# Access multiple characters
print(my_text[4:7])  # cis
print(my_text[-5:-2])  # ark
print(my_text[:7])  # Francis
print(my_text[-6:])  # Parker

for char in my_text:
    print(char)







