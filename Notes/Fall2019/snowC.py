"""
Pygame Template
Aaron Lee - 2019
"""

import pygame
import math
import random

pygame.init()  #  initializes pygame


# Define variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
GRAY = (100, 100, 100)
PINK = (255, 200, 200)
ORANGE = (255, 150, 0)
MAROON = (100, 0, 0)
BROWN = (100, 50, 50)


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # condition for my game loop


# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mr. Lee's Game")

clock = pygame.time.Clock()  # creates a clock object that manages updates

# Snow variables
snowflakes = []

for i in range(1000):
    flake_size = 5
    flake_x = random.randrange(SCREEN_WIDTH - flake_size)
    flake_y = random.randrange(SCREEN_HEIGHT - flake_size)
    snowflakes.append([flake_x, flake_y])

print(snowflakes)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard, controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    for i in range(len(snowflakes)):
        snowflakes[i][1] += 1
        if snowflakes[i][1] > SCREEN_HEIGHT:
            snowflakes[i][1] = -flake_size

    # --- Drawing code goes here
    screen.fill(BLACK)

    for flake in snowflakes:
        pygame.draw.ellipse(screen, WHITE, [flake[0], flake[1], flake_size, flake_size])

    # snowman
    pygame.draw.ellipse(screen, WHITE, [23 + 280, 20 + 340, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [0 + 280, 65 + 340, 100, 100])


    pygame.display.flip()  # updates the screen

    clock.tick(60) # frames per second

pygame.quit() # Close the window and quit.
