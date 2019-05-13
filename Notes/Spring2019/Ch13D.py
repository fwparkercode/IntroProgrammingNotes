"""
Pygame base template
by Aaron Lee 2019
"""
import random

import pygame
pygame.init()  # do not put anything pygame above this line

# Define some colors (red, green, blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen_width = 700
screen_height = 500
size = (screen_width, screen_height)  # width, height
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Window Bar Name")

done = False  # condition for my game loop

clock = pygame.time.Clock() # Used to manage how fast the screen updates


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect() # grabs the rect based on the image
        self.rect.x = random.randrange(screen_width // 2, screen_width - self.rect.width)
        self.rect.y = random.randrange(screen_height - self.rect.height)

# Make groups to contain our sprites
all_sprites_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

# Make all my sprites
player = Block()
player.image.fill(RED)
player.rect.left = 0
player.rect.centery = screen_height // 2
all_sprites_group.add(player)  # placed player in the group

for i in range(50):
    new_coin = Block()
    all_sprites_group.add(new_coin)
    coin_group.add(new_coin)

pygame.mouse.set_visible(False)
score = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop  (user inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    player.rect.center = pygame.mouse.get_pos()
    hit_list = pygame.sprite.spritecollide(player, coin_group, True)
    for hit in hit_list:
        score += 1
        print(score)
        area = player.rect.width ** 2
        pos = player.rect.center
        new_area = hit.rect.width ** 2 + area
        new_width = int(new_area ** 0.5)
        player.image = pygame.Surface([new_width, new_width])
        player.rect = player.image.get_rect()
        player.image.fill(RED)
        player.rect.center = pos

    # --- Drawing code should go here
    screen.fill(WHITE)

    all_sprites_group.draw(screen)

    pygame.display.flip() # Update the screen with what we've drawn.

    clock.tick(60)  # frames per second

# Close the window and quit.
pygame.quit()

