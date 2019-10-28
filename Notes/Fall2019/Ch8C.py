"""
Pygame Template
Aaron Lee - 2019

X linear motion with wrapping (i.e. cars going down road, clouds going by)
X linear motion with bouncing (i.e. tennis match, eyes looking left right)
X color shift (i.e. sky color shift)
X blinking (i.e. twinkling stars, flickering candle)
X color change (flashing lights on fire truck, lights on Christmas tree)
 acceleration (i.e. gravity fall, bouncing, changing speeds)
 rotation (requires trig - ferris wheel, clock etc.)
X animation with lists (i.e. snowfall, leaves falling)
"""

import pygame
import math
import random

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

rect_x = 0
change_x = 5
rect_y = 0
change_y = 0
accel_y = 0.1


bg_color = [0, 0, 0]
color_list = [RED, ORANGE, YELLOW, GREEN, BLUE]
color_index = 0

angle = 0
angle_speed = -0.05
length = 200

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard, controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # --- Game logic should go here
    # print(pygame.time.get_ticks())  # time in millis

    angle += angle_speed
    dx = math.cos(angle) * length
    dy = math.sin(angle) * length

    # color shift
    if bg_color[2] <255:
        bg_color[2] += 1  # must be an integer from 0 to 255
    if bg_color[1] < 255:
        bg_color[1] += 1  # must be an integer from 0 to 255
    if bg_color[0] <255:
        bg_color[0] += 1  # must be an integer from 0 to 255

    # move our rectangle
    change_y += accel_y
    rect_x += change_x
    rect_y += change_y

    if rect_x > SCREEN_WIDTH - 50 or rect_x < 0:
        change_x = change_x * -1
        # cycle through colors
        color_index += 1

    if rect_y > SCREEN_HEIGHT - 50:
        rect_y = SCREEN_HEIGHT - 50
        change_y *= -0.7  # dampen by using number less than 1
        change_x *= 0.7
        color_index += 1
    if rect_y < 0:
        change_y *= -1
        color_index += 1

    # Wrap
    '''
    if rect_x > SCREEN_WIDTH:
        rect_x = -50
    '''

    # --- Drawing code goes here
    screen.fill(bg_color)


    pygame.draw.rect(screen, color_list[color_index % len(color_list)], [rect_x, rect_y, 50, 50])

    # appears on screen after 5seconds
    if pygame.time.get_ticks() > 5000:
        pygame.draw.rect(screen, BLUE, [100, 200, 50, 50])

    # blinking
    if pygame.time.get_ticks() % 500 < 250:
        pygame.draw.rect(screen, RED, [100, 300, 50, 50])
    else:
        pygame.draw.rect(screen, BLUE, [100, 300, 50, 50])

    pygame.draw.line(screen, BLACK, [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], [SCREEN_WIDTH // 2 + dx, SCREEN_HEIGHT // 2 + dy], 3)
    pygame.draw.circle(screen, BLACK, [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], 200, 1)

    pygame.display.flip()  # updates the screen

    clock.tick(60) # frames per second

pygame.quit() # Close the window and quit.
