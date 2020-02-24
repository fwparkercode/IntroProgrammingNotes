#  Chapter 4 - Loops and Random Numbers

import random


# randrange function to create random integers
# randrange(stop)  Assumes 0 up to but not including the stop number
# randrange(start, stop)  from start up to but not including stop number
# randrange(start, stop, step)  step is what we count by

my_number = random.randrange(10)  # random int from 0 to 9
print(my_number)

my_number = random.randrange(10, 21)  # random int from 10 to 20
print(my_number)

my_number = random.randrange(10, 51, 5)  # random multiple of 5 from 10 to 50
print(my_number)

my_number = random.randrange(10, 21, 2)  # random even number from 10 to 20
print(my_number)

my_number = random.randrange(-10, 1)  # random int from -10 to 0
print(my_number)

# random floats
# random function generates a random float from 0 to 1
# multiply to change the range
# add or subtract to offset the range

my_number = random.random()  # generates float from 0 to 1
print(my_number)

my_number = random.random() * 10  # generates float from 0 to 10
print(my_number)

my_number = random.random() * 10 + 5  # generates float from 5 to 15
print(my_number)

my_number = random.random() * 7 - 5 # generates float from -5 to 2
print(my_number)


# FOR LOOPS
# use these when we want to iterate a specific number of times

for i in range(10):
    print("Loops are fun")

# the iterable number can be used in the loop
for i in range(10):
    # print("#####")
    print(i)


# Print the numbers 1 to 10
for i in range(1, 11):
    print(i)

# alternate way
for i in range(10):
    print(i + 1)


# Count by numbers other than 1
for x in range(0, 501, 50):
    print(x)

# Count down from 20 to 10 by -1s
for i in range(20, 9, -1):
    print(i)


# printing numbers from a list (introduce only - covered in Ch7)
for i in [8, 2, 2, 6, 0, 9]:
    print(i)


# Nested loops
# loop inside a loop

for i in range(5):
    print("Hello")
for j in range(3):
    print("Class")


for i in range(5):
    print("Hello")
    for j in range(3):
        print("Class")


# make a clock
# import time
# for hour in range(24):
#     for minute in range(60):
#         for second in range(60):
#             print(hour, minute, second)
#             time.sleep(1)


#  Keep a running total or Find a sum
total = 0

# add up all of the numbers from 1 to 100
for i in range(1, 101):
    total += i

print(total)


# What is the total
total = 0
for i in range(10):
    total += 1

print(total)  # total is 10


total = 0
for i in range(10):
    total += 1
for j in range(10):
    total += 1

print(total)  # total is 20


total = 0
for i in range(10):
    total += 1
    for j in range(10):
        total += 1

print(total)  # total is 110


# WHILE LOOP
# more capable, but more trouble
# If you have a choice, use a FOR LOOP
# we get to set the condition for exiting the loop

# count from 1 to 10
for i in range(1, 11):
    print(i)

i = 1  # equivalent to start of range
while i < 11:
    print(i)
    i += 1

# count down from 20 to 10 using a while loop
i = 20
while i > 10:
    i -= 1  # order matters
    print(i)


# Infinite Loops (BAD)
i = 1
while i < 11:
    print(i)






