# Chapter 4 - Loops and Random Numbers

# FOR loop
# Useful for repeating code a specific number of times

for i in range(10):
    print("Hello")
    print("Goodbye")
print("This will print once")

# We can use the index in the loop
for i in range(10):
    print(i)

# We can even adjust the range
for j in range(1, 11):
    print(j)

# We can do steps
for k in range(5, 50, 5):
    print(k)

# We can go backwards and negative
for i in range(5, -5, -3):
    print(i)

# Nested Loops

for i in range(10):
    print("i")
    for j in range(10):
        print("j")


#import time

'''
for a in range(24):
    for b in range(60):
        for c in range(60):
            print(a, b, c)
            #time.sleep(1)
'''


# Running Totals

# add all the numbers from 1 to 100
total = 0

for i in range(101):
    total += i

print(total)

# add user input numbers together
total = 0

for i in range(3):
    #  my_number = int(input("Number: "))
    my_number = 2
    total += my_number

print(total)



# Random Numbers

import random

my_number = random.randrange(10)  # int from 0 to 9
print(my_number)
# randrange follows same format as range() in a FOR loop

print(random.randrange(10, 21))  # int from 10 to 20

print(random.randrange(0, 51, 5)) # random multiple of 5 from 0 to 50

# Sometimes you need a float
print(random.random())  # random float from 0 approaching 1.00000

print(random.random() * 10)  # random float from 0 to 10.0000

print(random.random() * 5 + 5)  # random float from 5 to 10.000

print(random.random() * 10 - 5) # random float from -5 to 5

# WHILE loop
# has more flexibility than the FOR loop
# if you have the choice, use a FOR loop
# WHILE loop continues until a condition is satisfied
# Looks similar to IF condition

# FOR loop
for i in range(10):
    print(i)

# WHILE loop
i = 0  # establish a condition you can check
while i < 10:
    print(i)  # the location of a print or code is important
    i += 1

for i in range(5, 15):
    print(i)

i = 5
while i < 15:
    print(i)
    i += 1

for i in range(5, -10, -2):
    print(i)

i = 5
while i > -10:
    print(i)
    i -= 2

# The game loop
done = True
while not done:
    answer = input("Do you want to quit? ")
    if answer.upper() == "YES" or answer.upper() == "Y":
        done = True
    else:
        print("I hope you are enjoying the game.")

print("Game Over")



# The problem with while loops
'''
x = 5
while x > 0:
    print("Hi")

x = 10
while x > 0:
    x += 1
    print(x)
'''

# Roll two die added together 100000 times
# find out how many sixes you rolled

sixes = 0
rolls = 1000

for i in range(rolls):
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    #print(die)
    if die1 + die2 == 6:
        sixes += 1

print("You rolled", sixes, "sixes.")
print(round(sixes / rolls * 100, 3), end = "%")



# for problem set
import random
flip = random.randrange(2)

if flip == 1:
    pass
    # do something
else:
    pass
    # do something else

