"""
Animated Snowfall
Aaron Lee - 2019
"""

import pygame
import random
pygame.init()  # initializes pygame (necessary before any pygame functions)


# Global Variables
BLACK = (0, 0, 0)  # red, green, blue (RGB)
WHITE = (255, 255, 255)


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)  # Screen object we draw to

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

# make snowflakes
depth = 1
flake_size = 5
snowflakes = []

for i in range(1000):
    flake_size = random.randrange(3, 10)
    speed = flake_size / 3
    x = random.randrange(SCREEN_WIDTH)
    y = random.randrange(-flake_size, SCREEN_HEIGHT)
    snowflakes.append([x, y, flake_size, speed])

print(snowflakes)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here
    for i in range(len(snowflakes)):
        snowflakes[i][0] += 0.1  # change y value
        if snowflakes[i][0] > SCREEN_WIDTH:
            snowflakes[i][0] = -flake_size  # resets to top of screen
            snowflakes[i][1] = random.randrange(SCREEN_HEIGHT)
            depth += 0.005

    # --- Draw to screen
    screen.fill(BLACK)

    for flake in snowflakes:
        pygame.draw.ellipse(screen, WHITE, [flake[0], flake[1], flake[2], flake[2]])

    pygame.draw.rect(screen, WHITE, [0, SCREEN_HEIGHT - depth, SCREEN_WIDTH, depth + 1])

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.