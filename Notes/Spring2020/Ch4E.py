# Chapter 4 - Loops and random numbers

import random

# randrange function
# creates a random integer randrange(start, stop, step)
# first number (start) is included, but stop is not.

my_number = random.randrange(100)  # random number from 0 to 99
print(my_number)

my_number = random.randrange(1, 7)  # random 1 to 6
print(my_number)

my_number = random.randrange(5, 51, 5)  # random 5 to 50 by 5's
print(my_number)

my_number = random.randrange(20, 41, 2)  # random even number from 20 to 40
print(my_number)


# random function
# generates a random float from 0 to 1
# multiply by number to change the range of values
# add or subtract to offset the range

my_number = random.random()  # random float 0 to 1
print(my_number)

my_number = random.random() * 10  # random float from 0 to 10
print(my_number)

my_number = random.random() * 10 + 5  # random float from 5 to 15
print(my_number)

my_number = random.random() * 9 - 6  # random float from -6 to 3
print(my_number)