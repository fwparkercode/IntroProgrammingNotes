"""
Pygame base template
Aaron Lee - 2019
"""
import random

import pygame

if True:
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
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()


# GROUPS
all_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

# INSTANCES
player = Player()
all_sprites.add(player)

for i in range(50):
    coin = Coin()
    coin.rect.x = random.randrange(SCREEN_WIDTH - coin.rect.width)
    coin.rect.y = random.randrange(SCREEN_HEIGHT - coin.rect.height)
    all_sprites.add(coin)
    coin_sprites.add(coin)


score = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    player.rect.x, player.rect.y = pygame.mouse.get_pos()

    hit_list = pygame.sprite.spritecollide(player, coin_sprites, False)

    for coin in hit_list:
        score += 1
        print(score)
        coin.image.fill(GREEN)

    # --- Drawing code goes here
    screen.fill(WHITE)

    all_sprites.draw(screen)

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second


pygame.quit()  # Close the window and quit.