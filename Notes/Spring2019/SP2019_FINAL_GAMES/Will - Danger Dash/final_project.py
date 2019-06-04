'''
Multiline Comment --
In this simple fighting game titled, "Danger Dash" the player is given the simple control scheme of the arrow keys
and space bar. Dash, the main character, is controlled using the arrow keys, using them to duck, dodge, and jump over
obstacles. The space bar, on the other hand, is used to dash through enemies! With the power of this dash at your
disposal, you can dodge fireballs and kill enemies. As the game progresses, the player is slowly exposed to more
challenges and even some useful powerups. Can you survive the five difficult levels? Goodluck, and remember to have fun
dashing your way to the top.
'''

# Made by William Leonard Holtz

import pygame
import random
import math

# Initialize the game engine
pygame.init()

# TEST
pygame.image.load("armor_up.png")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 243, 22)
LIGHT_BLUE = (150, 150, 255)

# Set the height and width of the screen
size = (680, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Danger Dash!")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Global Variables
score = 0
time = 0
action = "stand"
death = False
sound_played = False
frame = 0
game_over = False
win = False
playing = False
difficulty = 1
level = 1
key_pressed = 0
tutorial = False
enemy_count = 1
level_2_transition = False
level_3_transition = False
level_4_transition = False
level_5_transition = False

### Image resources

# Text
big_font = pygame.font.SysFont('Calibri', 40, True, False)
medium_font = pygame.font.SysFont('Calibri', 30, True, False)
small_font = pygame.font.SysFont('Calibri', 20, True, False)
duck_tutorial = big_font.render("Down Arrow = Duck", True, BLACK)
jump_tutorial = big_font.render("Up Arrow = Jump", True, BLACK)
death_game_over = big_font.render("Game over, you lose!", True, WHITE)
win_game_over = big_font.render("Congratulations, you win!", True, BLACK)
dash = small_font.render("Dash!", True, BLACK)
charging = small_font.render("Charging...", True, BLACK)
health_bar = small_font.render("Health", True, BLACK)
dash_tutorial = big_font.render("Spacebar = Dash", True, BLACK)
title = big_font.render("Welcome to Danger Dash!", True, BLACK)
press_spacebar = small_font.render("Press the spacebar to continue.", True, WHITE)
instructions = medium_font.render("Dash through enemies and dodge fireballs to win!", True, BLACK)
goodluck = medium_font.render("Goodluck", True, BLACK)
level_1 = big_font.render("LEVEL 1", True, WHITE)
level_2 = big_font.render("LEVEL 2", True, WHITE)
level_3 = big_font.render("LEVEL 3", True, WHITE)
level_4 = big_font.render("LEVEL 4", True, WHITE)
level_5 = big_font.render("LEVEL 5", True, WHITE)
invincible = small_font.render("Invulnerable!", True, BLACK)

# Images
sky = pygame.image.load("skybox.png")
far_mountain = pygame.image.load("far_mountain.png")
close_mountain = pygame.image.load("close_mountain.png")
treeline = pygame.image.load("trees.png")
meteor_spritesheets = ["meteor.png",
                       "armor_meteor.png",
                       "potion_meteor.png"]

# Sound resources
victory = pygame.mixer.Sound("Victory.wav")
pygame.mixer.Sound.set_volume(victory, 0.2)
background_music = pygame.mixer.Sound("background_music.wav")
pygame.mixer.Sound.set_volume(background_music, 0.5)
punch_sound = pygame.mixer.Sound("punch.wav")
pygame.mixer.Sound.set_volume(punch_sound, 0.5)

# Functions / Classes


class SpriteSheet:
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name)

    def get_image(self, x, y, width, height):    # Used to set up class spritesheets
        image = pygame.Surface([width, height])
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(BLACK)
        return image


