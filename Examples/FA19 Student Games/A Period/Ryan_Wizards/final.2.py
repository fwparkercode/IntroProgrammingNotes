"""
Ryan Toulouse - 2019
Final Game Code
I made a shooter game where the player has to try and beat all the levels to complete ninja training
Once a player clears all the enemies on screen, a next  level will appear
After a certain amount of levels the player with run into different types of enemies that make the game harder
The player has five lives which are shown in th bottom left, and different enemies take away different types of lives
"""

import pygame
import random

#  variables
wizard_count = 0
count = 0
score = 0
level = 4 # change level to 7 to see lux work
lives_x = 0
lux_count = 0
jinx_count = 0

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
lives = pygame.image.load("heart.png")
bow_sound = pygame.mixer.Sound("shoot (1).ogg")
bow_sound.set_volume(0.6)
throw_sound = pygame.mixer.Sound("throwing.wav")
background_music = pygame.mixer.Sound("bensound-instinct.wav")
background_music.play(-1)
background_music.set_volume(0.5)
ninja_star = pygame.image.load("ninjastar.png")
true_ninja = pygame.image.load("final.png")
magic_music = pygame.mixer.Sound("N Orchard St.ogg")

# text code
my_font = pygame.font.SysFont("Calibri", 60, True, False)
my_font_1 = pygame.font.SysFont("Calibri", 40, True, False)
my_font_2 = pygame.font.SysFont("Calibri", 50, True, False)
my_font_3 = pygame.font.SysFont("Calibri", 70, True, False)
my_font_4 = pygame.font.SysFont("Calibri", 30, True, False)

#  function for intro screen
def intro_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
        my_text = my_font.render("Welcome to Ninja Training", True, WHITE)
        space = my_font_1.render("Hit Space Bar to Throw Your Ninja Star : ", True, WHITE)
        keys = my_font_1.render("Use Arrows Keys to Move", True, WHITE)
        game = my_font_2.render("Defeat all the enemies on screen to advance levels", True, WHITE)
        question = my_font_3.render("Can you beat all the levels?", True, WHITE)
        start = my_font_4.render("Hit return to begin ", True, WHITE)


        screen.fill(BLACK)
        screen.blit(my_text, [300, 0])
        screen.blit(space, [25, 225])
        screen.blit(ninja_star, [300, 275])
        screen.blit(keys, [800, 225])
        screen.blit(game, [150, 100])
        screen.blit(question, [250, 400])
        screen.blit(start, [525, 500])

        pygame.display.flip()
        clock.tick(60)

def win_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        final_text = my_font_2.render("Congratulations, you are a true Ninja", True, WHITE)
        screen.fill(BLACK)
        screen.blit(final_text, [250, 25])
        screen.blit(true_ninja, [300, 50])

        pygame.display.flip()
        clock.tick(60)


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
        if self.rect.x > 300:
            self.rect.x = 300
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
            arrow.rect.x = self.rect.x - 7
            arrow.rect.y = self.rect.y + 12
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
        if self.rect.x < 0 - 115:
            Arrow.kill(self)


class Wizard(pygame.sprite.Sprite):
    health = 4

    def __init__(self):
        super().__init__()

        self.frame = 0
        self.image = pygame.image.load("icewitch.png")

        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(800, SCREEN_WIDTH - 115)
        self.rect.y = random.randrange(100, SCREEN_HEIGHT - 115)

    def update(self):
        self.frame += 1
        if self.frame % 60 == random.randrange(25, 50):
            spell = Iceball()
            spell.rect.x = self.rect.x
            spell.rect.y = self.rect.y + 20
            ice_list.add(spell)
            all_sprites_list.add(spell)
            magic_music.play()


class Iceball(pygame.sprite.Sprite):
    health = 2

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("ice.png")
        self.rect = self.image.get_rect()
        self.change_x = - 18

    def update(self):
        self.rect.x += self.change_x
        if self.rect.x < -115:
            Iceball.kill(self)


