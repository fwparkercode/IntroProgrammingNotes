"""
 Pygame base template for opening a window

 Intro to Programming
 Aaron Lee 2018
"""

import pygame
import random
pygame.init()


# Define some colors
BLACK = (0, 0, 0)  # (red, green, blue)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (120, 120, 120)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Template")

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Classes
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

player = Block()
player.image.fill(BLUE)

all_sprites_group = pygame.sprite.Group()  # bucket for all sprites
all_sprites_group.add(player)

block_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

for i in range(100):
    block = Block()
    block.image.fill(GREEN)
    block.rect.x = random.randrange(0, screen_width - block.rect.width)
    block.rect.y = random.randrange(0, screen_height - block.rect.height)
    all_sprites_group.add(block)
    block_group.add(block)

for i in range(10):
    block = Block()
    block.image.fill(RED)
    block.rect.x = random.randrange(0, screen_width - block.rect.width)
    block.rect.y = random.randrange(0, screen_height - block.rect.height)
    all_sprites_group.add(block)
    enemy_group.add(block)

score = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    x, y = pygame.mouse.get_pos()
    player.rect.centerx = x
    player.rect.centery = y

    for enemy in enemy_group:
        enemy.rect.y += 5
        if enemy.rect.y > screen_height:
            enemy.rect.bottom = 0
            enemy.rect.x = random.randrange(0, screen_width - enemy.rect.width)

    hit_list = pygame.sprite.spritecollide(player, block_group, True)
    for block in hit_list:
        score += 1
        print(score)

    hit_list = pygame.sprite.spritecollide(player, enemy_group, True)
    for block in hit_list:
        done = True

    screen.fill(WHITE)
    # --- Drawing code should go here
    all_sprites_group.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()