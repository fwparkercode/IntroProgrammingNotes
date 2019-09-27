# Chapter 4 - Loops and Random Numbers

# Random Numbers
import random

# random.randrange() - generate a random int in a range you choose
# random.randrange(start, end+1, count_by)

print(random.randrange(10))  # generate a random int from 0 to 9
print(random.randrange(1, 11))  # random int from 1 to 10
print(random.randrange(5, 50, 5))  # random number from 5 to 45 by 5s


print(random.randrange(10, 16))  # random number from 10 to 15
print(random.randrange(-5, 6))  # random number from -5 to 5
print(random.randrange(-8, -3))  # random number from -8 to -4
print(random.randrange(8, 41, 2))  # random even number from 8 to 40


# random.random() - generates a random float from 0 to 1
# random.random() * spread + offset

print(random.random())
print(random.random() * 5)  # random float from 0 to 5
print(random.random() * 5 + 5)  # random float from 5 to 10
print(random.random() * 25 - 5)# random float from -5 to 20


# FOR loops
# allows us to repeat code a specific number of times

for i in range(10):
    print("Taco Tuesday")
    print("And Quesadillas")
    print()

print("Waffle Wednesday")

# print 0 to 9
for i in range(10):
    print(i)

# print 1 to 10
for i in range(1, 11):
    print(i)

# print from -10 to -5
for i in range(-10, -4):
    print(i)

# print 5 to 100 by 5s
for i in range(5, 101, 5):
    print(i)

# print 20 to 10 by 1s
for i in range(20, 9, -1):
    print(i)


# Nested FOR loops

print()
for i in range(3):
    print("a")
for j in range(3):
    print("b")

print()
for i in range(3):
    print("a")
    for j in range(3):
        print("b")

x = 0
for i in range(5):
    x += 1
    for j in range(5):
        x += 1

print(x)

'''
for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print(hour, minute, second)
'''

# Keep a running total

# add all the numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i

print(total)

# roll a die 1 to 6
roll = random.randrange(1, 7)
print(roll)

# roll 5 dice
for i in range(5):
    roll = random.randrange(1, 7)
    print(roll)
print()

# roll 5 dice and find the total

total = 0
for i in range(5):
    roll = random.randrange(1, 7)
    total += roll
    print(roll)
print(total)

# WHILE loops
# Use a FOR loop when you can
# Use a WHILE loop when you don't know when to quit
# look a lot like IF statements

# count from 1 to 10
for i in range(1, 11):
    print(i)

x = 1
while x < 11:
    print(x)
    x += 1


# count from 10 to 50 by 5's
x = 10
while x <= 50:
    print(x)
    x += 5


#  Some problems are best solved with a WHILE
#  find all of the powers of 2 less than 10,000,000

n = 1
while 2 ** n < 10000000:
    print(2 ** n)
    n += 1


# The Game Loop
print("Welcome to my exciting game!")
done = False # boolean condition for my game loop

'''
while not done:
    answer = input("Press q to Quit: ")
    if answer.lower() == "q":
        done = True
    else:
        print("I hope you are enjoying the game")
'''

# BEWARE THE INFINITE LOOP!!
'''
while True:
    print("Infinity and Beyond")


x = 10
while x > 0:
    print(x)
    x = x * 2
'''


# for fun
total = 0
number_rolls = 0

while total < 30:
    total = 0
    for i in range(5):
        roll = random.randrange(1, 7)
        total += roll
        print(roll)
    print(total)
    number_rolls += 1

print(number_rolls)












