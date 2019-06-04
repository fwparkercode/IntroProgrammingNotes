'''''
Track Dash
Spring 2019
By Star Rothkopf

The below code is to display a functional game called 'Track Dash', to be played using the left and right arrow keys.

The objective is to run as far on the track as possible before losing all of three lives. The player loses lives by 
running into obstacles on the track. The player may gain lives by running into a power-up icon.
'''''

import pygame
import random

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
TRACK_COLOR = (210, 100, 75)
LT_TRACK_COLOR = (240, 130, 105)

pygame.init() # starts pygame (Vrooom!)

# Set the width and height of the screen [width, height]
screen_width = 500
screen_height = 700
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
level = 0


pygame.display.set_caption("Track Dash - Star Rothkopf")

# Loop until the user clicks the close button
done = False # condition for the game loop

clock = pygame.time.Clock()

# CLASSES


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(random.choice(["log.png","mud.png","bush.png"]))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice([75, 245, 420])
        self.rect.centery = 0 - self.rect.height
        self.change_y = 0

    def update(self):
        self.change_y = 5 + level
        self.rect.y += self.change_y


class PowerUp(Obstacle):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("refill_powerup.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice([75, 245, 420])
        self.rect.y = -75


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image_list = []
        self.image_list.append(pygame.image.load("runningman_left.png"))
        self.image_list.append(pygame.image.load("runningman_right.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = 245
        self.rect.centery = 500
        self.change_x = 0
        self.frame = 0

    def update(self):
        player.rect.x += player.change_x
        self.frame += 1
        if self.frame > 10:
            self.image = self.image_list[0]
        elif self.frame <= 10:
            self.image = self.image_list[1]
        if self.frame >= 20:
            self.frame = 0


player = Player("runningman_right.png")

# GROUPS
all_sprites_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()

all_sprites_group.add(player)
player.rect.y = 520

# GLOBAL VARIABLES
score = 0
lives = 3
change_numbers = 0
frame = 0

# FONTS
score_font = pygame.font.SysFont("Calibri", 25, False, False)
numbers_font = pygame.font.SysFont("Calibri", 160, False, False)
title_font = pygame.font.SysFont("Calibri", 160, False, False)

# SOUNDS
background_music = pygame.mixer.Sound("bMusic.wav")
lane_switch_sound = pygame.mixer.Sound("swish.wav")
level_up_sound = pygame.mixer.Sound("levelup.wav")
hit_obstacle_sound = pygame.mixer.Sound("swish.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")

# SCREEN FUNCTIONS


def start_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
                background_music.play(-1)
        screen.fill(WHITE)
        # instruction text
        instructions = score_font.render("Welcome to", True, BLACK)
        title = title_font.render("TRACK", True, LT_TRACK_COLOR)
        title1 = title_font.render("DASH", True, TRACK_COLOR)
        pygame.draw.rect(screen, LT_TRACK_COLOR, [20, 360, 460, 320])
        pygame.draw.rect(screen, TRACK_COLOR, [20, 360, 460, 320], 5)
        instructions1 = score_font.render("Instructions: Use the arrow keys to move", True, BLACK)
        instructions2 = score_font.render("between lanes and avoid obstacles.", True, BLACK)
        instructions3 = score_font.render("Collect a", True, WHITE)
        instructions4 = score_font.render("to refill your lives.", True, WHITE)
        instructions5 = score_font.render("Press any button to start!", True, BLACK)
        screen.blit(title, [40, 140])
        screen.blit(title1, [90, 230])
        screen.blit(instructions, [200, 100])
        screen.blit(instructions1, [40, 380])
        screen.blit(instructions2, [40, 400])
        screen.blit(instructions3, [40, 480])
        screen.blit(instructions4, [230, 480])
        screen.blit(instructions5, [40, 555])
        powerup_image = pygame.image.load("refill_powerup.png")
        screen.blit(powerup_image, [130, 450])
        pygame.display.flip()
        clock.tick(60)


def end_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [10, 10, 480, 680])
        pygame.draw.rect(screen, YELLOW, [145, 345, 210, 70])

        game_over = title_font.render("GAME", True, YELLOW)
        game_over3 = title_font.render("GAME", True, BLACK)
        game_over2 = title_font.render("OVER", True, YELLOW)
        game_over4 = title_font.render("OVER", True, BLACK)
        score_gameover = score_font.render("You reached level " + str(level) + "!", True, BLACK)
        final_score = score_font.render("Your final score is: " + str(score), True, BLACK)
        screen.blit(final_score, [150, 350])
        screen.blit(score_gameover, [175, 375])
        screen.blit(game_over3, [75, 110])
        screen.blit(game_over, [75, 100])
        screen.blit(game_over4, [90, 200])
        screen.blit(game_over2, [90, 190])
        pygame.display.flip()
        clock.tick(60)


start_screen()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and player.rect.centerx == 245:
                player.rect.centerx = 420
            if event.key == pygame.K_LEFT and player.rect.centerx == 245:
                player.rect.centerx = 75
            if event.key == pygame.K_RIGHT and player.rect.centerx == 75:
                player.rect.centerx = 245
            if event.key == pygame.K_LEFT and player.rect.centerx == 420:
                player.rect.centerx = 245
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.change_x = 0

    # --- Game logic should go here
    score += 1
    frame += 1

    # INSTANCES ON INTERVALS, LEVELS
    level = frame // 1000 + 1

    if frame % 100 == 0:            # help from mr.lee
        pos = [75, 245, 420]
        obstacle_num = random.randrange(1,3)
        for i in range(obstacle_num):
            obstacle = Obstacle()
            all_sprites_group.add(obstacle)
            obstacle_group.add(obstacle)
            new_pos = pos.pop(random.randrange(len(pos)))
            obs_hit_list = pygame.sprite.spritecollide(obstacle, obstacle_group, False)
            if len(obs_hit_list) > 1:
                obs_hit_list = pygame.sprite.spritecollide(obstacle, obstacle_group, True)
                break

    if frame % 1000 == 0:
        powerup = PowerUp()
        all_sprites_group.add(powerup)
        powerup_group.add(powerup)

    # COLLISIONS
    all_sprites_group.update()
    hit_list = pygame.sprite.spritecollide(player, obstacle_group, True)
    for hit in hit_list:
        hit_obstacle_sound.play()
        lives -= 1
    if lives <= 0:
        game_over_sound.play()
        end_screen()
        done = True
    powerup_list = pygame.sprite.spritecollide(player, powerup_group, True)
    for powerup in powerup_list:
        level_up_sound.play()
        lives = 3

    # DRAWING CODE
    screen.fill(TRACK_COLOR)

    # lane lines
    pygame.draw.line(screen, LT_TRACK_COLOR, [155, 0], [155, screen_height], 10)
    pygame.draw.line(screen, LT_TRACK_COLOR, [332, 0], [332, screen_height], 10)
    pygame.draw.line(screen, LT_TRACK_COLOR, [0, 120 + change_numbers], [screen_width, 120 + change_numbers], 10)

    # lane numbers
    one = numbers_font.render("1", True, WHITE)
    two = numbers_font.render("2", True, WHITE)
    three = numbers_font.render("3", True, WHITE)
    screen.blit(one, [50, 200 + change_numbers])
    screen.blit(two, [215, 200 + change_numbers])
    screen.blit(three, [390, 200 + change_numbers])

    all_sprites_group.draw(screen)

    # lives/score text
    pygame.draw.rect(screen, YELLOW, [15, 15, 170, 25])
    pygame.draw.rect(screen, YELLOW, [395, 15, 85, 25])
    score_text = score_font.render("SCORE: " + str(score), True, BLACK)
    lives_text = score_font.render("LIVES: " + str(lives), True, BLACK)
    level_text = score_font.render("LEVEL: " + str(level), True, BLACK)
    screen.blit(score_text, [20, 20])
    screen.blit(lives_text, [15, 50])
    screen.blit(level_text, [400, 20])

    change_numbers += 5

    pygame.display.flip() # update the screen
    clock.tick(60)    # Limit to 60 frames per second


pygame.quit() # Close the window and quit (outside main loop)
