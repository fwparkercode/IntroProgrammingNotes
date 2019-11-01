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
GREEN = (0, 255, 0)
DARK_GREEN = (0, 150, 0)
BROWN = (150, 100, 50)


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

def draw_tree(x, y, color):
    """ Draws a tree at x, y position """
    pygame.draw.rect(screen, BROWN, [60 + x, 170 + y, 30, 45])
    pygame.draw.polygon(screen, color, [[150 + x, 170 + y], [75 + x, 20 + y], [x, 170 + y]])
    pygame.draw.polygon(screen, color, [[140 + x, 120 + y], [75 + x, y], [10 + x, 120 + y]])


tree_x = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here
    for i in range(len(snowflakes)):
        snowflakes[i][1] += snowflakes[i][3]  # change y value
        if snowflakes[i][1] > SCREEN_HEIGHT:
            snowflakes[i][1] = -flake_size  # resets to top of screen
            snowflakes[i][0] = random.randrange(SCREEN_WIDTH)
            depth += 0.005
    # --- Draw to screen
    tree_x += 1

    screen.fill(BLACK)
    for x in range(0, SCREEN_WIDTH, 100):
        draw_tree(x + tree_x, 250, DARK_GREEN)
        draw_tree(x - 50, 300, GREEN)


    for flake in snowflakes:
        pygame.draw.ellipse(screen, WHITE, [flake[0], flake[1], flake[2], flake[2]])

    pygame.draw.rect(screen, WHITE, [0, SCREEN_HEIGHT - depth, SCREEN_WIDTH, depth + 1])

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.