class Lux(pygame.sprite.Sprite):
    health = 3

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("lux.png")
        self.rect = self.image.get_rect()
        self.frame = 0

        self.rect.x = random.randrange(700, SCREEN_WIDTH - 115)
        self.rect.y = random.randrange(100, SCREEN_HEIGHT - 115)

    def update(self):
        self.frame += 1
        if self.frame % 180 == 0:  # mr lee helped here for laser code
            laser = Laser()
            laser.rect.right = self.rect.left - 310
            laser.rect.centery = self.rect.centery - 50
            laser_list.add(laser)
            all_sprites_list.add(laser)


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([SCREEN_WIDTH, 20])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.laser_image = pygame.image.load("laser.png")
        self.laser_part = pygame.image.load("part of laser.png")
        self.health = 60

    def update(self):
        self.health -= 1
        if self.health < 0:
            self.kill()

    def draw_me(self):  # mr.lee helped with this laser part to get it to work
        screen.blit(self.laser_image, [self.rect.right, self.rect.top])
        screen.blit(self.laser_part, [self.rect.right - self.laser_image.get_width() + 55, self.rect.top])
        screen.blit(self.laser_part, [self.rect.right - self.laser_image.get_width() - self.laser_part.get_width() + 65, self.rect.top])
        screen.blit(self.laser_part, [self.rect.right - self.laser_image.get_width() - self.laser_part.get_width() * 2 + 70, self.rect.top])


class Jinx(pygame.sprite.Sprite):
    health = 6

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("jinx.png")
        self.rect = self.image.get_rect()
        self.frame = 0

        self.rect.x = random.randrange(700, SCREEN_WIDTH - 115)
        self.rect.y = random.randrange(100, SCREEN_HEIGHT - 115)

    def update(self):
        self.frame += 1
        if self.frame % 120 == random.randrange(0, 30):
            rocket = Rocket()
            rocket.rect.x = self.rect.x
            rocket.rect.y = self.rect.y
            rockect_list.add(rocket)
            all_sprites_list.add(rocket)
            rocket_1 = Rocket()
            rocket_1.change_y = 3
            rocket_1.rect.x = self.rect.x
            rocket_1.rect.y = self.rect.y
            rockect_list.add(rocket_1)
            all_sprites_list.add(rocket_1)
            rocket_2 = Rocket()
            rocket_2.change_y = - 3
            rocket_2.rect.x = self.rect.x
            rocket_2.rect.y = self.rect.y
            rockect_list.add(rocket_2)
            all_sprites_list.add(rocket_2)


