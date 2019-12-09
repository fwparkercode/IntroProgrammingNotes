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


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()  # grabs rect based on the image)

class Enemy(Block):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()  # grabs rect based on the image)
        self.change_y = 1
        self.change_x = random.randrange(-3, 4)

    def update(self):
        # x move
        self.rect.x += self.change_x

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.change_x *= -1

        if self.rect.left <= 0:
            self.rect.left = 0
            self.change_x *= -1


        # y move
        self.rect.y += self.change_y

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)



player = Block()
player.rect.bottom = SCREEN_HEIGHT  # put player at bottom

# make my groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

enemy_sprites = pygame.sprite.Group()

for i in range(20):
    enemy = Enemy()
    enemy.rect.x = random.randrange(0, SCREEN_WIDTH - enemy.rect.width)
    enemy.rect.y = random.randrange(-200, SCREEN_HEIGHT - 200)
    enemy.image.fill(GREEN)
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)



# game variables
score = 0
lives = 3
frame = 0



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard, controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    frame += 1
    enemy_sprites.update()
    player.rect.x = pygame.mouse.get_pos()[0]

    hit_list = pygame.sprite.spritecollide(player, enemy_sprites, True)

    for enemy in hit_list:
        enemy.image.fill(RED)
        lives -= 1

    if lives < 0:
        done = True

    if frame % 600 == 0:
        for enemy in enemy_sprites:
            enemy.change_y += 1


    # --- Drawing code goes here
    screen.fill(WHITE)

    all_sprites.draw(screen)  # draws the image to the rect location

    pygame.display.flip()  # updates the screen

    clock.tick(60) # frames per second

pygame.quit() # Close the window and quit.
