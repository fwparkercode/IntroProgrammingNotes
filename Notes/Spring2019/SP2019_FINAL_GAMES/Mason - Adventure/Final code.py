"""
Mason Gardner
Final code game
Maze game in the vein of adventure for the atari 2600
Computer programing 1
"""

import pygame

# -- Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255, 130, 115)
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Classses

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # Constructor function
    def __init__(self, x, y):
        super().__init__()

        # Set height, width
        self.image = pygame.image.load("knight.png")

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom



class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Key(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Skeleton Key - 2.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.dead = False

class Flag(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x,  y):
        super().__init__()
        self.image = pygame.image.load("download.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.collide = False

class Princess(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x,  y):
        super().__init__()
        self.image = pygame.image.load("character princess girl.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.collide = False


# Initialize Pygame
pygame.init()

# Sound
bgm = pygame.mixer.Sound("Happy Sunset.wav")
bgm.play(-1)
keysound = pygame.mixer.Sound("sd_0.wav")
winsound = pygame.mixer.Sound("round_end.wav")
# Create the screen dimensions
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the caption on the top
pygame.display.set_caption('Mason Final')

# Groups
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
level2sprites = pygame.sprite.Group()
wall_list2 = pygame.sprite.Group()
# Draw level one stuff here

wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(SCREEN_WIDTH - 10, 0, 10, SCREEN_HEIGHT)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(110, 200, 10, 300)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(110, 500, 560, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(410, 200, 10, 250)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(170, 200, 10, 250)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(170, 450, 250, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 80, 300, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(300, 80, 10, 300)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(235, 200, 10, 180)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(180, 200, 60, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(235, 150, 10, 230)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 150, 190, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 150, 190, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(480, 280, 10, 180)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(490, 450, 90, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(580, 450, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(490, 280, 90, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(420, 200, 160, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(580, 280, 10, 100)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(580, 0, 10, 210)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(410, 0, 10, 140)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(495, 60, 10, 140)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(660, 70, 10, 440)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(120, 450, 20, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(130, 450, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(SCREEN_WIDTH-50, SCREEN_HEIGHT-50, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(SCREEN_WIDTH-50, SCREEN_HEIGHT-50, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

dispwall = Wall(600, 500, 10, 95)
wall_list.add(dispwall)
all_sprite_list.add(dispwall)

key1 = Key(530, 160)
all_sprite_list.add(key1)

flag1 = Flag(50, 210)
all_sprite_list.add(flag1)

level = 1
# level 2 stuff

wall = Wall(0, 0, 10, SCREEN_HEIGHT)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(SCREEN_WIDTH - 10, 0, 10, SCREEN_HEIGHT)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(0, 0, SCREEN_WIDTH, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(0, 200, 100, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(0, 240, 110, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(100, 130, 10, 80)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(140, 50, 10, 160)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(0, 130, 100, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(140, 50, 100, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(100, 240, 10, 100)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(140, 240, 10, 140)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(60, 380, 220, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(60, 300, 10, 80)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(0, 440, 150, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(0, 440, 150, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(230, 50, 10, 100)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(140, 150, 100, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(140, 200, 100, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(230, 200, 10, 150)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(190, 200, 10, 150)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(270, 200, 10, 190)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(270, 200, 100, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(270, 50, 10, 110)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(270, 150, 100, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(190, 340, 40, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(200, 380, 10, 240)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(150, 440, 10, 100)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(270, 50, 200, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(470, 50, 10, 200)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(510, 50, 10, 200)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(510, 50, 100, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(610, 50, 10, 150)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(670, 50, 150, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(670, 50, 10, 200)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(520, 240, 150, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(360, 100, 10, 50)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(310, 100, 50, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(350, 200, 80, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(320, 240, 150, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(320, 240, 10, 200)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(250, 430, 80, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(250, 430, 10, 120)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(250, 550, 300, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(550, 460, 10, 100)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(550, 460, 150, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(700, 460, 10, 50)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(600, 510, 10, 80)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(600, 510, 175, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(470, 290, 10, 100)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(380, 290, 90, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(380, 290, 10, 100)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(380, 390, 100, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(330, 430, 150, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(470, 430, 10, 80)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(300, 500, 180, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(510, 290, 230, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(740, 100, 10, 320)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(700, 420, 50, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(700, 420, 10, 40)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(740, 460, 50, 10)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(510, 290, 10, 200)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(550, 340, 10, 150)
wall_list2.add(wall)
level2sprites.add(wall)

wall = Wall(550, 370, 150, 10)
wall_list2.add(wall)
level2sprites.add(wall)

dispwall2 = Wall(470, 100, 50, 10)
wall_list2.add(dispwall2)
level2sprites.add(dispwall2)

key2 = Key(114, 465)
level2sprites.add(key2)

princess = Princess(SCREEN_WIDTH - 32, SCREEN_HEIGHT - 50)
level2sprites.add(princess)

# Code for the Player

player = Player(50, 50)
player.walls = wall_list
all_sprite_list.add(player)


clock = pygame.time.Clock()

done = False
my_font = pygame.font.SysFont('Calibri', 40, True, False)

# Code for cut screens

def cut_screen():
    done = False
    text = my_font.render("Welcome to Adventure 2! Press any key to start!", True, BLACK)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(WHITE)

        screen.blit(text, [SCREEN_WIDTH // 2 - text.get_rect().width // 2, SCREEN_HEIGHT // 2 - text.get_rect().height // 2])
        pygame.display.flip()
        clock.tick(60)

def cut_screen2():
    done = False
    text = my_font.render("You passed the level! Press any key to continue!", True, BLACK)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(GREEN)

        screen.blit(text, [SCREEN_WIDTH // 2 - text.get_rect().width // 2, SCREEN_HEIGHT // 2 - text.get_rect().height // 2])
        pygame.display.flip()
        clock.tick(60)

def cut_screen3():
    done = False
    text = my_font.render("You saved the Princess! You win!", True, BLACK)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.QUIT()

        screen.fill(YELLOW)

        screen.blit(text, [SCREEN_WIDTH // 2 - text.get_rect().width // 2, SCREEN_HEIGHT // 2 - text.get_rect().height // 2])
        pygame.display.flip()
        clock.tick(60)

cut_screen()

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Controls
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-10, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(10, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -10)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 10)
            elif event.key == pygame.K_c:
                cut_screen2()
                all_sprite_list.empty()
                wall_list.empty()
                all_sprite_list.add(player)

                for sprite in level2sprites:
                    all_sprite_list.add(sprite)
                    all_sprite_list.draw(screen)

                for wall in wall_list2:
                    wall_list.add(wall)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(10, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-10, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 10)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -10)


    # updates
    all_sprite_list.update()

    # Collisions

    if pygame.sprite.collide_rect(player, key1):
        key1.rect.x = -1000
        key1.kill()
        dispwall.kill()
        keysound.play(1)

    if pygame.sprite.collide_rect(player, key2):
        key2.rect.x = -1000
        key2.kill()
        dispwall2.kill()
        keysound.play(1)

    screen.fill(BLACK)

    if pygame.sprite.collide_rect(player, flag1):
        flag1.rect.x = -1000
        winsound.play()
        player.change_x = 0
        player.change_y = 0
        cut_screen2()
        all_sprite_list.empty()
        wall_list.empty()
        all_sprite_list.add(player)
        level = 2
        for sprite in level2sprites:
            all_sprite_list.add(sprite)
            all_sprite_list.draw(screen)

        for wall in wall_list2:
            wall_list.add(wall)

    if pygame.sprite.collide_rect(player, princess):
        princess.rect.x = -1000
        princess.kill()
        winsound.play()
        player.kill()
        all_sprite_list.empty()
        cut_screen3()
        done = True

    all_sprite_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()