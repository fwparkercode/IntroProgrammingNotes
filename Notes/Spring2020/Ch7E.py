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
sevens = 0

for roll in my_rolls:
    total = roll[0] + roll[1]
    if total == 7:
        sevens += 1

print(sevens / len(my_rolls) * 100, "percent sevens")

# String slicing
my_string = "Strings are a lot like lists!"

# indexing strings
print(my_string[0])  # works like a list
print(my_string[7])  # spaces are characters too
print(my_string[-1])  # print the exclamations mark using reverse index

# ranges of indices
print(my_string[:4])  # beginning up to but not including index 4
print(my_string[15:])  # 15 to the end
print(my_string[-3:])  # last three characters
print(my_string[6:13])  # print "s are a"

# string math
a = "Francis"
b = "Wayland"
c = "Parker"

print(a + b + c)
print(a * 3)

for character in a:
    print(character)


# challenge problem
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# n = int(input("Enter a month number: "))
n = 1

# write code that will print the correct three letter month abbreviation for the number
# if I enter 3, it prints "Mar"
# start by just printing first letter of month
# USE STRING SLICING

print(months[(n - 1) * 3:(n - 1) * 3 + 3])


# Caesar cipher
message = "Leave room"




encoded_message = ""

for char in message:
    new_char = ord(char) + 2  # ordinal function changes character to number
    new_char = chr(new_char)  # chr changes ordinal into character
    encoded_message += new_char

print(encoded_message)

# decode
decoded_message = ""
for char in 'Ngcxg"tqqo':
    new_char = ord(char) - 2