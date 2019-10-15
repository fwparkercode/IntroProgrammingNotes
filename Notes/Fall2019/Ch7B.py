#   Chapter 7 - Lists (Arrays)

#  Data Types
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