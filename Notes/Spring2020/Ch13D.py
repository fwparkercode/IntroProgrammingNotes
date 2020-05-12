"""
Pygame base template
by Aaron Lee 2020
"""
import random

import pygame

# Define global varibles
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
WIDTH = 800
HEIGHT = 600
done = False

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])  # create a 20x20 rectangle
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

# create groups
all_sprites = pygame.sprite.Group()  # bucket for everyone (sprites)
block_sprites = pygame.sprite.Group()  # bucket for blocks

# create sprites
player = Player()
all_sprites.add(player)

for i in range(50):
    block = Block()
    block.rect.x = random.randrange(WIDTH)
    block.rect.y = random.randrange(HEIGHT)
    all_sprites.add(block)  # makes it update and draw
    block_sprites.add(block)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            player.rect.right, player.rect.bottom = event.pos

    # --- Game logic should go here
    all_sprites.update()

    pygame.sprite.spritecollide(player, block_sprites, True)

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas

    all_sprites.draw(screen)  # draws the image of each sprite at their rect location

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