class Player(pygame.sprite.Sprite):
    def __init__(self, spritesheet_name):
        super().__init__()
        ### Unique variables
        # Image lists
        self.stand_list = []
        self.run_list = []
        self.duck_list = []
        self.die_list = []
        self.jump_list = []
        self.duck_atk_list = []
        self.atk_list = []
        self.jump_atk_list = []

        # Movement variables
        self.direction = "R"
        self.action = "stand"
        self.jump_height = 1
        self.jump_cycle = False
        self.attacking = False
        self.air_run = False

        # Other
        self.invulnerable = False
        self.invulnerability = 0
        self.invincibility_time = 0
        self.collected_frame = 0
        self.cooldown = 0
        self.armor = "none"
        self.health = 3
        self.add(all_sprite_group)
        self.death = False
        self.death_frame = 0
        self.dead = False
        self.enemies_killed = 0

        # Sprite image setup
        self.spritesheet = SpriteSheet(spritesheet_name)
        for j in range(1):
            self.stand_list.append(self.spritesheet.get_image(46 * j, 0, 46, 50))
        for j in range(8):
            self.run_list.append(self.spritesheet.get_image(46 * j, 150, 46, 50))
        for j in range(1):
            self.duck_list.append(self.spritesheet.get_image(46, 0, 46, 50))
        self.die_list.append(self.spritesheet.get_image(0, 50, 46, 50))
        for j in range(2):
            self.die_list.append(self.spritesheet.get_image(46 * j, 100, 46, 50))
        for j in range(2):
            self.jump_list.append(self.spritesheet.get_image(46 * j + 276, 0, 46, 50))
        for j in range(4):
            self.duck_atk_list.append(self.spritesheet.get_image(46 * j + 92, 100, 46, 50))
        for j in range(4):
            self.atk_list.append(self.spritesheet.get_image(46 * j + 92, 0, 46, 50))
        for j in range(4):
            self.jump_atk_list.append(self.spritesheet.get_image(46 * j + 92, 50, 46, 50))
        self.image = self.stand_list[0]

        # Sprite positioning
        self.rect = self.image.get_rect()
        self.rect.x = 325
        self.rect.y = 350
        self.change_x = 0
        self.change_y = 0

    def update(self):
        if self.action == "stand":  # Determines image according to action
            self.change_x = 0
            self.change_y = 0
            if self.direction == "L":
                self.image = pygame.transform.flip(self.stand_list[0], True, False)
            else:
                self.image = self.stand_list[0]
        if self.action == "run":
            self.change_y = 0
            if self.direction == "L":
                self.change_x = -3
                self.image = pygame.transform.flip(self.run_list[int(frame / 4) % 4], True, False)
            else:
                self.change_x = 3
                self.image = self.run_list[int(frame / 4) % 4]
        if self.action == "duck":
            self.change_y = 0
            self.change_x = 0
            if self.direction == "L":
                self.image = pygame.transform.flip(self.duck_list[0], True, False)
            else:
                self.image = self.duck_list[0]
        if not self.attacking:  # Jump code
            if self.action == "rise":
                if self.direction == "L":
                    self.image = pygame.transform.flip(self.jump_list[1], True, False)
                else:
                    self.image = self.jump_list[1]
                self.change_y = -int(10 / self.jump_height)
                if self.jump_height >= 15:
                    self.action = "fall"
                self.jump_height += 1
            if self.action == "fall":
                if self.direction == "L":
                    self.image = pygame.transform.flip(self.jump_list[0], True, False)
                else:
                    self.image = self.jump_list[0]
                if self.jump_height != 1:
                    self.jump_height -= 1
                self.change_y = int(10 / self.jump_height)

        if self.attacking:  # Dashing image code
            self.change_y = 0
            if self.direction == "L":
                if self.action == "run" or self.action == "stand":
                    self.image = pygame.transform.flip(self.atk_list[int((35 - self.cooldown) / 5)], True, False)
                elif self.action == "duck":
                    self.image = pygame.transform.flip(self.duck_atk_list[int((35 - self.cooldown) / 5)], True, False)
                elif self.action == "fall" or self.action == "rise":
                    self.image = pygame.transform.flip(self.jump_atk_list[int((35 - self.cooldown) / 5)], True, False)
                self.change_x = -15
            else:
                if self.action == "run" or self.action == "stand":
                    self.image = self.atk_list[int((35 - self.cooldown) / 5)]
                elif self.action == "duck":
                    self.image = self.duck_atk_list[int((35 - self.cooldown) / 5)]
                elif self.action == "fall" or self.action == "rise":
                    self.image = self.jump_atk_list[int((35 - self.cooldown) / 5)]
                self.change_x = 15
            if self.cooldown == 45:
                self.attacking = False
                if self.action == "rise":
                    self.action = "fall"
                if self.action == "fall":
                    if self.air_run:
                        if self.direction == "L":
                            self.change_x = -3
                        else:
                            self.change_x = 3
                    else:
                        self.change_x = 0

        if self.jump_height == 1 and self.action == "fall":  # Landing code
            self.jump_cycle = False
            if self.change_x == 0:
                self.action = "stand"
            else:
                self.action = "run"
        if self.cooldown > 0:
            self.cooldown -= 1

        # Armor code
        if self.health == 3:
            self.armor = "robe"
        elif self.health == 2:
            self.armor = "armor"
        elif self.health == 1:
            self.armor = "none"
        elif self.health == 0:
            self.death = True

        # Death code
        if self.death:
            if self.direction == "L":
                self.image = pygame.transform.flip(self.die_list[int(self.death_frame)], True, False)
            else:
                self.image = self.die_list[int(self.death_frame)]
            if self.death_frame >= 2.9:
                self.dead = True
                self.kill()
            self.death_frame += 0.07
            self.change_x = 0
            self.change_y = 0

        # Invincibility bug fix
        self.invulnerability = 200 - self.invincibility_time
        self.invincibility_time += 1
        if 200 - self.invincibility_time <= 0:
            self.invulnerable = False

        # Movement code
        self.rect.x += self.change_x
        self.rect.y += self.change_y


