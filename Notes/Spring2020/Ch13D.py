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

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


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

        # put at bottom of screen
        self.rect.bottom = HEIGHT

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        # self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH


        self.rect.y += self.change_y
        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.change_x = random.randrange(-3, 4)
        self.change_y = random.randrange(1, 3)

    def update(self):
        self.rect.x += self.change_x
        if self.rect.left < 0:
            self.rect.left = 0
            self.change_x *= -1
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.change_x *= -1

        self.rect.y += self.change_y
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

# create groups
all_sprites = pygame.sprite.Group()  # bucket for everyone (sprites)
block_sprites = pygame.sprite.Group()  # bucket for blocks

# create sprites
player = Player(0, 0)
all_sprites.add(player)

for i in range(30):
    block = Block()
    block.rect.x = random.randrange(WIDTH - block.rect.width)
    block.rect.y = random.randrange(HEIGHT - block.rect.height)
    all_sprites.add(block)  # makes it update and draw
    block_sprites.add(block)

score = 0

my_font = pygame.font.SysFont('Calibri', 30, True, False)


# -------- Main Program Loop -----------
while not done:
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
    all_sprites.update()  # runs the update method for every sprite in the group

    hit_list = pygame.sprite.spritecollide(player, block_sprites, True)

    for block in hit_list:
        score += 1
        #block.image.fill(GREEN)
        print(score)

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas

    all_sprites.draw(screen)  # draws the image of each sprite at their rect location

    my_text = my_font.render("Score: " + str(score), True, BLACK)
    screen.blit(my_text, [20, 20])

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
