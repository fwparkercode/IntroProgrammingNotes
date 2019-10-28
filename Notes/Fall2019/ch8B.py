"""
Pygame base template
Aaron Lee - 2019
X linear motion with wrapping (i.e. cars going down road, clouds going by)
X linear motion with bouncing (i.e. tennis match, eyes looking left right)
 growing or shrinking (i.e. window rolling down on car)
 color shift (i.e. sky color shift)
 blinking (i.e. twinkling stars, flickering candle)
 color change (flashing lights on fire truck, lights on Christmas tree)
 acceleration (i.e. gravity fall, bouncing, changing speeds)
 rotation (requires trig - ferris wheel, clock etc.)
X animation with lists (i.e. snowfall, leaves falling)
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
change_x = 5
rect_y = 0
change_y = 5

my_color = [random.randrange(256), random.randrange(256), random.randrange(256)]

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    rect_x += change_x
    rect_y += change_y

    '''
    # wrapping around the screen
    if rect_x > SCREEN_WIDTH:
        rect_x = -50
    '''

    # bounce in x
    if rect_x > SCREEN_WIDTH - 50:
        change_x *= -1
    if rect_x < 0:
        change_x *= -1


    # bounce in y
    if rect_y > SCREEN_HEIGHT - 50:
        change_y *= -1
    if rect_y < 0:
        change_y *= -1


    # --- Draw to screen
    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, [rect_x, rect_y, 50, 50])

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.