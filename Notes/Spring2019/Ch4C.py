# Chapter 4 - Loops and Random Numbers

# Random Numbers
import random

# Generate a random integer using randrange
print(random.randrange(10))  # generates a random int from 0 to 9

# you can also set low and high range for randrange function
print(random.randrange(1, 11))  # first one is included, last one is not
print(random.randrange(15, 21))  # random number from 15 to 20
print(random.randrange(-5, 6))  # random int from -5 to 5

# you can also dictate the count with the third argument
print(random.randrange(2, 101, 2))  # counts by 2 (random even number from 2 to 100)

# roll a die
print("You rolled a", random.randrange(1, 7))


# Random floats are generated using random() function
# random function only generates a number from 0 to 1
print(random.random())

# you can adjust the range of your random float
# random.random(0) * range + offset
print(random.random() * 10)  # random float from 0 to 10
print(random.random() * 5 + 10)  # random float from 10 to 15
print(random.random() * 15 - 5)  # float from -5 to 10


#  FOR LOOPS
#  repeats code a specific number of times

# i is the index, range is how many times to repeat
for i in range(10):
    print("Hello World")
    print("Hello Class")

# i can also be used as a variable
for i in range(10):
    print(i)

# the range function looks like the randrange function (start, end, count_by)

# counts 1 to 10
for i in range(1, 11):
    print(i)

# counts by 5s from 5 to 45
for i in range(5, 50, 5):
    print(i)

# count from - 5 to 3
for i in range(-5, 4):
    print(i)

# count from - 20 to -12 by 2s
for i in range(-20, -11, 2):
    print(i)

# you can even use a negative count_by
for i in range(20, -1, -1):
    print(i)


# Nested loops

for i in range(5):
    print("Francis")
    for j in range(5):
        print("Parker")

# Keeping a running total
# Sum all of the numbers from 1 to 100

total = 0
for i in range(1, 101):
    total += i

print(total)

a = 0

for i in range(10):
    a += 1
    for j in range(10):
        a += 1
        for j in range(10):
            a += 1

print(a)

print("${:.2f}".format(5.80))

number = input("Enter a number")
try:
    number = float(number)
except:
    print("That is not a number")















