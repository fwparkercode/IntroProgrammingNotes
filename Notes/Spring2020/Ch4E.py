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


# FOR LOOPS
# When you want to do something a certain number of times

for i in range(5):
    print("Hello")

print("World")

# print 0 to 9
for i in range(10):
    print(i)  # we can use the index variable in the loop


# print 1 to 10
for i in range(1, 11):
    print(i)

# alternate way
for i in range(10):
    print(i + 1)

# print number from 50 to 500 by 50s
for x in range(50, 501, 50):
    print(x)


# print numbers from 20 to 10 by 2s
for i in range(20, 9, -2):
    print(i)


# Nested loops (loop inside a loop)
for i in range(5):
    print("spam")
    for j in range(3):
        print("eggs")


# What does this print
x = 0
for i in range(10):
    x += 1
for j in range(10):
    x += 1

print(x)  # prints 10

x = 0
for i in range(10):
    x += 1  # adds 10 times
    for j in range(10):
        x += 1 # adds 10 * 10 times

print(x)


# Clock
# import time
#
# for hour in range(24):
#     for minute in range(60):
#         for second in range(60):
#             print(hour, minute, second)
#             time.sleep(1)



# Keep a running total
total = 0

for i in range(1, 11):
    total += i

print(total)


# find the total of all numbers 1 to 100
total = 0

for i in range(1, 101):
    total += i

print(total)


# roll a random die 10 times and print result (1 to 6)

for i in range(10):
    print(random.randrange(1, 7) + random.randrange(1, 7)) # two dice


# incrementing
x = 0
x += 1  # increments by 1
x += 2  # increment by 2
x *= 2  # multiply self by 2
x /= 3  # divide by 3 (division always gives a float)
x **= 3  # raise self to power of 3
print(x)



# WHILE LOOPS

# 5 to 10 with FOR loop
for i in range(5, 11):
    print(i)


# 5 to 10 with WHILE loop
i = 5
while i < 11:
    print(i)
    i += 1


# Countdown from 20 to 10
i = 20
while i > 9:
    print(i)
    i -= 1

# Unknown conditions
# print all of the squares below a million

n = 1

while n ** 2 < 1000000:
    print(n, "squared is", n ** 2)
    n += 1


# Infinite loops (problem with while loops)

# condition cannot ever be False
# while 1 < 2:
#     print("Yay")

# change in wrong direction
# x = 10
# while x > 0:
#     x += 1
#     print(x)

# accelerates away from condition
# x = 2
# while x > 0:
#     x *= 2
#     print(x)


# Continuing until user wants to quit
done = False

# while not done:
#     answer = input("Do you want to quit?")
#     if answer.lower() == "y":
#         done = True
#
# print("Thanks for playing!")



# roll two die 100 times
# print the sum of the two die
# how many 7s did you roll
# how many 12s did you roll

sevens = 0
twelves = 0
pairs = 0
total_rolls = 1000000

for i in range(total_rolls):
    roll1 = random.randrange(1, 7)
    roll2 = random.randrange(1, 7)
    total = roll1 + roll2
    if total == 7:
        sevens += 1
    if total == 12:
        twelves += 1
    if roll1 == roll2:
        pairs += 1

print(sevens / total_rolls * 100, "percent sevens")
print(twelves / total_rolls * 100, "percent twelves")
print(pairs / total_rolls * 100, "percent pairs")











