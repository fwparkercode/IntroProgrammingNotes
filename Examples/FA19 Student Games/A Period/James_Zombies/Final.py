"""
Pygame Final Game
James Leet - 2019

Zombie survival game. Player is placed in the center of the
screen and has to survive an onslaught of zombies.
They recieve a health pack every two levels. The aim of the
game is to survive for as long as possible.
"""

import pygame
import math
import random

pygame.init()  # initializes pygame

# Define variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
GRAY = (100, 100, 100)
PINK = (255, 200, 200)
ORANGE = (255, 150, 0)
MAROON = (100, 0, 0)
BROWN = (100, 50, 50)

level = 1 # defines the round / level
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 650
frames = 60
time_away = 10
done = False  # condition for my game loop
game_over = False
all_sprites_list = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
health_pack_sprite = pygame.sprite.Group()
# Set up
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Leet's Game")
clock = pygame.time.Clock()  # creates a clock object that manages updates
pygame.mouse.set_visible(False)
bg_image = pygame.image.load("background-1_0.png")
firing_sound = pygame.mixer.Sound("9_mm_gunshot-mike-koenig-123.wav")
death_zombie_sound = pygame.mixer.Sound("zomSound.ogg")
bg_sound = pygame.mixer.Sound("BG_Sound.ogg")
bg_sound.play(-1)
bg_sound.set_volume(.5)
health_pack_img = pygame.image.load("Heart.png")
sight = pygame.image.load("crosshair038.png")
font = pygame.font.SysFont('Calibri', 25, True, False)
end_font = pygame.font.SysFont('Calibri', 50, True, False)

sight_x = 0
sight_y = 0
zombies_left = 0
# Classes
def rot_center_player(image, old_rect, angle): # two different rotate functions to compinsate for the need to realign the original position
    # rotate image around center of rect
    center = image.get_rect().center
    rotated_image = pygame.transform.rotate(image, -70 - angle * 180 / math.pi)
    new_rect = rotated_image.get_rect(center = center)
    new_rect.center = old_rect.center
    return rotated_image, new_rect

def rot_center_zombie(image, old_rect, angle):
    # rotate image around center of rect
    center = image.get_rect().center
    rotated_image = pygame.transform.rotate(image, angle * 180 / math.pi)
    new_rect = rotated_image.get_rect(center = center)
    new_rect.center = old_rect.center
    return rotated_image, new_rect

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Set height, width
        self.original_image = pygame.image.load("hitman1_reload.png") # declare this to fufill the rotation function's imput
        self.rect = self.original_image.get_rect()
        self.rect.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
        self.pos = pygame.mouse.get_pos()
        self.angle = math.atan2(self.pos[0] - self.rect.centerx, self.pos[1] - self.rect.centery) #determines an angle for the player object's aim / rotation
        self.image, self.rect = rot_center_player(self.original_image, self.rect, self.angle)
        self.rect.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
        self.hit_points = 5


    def update(self):
        self.pos = pygame.mouse.get_pos()
        self.angle = math.atan2(self.pos[0] - self.rect.centerx, - self.pos[1] + self.rect.centery) - math.pi/2
        self.image, self.rect = rot_center_player(self.original_image, self.original_image.get_rect(), self.angle)
        self.rect.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]



class Zombie(pygame.sprite.Sprite):
    # -- Methods
    def __init__(self):
        super().__init__()
        # Set height, width
        self.original_image = pygame.image.load("zoimbie1_hold.png")  #declare this to fufill the rotation function's imput
        self.rect_Original_x = random.randrange(-SCREEN_WIDTH * .5, SCREEN_WIDTH * 1.5)
        self.rect_Original_y = random.randrange(-SCREEN_HEIGHT * .5, SCREEN_HEIGHT * 1.5)
        while (self.rect_Original_x >= 350 and self.rect_Original_x <= 450) and (self.rect_Original_y >= 275 and self.rect_Original_y <= 375):
            self.rect_Original_x = random.randrange(SCREEN_WIDTH - 50)
            self.rect_Original_y = random.randrange(SCREEN_HEIGHT - 50) # causes zombies to not spawn too close to player
        self.rect = self.original_image.get_rect()
        self.angle = math.atan2(-SCREEN_HEIGHT/2 + self.rect_Original_y, SCREEN_WIDTH/2 - self.rect_Original_x)
        print(self.angle)
        self.image, self.rect = rot_center_zombie(self.original_image, self.rect, self.angle)
        self.rect.x = self.rect_Original_x
        self.rect.y = self.rect_Original_y
        self.rect_x = 0 # created another variable to hold the total distance travelled by the zombie as a float to compensate for the
        self.rect_y = 0 # smaller numbers lost to rounding from pygame's rect coordinate system.
        self.time_to_reach = random.randrange(9, 16) - .3 * level # causes zombies to reach the player at different times while also decreasing the total time taken as rounds go up
        self.change_x = (SCREEN_WIDTH/2 - self.rect.x) / (frames * self.time_to_reach)
        self.change_y = (SCREEN_HEIGHT/2 - self.rect.y) / (frames * self.time_to_reach)# makes zombie run towards the center
        self.hit_points = 5

    def update(self):
        """ Find a new position for the player"""
        self.rect_x -= self.change_x
        self.rect_y -= self.change_y
        self.rect.x = self.rect_Original_x - self.rect_x
        self.rect.y = self.rect_Original_y - self.rect_y

