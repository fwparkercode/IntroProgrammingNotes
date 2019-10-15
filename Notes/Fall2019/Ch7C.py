#  Chapter 7 - Lists (Arrays)

#  Data Types
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


