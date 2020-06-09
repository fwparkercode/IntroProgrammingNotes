"""
Pygame base template
Ryan Toulouse - 2019
"""

# need to make sure enemies don't spawn on each other
# need to make it so wizard are not killed in one shot, they have lives of some kind
# need to make "levels" of some kind
# need to make restrictions on how many ninja star can be used at once, rn there are unlimited and that is too much
# need to make the fire/ice-ball go in more than one direction

import pygame
import random

count = 0
wizard_count = 0
score = 0
level = 0

pygame.init()  # initializes pygame (need to do this before you use it)

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

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 600
done = False  # Loop until the user clicks the close button.

background_image = pygame.image.load("background image.png")
game_over = pygame.image.load("gameover.png")


# functions

def death_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(RED)
        pygame.display.flip()

#   while not done:
#       screen.blit(background_image, [0, 0])
#       screen.blit(game_over, [0, 0])


# class that has all the chracteristics for player
class Player(pygame.sprite.Sprite):
    health = 5

    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        self.image = pygame.image.load("player.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 5

        # -- Attributes
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # restrictions on player and keeping it within certain area
        if self.rect.x < -1:
            self.rect.x = -1
        if self.rect.x > 200:
            self.rect.x = 200
        if self.rect.y < -5:
            self.rect.y = -5
        if self.rect.y > SCREEN_HEIGHT - 115:
            self.rect.y = SCREEN_HEIGHT - 115


# general enemy class that has attributes of just an enemy
class Enemy(pygame.sprite.Sprite):
    health = 1

    def __init__(self):
        # calls parent  constructor
        super().__init__()
        self.frame = 0

        self.image = pygame.image.load("archer.png")

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800, SCREEN_WIDTH - 110)
        self.rect.y = random.randrange(0, SCREEN_HEIGHT - 115)

    def update(self):
        self.frame += 1
        if self.frame % 400 == random.randrange(200, 375):
            arrow = Arrow()
            arrow.rect.x = self.rect.x
            arrow.rect.y = self.rect.y
            arrow_list.add(arrow)
            all_sprites_list.add(arrow)


class Wizard(pygame.sprite.Sprite):
    health = 3

    def __init__(self):
        super().__init__()
        self.health = 3
        self.frame = 0
        self.health = 3
        self.image = pygame.image.load("icewitch.png")

        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(800, SCREEN_WIDTH - 250)
        self.rect.y = random.randrange(250, 300)

    def update(self):
        self.frame += 1
        if self.frame % 600 == 300:
            ice = Iceball()
            ice.rect.x = self.rect.x
            ice.rect.y = self.rect.y
            ice_list.add(ice)
            all_sprites_list.add(ice)


class Ninja_Star(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("ninjastar.png")
        self.rect = self.image.get_rect()
        self.rect.x = character.rect.x
        self.change_x = 13

    def update(self):
        self.rect.x += self.change_x
        if self.rect.x >= SCREEN_WIDTH:
            star.kill()


class Arrow(pygame.sprite.Sprite):  # make archers shoot

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Ice Bow Set_0.png")
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0
        self.change_x = - 10

    def update(self):
        self.rect.x += self.change_x


# think about you can make it so there are three objects going in diff directions from this class
class Iceball(pygame.sprite.Sprite):  # need help adding this to the wizard class so the wizard shoots these

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("ice.png")  # need to make it an ice ball b/c switched photo
        self.rect = self.image.get_rect()
        self.change_x = - 15

    def update(self):
        self.rect.x += self.change_x


# list that keeps all sprites in a list
enemy_list = pygame.sprite.Group()
wizard_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
star_list = pygame.sprite.Group()
archer_list = pygame.sprite.Group()
arrow_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
ice_list = pygame.sprite.Group()

# creates instances of a class
character = Player(0, 0)
# need help for making enemies not spawn on each other and this code here

while count < 5:
    archer = Enemy()
    hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
    if len(hit_list) > 0:
        pass
    else:
        all_sprites_list.add(archer)
        enemy_list.add(archer)
        archer_list.add(archer)
        count += 1

while wizard_count < 2:
    wizard = Wizard()
    hit_list = pygame.sprite.spritecollide(wizard, enemy_list, False)
    if len(hit_list) > 0:
        pass
    else:
        all_sprites_list.add(wizard)
        enemy_list.add(wizard)
        wizard_list.add(wizard)
        wizard_count += 1

# adds characters/player to sprite list/ bucket
player_list.add(character)
all_sprites_list.add(player_list)
# code that adds both wizard and archer list to all sprites list so they will all be drawn
all_sprites_list.add(enemy_list)

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game!")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character.changespeed(-5, 0)
            elif event.key == pygame.K_RIGHT:
                character.changespeed(5, 0)
            elif event.key == pygame.K_UP:
                character.changespeed(0, -5)
            elif event.key == pygame.K_DOWN:
                character.changespeed(0, 5)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character.changespeed(5, 0)
            elif event.key == pygame.K_RIGHT:
                character.changespeed(-5, 0)
            elif event.key == pygame.K_UP:
                character.changespeed(0, 5)
            elif event.key == pygame.K_DOWN:
                character.changespeed(0, -5)

            if event.key == pygame.K_SPACE and len(star_list) < 2:
                star = Ninja_Star()
                star.rect.centery = character.rect.centery
                # star.rect.midtop = character.rect.midtop
                all_sprites_list.add(star)
                star_list.add(star)

    # --- Game logic should go here
    all_sprites_list.update()

    # code that removes enemy archers when a ninja star hits them
    for star in star_list:
        hit_list = pygame.sprite.spritecollide(star, archer_list, True)
        for hit in hit_list:
            star.kill()

    for star in star_list:
        hit_list = pygame.sprite.spritecollide(star, arrow_list, True)
        for hit in hit_list:
            star.kill()

    for arrow in arrow_list:
        hit_list = pygame.sprite.spritecollide(arrow, player_list, False)
        for hit in hit_list:
            arrow.kill()
            hit.health -= 1

    for ice in ice_list:
        hit_list = pygame.sprite.spritecollide(ice, player_list, False)
        for hit in hit_list:
            ice.kill()
            hit.health -= 2

    # code that kills wizard when ninja star is hit, might want to make it so that 3 ninja stars kill wizard to make harder
    for star in star_list:
        hit_list = pygame.sprite.spritecollide(star, wizard_list, False)
        for hit in hit_list:
            star.kill()
            hit.health -= 1
    for wizard in wizard_list:
        if wizard.health == 0:
            wizard.kill()

    if character.health == 0:
        character.kill()
        death_screen()
        # all_sprites_list.empty()
        # enemy_list.empty()
        # star_list.empty()
        # ice_list.empty()
        # arrow_list.empty()
        # screen.blit(game_over, [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2])

    # --- Drawing code goes here
    screen.blit(background_image, [0, 0])

    all_sprites_list.draw(screen)

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60     for star in star_list:

pygame.quit()  # Close the window and quit.
