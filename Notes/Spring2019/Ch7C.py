# Chapter 7 - Lists

my_int = 7
my_float = 5.23
my_string = "Hello World"
my_bool = False

# new in this chapter
my_list = ["Hi", 0, 4.5, True]
my_tuple = (255, 0, 0)

# Working with lists
x = [4, 3, 9, 8, 2]
print(x)  # prints the list

print(x[0])  # prints the zero index of the list
print(x[2])
print(x[4])  # don't go past end of list (IndexError)

# changing a value in a list
x[0] = 44
print(x)

# Tuple is just the less capable cousin of a list
# Tuples are immutable (cannot be changed)
my_tuple = (100, 200, 300)
#my_tuple[0] = 150  # this doesn't work


# Iterating through a list
groceries = ["Spam", "Eggs", "Milk"]

for item in groceries:
    print("Don't forget to buy", item)

for number in my_tuple:
    print(number)

# We can even have lists of lists
my_2dlist = [[0, 0], [100, 200], [200, 0]]

for item in my_2dlist:
    print(item)

for item in my_2dlist:
    for number in item:
        print(number)

# For each loop  (cannot change the list)
for item in groceries:
    item = "Spam"
    print(item)

print(groceries)

# Index variable loop (used if you want to talk to the list or change)
# len() function returns the length of the list
print(len(groceries))

for i in range(len(groceries)):
    print(groceries[i])
    groceries[i] = "Spam"

print(groceries)


# Adding to a list (append method)
groceries.append("Cereal")  # adds on to the end of the list
print(groceries)


# Make a list of user inputs
my_numbers = []

for i in range(0):
    num = int(input("Enter a number"))
    my_numbers.append(num)
    print(my_numbers)

# make a list of 100 random rolls of a die (1 to 6)
import random
rolls = []

for i in range(100):
    my_roll = random.randrange(1, 7)
    rolls.append(my_roll)

print(rolls)

# rolling two die
rolls2 = []

for i in range(100):
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    rolls2.append([die1, die2])

print(rolls2)


# Summing and modifying a list.
my_list = [5, 8, 2, 12, 0]

total = 0
for number in my_list:
    print(number)
    total += number

print(total)

# square every term in my_list
for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 2

print(my_list)

# String slicing
# strings can be idexed just like a list

my_text = "Python Is Fun"
print(my_text[0])  # prints P
print(my_text[6])  # prints a blank space (spaces are characters)
print(my_text[-1])  # you can even use reverse indices (prints n)

print(my_text[:])  # colon is used for ranges (start on left, end on right)
print(my_text[:5])  # Pytho
print(my_text[3:8]) # hon I
print(my_text[7:])  # Is Fun
print(my_text[-3:])  # Fun

# String manipulation
# concatenation
first = "Francis"
last = "Parker"
print(first + last)
print(first + " " + last)

# other sometimes useful things
print((first + " ") * 10)
print((first * 3) + (last * 4))

# Problem for you (this is tricky)
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = 1
print(months[(n - 1) * 3: n * 3])  # print out the three letter month

# Accessing a 2d list
list_of_lists = [[10, 11], [12, 13], [14, 15, 16, 17], [18, [19, 20]]]
print(list_of_lists[1])  # print [12, 13]
print(list_of_lists[1][0])  # print 12
print(list_of_lists[2][3])  # print 17
print(list_of_lists[-1][-1][-1])#  print 20
print(list_of_lists[3][1][1])


# Decode me  (not a skill we will test)
my_char = "a"
print(ord(my_char))  # ordinal of the character converts to a decimal number
my_num = ord(my_char) + 1
print(my_num)
my_new_char = chr(my_num)  # convert a number to a character
print(my_new_char)



message = "Qsphsbnnjoh!jt!gvo"
new_message = ""

for char in message:
    my_num = ord(char) - 1
    my_new_char = chr(my_num)  # convert a number to a character
    new_message += my_new_char

print(new_message)
