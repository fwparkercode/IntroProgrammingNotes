# Chapter 09 Problem Set - FUNCTIONS are FUN! (18pts)
# 11

#############################################################################################
# Section 1                                                                            #
# This next section involves finding the mistakes in the code.                              #
# Videos at the end of the chapter can help with these problems if you need an explanation. #
# This section is worth 6 points.                                                           #
#############################################################################################


# Problem 1 (1pt)
# Correct the following code: (Don't let it print out the word `None')
# Only change the function.  Do not change the call to the function.


def find_sum(a, b, c):
    return a + b + c


print(find_sum(10, 11, 12))


# Problem 2 (1pt)
# Correct the following code: (x should increase by one, but it doesn't.)
# The correct solution involves capturing and use the returned value from the function.

def increase(x):
    return x + 1


x = 10
print("x is", x, " I will now increase x.")
x = increase(x)  # AND CAPTURE
print("x is now", x)


# Problem 3
# Correct the following code (1pt)

def print_hello():
    print("Hello")


print_hello()


# Problem 4
# Correct the following code (1pt)

def count_to_ten():
    for i in range(10):
        print(i)


count_to_ten()


# Problem 5
# There are two things wrong with this one
# Correct the following code (1pt)

def sum_list(my_list):
    total = 0
    for i in my_list:
        total += i
    return total


favorite_numbers = [45, 2, 10, -5, 100]
print(sum_list(favorite_numbers))


# Problem 6 (1pts)
# Correct the following code: (This almost reverses the string. What is wrong?)
# Think about how reverse indices work.

def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[(i + 1) * -1]
    return result


text = "Programming is the coolest thing ever."
print(reverse(text))


############################################################################
#  Section 2                                                          #
#  (12 pts) For this section, write code that satisfies each description    #
#  Make sure that you both write AND call the function you create.         #
############################################################################

# Problem # 7 (2pts)
# writeL a function called multiprint that takes in two parameters.
# The first parameter will be a string named phrase.
# The second parameter will be a number named count.
# Print phrase to the screen count times.
# (e.g., the function takes in "Hello" and 5, then prints "Hello" five times.)

def multiprint(phrase, count):
    for i in range(count):
        print(phrase)

multiprint("hello", 5)


# Problem # 8 (2pts)
# Write a function that takes in a number, and returns the square of that number.
# Note, this function should RETURN the answer, not print it out.

def square_me(n):
    return n ** 2

print(square_me(5))


# Problem # 9 (2pts)
# Write a function that will take two numbers as parameters
# and RETURN their product AND sum as a tuple.

def product_sum(n1, n2):
    my_sum = n1 + n2
    my_product = n1 * n2
    return my_sum, my_product

print(product_sum(4, 6))

# Problem # 10 (3pts)
# Write a function called min3 that will take three parameters and return the smallest value.
# If more than one number tied for smallest, it will still return that smallest number.
# Use a proper if/elif/else chain.

'''
Once you've finished writing your function, copy/paste the following code and make sure that it runs against the function you created:
print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))
You should get this result:

4
4
4
-100
A
'''


def min3(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))

# Problem # 11 (3pts)
# Write a function called 'find' that will take a list of numbers called my_list and a number called key.
# Have it search the list for the value contained in key.
# Each time your function finds the key value, print the index position of the key as shown in the sample run below.
# You will need to juggle three variables, one for the list, one for the key, and one for the position of where you are in the list.

def find(my_list, key):
    for i in range(len(my_list)):
        if my_list[i] == key:
            print("Found", key, 'at', i)


my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(my_list, 12)
find(my_list, 91)
find(my_list, 80)


'''
Sample Run

...copy/paste this code to test it:

my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(my_list, 12)
find(my_list, 91)
find(my_list, 80)


...check for this output:

Found 12 at position 11
Found 12 at position 13
Found 91 at position 5
'''


