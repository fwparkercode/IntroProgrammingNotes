"""
This program shows how to create a pixel per pixel mask for sprites.
Normally, pygame uses the rect for collisions, but if you have a mask,
it uses that instead.
Using this method, any part of the image that was "clear" alpha image would not be part of the mask.  Any part of the image that was not alpha, is part of the mask and would trigger a collision.

How to do it:
After assigning the image, use the image to make a mask.
Generically, it looks like this:
        my_mask = pygame.mask.from_surface(my_image)






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


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("kick.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

class Zombie(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("zombie.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 200
        self.rect.y = 200

player = Player()
zombie = Zombie()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(zombie)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard, controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    player.rect.center = pygame.mouse.get_pos()

    # --- Drawing code goes here

    if pygame.sprite.collide_mask(player, zombie):
        screen.fill(RED)
    else:
        screen.fill(WHITE)

    all_sprites.draw(screen)

    pygame.display.flip()  # updates the screen

    clock.tick(60) # frames per second

pygame.quit() # Close the window and quit.
