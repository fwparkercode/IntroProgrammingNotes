"""
Chapter 8 - Animation
Aaron Lee - 2019
X linear motion with wrapping (i.e. cars going down road, clouds going by)
X linear motion with bouncing (i.e. tennis match, eyes looking left right)
X growing or shrinking (i.e. window rolling down on car)
color shift (i.e. sky color shift)
blinking (i.e. twinkling stars, flickering candle)
color change (flashing lights on fire truck, lights on Christmas tree)
acceleration (i.e. gravity fall, bouncing, changing speeds)
rotation (requires trig - ferris wheel, clock etc.)
X animation with lists (i.e. snowfall, leaves falling)
"""

import pygame
pygame.init()  # initializes pygame (need to do this before you use it)


# Global Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 150, 150)
MAROON = (100, 0, 0)
ORANGE = (255, 150, 0)
PURPLE = (100, 50, 150)


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.


size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game!")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

rect_x = 100
change_x = 0
rect_y = 100
change_y = 0

rect_width = 50

bg_color = [0, 0, 255]

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    rect_x += change_x
    rect_y += change_y

    # growing rect - health/energy bar?
    rect_width += 1
    if rect_width > 300:
        rect_width = 300  # makes it stop

    # wrapping around
    '''
    if rect_x > SCREEN_WIDTH:
        rect_x = -50
    '''

    # bouncing rectangle
    if rect_x > SCREEN_WIDTH - 50:
        change_x = change_x * -1
        # change_x *= -1
    if rect_x < 0:
        change_x *= -1


    if rect_y > SCREEN_HEIGHT - 50:
        change_y = change_y * -1
    if rect_y < 0:
        change_y *= -1


    # Color shift - same rules as bouncing or wrapping
    screen.fill(bg_color)

    pygame.draw.rect(screen, RED, [rect_x, rect_y, rect_width, 50])


    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second


pygame.quit()  # Close the window and quit.