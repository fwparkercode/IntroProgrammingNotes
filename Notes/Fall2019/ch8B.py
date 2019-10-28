"""
Pygame base template
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
import math

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

rect_x = 100
change_x = 0
rect_y = 100
change_y = 0
accel_y = 0.1

rect_width = 50
rect_color = [0, 0, 255]

frame = 0

color_list = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
color_index = 0

# Rotating line
line_length = 200
angle = 0
angle_speed = 0.01

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    angle += angle_speed
    dx = math.cos(angle) * line_length
    dy = math.sin(angle) * line_length

    frame += 1

    if frame % 120 == 0:
        color_index += 1

    change_y += accel_y # accelerate in y

    rect_x += change_x  # moves x
    rect_y += change_y  # moves y

    # Change width (like a health bar)
    if rect_width < 300:
        rect_width += 1


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
        rect_y = SCREEN_HEIGHT - 50
        change_y *= -0.3  # dampen with number less than 1
    if rect_y < 0:
        change_y *= -1

    # Color shift
    if rect_color[0] < 255:
        rect_color[0] += 1  # cannot go past 255
    if rect_color[1] < 255:
        rect_color[1] += 1  # cannot go past 255

    # --- Draw to screen
    screen.fill(color_list[color_index % len(color_list)])

    pygame.draw.line(screen, BLACK, [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], [SCREEN_WIDTH // 2 + dx, SCREEN_HEIGHT // 2 + dy], 3)

    for i in range(0, 360, 30):
        my_angle = math.pi / 360 * i * 2
        my_angle += angle
        my_dx = math.cos(my_angle) * line_length
        my_dy = math.sin(my_angle) * line_length
        pygame.draw.circle(screen, BLACK, [int(SCREEN_WIDTH // 2 + my_dx), int(SCREEN_HEIGHT // 2 + my_dy)], 10)

    pygame.draw.rect(screen, rect_color, [rect_x, rect_y, rect_width, 50])

    # doesn't show rect for first two seconds
    if frame > 120:
        pygame.draw.rect(screen, GREEN, [100, 200, 50, 50])

    # blinking
    if frame % 30 > 15:
        pygame.draw.rect(screen, BLUE, [100, 300, 50, 50])
    else:
        pygame.draw.rect(screen, RED, [100, 300, 50, 50])


    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.