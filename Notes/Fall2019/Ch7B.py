#   Chapter 7 - Lists (Arrays)

#  Data Types
import random

my_int = -6  # counting numbers
my_float = 2.08  # decimal
my_str = "Hello"  # text
my_bool = False  # only True or False
my_list = [11, 12, 13, 14]
my_tuple = (255, 255, 0)  # YELLOW

# Working with lists

my_list = [11, 12, 13, 14]  # index 0 has a value of 11
print(my_list)
print(my_list[0])  # index 0
print(my_list[3])
# print(my_list[4]) # produces error "index out of range"

my_list = [21, 22, 23, 24]  # you can overwrite a list
print(my_list)

my_list[0] = 31  # changed the value in the zero index to 31
print(my_list)

# Tuples
# the less capable cousin of the list
# immutable list (unchangable)

my_tuple = (255, 0, 255)
print(my_tuple[0])
#my_tuple[0] = 0  # tuples do not support item assignment


# Iterating through a list (2 ways)
groceries = ["Spam", "eggs", "milk", "cereal"]

# FOR EACH LOOP - iterates through a copy of each item
for item in groceries:
    print("You added", item, "to your cart.")

for item in groceries:
    item = "Spam"
    print(item)

print(groceries)  # the groceries list did not change

# INDEX VARIABLE LOOP - iterates through list by using list directly

for i in range(len(groceries)):
    print(groceries[i])

print(groceries)

for i in range(len(groceries)):
    groceries[i] = "Spam"

print(groceries)

print("The length of groceries is", len(groceries))

# Adding to a list (appending)
groceries.append("apples")  # adds to end of the list
print(groceries)

#  Two dimensional lists (lists of lists)
my_2d_list = [[10, 20], [30, 40, 50], [False, "Clark", "Belden"]]
print(my_2d_list[0])
print(my_2d_list[0][1])
print(my_2d_list[2][2])


# Summing a List (10/17)
my_list = [4, 5, 6, 7, 10, 8]

total = 0

for num in my_list:
    total += num

print(total)  # sum of list
print(total / len(my_list))  # average of the list

# Modify a list
# square every item in the list

for num in my_list:
    num = num ** 2  # this is only a copy

print(my_list)

for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 2

print(my_list)  # this way modified the list


#  String Slicing
#  Strings are just lists of characters
my_school = "Francis W. Parker"

print(my_school[:])  # print whole string using index
print(my_school[0])  # print F
print(my_school[8]) # print W  (spaces count)
print(my_school[len(my_school) - 2]) #  print e
print(my_school[-2])  # print e  (use negative indices)

# Colon notation [start:stop]
print(my_school[:4])  # print Fran
print(my_school[4:9])  # print cis W
print(my_school[-3:])  # print ker

# Other stuff with strings
# Concatenation
print("Hello" + "World")  # glues them together
print("Lee " * 10)
print(("Hello" * 3) + ("World" * 3))

my_list = [1, 2, 3]
print(my_list * 3)
print(my_list + my_list)


# FOR FUN
message = "Leemazing"







encoded_message = ""

for letter in message:
    my_ord = ord(letter)  # ordinal changes chr to an int
    my_ord -= 3
    new_char = chr(my_ord)  # change back to character
    encoded_message += new_char  # concatenate every new character to it

print(encoded_message)


# Chapter 6 extras

print("Purple")
print("Panda")

print("Purple", "Panda")
print("Purple" + "Panda")

print("Purple", end=" ")  # by default this value is \n
print("Panda")


#  making grids

for i in range(10):
    print("*", end=" ")

#  * * * * * * * * * *

print()
print()
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


print()
print()
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
print("\n")
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

print("\n")
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

print("\n")
for row in range(10):
    for i in range(row + 1):
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













#  Roll a die 100 times and record it into a list
# Go back through the list and count the number of sixes you rolled.

rolls = []

for i in range(1000):
    my_roll = random.randrange(1, 7)
    rolls.append(my_roll)
print(rolls)

sixes = 0
for num in rolls:
    if num == 6:
        sixes += 1

print("Sixes:", sixes)
print("Percent sixes:", sixes / len(rolls))
print(1 / 6)



# Roll a pair of dice 100 times and record it into a 2d list
# Go back through the list and count the number of sevens.

rolls = []  # [[1, 4], [2, 3], [5, 6]]

for i in range(1000000):
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







