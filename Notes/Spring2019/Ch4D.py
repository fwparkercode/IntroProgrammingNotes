# Chapter 4 - Loops and Random Numbers

#  FOR loop
#  Repeats code a specific number of times

for i in range(10):
    print("Francis")
    print("Parker")

#  the i (or j or whatever) is the index variable
#  The index (i) can be used in your loop
for i in range(10):
    print(i)
print()

# range function can take three parameters (start, end, count_by)
# count from 1 to 10
for i in range(1, 11):
    print(i)
print()

# count from 1 to 100 by 2
for i in range(1, 101, 2):
    print(i)
print()

# count from -20 to -5
for i in range(-20, -4):
    print(i)
print()

# count from 10 down to 1h
for i in range(10, 0, -1):
    print(i)
print()


# Nested loops
for i in range(5):
    print("Francis")
for j in range(5):
    print("Parker")

for i in range(5):
    print("Francis")
    for j in range(5):
        print("Parker")


#  Keep a running total
# find the sum of the series 1 to 100 (1 + 2 + 3 ... + 100)

total = 0

for i in range(1, 101):
    # print(i)
    total += i

print(total)

a = 0

for i in range(10):
    a += 1
    for j in range(10):
        a += 1
        for k in range(10):
            a += 1

print(a)

# While loops
#  The more capable cousins of FOR loops
#  Little more difficult to control

#  count from 0 to 9
for i in range(10):
    print(i)

x = 0
while x < 10:
    print(x)  # position of the print matters
    x += 1

# count from 1 to 10
for whatever in range(1, 11):
    print(whatever)

x = 0
while x < 10:
    x += 1
    print(x)  # position of the print matters

x = 1
while x <= 10:
    print(x)
    x += 1

# print even numbers from 2 to 100
x = 2
while x <= 100:
    print(x)
    x += 2

# print all squares less than 100000
x = 1
square = 0
while square < 100000:
    print(square)
    square = x ** 2
    x += 1

x = 1
while x ** 2 < 100000:
    print(x ** 2)
    x += 1

# powers of 2 less than 1000000
x = 1

while x < 1000000:
    print(x)
    x *= 2

# Game loop
'''
print("Welcome to Dragon's Quest 3!")
done = False  # boolean for game over condition
while done == False:
    print("There is a dragon blocking the exit.")
    answer = input("Do you want to attack the dragon? ")
    if answer.upper() == "YES" or answer.upper() == "Y":
        print("Poor choice, the dragon ate you!")
        done = True
    else:
        print("The room is getting hotter.")

print("Thank you for playing!")
'''

# Infinite loops
# not good (no way to exit)

'''
x = 5

while x < 10:
    print("Hello")
'''

'''
x = 10

while x > 0:
    x *= 2
    print(x)
'''

# Random numbers
# pseudo random numbers are generated from the random library
import random

# randrange function takes 3 parameters (start, end, count_by)
# returns a random int
for i in range(10):
    print(random.randrange(10))  # 0 to 9

print()

for i in range(10):
    print(random.randrange(1, 11))  # 1 to 10

print()

for i in range(10):
    print(random.randrange(2, 101, 2))  # even from 2 to 100

print()

# random function returns a float from 0 to 1 (no parameters)
for i in range(10):
    print(random.random())

# to get number other than 0 to 1...
#  random() * range + offset

for i in range(10):
    print(random.random() * 10)  # random float from 0 to 10

print()
for i in range(10):
    print(random.random() * 10 + 5)  # random float from 5 to 15


print()
for i in range(10):
    print(random.random() * 11 - 4)  # random float from -4 to 7


# roll a 6 sided die one million times.  How many sixes did you get?
sixes = 0
for i in range(1000):
    roll = random.randrange(1,7)
    if roll == 6:
        sixes += 1

print(sixes / 1000 * 100, "%")


# coin flipper
heads = 0
tails = 0

flip = random.randrange(2)
if flip == 0:
    print("Heads")
    heads += 1
else:
    print("Tails")
    tails += 1


# rock paper scissor
player = int(input("Enter your choice (0 for rock, 1 for paper, 2 for scissors)"))
computer = random.randrange(3)










