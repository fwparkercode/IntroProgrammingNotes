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

pygame.mouse.set_visible(False)

rect_x = 0
rect_y = 0
rect_color = RED

ellipse_x = 0
ellipse_y = 0
change_x = 0
change_y = 0

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


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard, controller)
    # You can only have one event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos, event.button)
            rect_color = BLUE
        elif event.type == pygame.MOUSEBUTTONUP:
            rect_color = RED
        elif event.type == pygame.MOUSEMOTION:
            #rect_color = GREEN
            print(event.pos, event.rel, event.buttons)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_x = 3
            elif event.key == pygame.K_LEFT:
                change_x = -3
            elif event.key == pygame.K_DOWN:
                change_y = 3
            elif event.key == pygame.K_UP:
                change_y = -3
        elif event.type == pygame.KEYUP:  # lift finger off key
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                change_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                change_y = 0


    # --- Game logic should go here
    ellipse_x += change_x
    ellipse_y += change_y

    # keyboard boundary checks
    if ellipse_x > SCREEN_WIDTH - 30:
        ellipse_x = SCREEN_WIDTH - 30
    if ellipse_y > SCREEN_HEIGHT - 30:
        ellipse_y = SCREEN_HEIGHT - 30
    if ellipse_y < 0:
        ellipse_y = 0
    if ellipse_x < 0:
        ellipse_x = 0

    rect_x, rect_y = pygame.mouse.get_pos()


    if rect_x > SCREEN_WIDTH - 30:
        rect_x = SCREEN_WIDTH - 30
    if rect_y > SCREEN_HEIGHT - 30:
        rect_y = SCREEN_HEIGHT - 30

    # --- Drawing code goes here
    screen.fill(WHITE)


    pygame.draw.rect(screen, rect_color, [rect_x, rect_y, 30, 30])
    pygame.draw.ellipse(screen, MAGENTA, [ellipse_x, ellipse_y, 30, 30])
    draw_stickman(0, 0)


    pygame.display.flip()  # updates the screen

    clock.tick(60) # frames per second

pygame.quit() # Close the window and quit.
