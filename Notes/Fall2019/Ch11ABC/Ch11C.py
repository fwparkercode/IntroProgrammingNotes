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


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
done = False  # condition for my game loop


# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mr. Lee's Game")

clock = pygame.time.Clock()  # creates a clock object that manages updates

pygame.mouse.set_visible(False)

# Images
bg_image = pygame.image.load("bgCave.bmp")  # function returns image object
dragon_right = pygame.image.load("dragon2.png")
dragon_left = pygame.image.load("dragon3.png")
dragon_image = dragon_right



# Sounds
bg_music = pygame.mixer.Sound("bgMusic.wav")
bg_music.play(-1)  # play(number of times to play) (-1 is loop forever)
bg_music.set_volume(0.5)  # float between 0 and 1

fireball_sound = pygame.mixer.Sound("fireball.wav")
fireball_sound.play()

# Control variables
dragon_x = 0
dragon_y = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard, controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            fireball_sound.play()
        if event.type == pygame.MOUSEMOTION:
            if event.rel[0] >= 0:
                dragon_image = dragon_right
            else:
                dragon_image = dragon_left

    # --- Game logic should go here
    dragon_x, dragon_y = pygame.mouse.get_pos()

    # --- Drawing code goes here
    #screen.fill(WHITE)
    screen.blit(bg_image, [0, 0])
    screen.blit(dragon_image, [dragon_x, dragon_y])


    pygame.display.flip()  # updates the screen

    clock.tick(60) # frames per second

pygame.quit() # Close the window and quit.
