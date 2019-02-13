# Loops and Random Numbers
# Loops are useful when you want to repeat a step

for i in range(10):
    print("Hello World")
    print("Hello Mom")
print("Back to the global scope indent")

# we can use that index variable in the code
for i in range(10):
    print(i)

# we can even specify the range
for i in range(1, 11):
    print(i)

for i in range(-5, 6):
    print(i)

# we can even specify what we are counting by (default is 1)
for i in range(50, 100, 10):
    print(i)

# show me -5 to 25 counting by 5s
for i in range(-5, 26, 5):
    print(i)

# you can count backwards
for i in range(10, 0, -1):
    print(i)


# Nested loops
for i in range(5):
    print("Francis")
    for j in range(5):
        print("Parker")
'''
for i in range(25):
    for j in range(60):
        for k in range(60):
            print(i, j, k)
'''
# Keep a running total with a loop
total = 0


for i in range(3):
    #num = int(input("Enter a number: "))
    num = 0
    total += num


print(total)

# find the sum of all numbers from 1 to 100
total = 0

for i in range(1, 101):
    print(i)
    total += i

print(total)


# RANDOM numbers
import random

# create a random integer using random.randrange()
my_num = random.randrange(5)  # generates a random 0 to 4
print(my_num)

print(random.randrange(1, 11))  # int from 1 to 10

print(random.randrange(10, 21))  # int from 10 to 20

print(random.randrange(5, 16, 3))  # int from 5 to 15 by 3s

print(random.randrange(-5, 11, 5)) # int from -5 to 10 by 5s

# Make a roll of two dice
die1 = random.randrange(1, 7)
die2 = random.randrange(1, 7)
two_dice = die1 + die2
print(die1, "+", die2, "=", two_dice)


# RANDOM Floats
print(random.random())  # float from 0 to 1

print(random.random() * 10)  # float from 0 to 10
print(random.random() * 10 + 5)  # float from 5 to 15
print(random.random() * 8 - 12)  # float from -12 to -4

# WHILE LOOPS
# more capable cousin of the FOR loop

# as a FOR loop
for i in range(5, 0, -1):
    print(i)

# as a WHILE loop
x = 5
while x > 0:
    print(x)  # it matters where this print statement is
    x -= 1

# as a FOR Loop
for i in range(5, 100, 5):
    print(i)

# as a WHILE Loop
x = 5
while x < 100:
    print(x)
    x += 5


# Looping until user wants to quit
# Done with a WHILE loop, never a FOR loop
print("Welcome to Dragon Quest 2")
done = False  # this is the loop condition (trigger/switch)

while not done:
    print()
    print("You are in a cave.")
    print("A dragon is blocking the exit.")
    answer = input("Do you want to wake the dragon? ")

    if answer.upper() == "YES" or answer.upper() == "Y":
        print("The dragon eats you.")
        done = True

print()
print("Game Over")
print("Thank you for playing Dragon Quest 2!")

# The problem with a WHILE loop

# this is an infinite loop
'''
i = 0
while i < 5:
    i -= 1
    print(i)


done = False
while not done:
    print("Hello")
'''

# roll a die
import random
sevens = 0

for i in range(10000000):
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    total = die1 + die2
    if total == 7:
        # print("You rolled a seven")
        sevens += 1

print("you rolled", sevens, "sevens.")


# problem set help

import random
flip = random.randrange(2)
if flip == 0:
    pass
    # do something
elif flip == 1:
    pass
    # do something else