class Health_Pack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = health_pack_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - 50)
        self.rect.y = random.randrange(SCREEN_HEIGHT - 50)
        while (self.rect.x >= 370 and self.rect.x <= 470) and (self.rect.y >= 275 and self.rect.y <= 375):
            self.rect.x = random.randrange(SCREEN_WIDTH - 50) # causes health pack to not spawn too close to player
            self.rect.y = random.randrange(SCREEN_HEIGHT - 50)


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([6,6])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center
        self.pos = pygame.mouse.get_pos()
        self.angle = math.atan2(self.pos[0] - self.rect.centerx, -self.pos[1] + self.rect.centery) + math.pi/2 # calculates angle to launch bullet at based on mouse position
        self.rect_Original_x, self.rect_Original_y = SCREEN_WIDTH/2 + math.cos(self.angle) * 15 + math.cos(self.angle - math.pi/2) * 10, SCREEN_HEIGHT/2 + math.sin(self.angle) * 15 + math.sin(self.angle - math.pi/2) * 10 # aligns the bullet with the center of the gun barrel
        self.rect.x = self.rect_Original_x
        self.rect.y = self.rect_Original_y
        self.rect_x = 0  # ones again created another variable to store the total distance travelled as a float
        self.rect_y = 0
        self.change_x, self.change_y = math.cos(self.angle) * 10, math.sin(self.angle) * 10

    def update(self):
        self.rect_x += self.change_x
        self.rect_y += self.change_y
        self.rect.centerx = self.rect_Original_x - self.rect_x
        self.rect.centery = self.rect_Original_y - self.rect_y

def Intro_Screen():
    done = False
    frame = 0
    shift = 5
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        frame += 1
        screen.fill(RED)
        font = pygame.font.SysFont('Franklin Gothic', 50, True, False)
        screen.blit(font.render("Press Button to Begin...", True, YELLOW), [200, SCREEN_HEIGHT - 150])
        if frame % 40 == 0:
            frame = 0 # makes the title molve
            shift = -shift
        screen.blit(font.render("Aim with the mouse", True, BLACK), [240, 220])
        screen.blit(font.render("Click to shoot", True, BLACK), [290, 270])
        screen.blit(font.render("Shoot hearts for additional hit points", True, BLACK), [70, 320])  # Creates title screen text
        screen.blit(font.render("DO NOT DIE", True, BLACK), [300, 370])
        screen.blit(font.render("APOCALYPSE SURVIVAL", True, YELLOW), [200 + shift, SCREEN_HEIGHT / 2 - 200 + shift])
        pygame.display.flip()
        clock.tick(60)


player = Player()
player_sprite.add(player)
all_sprites_list.add(player)

def Zombie_Spawn(lvl): # function to spawn each round of zombies
    zombie_left = 10 + 2 * lvl # number of zombies scale up as the game progresses
    for i in range(10 + 2 * lvl):
        zombie1 = Zombie()
        enemy_sprites.add(zombie1)
        all_sprites_list.add(zombie1)
    return (zombie_left)

zombies_left = Zombie_Spawn(level) # spawns first level
Intro_Screen() # activates intro screen
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    while game_over == False:
       # --- Main event loop (input from user mouse, keyboard, controller)
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                firing_sound.play(0)
                firing_sound.set_volume(1)
                new_bullet = Bullet() #fires bullet when mouse clocked pressed
                new_bullet.rect.center = player.rect.center
                all_sprites_list.add(new_bullet)
                bullet_sprites.add(new_bullet)

        # --- Game logic should go here

         sight_x, sight_y = pygame.mouse.get_pos()
         sight_x, sight_y = sight_x, sight_y

         for zombie in enemy_sprites: # checks for zombies reaching the player
            death = pygame.sprite.collide_rect(zombie, player)
            if death == True:
                player.hit_points -= 1 # lowers health
                zombies_left -= 1 # keeps track of rounds
                zombie.kill()

         for bullet in bullet_sprites: # checks for bullets and enemies hitting
            for enemy in enemy_sprites:
                kill_enemy_hit = pygame.sprite.collide_rect(bullet, enemy)
                if kill_enemy_hit == True:
                    zombies_left -= 1 # keeps track of rounds
                    death_zombie_sound.play(0)
                    death_zombie_sound.set_volume(1) # makes zombies growl
                    bullet.kill()
                    enemy.kill()

         for bullet in bullet_sprites: # checks for bullets and health packs hitting
            for pack in health_pack_sprite:
                kill_enemy_hit = pygame.sprite.collide_rect(bullet, pack)
                if kill_enemy_hit == True:
                    player.hit_points += 2 # heals you
                    bullet.kill()
                    pack.kill()

         if player.hit_points == 0:
            game_over = True # ends the game if health is emptied
         if zombies_left == 0:
             level += 1 # starts the next round once no zombies are left
             zombies_left = Zombie_Spawn(level)
             if level % 2 == 0:
                 pack_spawn = Health_Pack() # spawns a health pack every 2 levels
                 health_pack_sprite.add(pack_spawn)
                 all_sprites_list.add((pack_spawn))

         # --- Drawing code goes here
         screen.blit(bg_image, [0, 0])
         bullet_sprites.draw(screen)
         player_sprite.draw(screen) #draws sprites to screen
         enemy_sprites.draw(screen)
         health_pack_sprite.draw(screen)
         all_sprites_list.update()
         screen.blit(sight, [sight_x - 32 + math.cos(-player.angle -70 / 180 * math.pi) * 12, sight_y - 32 - math.sin(-player.angle -70 / 180 * math.pi) * 12])  # aligns sight with bullet path
         screen.blit(font.render("Health: " + str(player.hit_points), True, RED), [SCREEN_WIDTH - 120, 30])
         screen.blit(font.render("Round " + str(level), True, GREEN), [30, 30]) # creates score keepers

         pygame.display.flip()  # updates the screen
         clock.tick(60)
    screen.blit(end_font.render("Game Over...", True, RED), [SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 25])
    pygame.display.flip()  # updates the screen
      # frames per second

pygame.quit()  # Close the window and quit.