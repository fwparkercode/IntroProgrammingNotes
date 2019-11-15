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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
done = False  # Loop until the user clicks the close button.

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)  # Screen object we draw to

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates
pygame.mouse.set_visible(False)

# Images
bg_image = pygame.image.load("bgCave.bmp")  # creates image object
dragon_image1 = pygame.image.load("dragon.png")
dragon_image2 = pygame.image.load("dragon_left.png")

dragon_image = dragon_image1

# Sounds
bg_music = pygame.mixer.Sound("bgMusic.wav")
bg_music.play(-1)  # plays forever with -1
bg_music.set_volume(0.5)

fireball_sound = pygame.mixer.Sound("fireball.wav")

dragon_x = 0
dragon_y = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            fireball_sound.play()
        if event.type == pygame.MOUSEMOTION:
            if event.rel[0] < 0:
                dragon_image = dragon_image2
            else:
                dragon_image = dragon_image1


    # --- Game logic should go here
    dragon_x, dragon_y = pygame.mouse.get_pos()

    # --- Draw to screen
    #screen.fill(BLACK)
    screen.blit(bg_image, [0, 0])
    screen.blit(dragon_image, [dragon_x, dragon_y])


    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.