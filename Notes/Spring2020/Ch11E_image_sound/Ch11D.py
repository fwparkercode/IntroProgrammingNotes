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
WIDTH = 800
HEIGHT = 500
done = False

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# load images
bg_image = pygame.image.load('space.jpg')
dragon_image = pygame.image.load('dragon.png')
dragon_image2 = pygame.image.load('dragon2.png')

# animation variables
dragon_x = 0
dragon_y = 0


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            dragon_x, dragon_y = event.pos

    # --- Game logic should go here

    # --- Drawing code should go here
    #screen.fill(WHITE)  # paint the blank canvas
    screen.blit(bg_image, [0, 0])

    screen.blit(dragon_image, [dragon_x, dragon_y])
    screen.blit(dragon_image2, [0, 0])

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
