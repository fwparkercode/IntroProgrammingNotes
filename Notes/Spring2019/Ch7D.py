# Chapter 7 - Lists (Arrays)

# Data types
my_int = 4
my_float = 4.5
my_string = "Four"
my_bool = True

# New data types
my_list = [10, 11, 12, 13]
my_tuple = (255, 0, 0)


# Working with Lists
print(my_list)
print(my_list[0])  # index goes in the square brackets
print(my_list[3])  # last number in my_list
#print(my_list[4])  # cannot print beyond length of list

# len() function - gives the length of the list (not the last item)
print(len(my_list))

# Change a value in a list
my_list[1] = 20  # overwrites the value in index 1
print(my_list)


# Tuple - The less capable cousin of the list.
# tuples are immutable - they cannot be changed
print(my_tuple)
print(my_tuple[0])
#my_tuple[0] = 200
print(my_tuple)


# ITERATION
# Iterating using a for each loop
# working with a copy of each item in the list
grocery_list = ["spam", "eggs", "milk", "garlic"]

for item in grocery_list:
    item += "."
    print("Don't forget the", item)

print(grocery_list)

number_list = [10, 11, 12, 13, 14]

for number in number_list:
    number **= 2
    print(number)

print(number_list)

# Iteration using the index variable loop

for i in range(len(grocery_list)):
    grocery_list[i] += "."
    print("Don't forget the", grocery_list[i])

print(grocery_list)

for i in range(len(number_list)):
    number_list[i] **= 2

print(number_list)

# Adding to a list using the .append() method
print(grocery_list)
grocery_list.append("Cereal")
print(grocery_list)
grocery_list.append(12)  # python does not care about mixing types
print(grocery_list)

# Make a list of 100 random die rolls
# Start with an empty list
# use a for loop and append

import random
rolls = []

for i in range(100):
    die = random.randrange(1, 7)
    rolls.append(die)

print(rolls)

# how many 6s did I roll?
sixes = 0

for roll in rolls:
    if roll == 6:
        sixes += 1

print("You rolled", sixes, "sixes.")


# Summing a list
my_list = [4, 3, 5, 9]

total = 0

for num in my_list:
    total += num

print(total)


# Double every number in a list (must use index variable loop)

for i in range(len(my_list)):
    #my_list[i] = my_list[i] * 2
    my_list[i] *= 2

print(my_list)


# String slicing
my_string = "Francis Parker"
print(my_string[0])  # strings can be indexed
print(len(my_string))  # len function works on strings
print(my_string[5])  # print i
print(my_string[:])  # prints the whole thing [start:end]
print(my_string[:5])  # prints from left up to but not including index 5
print(my_string[4:10])  # cis Pa
print(my_string[11:])  # ker
print(my_string[-1])  # reverse index starts at -1


# indexing dimensional lists (lists of lists)
list_of_lists = [[10, 11], [12, 13], [14, 15, 16, 17], [18, [19, 20]]]

print(list_of_lists[1])  # print [12, 13]
print(list_of_lists[1][0])  #  print 12#
print(list_of_lists[2][-1])   # print 17
print(list_of_lists[3][1][1])  # print 20
print(list_of_lists[-1][-1][-1])  # if you wanted


# Encoding and decoding
my_char = "P"
my_ord = ord(my_char)  # ordinal function converts text to number (decimal)
print(my_ord)
# print(bin(my_ord))
my_ord += 1
my_new_char = chr(my_ord) # convert number to letter
print(my_new_char)

message = "Qsphsbnnjoh!jt!gvo"
decoded_message = ""

for char in message:
    my_ord = ord(char)
    my_ord -= 1
    my_new_char = chr(my_ord)
    decoded_message += my_new_char
    print(my_new_char)

print(decoded_message)




# Use string slicing so that when the user enters
# the month number, the three letter month is printed.

n = int(input("Enter a month number: "))
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
print(months[n])  # change this line only