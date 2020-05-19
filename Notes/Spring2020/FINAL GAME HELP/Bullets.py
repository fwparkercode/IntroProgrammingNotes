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
score = 0

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# CLASSES
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        # self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        self.rect.y += self.change_y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()  # makes it a real sprite
        self.image = pygame.Surface([20, 20])  # create a surface (could also load image file)
        self.image.fill(RED)  #  fill with BLACK or other color
        self.rect = self.image.get_rect()  # grabs the rectangle based on the surface/image size
        self.rect.x = x
        self.rect.y = y
        self.change_y = random.randrange(1, 4)
        self.change_x = random.randrange(-4, 5)


        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def update(self):
        self.rect.y += self.change_y
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

        self.rect.x += self.change_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.change_x *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.change_x *= -1

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 10])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 8
        if self.rect.bottom < 0:
            self.kill()


# make my groups
all_sprites = pygame.sprite.Group()  # making a bucket for everything
coin_sprites = pygame.sprite.Group()  # bucket for coins
enemy_sprites = pygame.sprite.Group()  # enemy bucket
bullet_sprites = pygame.sprite.Group()  # player bullets

# creating instances of sprites
player = Player(0, 0)
player.rect.bottom = HEIGHT
player.rect.centerx = WIDTH // 2

all_sprites.add(player)

for i in range(50):
    x = random.randrange(WIDTH)
    y = random.randrange(-HEIGHT, 0)
    block = Block(x, y)
    block.image.fill(GREEN)
    all_sprites.add(block)  # for drawing purposes
    coin_sprites.add(block)  # for collisions

for i in range(50):
    x = random.randrange(WIDTH)
    y = random.randrange(-HEIGHT, 0)
    block = Block(x, y)
    block.image.fill(RED)
    all_sprites.add(block)  # for drawing purposes
    enemy_sprites.add(block)  # for collisions

# Text resources
my_font = pygame.font.SysFont('Calibri', 40, True, False)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
            elif event.key == pygame.K_SPACE:
                bullet = Bullet()
                bullet.rect.centerx = player.rect.centerx
                bullet.rect.centery = player.rect.centery
                all_sprites.add(bullet)
                bullet_sprites.add(bullet)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    # --- Game logic should go here
    all_sprites.update()  # move everything

    hit_list = pygame.sprite.spritecollide(player, coin_sprites, True)

    for coin in hit_list:
        score += 1
        print(score)

    hit_list = pygame.sprite.spritecollide(player, enemy_sprites, True)

    for coin in hit_list:
        score -= 1
        print(score)

    for bullet in bullet_sprites:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_sprites, True)
        for hit in hit_list:
            score += 10
            bullet.kill()

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas

    all_sprites.draw(screen)

    my_text = my_font.render("Score: " + str(score), True, BLACK)
    screen.blit(my_text, [20, 20])

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
