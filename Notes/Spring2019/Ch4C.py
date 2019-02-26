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