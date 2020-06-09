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
count_1 = 0

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
# sounds and main images
background_image = pygame.image.load("background image.png")
game_over = pygame.image.load("gameover.png")
bow_sound = pygame.mixer.Sound("shoot (1).ogg")
throw_sound = pygame.mixer.Sound("throwing.wav")
spell_sound = pygame.mixer.Sound("spell.wav")
"""
# Functions
def death_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break

        screen.blit(game_over, [0, 0])

        pygame.display.flip()
        clock.tick(60)
"""
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

class Heart(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        x = 5
        self.image = pygame.image.load("heart.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0 + x
        x += 25
        self.rect.y = 600

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
        if self.frame % 150 == random.randrange(50, 149):
            arrow = Arrow()
            arrow.rect.x = self.rect.x
            arrow.rect.y = self.rect.y
            arrow_list.add(arrow)
            all_sprites_list.add(arrow)

class Arrow(pygame.sprite.Sprite):  # make archers shoot

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Ice Bow Set_0.png")
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0
        self.change_x = - 10
        bow_sound.play()

    def update(self):
        self.rect.x += self.change_x



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
""" trying  to get health  to display  and work 
for i in range(character.health):
    heart = Heart()
    all_sprites_list.add(heart)
"""
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
""" trying to make levels work
if score > 4:
    while count_1 < 5:
        archer_1 = Enemy()
        Arrow.change_x = -20
        hit_list = pygame.sprite.spritecollide(archer_1, enemy_list, False)
        if len(hit_list) > 0:
            pass
        else:
            all_sprites_list.add(archer_1)
            enemy_list.add(archer_1)
            archer_list.add(archer_1)
            count_1 += 1
"""
"""

class Jinx(pygame.sprite.Sprite):
    health = 6

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("jinx.png")
        self.rect = self.image.get_rect()
        self.frame = 0

        self.rect.x = random.randrange(700, SCREEN_WIDTH - 115)
        self.rect.y = random.randrange(100, SCREEN_HEIGHT - 115)

        self.change_x = random.randrange(-3, 3)
        self.change_y = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.change_x


class Rockets(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("jinx_projectile.png")

    if level == 9:
        while jinx_count < 1 and level == 9:
            jinx = Jinx()
            hit_list = pygame.sprite.spritecollide(jinx, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(jinx)
                enemy_list.add(jinx)
                jinx_list.add(jinx)
                jinx_count += 1
    if level == 9:
        while jinx_count < 1 and level == 9:
            jinx = Jinx()
            hit_list = pygame.sprite.spritecollide(jinx, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(jinx)
                enemy_list.add(jinx)
                jinx_list.add(jinx)
                jinx_count += 1
                
            while lux_count < 1 and level == 8:
            lux = Lux()
            hit_list = pygame.sprite.spritecollide(lux, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(lux)
                enemy_list.add(lux)
                lux_list.add(lux)
                lux_count += 1
                
def win_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        final_text = my_font_2.render("Congratulations, you are a true Ninja", True, WHITE)
        screen.blit(final_text, [300, 100])
        screen.blit(true_ninja, [600, 200])
"""

# adds characters/player to sprite list/ bucket
player_list.add(character)
all_sprites_list.add(player_list)

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
                throw_sound.play()
                all_sprites_list.add(star)
                star_list.add(star)
    screen.blit(background_image, [0, 0])
    # --- Game logic should go here
    all_sprites_list.update()

    for star in star_list:
        hit_list = pygame.sprite.spritecollide(star, archer_list, True)
        for hit in hit_list:
            star.kill()
            score += 1
            print(score)

    for star in star_list:
        hit_list = pygame.sprite.spritecollide(star, arrow_list, True)
        for hit in hit_list:
            star.kill()

    for arrow in arrow_list:
        hit_list = pygame.sprite.spritecollide(arrow, player_list, False)
        for hit in hit_list:
            arrow.kill()
            hit.health -= 1

    if character.health == 0:
        all_sprites_list.empty()

        screen.blit(game_over, [100, 100])


    # --- Drawing code goes here


    all_sprites_list.draw(screen)

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60     for star in star_list:

pygame.quit()  # Close the window and quit.