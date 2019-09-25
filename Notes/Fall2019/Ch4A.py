#  Chapter 4 - Loops and Random Numbers

#  Random Integers
#  random.randrange(start, stop, step)

import random

print(random.randrange(10))  # random int from 0 to 9
print(random.randrange(1, 11))  # random int from 1 to 10
print(random.randrange(11, 15))  # random 11 to 14
print(random.randrange(-5, 6))  # random -5 to 5
print(random.randrange(-10, -4))  # random -10 to -5
print(random.randrange(10, 51, 5))  # random multiple of 5 from 10 to 50


#  Random Floats
#  random.random()
#  generates a float from 0 to 1
#  random.random() * (high-low) + offset

print(random.random())  # float from 0 to 1
print(random.random() * 5)  # float from 0 to 5
print(random.random() * 4 + 6)  # float from 6 to 10
print(random.random() * 5 - 10)  # float from -10 to -5


# FOR loops

for i in range(10):
    print("Taco Tuesday")
    print("and Quesadillas")
    print()

print("Waffle Wednesday")

# we can use the index variable
for i in range(10):
    print(i)

# range works just like random.randrange()
# start stop step

# 1 to 10
for i in range(1, 11):
    print(i)

print()
# 10 to 30 by 2s
for i in range(10, 31, 2):
    print(i)

# 20 to 10
for i in range(20, 9, -1):
    print(i)


# Nested loops
for i in range(3):
    print("a")
for j in range(3):
    print("b")

print()
for i in range(3):
    print("a")
    for j in range(3):
        print("b")

for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print(hour, minute, second)