class Armor(pygame.sprite.Sprite):
    def __init__(self, spritesheet_name, name):
        super().__init__()
        # Image lists
        self.stand_list = []
        self.run_list = []
        self.duck_list = []
        self.die_list = []
        self.jump_list = []
        self.duck_atk_list = []
        self.atk_list = []
        self.jump_atk_list = []

        # Movement
        self.direction = "R"
        self.action = "stand"
        self.jump_height = 1
        self.jump_cycle = False
        self.attacking = False
        self.air_run = False

        self.cooldown = 0
        self.name = name
        self.player = None
        self.add(all_sprite_group)

        # Images
        self.spritesheet = SpriteSheet(spritesheet_name)
        for j in range(1):
            self.stand_list.append(self.spritesheet.get_image(46 * j, 0, 46, 50))
        for j in range(8):
            self.run_list.append(self.spritesheet.get_image(46 * j, 150, 46, 50))
        for j in range(1):
            self.duck_list.append(self.spritesheet.get_image(46, 0, 46, 50))
        self.die_list.append(self.spritesheet.get_image(0, 50, 46, 50))
        for j in range(2):
            self.die_list.append(self.spritesheet.get_image(46 * j, 100, 46, 50))
        for j in range(2):
            self.jump_list.append(self.spritesheet.get_image(46 * j + 276, 0, 46, 50))
        for j in range(4):
            self.duck_atk_list.append(self.spritesheet.get_image(46 * j + 92, 100, 46, 50))
        for j in range(4):
            self.atk_list.append(self.spritesheet.get_image(46 * j + 92, 0, 46, 50))
        for j in range(4):
            self.jump_atk_list.append(self.spritesheet.get_image(46 * j + 92, 50, 46, 50))
        self.image = self.stand_list[0]

        # Sprite positioning
        self.rect = self.image.get_rect()

        self.rect.x = 325
        self.rect.y = 350

        self.change_x = 0
        self.change_y = 0

    def update(self):
        # Sets action/movement equal to player action/movement
        self.action = self.player.action
        self.direction = self.player.direction
        self.cooldown = self.player.cooldown

        # Image determination
        if self.action == "stand":
            if self.direction == "L":
                self.image = pygame.transform.flip(self.stand_list[0], True, False)
            else:
                self.image = self.stand_list[0]
        if self.action == "run":
            if self.direction == "L":
                self.image = pygame.transform.flip(self.run_list[int(frame / 4) % 4], True, False)
            else:
                self.image = self.run_list[int(frame / 4) % 4]
        if self.action == "duck":
            if self.direction == "L":
                self.image = pygame.transform.flip(self.duck_list[0], True, False)
            else:
                self.image = self.duck_list[0]
        if not self.player.attacking:
            if self.action == "rise":
                if self.direction == "L":
                    self.image = pygame.transform.flip(self.jump_list[1], True, False)
                else:
                    self.image = self.jump_list[1]
                self.change_y = -int(10 / self.jump_height)
                if self.player.jump_height >= 15:
                    self.action = "fall"
            if self.action == "fall":
                if self.direction == "L":
                    self.image = pygame.transform.flip(self.jump_list[0], True, False)
                else:
                    self.image = self.jump_list[0]
        if not self.player.attacking:
            if self.action == "rise":
                if self.direction == "L":
                    self.image = pygame.transform.flip(self.jump_list[1], True, False)
                else:
                    self.image = self.jump_list[1]
            if self.action == "fall":
                if self.direction == "L":
                    self.image = pygame.transform.flip(self.jump_list[0], True, False)
                else:
                    self.image = self.jump_list[0]
        if self.player.attacking:
            if self.direction == "L":
                if self.action == "run" or self.action == "stand":
                    self.image = pygame.transform.flip(self.atk_list[int((35 - self.cooldown) / 5)], True, False)
                elif self.action == "duck":
                    self.image = pygame.transform.flip(self.duck_atk_list[int((35 - self.cooldown) / 5)], True, False)
                elif self.action == "fall" or self.action == "rise":
                    self.image = pygame.transform.flip(self.jump_atk_list[int((35 - self.cooldown) / 5)], True, False)
            else:
                if self.action == "run" or self.action == "stand":
                    self.image = self.atk_list[int((35 - self.cooldown) / 5)]
                elif self.action == "duck":
                    self.image = self.duck_atk_list[int((35 - self.cooldown) / 5)]
                elif self.action == "fall" or self.action == "rise":
                    self.image = self.jump_atk_list[int((35 - self.cooldown) / 5)]

        # Movement
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y

        # Armor disappears if not used
        if self.name != self.player.armor:
            self.image = pygame.Surface([1, 1])


