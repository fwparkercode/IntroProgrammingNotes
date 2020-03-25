# Chapter 7 - Lists


# data types
my_string = "Hello"
my_int = 4
my_float = 4.5
my_bool = False
my_list = [1, 5, 0, -3, "hi"]
my_tuple = (True, 5.8, 7, 2)  # like a list, but immutable

# working with lists
grocery_list = ["spam", "eggs", "milk", "cereal"]
print(grocery_list)

print(grocery_list[0])  # index 0 is 'spam'

# iterating through a list
# using a FOR EACH loop
for item in grocery_list:
    print("Don't forget to buy", item)

# indexing a list
my_list = ["string", 4.5, [6, 3, 2], [1, 5, 4], ["left", "right"]]
print(my_list)
print(my_list[1])  # prints 4.5
print(my_list[2])  # prints list
print(my_list[3][0])  # print 1
print(my_list[4][1])  # print right
# print(my_list[5])  # IndexError: list index out of range

# modify a list
my_list[0] = "python"  # use index to assign values
print(my_list)

my_list.append(99)  # adds an item to the end of the list
print(my_list)


# Iterating through a list
# FOR EACH loop looks at a copy of each item in the list
# cannot use FOR EACH to modify the list
for item in my_list:
    item = 8
    print(item)

print(my_list)


# INDEX VARIABLE loop uses the index of each item in the list
# Use it when you need to modify the list
# speaking directly to the list
for i in range(len(my_list)):
    my_list[i] = 8

print(my_list)


# square every item in the list
my_list = [5, 2, 8, 9, 1]
print(len(my_list))  # prints 5

for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 2

print(my_list)


# sum a list
total = 0

for num in my_list:
    # print(num)
    total += num

print(total)

# Tuple - immutable list (can't change it)
my_tuple = (255, 0, 0)
# my_tuple[1] = 255  # can't change a tuple
# my_tuple.append(255)  # can't append to a tuple

print(my_tuple[0])
for color in my_tuple:
    print(color)


# String slicing
my_string = "Francis W. Parker"

print(my_string[0])  # index like lists

for character in my_string:
    print(character)  # iterate like a list

print(my_string[:])  # prints entire string
print(my_string[:4])  # prints beginning up to but not including index 4
print(my_string[:9])  # spaces are characters
print(my_string[4:7])  # print cis
print(my_string[14:])  # print ker
print(my_string[-1])  # negative indices work
print(my_string[-3:])  # print ker


# string math
a = "Hello"
b = "World"
print(a + b)  # concatenation
print(a * 2)
print((a + b) * 100)


# Caesar cipher
message = "Have a great day"
encoded_message = ""

for letter in message:
    n = ord(letter) # ordinal changes char into an int
    n += 4
    character = chr(n)  # chr changes int into a character
    encoded_message += character

print(encoded_message)


encoded_message = "Lezi$e$kviex$he}"
decoded_message = ""




