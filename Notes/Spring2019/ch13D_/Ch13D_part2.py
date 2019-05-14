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
        #self.image = pygame.Surface([30, 30])
        self.image = pygame.image.load("ship.png")
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect() # grabs the rect based on the image
        self.rect.x = random.randrange(screen_width // 2, screen_width - self.rect.width)
        self.rect.y = random.randrange(screen_height - self.rect.height)
        self.health = 3


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([8, 3])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.change_y = -3
        self.accel = 0.1

    def update(self):
        self.rect.x += 8
        self.change_y += self.accel
        self.rect.y += self.change_y

        if self.rect.x > screen_width:
            self.kill()



# Make groups to contain our sprites
all_sprites_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# Make all my sprites
player = Block()
player.image.fill(RED)
player.rect.left = 0
player.rect.centery = screen_height // 2
all_sprites_group.add(player)  # placed player in the group

for i in range(50):
    new_coin = Block()
    all_sprites_group.add(new_coin)
    enemy_group.add(new_coin)

pygame.mouse.set_visible(False)
score = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop  (user inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet()
                new_bullet.rect.center = player.rect.center
                all_sprites_group.add(new_bullet)  # so it will draw
                bullet_group.add(new_bullet)


    # --- Game logic should go here

    player.rect.centery = pygame.mouse.get_pos()[1]
    bullet_group.update()


    hit_list = pygame.sprite.spritecollide(player, enemy_group, True)
    for hit in hit_list:
        score += 1
        print(score)

    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, False)
        for hit in hit_list:
            bullet.kill()  # eliminate bullet from game
            hit.health -=1
            if hit.health <= 0:
                hit.kill()


    # --- Drawing code should go here
    screen.fill(WHITE)

    all_sprites_group.draw(screen)

    pygame.display.flip() # Update the screen with what we've drawn.

    clock.tick(60)  # frames per second

# Close the window and quit.
pygame.quit()