class Enemy(pygame.sprite.Sprite):
    def __init__(self, spritesheet_name):
        super().__init__()
        # Unique variables
        self.walk_list = []
        self.death_list = []

        self.hit = False
        self.attack = False
        self.hit_frame = 0
        self.add(all_sprite_group)
        self.frame = 0

        # Images
        self.spritesheet = SpriteSheet(spritesheet_name)

        for j in range(5):
            for k in range(2):
                self.walk_list.append(self.spritesheet.get_image(36 * j, k * 48, 36, 48))
        for j in range(5):
            self.death_list.append(self.spritesheet.get_image(36 * j, 144, 36, 48))

        self.image = self.walk_list[int(self.frame / 3) % 10]
        self.rect = self.image.get_rect()

        # Randomizes position
        if random.randrange(2) == 1:
            self.direction = "R"
            self.change_x = 2
            self.rect.x = -60
        else:
            self.direction = "L"
            self.change_x = -2
            self.rect.x = 710

        self.rect.y = 353

    def update(self):
        self.frame += 1
        if self.direction == "L":
            self.image = pygame.transform.flip(self.walk_list[int(self.frame / 3) % 10], True, False)
        else:
            self.image = self.walk_list[int(self.frame / 3) % 10]

        # Collision code
        if pygame.sprite.collide_rect(player, self):
            if not player.attacking and not self.attack and not self.hit:
                self.attack = True
                if not player.invulnerable:
                    player.health -= 1
            elif player.attacking:
                if not self.hit:
                    punch_sound.play(0)
                self.hit = True
                self.change_x = 0

        # Death sequence
        if self.hit:
            if self.direction == "L":
                self.image = pygame.transform.flip(self.death_list[int(self.hit_frame)], True, False)
                self.hit_frame += 0.2
            else:
                self.image = self.death_list[int(self.hit_frame)]
            self.hit_frame += 0.2
            if self.hit_frame >= 5:
                player.enemies_killed += 1
                self.kill()

        if level_2_transition or level_3_transition or level_4_transition or level_5_transition:
            self.kill()

        self.rect.x += self.change_x


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, spritesheet_name):
        super().__init__()
        # Unique variables
        self.fly_list = []
        self.hit_list = []
        self.hit = False
        self.hit_frame = 0
        self.add(all_sprite_group)

        # Images
        self.spritesheet = SpriteSheet(spritesheet_name)
        for j in range(3):
            for k in range(3):
                self.fly_list.append(self.spritesheet.get_image(30 * j, k * 15 + 15, 30, 15))
        for j in range(3):
            self.hit_list.append(self.spritesheet.get_image(30 * j, 60, 30, 15))

        self.image = self.fly_list[int(frame / 4) % 9]
        self.rect = self.image.get_rect()

        # Randomizes direction/height
        if random.randrange(2) == 1:
            self.direction = "R"
            self.change_x = 3
            self.rect.x = -60
        else:
            self.direction = "L"
            self.change_x = -3
            self.rect.x = 710

        if random.randrange(2) == 1:
            self.height = "top"
            self.rect.y = 350
        else:
            self.height = "bottom"
            self.rect.y = 375

    def update(self):
        # Collision testing
        if pygame.sprite.collide_rect(player, self):
            # Hitbox of player was difficult to manage, instead tested action in addition to collision
            if self.height == "top" and player.action != "duck":
                if not self.hit:
                    if not player.invulnerable:
                        player.health -= 1
                self.hit = True
                self.change_x = 0
                if self.direction == "L":
                    self.image = pygame.transform.flip(self.hit_list[int(frame / 4) % 3], True, False)
                else:
                    self.image = self.hit_list[int(frame / 4) % 3]
            elif self.height == "bottom" and player.action != "rise" and player.action != "fall":
                if not self.hit:
                    if not player.invulnerable:
                        player.health -= 1
                self.hit = True
                self.change_x = 0
                if self.direction == "L":
                    self.image = pygame.transform.flip(self.hit_list[int(frame / 4) % 3], True, False)
                else:
                    self.image = self.hit_list[int(frame / 4) % 3]
            else:
                if self.direction == "L":
                    self.image = pygame.transform.flip(self.fly_list[int(frame / 4) % 9], True, False)
                else:
                    self.image = self.fly_list[int(frame / 4) % 9]
        else:
            if self.direction == "L":
                self.image = pygame.transform.flip(self.fly_list[int(frame / 4) % 9], True, False)
            else:
                self.image = self.fly_list[int(frame / 4) % 9]

        if level_2_transition or level_3_transition or level_4_transition or level_5_transition:
            self.kill()

        # Collision sequence
        if self.hit:
            if self.direction == "L":
                self.image = pygame.transform.flip(self.hit_list[int(self.hit_frame)], True, False)
                self.hit_frame += 0.2
            else:
                self.image = self.hit_list[int(self.hit_frame)]
            self.hit_frame += 0.2
            if self.hit_frame >= 3:
                self.kill()

        self.rect.x += self.change_x


