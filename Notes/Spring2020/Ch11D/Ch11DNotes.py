"""
Pygame base template
by Aaron Lee 2020
"""

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
WIDTH = 600
HEIGHT = 500
done = False

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#  images
bg_image = pygame.image.load("trees.jpg")
squirrel_image = pygame.image.load('squirrel.png')

# animation variables
sq_x = 0
sq_y = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            # sq_x = event.pos[0]
            # sq_y = event.pos[1]
            # or use
            sq_x, sq_y = event.pos


    # --- Game logic should go here

    # --- Drawing code should go here
    #screen.fill(WHITE)  # paint the blank canvas
    screen.blit(bg_image, [0, 0])  # images are moved by top left corner

    screen.blit(squirrel_image, [sq_x, sq_y])

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
