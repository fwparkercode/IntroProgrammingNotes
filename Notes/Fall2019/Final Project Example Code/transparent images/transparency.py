"""
Image manipualtion examples
Aaron Lee - 2019
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

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)  # Screen object we draw to

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.png")  # THIS IMAGE IS NOT GOOD
        self.rect = self.image.get_rect()



def rot_center(image, old_rect, angle):
    # rotate image around center of rect
    center = image.get_rect().center
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = center)
    new_rect.center = old_rect.center
    return rotated_image, new_rect


all_sprites = pygame.sprite.Group()

for alpha in range(0, 255, 10):
    # makes apples with different alphas across the screen
    apple = Apple()
    apple.image = apple.image.convert()  # change to usable pygame format
    apple.image.set_colorkey(BLACK)  # remove background from converted image
    apple.image.set_alpha(alpha)  # set alpha (0 transparent >>> 255 opaque)
    apple.rect.x = alpha * 2  # draw across screen
    all_sprites.add(apple)



# In this example, note that the image rotates AND changes size when it does.
for angle in range(0, 360, 10):
    apple = Apple()
    apple.image = apple.image.convert()  # change to usable pygame format
    apple.image.set_colorkey(BLACK)  # remove background from converted image
    apple.image = pygame.transform.rotate(apple.image, angle)
    apple.rect.x = angle * 2  # draw bunch across screen
    apple.rect.y = apple.rect.height * 2  # move it down a row
    all_sprites.add(apple)


# If you want a truly rotating object, you need to move it up and to the left, then rotate it, then move it back.
# for this I use the function rot_image() above
for angle in range(0, 360, 10):
    apple = Apple()
    apple.rect.x = angle * 2  # draw bunch across screen
    apple.rect.y = apple.rect.height * 5  # move it down a row
    apple.image = apple.image.convert()  # change to usable pygame format
    apple.image.set_colorkey(BLACK)  # remove background from converted image
    apple.image, apple.rect = rot_center(apple.image, apple.rect, angle)
    all_sprites.add(apple)


# This code increases the size as we go across
for width in range(10, 100, 10):
    apple = Apple()
    apple.image = apple.image.convert()  # change to usable pygame format
    apple.image.set_colorkey(BLACK)  # remove background from converted image
    apple.image = pygame.transform.scale(apple.image, [width, width])
    apple.rect = apple.image.get_rect()
    apple.rect.x = width * 8  # draw bunch across screen
    apple.rect.y = 400  # move it down a row
    all_sprites.add(apple)



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Draw to screen
    screen.fill(WHITE)

    all_sprites.draw(screen)

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.