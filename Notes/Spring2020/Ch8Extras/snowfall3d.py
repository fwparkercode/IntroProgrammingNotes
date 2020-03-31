"""
Pygame base template
by Aaron Lee 2020
"""
import random

import pygame

# Define global varibles
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
WIDTH = 800
HEIGHT = 600
done = False

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# snowflake variables
flake_list = []

for i in range(500):
    flake_x = random.randrange(WIDTH)
    flake_y = random.randrange(HEIGHT)
    speed = random.randrange(1, 6)
    flake_list.append([flake_x, flake_y, speed])

print(flake_list)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    for flake in flake_list:
        flake[1] += flake[2]
        if flake[1] > HEIGHT:
            flake[1] = -5
            flake[0] = random.randrange(WIDTH)

    # --- Drawing code should go here
    screen.fill(BLACK)  # paint the blank canvas

    for flake in flake_list:
        pygame.draw.ellipse(screen, WHITE, [flake[0], flake[1], flake[2] + 4, flake[2] + 4])

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
