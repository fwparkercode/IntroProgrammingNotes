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

# CLASSES

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface([60, 60])
        # self.image.fill(BLACK)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(0, screen_height / 2)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 8])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.speedy = -8

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()



all_sprites_group = pygame.sprite.Group()
player = Player()
player.rect.bottom = screen_height
all_sprites_group.add(player)

enemy_group = pygame.sprite.Group()
for i in range(10):
    enemy = Enemy()
    all_sprites_group.add(enemy)
    enemy_group.add(enemy)

bullet_group = pygame.sprite.Group()

pygame.mouse.set_visible(False)


def intro_screen():
    done = False
    frame = 0
    my_font = pygame.font.SysFont("Calibri", 40, True, False)
    while not done:
        # --- event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        frame += 1
        if frame > 600:
            done = True
        screen.fill(BLACK)
        my_text = my_font.render("Click to Continue", True, WHITE)
        screen.blit(my_text, [screen_width/2, screen_height/2])

        pygame.display.flip()
        # --- Limit to 60 frames per second
        clock.tick(60)

intro_screen()

frame = 3600
level = 1

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.centerx = event.pos[0]
            bullet.rect.centery = player.rect.centery
            bullet_group.add(bullet)
            all_sprites_group.add(bullet)

    frame -= 1
    print(frame // 60)
    # --- Game logic should go here
    all_sprites_group.update()
    pos = pygame.mouse.get_pos()
    player.rect.centerx = pos[0]

    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, True)
        for hit in hit_list:
            bullet.kill()

    count = 0 # number of enemies
    for enemy in enemy_group:
        count += 1
    if count == 0:
        intro_screen()
        level += 1
        all_sprites_group.empty()
        bullet_group.empty()
        all_sprites_group.add(player)
        for i in range(10 * level):
            enemy = Enemy()
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