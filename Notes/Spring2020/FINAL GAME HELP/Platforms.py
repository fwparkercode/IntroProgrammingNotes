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
        self.gravity = 0.1

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        #self.change_y += y

    def update(self):
        self.change_y += self.gravity
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        hit_list = pygame.sprite.spritecollide(self, self.wall_sprites, False)

        for wall in hit_list:
            if self.change_x > 0:
                # moving right
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        self.rect.y += self.change_y
        hit_list = pygame.sprite.spritecollide(self, self.wall_sprites, False)

        for wall in hit_list:
            if self.change_y > 0:
                # moving down
                self.change_y = 0
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom


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
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# make my groups
all_sprites = pygame.sprite.Group()  # making a bucket for everything
coin_sprites = pygame.sprite.Group()  # bucket for coins
enemy_sprites = pygame.sprite.Group()  # enemy bucket
wall_sprites = pygame.sprite.Group()

# creating instances of sprites
wall = Wall(100, 100, 200, 20)
wall2 = Wall(0, 200, 200, 20)
all_sprites.add(wall)
all_sprites.add(wall2)
wall_sprites.add(wall)
wall_sprites.add(wall2)


player = Player(0, 0)
all_sprites.add(player)
player.wall_sprites = wall_sprites

for i in range(50):
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    block = Block(x, y)
    block.image.fill(GREEN)
    all_sprites.add(block)  # for drawing purposes
    coin_sprites.add(block)  # for collisions

for i in range(50):
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
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
                player.change_y = -5


        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)


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

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas

    all_sprites.draw(screen)

    my_text = my_font.render("Score: " + str(score), True, BLACK)
    screen.blit(my_text, [20, 20])

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
