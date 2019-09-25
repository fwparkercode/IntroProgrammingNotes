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

