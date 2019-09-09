"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (200, 0, 200)
YELLOW = (255, 255, 0)
time = 0
pygame.init()

# Set the width and height of the screen [width, height]
size = (1280, 720)
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode(size)
background_image = pygame.image.load("Cloud.jpg")
pygame.display.set_caption("My Final Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
player_image = pygame.image.load("sage_bitmoji.png")
background_music = pygame.mixer.Sound("music.wav")
background_music.set_volume(0.5)
background_music.play(-1)

fireball_sound = pygame.mixer.Sound("fireball.wav")
ding_sound = pygame.mixer.Sound("ding.wav")
level_sound = pygame.mixer.Sound("level.wav")


class Angel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("angel_bitmoji.png")
        self.rect = self.image.get_rect() # grabs the rect based on the current image
        self.rect.x = random.randrange(screen_width // 15, screen_width - self.rect.width)
        self.rect.y = random.randrange(screen_height - self.rect.height)
        self.change_y = random.randrange(5, 10)

    def update(self):
        self.rect.y += self.change_y
        if self.rect.bottom >= screen_height:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sage_bitmoji.png")
        self.rect = self.image.get_rect() # grabs the rect based on the current image
        self.rect.x = random.randrange(screen_width // 15, screen_width - self.rect.width)
        self.rect.y = random.randrange(screen_height - self.rect.height)
        self.change_y = random.randrange(5, 10)

    def update(self):
        pass
        #self.rect.y += self.change_y
        #if self.rect.bottom >= screen_height:
            #self.kill()


class Fire(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("fire_bitmoji.png")
            self.rect = self.image.get_rect()  # grabs the rect based on the current image
            self.rect.x = random.randrange(screen_width // 15, screen_width - self.rect.width)
            self.rect.y = random.randrange(screen_height - self.rect.height)
            self.change_y = random.randrange(5, 10)

        def update(self):
            self.rect.y += self.change_y
            if self.rect.top >= screen_height:
                self.kill()


# Make groups to contain our sprites
all_sprites_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
good_group = pygame.sprite.Group()

# Make all my sprites
player = Player()
#player.image.fill(GREEN)
#player.rect.left = 0
player.rect.bottom = screen_height
all_sprites_group.add(player)


for i in range(50):
    new_coin = Angel()
    new_coin2 = Fire()
    new_coin.rect.y = random.randrange(-screen_height * new_coin.change_y, 0)
    all_sprites_group.add(new_coin)
    good_group.add(new_coin)
    new_coin2.rect.y = random.randrange(-screen_height * new_coin2.change_y, 0)
    all_sprites_group.add(new_coin2)
    enemy_group.add(new_coin2)
pygame.mouse.set_visible(True)


score = 0
level = 1
lives = 3


my_font = pygame.font.SysFont('Calibri', 30, True, False)
my_font2 = pygame.font.SysFont('Calibri', 50, True, False)


def cut_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        pygame.display.flip()
        clock.tick(80)


cut_screen()


def game_over():
    done = False
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(RED)
        my_text = my_font2.render("GAME OVER!", True, BLACK)
        screen.blit(my_text, [screen_height / 2, 300])
        my_text = my_font2.render("press the space bar to start over", True, BLACK)
        screen.blit(my_text, [1, 400])

        pygame.display.flip()
        clock.tick(80)


def game_start():
    done = False
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(WHITE)
        my_text = my_font2.render("Click any key to start!", True, BLACK)
        screen.blit(my_text, [350, 100])
        my_text = my_font.render("Collect as many angel Ava's as you can! Avoid the fire Ava's.", True, BLACK)
        screen.blit(my_text, [300, 300])
        my_text = my_font.render(" If you collect a fire Ava, you will loose a life!", True, BLACK)
        screen.blit(my_text, [350, 400])


        pygame.display.flip()
        clock.tick(80)

game_start()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    player.rect.centerx = pygame.mouse.get_pos()[0]

    all_sprites_group.update()

    hit_list = pygame.sprite.spritecollide(player, good_group, True)
    for hit in hit_list:
        score += 1
        ding_sound.play()
        print(score)

    live_list = pygame.sprite.spritecollide(player, enemy_group, True)
    for live in live_list:
        lives -= 1
        fireball_sound.play()

    # Check for next level

    if (len(enemy_group)) == 0:
        level += 1
        level_sound.play()

        for i in range(level * 10 + 70):
            new_coin = Angel()
            new_coin2 = Fire()
            new_coin2.change_y *= level

            new_coin.rect.y = random.randrange(-screen_height * new_coin.change_y * 10, 0)
            all_sprites_group.add(new_coin)
            good_group.add(new_coin)
            new_coin2.rect.y = random.randrange(-screen_height * new_coin2.change_y * 10 , 0)
            all_sprites_group.add(new_coin2)
            enemy_group.add(new_coin2)

    if lives == 0:
        game_over()
        for i in range(70):
            new_coin = Angel()
            new_coin2 = Fire()
            new_coin.rect.y = random.randrange(-screen_height * new_coin.change_y * 10, 0)
            all_sprites_group.add(new_coin)
            good_group.add(new_coin)
            new_coin2.rect.y = random.randrange(-screen_height * new_coin2.change_y * 10, 0)
            all_sprites_group.add(new_coin2)
            enemy_group.add(new_coin2)
        pygame.mouse.set_visible(True)

        score = 0
        level = 1
        lives = 3

        # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])

    all_sprites_group.draw(screen)

    my_text = my_font.render("score: " + str(score), True, PINK)
    screen.blit(my_text, [30, 30])  # places rendered image on screen

    my_text = my_font.render("level: " + str(level), True, PINK)
    screen.blit(my_text, [30, 60])
    my_text = my_font.render("lives: " + str(lives), True, PINK)
    screen.blit(my_text, [30, 90])

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    all_sprites_group.draw(screen)
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(80)


# Close the window and quit.
pygame.quit()
