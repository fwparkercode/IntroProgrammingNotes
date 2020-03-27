'''
Chapter 7 Lights Out
'''
import random

done = False


# print numbers 0 to 9 using a for loop
# override "\n" by using keyword argument end = " "
print("Francis", end=" ")
print("Parker")


# create a random X O list
lights = []

for i in range(10):
    flip = random.randrange(2)

    if flip == 0:
        lights.append("O")
    else:
        lights.append("X")


while not done:
    for i in range(10):
        print(i, end=" ")

    print()

    for light in lights:
        print(light, end=" ")

    print()

    choice = int(input("Flip a switch 0 to 9: "))

    print()

    if 0 < choice < 9:
        if lights[choice] == "X":
            lights[choice] = "O"
        else:
            lights[choice] = "X"

        if lights[choice - 1] == "X":
            lights[choice - 1] = "O"
        else:
            lights[choice - 1] = "X"

        if lights[choice + 1] == "X":
            lights[choice + 1] = "O"
        else:
            lights[choice + 1] = "X"