class Meteor(pygame.sprite.Sprite):
    def __init__(self, spritesheet_name, meteor_type):
        super().__init__()
        # Unique variables
        self.fly_list = []
        self.hit_list = []
        self.hit = False
        self.hit_frame = 0
        self.add(all_sprite_group)
        self.frame = 0
        self.meteor_type = meteor_type

        # Images
        self.spritesheet = SpriteSheet(spritesheet_name)
        for j in range(3):
            for k in range(3):
                self.fly_list.append(self.spritesheet.get_image(15 * j + 15, k * 30, 15, 30))
        for j in range(3):
            self.hit_list.append(self.spritesheet.get_image(0, j * 30, 15, 30))
        self.image = self.fly_list[int(frame / 4) % 9]

        # Movement
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 4
        self.rect.y = -20
        self.rect.x = random.randrange(20, 645)

    def update(self):
        self.image = self.fly_list[int(self.frame / 4) % 9]

        # Collision testing
        if pygame.sprite.collide_rect(player, self):
            if not self.hit:
                if not player.invulnerable:
                    player.health -= 1
                self.hit = True
                self.change_y = 0
                self.image = self.hit_list[int(self.frame / 4) % 3]
        if self.rect.y >= 367:
                self.hit = True
                self.change_y = 0
                self.image = self.hit_list[int(self.frame / 4) % 3]
        if self.hit:
            self.image = self.hit_list[int(self.hit_frame)]
            self.hit_frame += 0.2
            if self.hit_frame >= 3:
                if self.rect.y >= 367:
                    # Creates powerup dependent on player health only if meteor lands
                    if self.meteor_type == 2:
                        potion = Invulnerable(self.rect.x, "potion.png")
                    elif self.meteor_type == 1:
                        health = ArmorUp(self.rect.x,"armor_up.png")
                self.kill()

        self.rect.y += self.change_y
        self.frame += 1

        if level_2_transition or level_3_transition or level_4_transition or level_5_transition:
            self.kill()


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x_pos, image_name):
        super().__init__()
        # Unique variables
        self.frame = 0
        self.image_list = []
        self.collected_frame = 0

        # Images
        self.spritesheet = SpriteSheet(image_name)
        self.image_list.append(self.spritesheet.get_image(0, 0, 16, 16))
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()

        self.rect.x = x_pos
        self.rect_y = 370

        self.add(all_sprite_group)


