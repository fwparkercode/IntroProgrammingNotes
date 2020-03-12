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



