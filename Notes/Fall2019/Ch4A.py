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

'''
for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print(hour, minute, second)
'''


# Keeping a running total

# roll a random die (1 to 6)
roll = random.randrange(1, 7)
print(roll)

# roll a random die 5 times
print()
for i in range(5):
    roll = random.randrange(1, 7)
    print(roll)

# add up all 5 dice
print()
score = 0

for i in range(5):
    roll = random.randrange(1, 7)
    print(roll)
    score += roll

print("Total:", score)


#  Add all the numbers from 1 to 100

total = 0

for i in range(1, 101):
    total += i

print(total)

#  WHILE loops
#  When you don't know when you are quitting
#  Looks like an IF statement

# count 1 to 10
for i in range(1, 11):
    print(i)

print()

x = 1
while x < 11:
    print(x)
    x += 1

# count from 20 to 50 by 5's
x = 20
while x <= 50:
    print(x)
    x += 5

# this one is best done with a WHILE loop
# print all the perfect squares less than 100000

n = 0
while n ** 2 < 100000:
    print(n, "squared is", n ** 2)
    n += 1


# GAME LOOPS - looping until you want to quit
done = False  # boolean game condition

'''
print("Welcome to my fun game!")
while not done:
    answer = input("Enter Q to quit: ")
    if answer.lower() == "q":
        done = True
    else:
        print("I hope you are enjoying the game.")
'''

# BEWARE THE INFINITE LOOP
# BAD!!!

'''
done = False
while not done:
    print("I am an infinite loop!")
'''

'''
n = 5
while n > 0:
    print(n)
    n += 1
'''

'''
n = 1 

while n > 0:
    print(n ** 2)
    n = n * 2
    
'''

'''
x = 5

while x == 5 or 6:
    print(x)
    x += 1
'''















