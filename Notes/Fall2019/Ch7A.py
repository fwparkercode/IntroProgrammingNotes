#  Chapter 7 - Lists (Arrays)

#  Data Types
import math
import random

my_int = -378  # counting number
my_float = 4.348  # decimal number
my_str = "Hello World"  # text
my_bool = False  # True or False
my_list = [0, 0, 200, 100]
my_tuple = (255, 255, 255)  # WHITE

# Working with lists
my_list = [11, 12, 13, 14]
print(my_list)
print(my_list[0])  # index zero has a value of 11
print(my_list[3])
# print(my_list[4])  # list out of range error

# using the index to alter a list
my_list[0] = 10
my_list[3] += 10
print(my_list)

# Tuple
# less capable cousin of the list
# immutable list (unchangeable)
my_tuple = (10, 20, 30)
print(my_tuple[1])  # prints 20
# my_tuple[1] = 50  # tuple does not support item assignment


# Iterating through a list (2 ways)
grocery_list = ["Spam", "eggs", "milk", "bananas"]

# FOR EACH LOOP - uses a copy of each item in the list
for item in grocery_list:
    print("You added", item, "to your cart.")

for item in grocery_list:
    item = "Spam"
    print(item)

print(grocery_list)

# INDEX VARIABLE LOOP - uses the actual indexed list

# len function
print(len(grocery_list))  # gives the length of the list (not last index)

for i in range(len(grocery_list)):
    print(grocery_list[i])

for i in range(len(grocery_list)):
    grocery_list[i] = "Spam"

print(grocery_list)


#  Lists of lists (2d lists)
my_2d_list = [[0, 0], [100, 0], [50, 50], [True, "Hello", 3.4, [99, 101]]]
print(my_2d_list)
print(my_2d_list[0])
print(my_2d_list[1][0])  # 100
print(my_2d_list[3][1])
print(my_2d_list[3][3][1])


print()
# you can iterate through 2d lists as well
for item in my_2d_list:
    for x in item:
        print(x)


# append to list

my_list = []
print(my_list)

my_list.append(19)  # adds the value to the end of the list
my_list.append("Mr. Lee")
my_list.append(True)
print(my_list)


my_list = []

for i in range(10):
    my_list.append(i)

print(my_list)

'''
for i in range(3):
    my_list.append(input("Enter a value to append: "))

print(my_list)
'''

# Summing a list

my_list = [534, 354, 67678, 234, 76867, 233]

total = 0
for number in my_list:
    total += number

print(total)
print(total / len(my_list))
print(sum(my_list))  # don't use sum in this chapter
print(sum(my_list) / len(my_list))

# double all the numbers in my_list
for number in my_list:
    number *= 2

print(my_list)

for i in range(len(my_list)):
    my_list[i] *= 2  # this is the only way to modify a value in a list (use the index)

print(my_list)


# String Slicing
# Strings are really just lists of characters
my_str = "Francis W. Parker"

print(my_str[0])  # print F
print(my_str[8])  # print W, spaces count
print(my_str[-2])  # print e, index backwards starts with -1

print(len(my_str))  # this works on strings too

print(my_str[:])  # print whole string
print(my_str[:4]) # print Fran
print(my_str[4:9])  # print cis W
print(my_str[8:])  # print W. Parker
print(my_str[-3:])  # print ker


#  THIS PART IS FYI
print("A")
print(ord("A"))  # ordinal value
print(chr(65))  # chr prints the ascii value of a number

my_message = "Mr. Lee is the Greatest"

# encode
my_encoded_message = ""

for letter in my_message:
    num = ord(letter)
    num += 1
    encoded_char = chr(num)
    my_encoded_message += encoded_char  # concatenation

print(my_encoded_message)

new_encoded_message = "Ns/!Mff!jt!uif!Hsfbuftu"  # decode me
decoded_message = ""

for letter in new_encoded_message:
    num = ord(letter)
    num -= 1
    decoded_char = chr(num)
    decoded_message += decoded_char

print(decoded_message)



#  EXTRA STUFF FROM CHAPTER 6/7
#  making grids

print("Purple")
print("Panda")

print("Purple", "Panda")
print("Purple" + "Panda")

print("Purple", end=" ")  # replace \n which is default ending
print("Panda")

# Making grids

for i in range(10):
    print("*", end=" ")

'''
* * * * * * * * * *
'''

print("\n")  # double space

for j in range(10):
    for i in range(10):
        print("*", end=" ")
    print()

'''
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
'''

print("\n")  # double space

for j in range(10):
    for i in range(5):
        print("*", end=" ")
    print()

'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''


print("\n")  # double space

for j in range(10):
    for i in range(10):
        print(i, end=" ")
    print()

'''
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
'''

print("\n")  # double space

for j in range(10):
    for i in range(10):
        print(j, end=" ")
    print()

'''
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
'''

print("\n")  # double space

for j in range(10):
    for i in range(j + 1):
        print(i, end=" ")
    print()

'''
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5
0 1 2 3 4 5 6
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8 9
'''

# multiplication table
print("\n")  # double space

for j in range(1, 10):
    for i in range(1, 10):
        if i * j < 10:
            print(" ", end="")
        print(i * j, end=" ")
    print()




#  Roll a die 100 times and record it into a list
# Go back through the list and count the number of sixes you rolled.

rolls = []

for i in range(1000):
    die = random.randrange(1, 7)
    rolls.append(die)

print(rolls)

sixes = 0
for num in rolls:
    if num == 6:
        sixes += 1

print("Sixes:", sixes)
print("Percent sixes:", str(sixes / len(rolls) * 100) + "%")


# Roll a pair of dice 100 times and record it into a 2d list
# Go back through the list and count the number of sevens.
# [[1, 4], [2, 3], [5, 6]]

rolls = []
for i in range(1000):
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    rolls.append([die1, die2])

print(rolls)

sevens = 0
for roll in rolls:
    total = roll[0] + roll[1]
    if total == 7:
        sevens += 1

print("Sevens:", sevens)
print("Percent sevens:", sevens / len(rolls) * 100)

