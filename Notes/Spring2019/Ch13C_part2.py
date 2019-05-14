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
        self.rect.y = random.randrange(0, screen_height // 2 - self.rect.height)
        self.change_x = random.randrange(-1, 2)
        self.change_y = random.randrange(1, 3)


    def update(self):
        self.rect.x += self.change_x
        if self.rect.right > screen_width or self.rect.left < 0:
            self.change_x *= -1

        self.rect.y += self.change_y
        if self.rect.top > screen_height:
            self.rect.bottom = 0


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 8])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 8
        if self.rect.bottom < 0:
            self.kill()  # removes from every Group


player = Block(BLACK)
player.rect.x = 0
player.rect.bottom = screen_height

# Make my sprite groups
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(player)
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# make my blocks
for i in range(10):
    new_block = Block(RED)
    all_sprites_group.add(new_block)
    enemy_group.add(new_block)

score = 0
level = 1

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_bullet = Bullet()
            new_bullet.rect.center = player.rect.center
            all_sprites_group.add(new_bullet)
            bullet_group.add(new_bullet)

    # --- Game logic should go here
    mouse_pos = pygame.mouse.get_pos()
    player.rect.centerx = mouse_pos[0]
    bullet_group.update()
    enemy_group.update()

    hit_list = pygame.sprite.spritecollide(player, enemy_group, True)

    for hit in hit_list:
        done = True

    count = 0
    for enemy in enemy_group:
        count += 1

    if count <= 0:
        # go to next level
        level += 1
        for i in range(5 * level):
            new_block = Block(RED)
            new_block.change_y *= level
            new_block.change_x = random.randrange(-level, level + 1)
            all_sprites_group.add(new_block)
            enemy_group.add(new_block)

# check for collision between bullets and enemy
    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, True)
        for hit in hit_list:
            bullet.kill()
            score += 1
            print(score)

    # --- Drawing code should go here
    screen.fill(WHITE)

    all_sprites_group.draw(screen)

    pygame.display.flip()  #update the screen
    clock.tick(60)  #60 frames per second

pygame.quit()  #Close the window and quit.
