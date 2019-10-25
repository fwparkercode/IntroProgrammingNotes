
import random

done = False  # condition for game loop
lights = []  # game board

for i in range(10):
    num = random.randrange(2)
    if num == 0:
        lights.append("X")
    else:
        lights.append("O")

# print(lights)

print("Welcome message")


while not done:

    for i in range(10):
        print(i, end=" ")

    print()

    # print my board (Xs and Os)  YOU DO THIS

    index = int(input("Flip a switch 0 to 9: "))

    if lights[index] == "X":
        lights[index] = "O"
    elif lights[index] == "O":
        lights[index] = "X"


    if lights[index + 1] == "X":
        lights[index + 1] = "O"
    elif lights[index + 1] == "O":
        lights[index + 1] = "X"