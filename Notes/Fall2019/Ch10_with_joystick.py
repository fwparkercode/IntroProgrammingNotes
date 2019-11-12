"""
Pygame Template
Aaron Lee - 2019
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



def draw_stickman(x, y):
    x -= 95
    y -= 83
    # Head
    pygame.draw.ellipse(screen, BLACK, [96 + x, 83 + y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [100 + x, 100 + y], [105 + x, 110 + y], 2)
    pygame.draw.line(screen, BLACK, [100 + x, 100 + y], [95 + x, 110 + y], 2)

    # Body
    pygame.draw.line(screen, RED, [100 + x, 100 + y], [100 + x, 90 + y], 2)

    # Arms
    pygame.draw.line(screen, RED, [100 + x, 90 + y], [104 + x, 100 + y], 2)
    pygame.draw.line(screen, RED, [100 + x, 90 + y], [96 + x, 100 + y], 2)


# set up joystick
joystick_count = pygame.joystick.get_count()
if joystick_count > 0:
    my_controller = pygame.joystick.Joystick(0)
    my_controller.init()
else:
    print("No joystick")
    done = True

# player pos
player_x = 100
player_y = 100
x_speed = 0
y_speed = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard, controller)
    # You can only have one event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # --- Game logic should go here
    x_speed = my_controller.get_axis(0) * 10
    y_speed = my_controller.get_axis(1) * 10
    print(x_speed, y_speed)

    player_x += x_speed
    player_y += y_speed

    # boundary check
    if player_x > SCREEN_WIDTH - 10:
        player_x = SCREEN_WIDTH - 10
    if player_x < 0:
        player_x = 0
    if player_y > SCREEN_HEIGHT - 29:
        player_y = SCREEN_HEIGHT - 29
    if player_y < 0:
        player_y = 0

    # --- Drawing code goes here
    screen.fill(WHITE)

    draw_stickman(player_x, player_y)

    pygame.display.flip()  # updates the screen

    clock.tick(60) # frames per second

pygame.quit() # Close the window and quit.
