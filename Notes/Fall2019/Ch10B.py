"""
Pygame base template
Aaron Lee - 2019
"""

import pygame
import random
pygame.init()  # initializes pygame (necessary before any pygame functions)


# Global Variables
BLACK = (0, 0, 0)  # red, green, blue (RGB)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 200, 200)
MAROON = (100, 0, 0)
ORANGE = (255, 150, 0)
PURPLE = (150, 50, 200)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)  # Screen object we draw to

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

rect_x = 0
rect_y = 0
rect_color = RED

ellipse_x = 0
ellipse_y = 0
change_x = 0
change_y = 0

pygame.mouse.set_visible(False)  # make mouse disappear

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    # can only occur once in your loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rect_color = BLUE
            print(event.pos)  # where was button pressed
            print(event.button) # which button was pressed
        elif event.type == pygame.MOUSEBUTTONUP:
            rect_color = RED
        elif event.type == pygame.MOUSEMOTION:
            pass
            #print(event.rel)  # speed of your mouse as tuple
        elif event.type == pygame.KEYDOWN:  # pressed key
            if event.key == pygame.K_RIGHT:
                change_x = 3
            if event.key == pygame.K_LEFT:
                change_x = -3
            if event.key == pygame.K_DOWN:
                change_y = 3
            if event.key == pygame.K_UP:
                change_y = -3
        elif event.type == pygame.KEYUP: # lifted my finger
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                change_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                change_y = 0

    # --- Game logic should go here
    ellipse_x += change_x
    ellipse_y += change_y

    rect_x, rect_y = pygame.mouse.get_pos()

    # boundary check
    if rect_x > SCREEN_WIDTH - 20:
        rect_x = SCREEN_WIDTH - 20
    if rect_y > SCREEN_HEIGHT - 20:
        rect_y = SCREEN_HEIGHT - 20

    #print(pos[0])

    # --- Draw to screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, rect_color, [rect_x, rect_y, 20, 20])
    pygame.draw.ellipse(screen, GREEN, [ellipse_x, ellipse_y, 20, 20])

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.