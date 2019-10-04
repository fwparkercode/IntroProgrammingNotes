"""
Pygame base template
Aaron Lee - 2019
"""

import pygame
pygame.init()  # initializes pygame (necessary before any pygame functions)


# Global Variables
BLACK = (0, 0, 0)  # red, green, blue (RGB)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
line_width = 20


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)  # Screen object we draw to

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Draw to screen
    screen.fill(CYAN)


    for x in range(0, SCREEN_WIDTH, line_width):
        if x % 2 == 0:
            pygame.draw.line(screen, GREEN, [x, 0], [x, SCREEN_HEIGHT], line_width)
        else:
            pygame.draw.line(screen, RED, [x, 0], [x, SCREEN_HEIGHT], line_width)

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(1)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.