class ArmorUp(PowerUp):
    def __init__(self, x_pos, image_name):
        super().__init__(x_pos, image_name)
        self.rect.y = self.rect_y

    def update(self):
        # Movement
        self.rect.y = self.rect_y + int(8 * math.sin(2 * math.pi * self.frame / 60))

        # Collection
        if pygame.sprite.collide_rect(player, self):
            if player.health <= 2:
                player.health += 1  # Effect
            self.kill()

        # Despawn code
        if self.frame - self.collected_frame >= 300:
            self.kill()

        self.frame += 1

        if level_2_transition or level_3_transition or level_4_transition or level_5_transition:
            self.kill()


class Invulnerable(PowerUp):
    def __init__(self, x_pos, image_name):
        super().__init__(x_pos, image_name)
        self.collected = False
        self.rect.y = self.rect_y

    def update(self):

        # Movement
        self.rect.y = self.rect_y + int(8 * math.sin(2 * math.pi * self.frame / 60))

        # Collection
        if pygame.sprite.collide_rect(player, self) and not self.collected:
            self.collected = True
            player.invincibility_time = 0
            player.invulnerable = True
            self.kill()

        # Despawn
        if self.frame - self.collected_frame >= 200:
            self.kill()

        self.frame += 1

        if level_2_transition or level_3_transition or level_4_transition or level_5_transition:
            self.kill()


def draw_star(x, y):
    pygame.draw.polygon(screen, YELLOW, [[20 + x, 2 + y], [26 + x, 14 + y], [38 + x, 14 + y], [28 + x, 22 + y],
                                         [30 + x, 34 + y], [20 + x, 26 + y], [10 + x, 34 + y], [12 + x, 22 + y],
                                         [2 + x, 14 + y], [14 + x, 14 + y], [20 + x, 2 + y]])


all_sprite_group = pygame.sprite.Group()

player = Player("player_sheet.png")
armor = Armor("armor.png", "armor")
robe = Armor("robe.png", "robe")
armor.player = player
robe.player = player

background_music.play(20)

