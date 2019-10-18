#  Chapter 7 - Lists (Arrays)

#  Data Types
import random

my_int = 3478  # counting numbers (pos and neg)
my_float = 4.9843  # decimal numbers
my_string = "Hello"  # text
my_bool = False  # True or False only
my_list = [11, 12, 13, "Hi", False]
my_tuple = (11, 12, 13)


#  Working with lists
my_list = [5, 6, 7]
print(my_list)
print(my_list[2])

my_list = [10, 11, 12]  # overwrite the list
print(my_list)

my_list[0] = 20
print(my_list)

my_list[0] += 1
print(my_list)

#  Iterating through a list (2 ways)
# FOR EACH LOOP (looking at a copy of each item in list)
grocery_list = ["Spam", "eggs", "milk", "cereal"]

for item in grocery_list:
    print(item)

for number in my_list:
    number += 1
    print(number)

print(my_list)  # list was not changed (only a copy)

#  INDEX VARIABLE LOOP (works directly with each item in list)

for i in range(len(grocery_list)):
    print(grocery_list[i])

for i in range(len(my_list)):
    my_list[i] *= 2  # changes the list directly

print(my_list)


# Lists of lists (2D list)
my_2d_list = [[11, 12], [13, 14, 15], ["Abe", "Bev", "Cam", "Dan"]]
print(my_2d_list[0])  # [11, 12]
print(my_2d_list[0][0])  # 11
print(my_2d_list[2][2])  # Cam

# iterate through a 2d list
for item in my_2d_list:
    for x in item:
        print(x, "in", item)

# len function
print(len(grocery_list))
print(len(my_2d_list))


#  Adding to a list (appending)
my_list = [12, 14, 16, 18]
print(my_list)
my_list.append(20)  # appends to end of list
print(my_list)
my_list.append(100)
print(my_list)

# Create a list of 10 random ints from 5 to 10

my_rando_list = []
for i in range(100):
    num = random.randrange(5, 11)
    my_rando_list.append(num)

print(my_rando_list)

# Summing a list
total = 0

for num in my_rando_list:
    total += num

print(total)
print(sum(my_rando_list))  # won't use for this chapter

print(total / len(my_rando_list))  # calculates average


# Modifying a list
# only do this using INDEX VARIABLE LOOP

my_list = [4, 5, 6, 7]

# cube every item
for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 3

print(my_list)


# Tuples
# Less capable cousin of the list
# immutable list (unchangeable)
RED = (255, 0, 0)
print(RED[0])
# RED[0] = 0  # TypeError: 'tuple' object does not support item assignment


# String Slicing
my_string = "Francis W. Parker"

print(my_string[0])  # prints F
print(my_string[8])  # print W  (spaces are characters too)
print(my_string[-2])  #  print e  (use negative indices)

print(my_string[:])  # colon notation [start:stop]
print(my_string[:4])  # print Fran
print(my_string[4:9])  # print cis W
print(my_string[-3:])  # print ker

# Other string stuff
first = "Francis"
last = "Parker"

print(first, last)
print(first + last)  # joined by concatenation
print(first * 100)
print((first * 3) + (last * 3))

# works with lists too
print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 10)

# print with end=  (from Ch6)
print(first, end="W.")  # by default end="\n"
print(last)


#  Encoding and Decoding
#  Caesar cipher

message = "Leemazing"

# changing a character to a number and back
my_char = "A"
my_ord = ord(my_char)  # changes the letter to a number
print(my_char, my_ord)

# encode
encoded_message = ""

for char in message:
    my_ord = ord(char)
    my_ord -= 7
    my_char = chr(my_ord) # changes back to character
    encoded_message += my_char

print(encoded_message)

# decode
encoded_message = "E^^fZsbg`"
decoded_message = ""

for char in encoded_message:
    my_ord = ord(char)
    my_ord += 7
    my_char = chr(my_ord) # changes back to character
    decoded_message += my_char

print(decoded_message)


# Simulations
rolls = []

for i in range(1000):
    die = random.randrange(1, 7)
    rolls.append(die)

print(rolls)

sixes = 0
for roll in rolls:
    if roll == 6:
        sixes += 1

print("Sixes:", sixes)
print(sixes / len(rolls) * 100)


