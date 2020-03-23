'''
Lights Out Lab
'''

# end= keyword argument
import random

print("Francis", end="")
print("Parker")


done = False
lights = []

for i in range(10):
    coin_flip = random.randrange(2)
    if coin_flip == 0:
        lights.append("X")
    else:
        lights.append("O")

#print(lights)

while not done:
    for i in range(10):
        print(i, end=" ")
    print()

    for light in lights:
        print(light, end=" ")
    print()

    choice = int(input("Flip a switch 0 to 9: "))  # grab an index from the user
