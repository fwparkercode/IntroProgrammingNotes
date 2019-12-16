"""
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
YELLOW = (255, 255, 0)
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
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT

    def update(self):
        pos = pygame.mouse.get_pos()  # (x, y) tuple
        self.rect.x = pos[0]

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(300)
        self.change_x = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.change_x

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.change_x *= -1
        if self.rect.left <= 0:
            self.rect.left = 0
            self.change_x *= -1


# GROUPS
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()

# INSTANCES
player = Player()
all_sprites.add(player)

for i in range(20):
    enemy = Enemy()
    enemy.image = pygame.image.load("spaceship.png")
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_bullet = Bullet()
            new_bullet.rect.centerx = player.rect.centerx
            new_bullet.rect.centery = player.rect.centery
            all_sprites.add(new_bullet)
            bullet_sprites.add(new_bullet)


    # --- Game logic should go here
    all_sprites.update()

    for bullet in bullet_sprites:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_sprites, True)
        for enemy in hit_list:
            bullet.kill()


    # --- Draw to screen
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.