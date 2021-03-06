"""
Space Shooter
Aaron Lee - 2019
"""
import random

import pygame

# Global Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 150, 150)
MAROON = (100, 0, 0)
ORANGE = (255, 150, 0)
PURPLE = (100, 50, 150)


pygame.init()  # initializes pygame (need to do this before you use it)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game!")
clock = pygame.time.Clock()  # Used to manage how fast the screen updates




# CLASSES
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT  # lock the player to bottom of screen

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.change_x = random.randrange(-3, 4)
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(300)
        self.change_y = random.randrange(1, 4)

    def update(self):
        self.rect.x += self.change_x

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.change_x *= -1

        if self.rect.left <= 0:
            self.rect.left = 0
            self.change_x *= -1

        self.rect.y += self.change_y

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 8])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.change_y = -10

    def update(self):
        self.rect.y += self.change_y
        if self.rect.bottom < 0:
            self.kill()

# GROUPS
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()

# INSTANCES
player = Player()
all_sprites.add(player)

for i in range(20):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)

pygame.mouse.set_visible(False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_bullet = Bullet()
            #new_bullet.rect.centery = player.rect.centery
            #new_bullet.rect.centerx = player.rect.centerx
            new_bullet.rect.midtop = player.rect.midtop
            all_sprites.add(new_bullet)
            bullet_sprites.add(new_bullet)

    # --- Game logic should go here
    all_sprites.update()

    for bullet in bullet_sprites:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_sprites, True)
        for hit in hit_list:
            bullet.kill()

    # --- Drawing code goes here
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second


pygame.quit()  # Close the window and quit.