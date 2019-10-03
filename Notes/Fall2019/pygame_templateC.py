"""
Pygame Template
Aaron Lee - 2019
"""

import pygame

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


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard, controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code goes here
    screen.fill(WHITE)

    # rect(surface, color, [top_left_x, top_left_y, width, height], optional_thickness)
    pygame.draw.rect(screen, RED, [0, 0, 100, 50])
    pygame.draw.rect(screen, BLACK, [0, 0, 100, 50], 3)
    pygame.draw.rect(screen, GREEN, [600, 400, 100, 100])
    pygame.draw.rect(screen, CYAN, [550, 350, 100, 100])
    

    pygame.display.flip()  # updates the screen

    clock.tick(60) # frames per second

pygame.quit() # Close the window and quit.
