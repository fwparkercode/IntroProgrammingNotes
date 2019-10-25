"""
Animated Snowfall using lists
Aaron Lee - 2019
"""
import random

import pygame
pygame.init()  # initializes pygame (need to do this before you use it)


# Global Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game!")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

# snowflake data
depth = 1
flake_list = []

for i in range(1000):
    flake_size = random.randrange(3, 10)
    flake_speed = flake_size / 3
    x = random.randrange(SCREEN_WIDTH)
    y = random.randrange(-flake_size, SCREEN_HEIGHT)
    flake_list.append([x, y, flake_size, flake_speed])
    

print(flake_list)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    for i in range(len(flake_list)):
        flake_list[i][1] += flake_list[i][3]
        if flake_list[i][1] > SCREEN_HEIGHT:
            flake_list[i][1] = -flake_size  # reset to top of screen
            flake_list[i][0] = random.randrange(SCREEN_WIDTH)   # randomize in x
            depth += 0.001

    # --- Drawing code goes here
    screen.fill(BLACK)

    for pos in flake_list:
        pygame.draw.ellipse(screen, WHITE, [pos[0], pos[1], pos[2], pos[2]])

    pygame.draw.rect(screen, WHITE, [0, SCREEN_HEIGHT - depth + 1, SCREEN_WIDTH, depth])  # snow on ground

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second


pygame.quit()  # Close the window and quit.