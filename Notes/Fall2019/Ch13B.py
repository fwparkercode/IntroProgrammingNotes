"""
Chapter 13, B Period
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
YELLOW = (200, 200, 0)
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


# CLASSES
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # makes official Sprite
        self.image = pygame.Surface([20, 20]) # Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # makes official Sprite
        self.image = pygame.Surface([10, 10]) # Surface([width, height])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()

# SPRITE GROUPS
all_sprites = pygame.sprite.Group()  # bucket for all my sprites
coins = pygame.sprite.Group()  # bucket for just coins

# INSTANCES
player = Player()  # created instance of the Player class
all_sprites.add(player)  # put player into all_sprites bucket

for i in range(50):
    coin = Coin()
    coin.rect.x = random.randrange(SCREEN_WIDTH - coin.rect.width)
    coin.rect.y = random.randrange(SCREEN_HEIGHT - coin.rect.height)
    all_sprites.add(coin)
    coins.add(coin)



score = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    player.rect.centerx, player.rect.centery = pygame.mouse.get_pos()

    hit_list = pygame.sprite.spritecollide(player, coins, False)

    for coin in hit_list:
        coin.image.fill(GREEN)


    # --- Draw to screen
    screen.fill(WHITE)

    all_sprites.draw(screen)  # draws everything in that group

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.