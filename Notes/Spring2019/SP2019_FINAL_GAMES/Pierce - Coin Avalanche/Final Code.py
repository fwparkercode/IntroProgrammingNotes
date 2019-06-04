"""
Pygame Base Template
Spring 2019
by Pierce Geene
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()    #starts pygame (Vroom!)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.display.set_caption("Pierce's Final Game")

# Condition for the game loop
done = False

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()  # grabs a rect based on image
        self.health = 5
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.top > screen_height:
            self.rect.bottom = 0



class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.image.load("rock.png")
        self.rect = self.image.get_rect()  # grabs a rect based on image
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(-screen_height, 0)
        self.change_x = random.randrange(-1, 2)
        self.change_y = random.randrange(1, 3)

    def update(self):
        self.rect.x += self.change_x
        if self.rect.right > screen_width or self.rect.left < 0:
            self.change_x *= -1

        self.rect.y += self.change_y
        if self.rect.top > screen_height:
            self.rect.bottom = 0



class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(0, 500)
        self.change_x = random.randrange(-1, 2)
        self.change_y = random.randrange(-1, 2)
    def update(self):
        self.rect.x += self.change_x
        if self.rect.right > screen_width or self.rect.left < 0:
            self.change_x *= -1




player = Player(200, 400)



all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(player)
rock_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

for i in range(7):
    new_block = Block(BLACK)
    all_sprites_group.add(new_block)
    rock_group.add(new_block)

for i in range(10):
    coin = Coin()
    all_sprites_group.add(coin)
    coin_group.add(coin)

score = 0
level = 1

# FONTS/TEXT

score_font = pygame.font.SysFont("Calibri", 30, True, True)
health_font = pygame.font.SysFont("Calibri", 30, True, True)
font = pygame.font.SysFont("Calibri", 50, True, False)
level_font = pygame.font.SysFont("Calibri", 30, True, True)
font2 = pygame.font.SysFont("Calibri", 40, True, False)
font3 = pygame.font.SysFont("Calibri", 50, True, False)

text = font.render("Press Space To Start", True, BLACK)
text2 = font2.render("You Lose!", True, BLACK)
text3 = font3.render("You Win!", True, BLACK)
coin_noise = pygame.mixer.Sound("Coin01.wav")
damage_noise = pygame.mixer.Sound("pain1.wav")


# FUNCTIONS
def cut_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True




        screen.fill(GREEN)
        screen.blit(text, [screen_width // 2 - text.get_rect().width // 2, screen_height // 2 - text.get_rect().height // 2])
        pygame.display.flip()
        clock.tick(60)

def cut_screen2():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(RED)
        screen.blit(text2, [screen_width // 2 - text2.get_rect().width // 2, screen_height // 2 - text2.get_rect().height // 2])
        pygame.display.flip()
        clock.tick(60)

def cut_screen3():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


        screen.fill(GREEN)
        screen.blit(text3, [screen_width // 2 - text3.get_rect().width // 2, screen_height // 2 - text3.get_rect().height // 2])
        pygame.display.flip()
        clock.tick(60)

cut_screen()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                    player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -3)
        if player.health <= 0:
            done = True
            cut_screen2()
        if score >= 75:
            done = True
            cut_screen3()





    # --- Game logic should go here
    all_sprites_group.update()

    hit_list = pygame.sprite.spritecollide(player, rock_group, True)
    for rock in hit_list:
        damage_noise.play()
        player.health -= 1

    count = 0
    for coin in coin_group:
        count += 1

    if count <= 0:
        # go to next level
        level += 1
        rock_group.empty()
        all_sprites_group.empty()
        all_sprites_group.add(player)
        for i in range(5 * level):
            new_block = Block(BLACK)
            all_sprites_group.add(new_block)
            rock_group.add(new_block)
        for i in range(10 * level):
            new_coin = Coin()
            all_sprites_group.add(new_coin)
            coin_group.add(new_coin)



    hit_list = pygame.sprite.spritecollide(player, coin_group, True)
    for coin in hit_list:
        coin_noise.play()
        score += 1





    # --- Drawing code should go here
    screen.fill(WHITE)

    all_sprites_group.draw(screen)

    text = score_font.render("Score:" + str(score), True, BLACK)
    screen.blit(text, [30, 30])

    health_text = health_font.render("Health:" + str(player.health), True, BLACK)
    screen.blit(health_text, [150, 30])

    level_text = level_font.render("Level:" + str(level), True, BLACK)
    screen.blit(level_text, [280, 30])

    pygame.display.flip()# Update the screen
    clock.tick(60)# --- Limit to 60 frames per second

# Close the window and quit.
pygame.quit()