# Game loop
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if not death:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Run left
                    if player.action == "stand" and player.action != "duck" and player.action != "attack":
                        player.action = "run"
                        player.direction = "L"
                    if player.action == "rise" or player.action == "fall":
                        player.direction = "L"
                        player.change_x = -3
                elif event.key == pygame.K_RIGHT:  # Run right
                    if player.action == "stand" and player.action != "duck" and player.action != "attack":
                        player.action = "run"
                        player.direction = "R"
                    if player.action == "rise" or player.action == "fall":
                        player.direction = "R"
                        player.change_x = 3
                elif event.key == pygame.K_UP:  # Jump
                    if not player.jump_cycle:
                        player.action = "rise"
                        player.jump_cycle = True
                elif event.key == pygame.K_DOWN:  # Duck
                    if player.action == "stand" or player.action == "run":
                        player.action = "duck"
                elif event.key == pygame.K_SPACE:  # Dash
                    key_pressed += 1
                    if player.cooldown == 0:
                        player.attacking = True
                        player.cooldown = 50
                        if player.change_x != 0:
                            player.air_run = True
                        else:
                            player.air_run = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if player.action == "run":
                        player.action = "stand"
                    if player.action == "rise" or player.action == "fall":
                        player.change_x = 0
                elif event.key == pygame.K_RIGHT:
                    if player.action == "run":
                        player.action = "stand"
                    if player.action == "rise" or player.action == "fall":
                        player.change_x = 0
                elif event.key == pygame.K_DOWN:
                    if player.action == "duck":
                        player.action = "stand"

    # Stops player from moving pre-tutorial
    if not playing and not tutorial:
        player.action = "stand"
        player.attacking = False
        player.direction = "R"
        player.jump_cycle = False

    # Stops player from moving off screen
    if player.rect.x <= -8:
        player.change_x = 0
        player.rect.x = -8
    elif player.rect.x >= 640:
        player.change_x = 0
        player.rect.x = 640

    frame += 1
    time += 1

    # Enemy spawning
    if playing:
        if frame % int(200 / (difficulty * level)) == 0:
            if random.randrange(3) >= 1 and level >= 2:
                fireball = Obstacle("fireball.png")
            else:
                skeleton = Enemy("skeleton.png")
        if random.randrange(0, 10000) >= (9933 - 10 * level) and level >= 3:
            if random.randrange(3) == 1 or not level <= 5:
                meteor_type = random.randrange(3)
                meteor = Meteor(meteor_spritesheets[meteor_type], meteor_type)
            else:
                meteor = Meteor(meteor_spritesheets[0], 0)

    all_sprite_group.update()

    # Goal management
    enemies_left = enemy_count - player.enemies_killed
    enemies_left_text = big_font.render("Enemies remaining: " + str(round(enemies_left)), True, BLACK)

    if player.dead:
        death = True

    #  Drawing code
    screen.fill(BLACK)

    # Backdrop
    screen.blit(sky, [0, 0])
    screen.blit(far_mountain, [0, 0])
    screen.blit(close_mountain, [0, 0])
    screen.blit(treeline, [0, 0])
    pygame.draw.rect(screen, (89, 59, 64), [0, 395, 685, 10])

    # Tutorial
    if tutorial:
        if 160 > time > 40:
            screen.blit(duck_tutorial, [360, 10])
        if 290 > time > 170:
            screen.blit(jump_tutorial, [400, 10])
        if 420 > time > 300:
            screen.blit(dash_tutorial, [410, 10])
        if time > 430:
            enemy_count = 3
            tutorial = False
            playing = True

    # Starts lvl 2, Ends lvl 1
    if key_pressed == 6 and level_2_transition:
        level_2_transition = False
        level = 2
        playing = True
        player.enemies_killed = 0
        enemy_count = 3
    elif enemies_left == 0 and level == 1:
        level_2_transition = True
        player.health = 3
        player.rect.x = 325
        player.rect.y = 350
        playing = False
        key_pressed = 5
        screen.fill(BLACK)
        screen.blit(level_2, [280, 180])
        screen.blit(press_spacebar, [5, 380])

    # Starts lvl 3, Ends lvl 2
    elif key_pressed == 9 and level_3_transition:
        level_3_transition = False
        level = 3
        playing = True
        player.enemies_killed = 0
        enemy_count = 5
    elif enemies_left == 0 and level == 2:
        level_3_transition = True
        player.rect.x = 325
        player.rect.y = 350
        player.health = 3
        playing = False
        key_pressed = 8
        screen.fill(BLACK)
        screen.blit(level_3, [280, 180])
        screen.blit(press_spacebar, [5, 380])

    # Starts lvl 4, Ends lvl 3
    elif key_pressed == 12 and level_4_transition:
        level_4_transition = False
        level = 4
        playing = True
        player.enemies_killed = 0
        enemy_count = 5
    elif enemies_left == 0 and level == 3:
        level_4_transition = True
        player.rect.x = 325
        player.rect.y = 350
        player.health = 3
        playing = False
        key_pressed = 11
        screen.fill(BLACK)
        screen.blit(level_4, [280, 180])
        screen.blit(press_spacebar, [5, 380])

    # Starts lvl 5, Ends lvl 4
    elif key_pressed == 15 and level_5_transition:
        level_5_transition = False
        level = 5
        playing = True
        player.enemies_killed = 0
        enemy_count = 10
    elif enemies_left == 0 and level == 4:
        level_5_transition = True
        player.rect.x = 325
        player.rect.y = 350
        player.health = 3
        playing = False
        key_pressed = 14
        screen.fill(BLACK)
        screen.blit(level_5, [280, 180])
        screen.blit(press_spacebar, [5, 380])
    elif level == 5 and enemies_left == 0:
        win = True
        level = 6
        victory.play(0)

    # Gameplay
    if not level_2_transition and not level_3_transition and not level_4_transition and not level_5_transition:
        all_sprite_group.draw(screen)

    if playing:
        screen.blit(enemies_left_text, [320, 10])
        pygame.draw.rect(screen, (180, 180, 255), [8, 8, 104, 24])
        pygame.draw.rect(screen, LIGHT_BLUE, [10, 10, 100 - (player.cooldown * 2), 20])
        if player.cooldown >= 1:
            screen.blit(charging, [13, 14])
        else:
            screen.blit(dash, [13, 14])
        if player.health <= 0:
            player.health = 0
        pygame.draw.rect(screen, (255, 180, 180), [8, 34, 104, 24])
        pygame.draw.rect(screen, (255, 100, 100), [10, 36, int(player.health * 33.33) + 1, 20])
        if player.invulnerable:
            pygame.draw.rect(screen, (255, 255, 102), [8, 34, 104, 24])
            pygame.draw.rect(screen, (255, 212, 22), [10, 36, int(player.invulnerability / 2), 20])
            screen.blit(invincible, [13, 39])
        else:
            screen.blit(health_bar, [13, 39])

    # Intro
    if key_pressed == 0:
        screen.blit(title, [140, 110])
        screen.blit(press_spacebar, [5, 380])
    if key_pressed == 1:
        screen.blit(instructions, [40, 70])
        screen.blit(goodluck, [280, 92])
        screen.blit(press_spacebar, [5, 380])
    if key_pressed == 2:
        screen.fill(BLACK)
        screen.blit(level_1, [280, 180])
        screen.blit(press_spacebar, [5, 380])
    if key_pressed == 3:
        tutorial = True
        time = 0
        key_pressed = 4
        player.jump_cycle = False

    # Lose
    if death:
        playing = False
        screen.fill(BLACK)
        screen.blit(death_game_over, [170, 180])
        background_music.fadeout(1240)

    # Win
    if win:
        time += 1
        background_music.fadeout(1240)
        screen.fill(WHITE)
        screen.blit(win_game_over, [150, 180])
        draw_star(100, 170 + int(15 * math.sin(time / 10)))
        draw_star(568, 170 + int(15 * math.sin(time / 10)))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
