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
level = 1

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# CLASSES
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # makes it a real sprite
        self.image = pygame.Surface([20, 20])  # create a surface (could also load image file)
        self.image.fill(BLACK)  #  fill with BLACK or other color
        self.rect = self.image.get_rect()  # grabs the rectangle based on the surface/image size

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()  # makes it a real sprite
        self.image = pygame.Surface([20, 20])  # create a surface (could also load image file)
        self.image.fill(RED)  #  fill with BLACK or other color
        self.rect = self.image.get_rect()  # grabs the rectangle based on the surface/image size
        self.rect.x = x
        self.rect.y = y

# make my groups
all_sprites = pygame.sprite.Group()  # making a bucket for everything
coin_sprites = pygame.sprite.Group()  # bucket for coins

# creating instances of sprites
player = Player()
all_sprites.add(player)

for i in range(10):
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    block = Block(x, y)
    all_sprites.add(block)  # for drawing purposes
    coin_sprites.add(block)  # for collisions

# text resources
my_font = pygame.font.SysFont("Calibri", 40, True, False)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            player.rect.centerx, player.rect.centery = event.pos

    # --- Game logic should go here
    all_sprites.update()  # move everything
    pygame.sprite.spritecollide(player, coin_sprites, True)

    if len(coin_sprites) == 0:
        # level up!!
        level += 1
        for i in range(10 * level):
            x = random.randrange(WIDTH)
            y = random.randrange(HEIGHT)
            block = Block(x, y)
            all_sprites.add(block)  # for drawing purposes
            coin_sprites.add(block)  # for collisions

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas
    my_text = my_font.render("Level: " + str(level), True, BLACK)
    screen.blit(my_text, [20, 20])

    all_sprites.draw(screen)

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
