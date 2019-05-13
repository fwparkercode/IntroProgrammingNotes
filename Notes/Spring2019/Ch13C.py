'''
Pygame Base Template C Period
Spring 2019
by Aaron Lee

Make a game!
'''
import random

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()  # starts pygame (Vroom!)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mr. Lee's Game")

done = False  # condition for the game loop

clock = pygame.time.Clock()

class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(color)
        self.rect = self.image.get_rect()  # grabs a rect based on image
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(0, screen_height - self.rect.height)

player = Block(BLACK)
player.rect.x = 0
player.rect.y = 0

# Make my sprite groups
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(player)
coin_group = pygame.sprite.Group()

# make my blocks
for i in range(50):
    new_block = Block(RED)
    all_sprites_group.add(new_block)
    coin_group.add(new_block)

score = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    mouse_pos = pygame.mouse.get_pos()
    player.rect.center = mouse_pos

    hit_list = pygame.sprite.spritecollide(player, coin_group, True)

    for hit in hit_list:
        score +=1
        print(score)

    # --- Drawing code should go here
    screen.fill(WHITE)

    all_sprites_group.draw(screen)

    pygame.display.flip()  #update the screen
    clock.tick(60)  #60 frames per second

pygame.quit()  #Close the window and quit.
