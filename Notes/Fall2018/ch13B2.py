"""
 Pygame base template for opening a window

 Intro to Programming
 Aaron Lee 2018
"""
import random

import pygame
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
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface([30, 30])
        # self.image.fill(BLUE)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.speedx = random.choice([-3, -2, -1, 1, 2, 3])

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            self.speedx *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx *= -1

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 8])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.speedy = -8

    def update(self):
        self.rect.y += self.speedy


# create groups
all_sprites_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# create player
player = Player()
player.rect.bottom = screen_height
all_sprites_group.add(player)

# create enemies
for i in range(50):
    enemy = Enemy()
    enemy.rect.x = random.randrange(0, screen_width - enemy.rect.width)
    enemy.rect.y = random.randrange(0, screen_height/2)
    all_sprites_group.add(enemy)
    enemy_group.add(enemy)

pygame.mouse.set_visible(False)


def cut_screen():
    frame = 300
    done = False  # local variable done
    my_font = pygame.font.SysFont("Calibri", 40, True, False)
    while not done:
        frame -= 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        print(frame // 60)  # floor
        if frame // 60 < 0:
            done = True
        screen.fill(BLACK)
        my_text = my_font.render("Ready in " + str(frame // 60), True, WHITE)
        screen.blit(my_text, [screen_width/2, screen_height/2])
        pygame.display.flip()
        clock.tick(60)

cut_screen()
level = 1

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            player.rect.centerx = x
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.centerx = player.rect.centerx
            bullet.rect.centery = player.rect.centery
            all_sprites_group.add(bullet)
            bullet_group.add(bullet)

    # --- Game logic should go here
    all_sprites_group.update()

    # check for collision
    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, True)
        for hit in hit_list:
            bullet.kill()

    count = 0
    for enemy in enemy_group:
        count += 1
    if count == 0:
        level += 1
        bullet_group.empty()
        all_sprites_group.empty()
        all_sprites_group.add(player)
        cut_screen()
        for i in range(50 * level):

            enemy = Enemy()
            enemy.rect.x = random.randrange(0, screen_width - enemy.rect.width)
            enemy.rect.y = random.randrange(0, screen_height / 2)
            enemy.speedx *= 2
            all_sprites_group.add(enemy)
            enemy_group.add(enemy)

    screen.fill(WHITE)
    # --- Drawing code should go here
    all_sprites_group.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()