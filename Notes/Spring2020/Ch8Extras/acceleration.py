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
HEIGHT = 600
done = False

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

rect_x = 0
change_x = 4

rect_y = 0
change_y = 0
gravity = 0.1
elasticity = 0.85

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    rect_x += change_x

    if rect_x >= WIDTH - 50:
        rect_x = WIDTH - 50
        change_x *= -1
    if rect_x <= 0:
        rect_x = 0
        change_x *= -1

    change_y += gravity
    rect_y += change_y

    if rect_y > HEIGHT - 50:
        rect_y = HEIGHT - 50
        change_y *= -elasticity
        change_x *= elasticity

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas

    pygame.draw.rect(screen, BLUE, [rect_x, rect_y, 50, 50])

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
