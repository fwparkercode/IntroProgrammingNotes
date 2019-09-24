# Chapter 4 - Loops and Random Numbers

# Random numbers
import random

# Randrange function - random.randrange(start, end, count_by)

print(random.randrange(10))  # generates a random int from 0 to 9
print(random.randrange(5, 10))  # random int from 5 to 9
print(random.randrange(50, 100, 5))  # random int from 50 to 99 counting by 5s


# make a random number between -10 and - 5
print(random.randrange(-10, -4))

# random even number from 28 to 36
print(random.randrange(28, 37, 2))


# random function - random.random()
# generates a random float from 0 to 1
print(random.random())

# to generate any other float use  random.random() * spread + offset
# random float from 0 to 10
print(random.random() * 10)

# random float from 10 to 15
print(random.random() * 5 + 10)

# random float from -5 to 0
print(random.random() * 5 - 5)


# FOR LOOPS

# for the example below: i is the index, range is from 0 to 9
for i in range(10):
    print("Taco Tuesday")
    print("and Quesadillas")

print("Pulled Pork Wednesday")


# print twenty random integers from 0 to 100
for i in range(20):
    print(random.randrange(101))


# Range function - range(start, end, count_by)
# works like random.randrange()
for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(0, 101, 2):
    print(i)

for i in range(50, 10, -5):
    print(i)



# Nested loops
for i in range(3):
    print("a")
for j in range(3):
    print("b")

print("\n\n")
for i in range(3):
    print("a")
    for j in range(3):
        print("b")

'''
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, minutes, seconds)
'''

for row in range(1, 21):
    for seat in range(1, 20):
        print("row", row, "seat", seat)