class Rocket(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("jinx_projectile.png")
        self.rect = self.image.get_rect()
        self.change_x = - 23
        self.change_y = 0

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x < - 100:
            self.kill()
        if self.rect.y > 700:
            self.kill()



# all my list groups
enemy_list = pygame.sprite.Group()
wizard_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
star_list = pygame.sprite.Group()
archer_list = pygame.sprite.Group()
arrow_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
ice_list = pygame.sprite.Group()
lux_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
jinx_list = pygame.sprite.Group()
rockect_list = pygame.sprite.Group()

# creates instances of a class
character = Player(0, 0)
""" trying  to get health  to display  and work 
for i in range(character.health):
    heart = Heart()
    all_sprites_list.add(heart)
"""
# spawns the first "level" of enemies
while count < 2 and level == 0:
    archer = Enemy()
    hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
    if len(hit_list) > 0:
        pass
    else:
        all_sprites_list.add(archer)
        enemy_list.add(archer)
        archer_list.add(archer)
        count += 1

# adds characters/player to sprite list/ bucket
player_list.add(character)
all_sprites_list.add(player_list)

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game!")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates
intro_screen()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character.changespeed(-8, 0)
            elif event.key == pygame.K_RIGHT:
                character.changespeed(8, 0)
            elif event.key == pygame.K_UP:
                character.changespeed(0, -8)
            elif event.key == pygame.K_DOWN:
                character.changespeed(0, 8)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character.changespeed(8, 0)
            elif event.key == pygame.K_RIGHT:
                character.changespeed(-8, 0)
            elif event.key == pygame.K_UP:
                character.changespeed(0, 8)
            elif event.key == pygame.K_DOWN:
                character.changespeed(0, -8)

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

    for i in range(character.health):  # code for lives appearing and mr.lee helped a little here
        screen.blit(lives, [i * lives.get_width() + 10, 560])

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

    for star in star_list:
        hit_list = pygame.sprite.spritecollide(star, wizard_list, False)
        for hit in hit_list:
            star.kill()
            hit.health -= 1

    for wizard in wizard_list:
        if wizard.health == 0:
            wizard.kill()

    for spell in ice_list:
        hit_list = pygame.sprite.spritecollide(spell, player_list, False)
        for hit in hit_list:
            spell.kill()
            hit.health -= 2

    for star in star_list:
        hit_list = pygame.sprite.spritecollide(star, ice_list, False)
        for hit in hit_list:
            star.kill()

    for star in star_list:
        hit_list = pygame.sprite.spritecollide(star, lux_list, False)
        for hit in hit_list:
            star.kill()
            hit.health -= 1
    for star in star_list:
        hit_list = pygame.sprite.spritecollide(star, laser_list, False)
        for hit in hit_list:
            star.kill()

    for laser in laser_list: # need help making laser not one shot lol
        hit_list = pygame.sprite.spritecollide(laser, player_list, False)
        for hit in hit_list:
            hit.health -= 3

    for star in star_list:
        hit_list = pygame.sprite.spritecollide(star, jinx_list, False)
        for hit in hit_list:
            star.kill()
            hit.health -= 1

    for rocket in rockect_list:
        hit_list = pygame.sprite.spritecollide(rocket, player_list, False)
        for hit in hit_list:
            rocket.kill()
            hit.health -= 1

    for star in star_list:
        hit_list = pygame.sprite.spritecollide(star, rockect_list, True)
        for hit in hit_list:
            star.kill()

    for lux in lux_list:
        if lux.health == 0:
            lux.kill()
            laser_list.empty()

    for jinx in jinx_list:
        if jinx.health == 0:
            jinx.kill()

    if len(enemy_list) == 0:
        level += 1
        count = 0
        wizard_count = 0
        lux_count = 0
        jinx_count = 0

    if level == 1:
        while count < 4 and level == 1:
            archer = Enemy()
            hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(archer)
                enemy_list.add(archer)
                archer_list.add(archer)
                count += 1

    if level == 2:
        while count < 6 and level == 2:
            archer = Enemy()
            hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(archer)
                enemy_list.add(archer)
                archer_list.add(archer)
                count += 1

    if level == 3:
        while count < 8 and level == 3:
            archer = Enemy()
            hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(archer)
                enemy_list.add(archer)
                archer_list.add(archer)
                count += 1

    if level == 4:
        while wizard_count < 1 and level == 4:
            wizard = Wizard()
            hit_list = pygame.sprite.spritecollide(wizard, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(wizard)
                enemy_list.add(wizard)
                wizard_list.add(wizard)
                wizard_count += 1

    if level == 5:
        while wizard_count < 1 and level == 5:
            wizard = Wizard()
            hit_list = pygame.sprite.spritecollide(wizard, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(wizard)
                enemy_list.add(wizard)
                wizard_list.add(wizard)
                wizard_count += 1

        while count < 3 and level == 5:
            archer = Enemy()
            hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(archer)
                enemy_list.add(archer)
                archer_list.add(archer)
                count += 1

    if level == 6:
        while wizard_count < 1 and level == 6:
            wizard = Wizard()
            hit_list = pygame.sprite.spritecollide(wizard, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(wizard)
                enemy_list.add(wizard)
                wizard_list.add(wizard)
                wizard_count += 1

        while count < 5 and level == 6:
            archer = Enemy()
            hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(archer)
                enemy_list.add(archer)
                archer_list.add(archer)
                count += 1

    if level == 7:
        while wizard_count < 2 and level == 7:
            wizard = Wizard()
            hit_list = pygame.sprite.spritecollide(wizard, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(wizard)
                enemy_list.add(wizard)
                wizard_list.add(wizard)
                wizard_count += 1

        while count < 3 and level == 7:
            archer = Enemy()
            hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(archer)
                enemy_list.add(archer)
                archer_list.add(archer)
                count += 1

    if level == 8:
        while wizard_count < 2 and level == 8:
            wizard = Wizard()
            hit_list = pygame.sprite.spritecollide(wizard, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(wizard)
                enemy_list.add(wizard)
                wizard_list.add(wizard)
                wizard_count += 1

        while count < 5 and level == 8:
            archer = Enemy()
            hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(archer)
                enemy_list.add(archer)
                archer_list.add(archer)
                count += 1

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

    if level == 10:
        while jinx_count < 1 and level == 10:
            jinx = Jinx()
            hit_list = pygame.sprite.spritecollide(jinx, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(jinx)
                enemy_list.add(jinx)
                jinx_list.add(jinx)
                jinx_count += 1
        while count < 5 and level == 10:
            archer = Enemy()
            hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(archer)
                enemy_list.add(archer)
                archer_list.add(archer)
                count += 1
    if level == 11:
        while jinx_count < 1 and level == 11:
            jinx = Jinx()
            hit_list = pygame.sprite.spritecollide(jinx, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(jinx)
                enemy_list.add(jinx)
                jinx_list.add(jinx)
                jinx_count += 1

        while wizard_count < 2 and level == 11:
            wizard = Wizard()
            hit_list = pygame.sprite.spritecollide(wizard, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(wizard)
                enemy_list.add(wizard)
                wizard_list.add(wizard)
                wizard_count += 1

        while count < 3 and level == 11:
            archer = Enemy()
            hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(archer)
                enemy_list.add(archer)
                archer_list.add(archer)
                count += 1

    if level == 12:
        while jinx_count < 2 and level == 12:
            jinx = Jinx()
            hit_list = pygame.sprite.spritecollide(jinx, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(jinx)
                enemy_list.add(jinx)
                jinx_list.add(jinx)
                jinx_count += 1

        while wizard_count < 2 and level == 12:
            wizard = Wizard()
            hit_list = pygame.sprite.spritecollide(wizard, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(wizard)
                enemy_list.add(wizard)
                wizard_list.add(wizard)
                wizard_count += 1

    if level == 13:
        while lux_count < 1 and level == 13:
            lux = Lux()
            hit_list = pygame.sprite.spritecollide(lux, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(lux)
                enemy_list.add(lux)
                lux_list.add(lux)
                lux_count += 1

        while count < 3 and level == 13:
            archer = Enemy()
            hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(archer)
                enemy_list.add(archer)
                archer_list.add(archer)
                count += 1

    if level == 14:
        while lux_count < 1 and level == 14:
            lux = Lux()
            hit_list = pygame.sprite.spritecollide(lux, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(lux)
                enemy_list.add(lux)
                lux_list.add(lux)
                lux_count += 1

        while jinx_count < 1 and level == 14:
            jinx = Jinx()
            hit_list = pygame.sprite.spritecollide(jinx, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(jinx)
                enemy_list.add(jinx)
                jinx_list.add(jinx)
                jinx_count += 1

        while count < 3 and level == 14:
            archer = Enemy()
            hit_list = pygame.sprite.spritecollide(archer, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(archer)
                enemy_list.add(archer)
                archer_list.add(archer)
                count += 1

    if level == 15:
        while lux_count < 1 and level == 15:
            lux = Lux()
            hit_list = pygame.sprite.spritecollide(lux, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(lux)
                enemy_list.add(lux)
                lux_list.add(lux)
                lux_count += 1

        while jinx_count < 1 and level == 15:
            jinx = Jinx()
            hit_list = pygame.sprite.spritecollide(jinx, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(jinx)
                enemy_list.add(jinx)
                jinx_list.add(jinx)
                jinx_count += 1

        while wizard_count < 2 and level == 15:
            wizard = Wizard()
            hit_list = pygame.sprite.spritecollide(wizard, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(wizard)
                enemy_list.add(wizard)
                wizard_list.add(wizard)
                wizard_count += 1

    if level == 16:
        while lux_count < 2 and level == 16:
            lux = Lux()
            hit_list = pygame.sprite.spritecollide(lux, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(lux)
                enemy_list.add(lux)
                lux_list.add(lux)
                lux_count += 1

        while jinx_count < 2 and level == 16:
            jinx = Jinx()
            hit_list = pygame.sprite.spritecollide(jinx, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(jinx)
                enemy_list.add(jinx)
                jinx_list.add(jinx)
                jinx_count += 1

        while wizard_count < 1 and level == 16:
            wizard = Wizard()
            hit_list = pygame.sprite.spritecollide(wizard, enemy_list, False)
            if len(hit_list) > 0:
                pass
            else:
                all_sprites_list.add(wizard)
                enemy_list.add(wizard)
                wizard_list.add(wizard)
                wizard_count += 1
    if level == 17:
        all_sprites_list.empty()
        win_screen()

    if character.health <= 0:
        all_sprites_list.empty()
        laser_list.empty()
        screen.blit(game_over, [150, 125])

    # updates all sprites
    all_sprites_list.draw(screen)
    for laser in laser_list:
        laser.draw_me()

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60     for star in star_list:

pygame.quit()  # Close the window and quit.
