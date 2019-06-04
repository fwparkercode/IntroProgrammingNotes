
"""
 Pygame base template
Spring 2019
by Leilani Kulkarni

Hi! In this game, tackle zombies in the zombie apocalypse as you try to get back to your home. Along the way, encounter
power-ups in the shape of stars to help you turn into a bat, power-downs in the shape of red X's that will fire
special zombies, and apples, which you must collect enough of so you don't die of starvation. After defeating all the
zombies, you must make it to the very right hand side of the screen to advance to the next level (there are 5). Each
have more zombies that move faster, so be prepared and good luck!
"""

import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
can_shoot = True

screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("leilani's epic zombie attack")

done = False

clock = pygame.time.Clock()

# Text resources
my_font = pygame.font.SysFont('Calibri', 25, True, False)

# Image resources
player_image = pygame.image.load("person.png")
zombie_image = pygame.image.load("zombie_image.bmp")
power_up_image = pygame.image.load("power_up.bmp")
power_down_image = pygame.image.load("power_down.png")
bat_image = pygame.image.load("bat_image.bmp")
gravestone1_image = pygame.image.load("gravestone1_image.bmp")
gravestone2_image = pygame.image.load("gravestone2_image.bmp")
apple_image = pygame.image.load("apple_image.bmp")
power_down_zombie = pygame.image.load("special_zombie2.bmp")
# images for different sprites in the game

background_image1 = pygame.image.load("city_background.bmp")
background_image2 = pygame.image.load("background_image2.bmp")
background_image3 = pygame.image.load("background_image6.bmp")
background_image4 = pygame.image.load("background_image8.bmp")
background_image5 = pygame.image.load("background_image5.bmp")
# different backgrounds that change with each level

background_image_list = []
background_image_list.append(background_image1)
background_image_list.append(background_image2)
background_image_list.append(background_image3)
background_image_list.append(background_image4)
background_image_list.append(background_image5)
# list created for different backgrounds so they can switch with each level

# Sound resources
background_music = pygame.mixer.Sound("background_music.wav")  # background music
zombie_kill_sound = pygame.mixer.Sound("zombie_attack_sound.wav")  # sound that plays when zombies are killed
player_scream_sound = pygame.mixer.Sound("player_scream.wav")  # sound when a special zombie falls onto the player

background_music.play(-1)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = key_x
        self.rect.y = key_y
        self.change_x = 0
        self.change_y = 0

    def update(self):
        if self.rect.right > screen_width or self.rect.left < 0:
            self.change_x *= -1

        self.rect.x += self.change_x
        self.rect.y += self.change_y
# code that creates a class for the player


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = zombie_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - 100, screen_width)
        self.rect.y = (screen_height / 2) - 10
        self.change_x = random.randrange(-3, -1)
        self.change_y = 0
# code that creates a class for the zombies who are the enemies

    def update(self):
        self.rect.x += self.change_x  # help was provided here
# function that makes the zombies move


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([8, 3])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
# code that creates a class for the bullets fired at the zombies

    def update(self):
        self.rect.x += 15
        if self.rect.right > screen_width:
            self.kill()
# function that moves the bullet and creates restraints for it


class Bat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.form = Player()
        self.image = power_up_image
        self.rect = self.image.get_rect()
        self.rect.x = key_x
        self.rect.y = key_y
        self.change_x = 0
        self.change_y = 0
# code that creates a class for the bat (which a player turns into when they hit a power-up)

    def change_form(self):
        if player.image == player_image:
            player.image = bat_image

        else:
            self.image = player_image
# code that changes a player to a bat and vice versa

    def update(self):
        if self.rect.right > screen_width or self.rect.left < 0:
            self.change_x *= -1

        self.rect.x += self.change_x
        self.rect.y += self.change_y
# function that moves the bat


class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = power_up_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, screen_width)
        self.rect.y = 100
        self.change_x = 0
        self.change_y = 0
# code that creates a class for the power-ups (shaped like stars)

    def update(self):
        self.change_x = 0
        self.change_y = 0
# function that makes the power-ups move (or in this case stay stable)


class PowerDown(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = power_down_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, screen_width - 100)
        self.rect.y = (screen_height / 2) - 10
        self.change_x = 0
        self.change_y = 0
# code that creates a class for the power-downs (shaped like red X's)

    def update(self):
        self.change_x = 0
        self.change_y = 0
# function that moves the power-downs (or in this case keeps them stable)


class PowerBullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 8])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
# code that creates a class for the power bullets which you can fire at power-ups to become a bat or at a special
# zombie to kill it

    def update(self):
        self.rect.y -= 15
        if self.rect.top > screen_height:  # help was provided with this line
            self.kill()
# function that moves the power bullet and creates restraints for it


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = apple_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, screen_width)
        self.rect.y = (screen_height / 2) + 10
        self.change_x = 0
        self.change_y = 0
# code that creates a class for the apples which the player has to collect along the way

    def update(self):
        self.change_x = 0
        self.change_y = 0
# function that keeps the apples stable


class SpecialZombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = power_down_zombie
        self.rect = self.image.get_rect()
# code that creates a class for the special zombie, which appears when a player hits a power-down

    def update(self):
        self.rect.y += 7
        if self.rect.bottom > screen_height:
            self.kill()
# function that moves the special zombie


key_x = 0
key_y = (screen_height / 2) - 20  # variables for the starting position the player is put in
change_x = 0
change_y = 0  # default movement for any sprite
count = 0  # default enemy count
level = 1  # defaults level at level 1
apple_score = 0  # defaults amount of apples to 0
bullets_used = 0  # defaults the bullets used to 0
power_up_count = 0  # defaults the amount of stored power-ups to 0
lives = 10  # default number of lives
score = 0  # default score

zombie = Enemy()
player = Player()
bullet = Bullet()
bat = Bat()
power_up = PowerUp()
power_down = PowerDown()
power_bullet = PowerBullet()
apple = Apple()
special_zombie = SpecialZombie()
# creates variable names for each of the classes

enemy_group = pygame.sprite.Group()
all_sprite_groups = pygame.sprite.Group()
all_sprite_groups.add(player)
bullet_group = pygame.sprite.Group()
power_up_group = pygame.sprite.Group()
power_down_group = pygame.sprite.Group()
power_bullet_group = pygame.sprite.Group()
apple_group = pygame.sprite.Group()
special_zombie_group = pygame.sprite.Group()
# creates a group for each of the classes


for i in range(5):
    new_block = Enemy()
    all_sprite_groups.add(new_block)
    enemy_group.add(new_block)
# creates 5 zombies

new_power_up = PowerUp()
all_sprite_groups.add(new_power_up)
power_up_group.add(new_power_up)
# creates a random power-up

if random.randrange(0, 3) == 2:
    new_power_down = PowerDown()
    all_sprite_groups.add(new_power_down)
    power_down_group.add(new_power_down)
# creates a random power-down

for i in range(random.randrange(6, 10)):
    new_apple = Apple()
    all_sprite_groups.add(new_apple)
    apple_group.add(new_apple)
# creates a random amount of 6 to 10 apples


def draw_grass():
    pygame.draw.rect(screen, GREEN, [0, (screen_height / 2) + 50, screen_width, screen_height / 2])
# function that draws grass on roughly the bottom half of the screen


def cut_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(GREEN)

        my_text1 = my_font.render("It was a regular day in A Town...until in the evening, people started seeing"
                                  , True, BLACK)
        screen.blit(my_text1, [10, 40])

        my_text21 = my_font.render("green figures roaming the streets. A zombie apocalypse has broke out!!", True, BLACK)
        screen.blit(my_text21, [10, 70])

        my_text3 = my_font.render("You need to get to your house safely, without getting eaten by zombies.", True,
                                  BLACK)
        screen.blit(my_text3, [10, 100])

        my_text4 = my_font.render("You have no faith that you can defeat the zombies, but you have an", True, BLACK)
        screen.blit(my_text4, [10, 130])

        my_text5 = my_font.render("advantage: you can turn into a bat, which zombies don't notice.", True, BLACK)
        screen.blit(my_text5, [10, 160])

        my_text6 = my_font.render("Be careful though - you can only turn into a bat a few times throughout", True,
                                  BLACK)
        screen.blit(my_text6, [10, 190])

        my_text7 = my_font.render("your journey. Do you think you can do it??", True, BLACK)
        screen.blit(my_text7, [10, 210])

        my_text8 = my_font.render("Press the down key to learn the rules of the game.", True, RED)
        screen.blit(my_text8, [10, 240])

        my_text26 = my_font.render("Also, remember to make it the right hand side of the", True, BLACK)
        screen.blit(my_text26, [10, 270])

        my_text27 = my_font.render("screen to advance to the next level!", True, BLACK)
        screen.blit(my_text27, [10, 300])

        my_text9 = my_font.render("Hint: capture as many power-ups as you can, and avoid power-downs!", True, BLACK)
        screen.blit(my_text9, [10, 400])


        pygame.display.flip()
        clock.tick(60)
# function that appears first in the game and gives the player a background story on what's happening


def cut_screen2():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(GREEN)

        my_text1 = my_font.render("So, here's how to use the game:", True, BLACK)
        screen.blit(my_text1, [10, 40])

        my_text14 = my_font.render("Press the right and left buttons to move the player.", True, BLACK)
        screen.blit(my_text14, [10, 70])

        my_text15 = my_font.render("", True, BLACK)
        screen.blit(my_text15, [10, 100])

        my_text16 = my_font.render("Use the up arrow to fire special bullets to catch power-ups,", True, BLACK)
        screen.blit(my_text16, [10, 130])

        my_text17 = my_font.render("which you can then use to become a bat.", True, BLACK)
        screen.blit(my_text17, [10, 160])

        my_text23 = my_font.render("You can also fire special bullets at zombies triggered when", True, BLACK)
        screen.blit(my_text23, [10, 190])

        my_text24 = my_font.render("you hit a power-down.", True, BLACK)
        screen.blit(my_text24, [10, 210])

        my_text18 = my_font.render("Use the mouse button to fire regular bullets to kill zombies.", True, BLACK)
        screen.blit(my_text18, [10, 230])

        my_text19 = my_font.render("Be careful though, you only have 20 to fire.", True, BLACK)
        screen.blit(my_text19, [10, 260])

        my_text20 = my_font.render("Press the down key to get started!", True, RED)
        screen.blit(my_text20, [10, 290])

        pygame.display.flip()
        clock.tick(60)
# function that appears right after the background story function, which tells the player what to press to do what


def cut_screen3():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(GREEN)

        my_text10 = my_font.render("Onto the next level! Can you defeat the zombies and collect", True, BLACK)
        screen.blit(my_text10, [10, 200])

        my_text25 = my_font.render("all the apples??", True, BLACK)
        screen.blit(my_text25, [10, 230])

        pygame.display.flip()
        clock.tick(60)
# function that makes a screen appearing between each of the levels, serving as a marker between levels


def game_over_lost():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(GREEN)

        my_text10 = my_font.render("game over - sorry, you lost - the zombies got the best of you :((((", True, RED)
        screen.blit(my_text10, [10, 200])

        my_text12 = my_font.render("press the down-key to exit the game.", True, BLACK)
        screen.blit(my_text12, [10, 230])

        pygame.display.flip()
        clock.tick(60)
# function that makes a screen appearing after the player has lost the game


def game_over_won():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.K_DOWN:
                done = True

        screen.fill(GREEN)

        my_text10 = my_font.render("game over - congrats, you made it safely to your home :)))).", True, RED)
        screen.blit(my_text10, [10, 200])

        my_text12 = my_font.render("press the down-key to exit the game.", True, BLACK)
        screen.blit(my_text12, [10, 230])

        pygame.display.flip()
        clock.tick(60)
# function that makes a screen appearing after the player has won the game


def game_over_apples_lost():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.K_DOWN:
                done = True

        screen.fill(GREEN)

        my_text10 = my_font.render("oh no! you didn't collect enough apples, so you die", True, RED)
        screen.blit(my_text10, [10, 200])

        my_text17 = my_font.render("from starvation. good job though!", True, RED)
        screen.blit(my_text17, [10, 230])

        my_text12 = my_font.render("press the down-key to exit the game.", True, BLACK)
        screen.blit(my_text12, [10, 260])

        pygame.display.flip()
        clock.tick(60)
# screen that plays if you didn't collect enough apples by the end of the game


def ask_power_up():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
            if event.type == pygame.K_2:
                done = True

        screen.fill(GREEN)

        my_text10 = my_font.render("you have two options: would you like to store your power-up?", True, BLACK)
        screen.blit(my_text10, [10, 200])

        my_text12 = my_font.render("If you want to use it now, press the down key, then press", True, BLACK)
        screen.blit(my_text12, [10, 230])

        my_text15 = my_font.render("key 3. If you want to save it for later, press the 2 key. ", True, BLACK)
        screen.blit(my_text15, [10, 260])

        my_text16 = my_font.render("If you want to use your saved power-up at any time in the game,", True, BLACK)
        screen.blit(my_text16, [10, 320])

        my_text17 = my_font.render("press key 3.", True, BLACK)
        screen.blit(my_text17, [10, 350])

        pygame.display.flip()
        clock.tick(60)
# screen that plays when a power bullet hits a power-up and asks the player whether they want to use it now or later


cut_screen()
cut_screen2()
# calls background story screen and instruction screen

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:  # if the mouse button is pressed, a zombie bullet is fired
            if can_shoot == True:
                new_bullet = Bullet()
                new_bullet.rect.center = player.rect.center
                bullet_group.add(new_bullet)
                all_sprite_groups.add(new_bullet)  # help was provided with this line
                bullets_used += 1
            if can_shoot == False:
                print("out of bullets")
            # creates a condition that makes a player able to shoot bullets until the condition is false
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.change_x = 7
        # if a player presses the right key, they move right by 7
            elif event.key == pygame.K_LEFT:
                player.change_x = -7
            # if a player presses the left key, they move left by 7
            elif event.key == pygame.K_UP:
                new_power_bullet = PowerBullet()
                new_power_bullet.rect.center = player.rect.center
                power_bullet_group.add(new_power_bullet)
                all_sprite_groups.add(new_power_bullet)
            # if the up key is pressed, a power bullet is fired up at either a power-up or a special zombie
            elif event.key == pygame.K_2:
                power_up_count += 1
                player.image = player_image
            elif event.key == pygame.K_3:
                if power_up_count >= 1:
                    bat.change_form()
                    power_up_count -= 1
                elif power_up_count <= 0:
                    player.image = player_image
            # keys to press if you want to either use a power up now, want to save it for later, or use it later
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.change_x = 0
            elif event.key == pygame.K_LEFT:
                player.change_x = 0
            # if the right or left key comes up, the player stops moving

    # --- Game logic should go here

    all_sprite_groups.update()  # updates the entire group of sprites

    if bullets_used < 20:
        can_shoot = True
    if bullets_used > 20:
        can_shoot = False
        print("out of bullets")
    # condition that has a player not be allowed to fire any more bullets if they have fired more than 20

    bullet_group.update()
    enemy_group.update()
    power_up_group.update()
    power_down_group.update()
    apple_group.update()
    power_bullet_group.update()
    special_zombie_group.update()
# updates all independent sprite groups so they move

    if player.image == player_image:
        hit_list = pygame.sprite.spritecollide(player, enemy_group, True)
        for hit in hit_list:
            lives -= 1
# if the player collides with the enemy group, the player loses a life (that is, if they aren't in bat form)

    if player.image == player_image:
        hit_apple = pygame.sprite.spritecollide(player, apple_group, True)
        for hit in hit_apple:
            apple.kill()
            apple_score += 1
# if a player collides with an apple, the apple disappears and their amount of apples goes up by 1

    if player.image == player_image:
        hit_power_down = pygame.sprite.spritecollide(player, power_down_group, True)
        for hit in hit_power_down:
            power_down.kill()
            new_special_zombie = SpecialZombie()
            new_special_zombie.rect.x = player.rect.x
            new_special_zombie.rect.y = 0
            all_sprite_groups.add(new_special_zombie)
            special_zombie_group.add(new_special_zombie)
# if the player collides with a power-down, the power-down disappears, and a special zombies comes down from the sky
# (that is, if they aren't in bat form)

    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, True)
        for hit in hit_list:
            bullet.kill()
            zombie_kill_sound.play()
            score += 1
# if the zombie bullet collides with a zombie, the bullet and zombie disappear, 

    for power_bullet in power_bullet_group:
        hit_power_up = pygame.sprite.spritecollide(power_bullet, power_up_group, True)
        for hit in hit_power_up:
            power_bullet.kill()
            ask_power_up()
            if player.image == player_image:
                power_up_count += 1
# code that causes the ask_power_up() screen to play when a player hits a power-up, and adds 1 to the power up count
# if they didn't want to use it right then

    for power_bullet in power_bullet_group:
        hit_zombie = pygame.sprite.spritecollide(power_bullet, special_zombie_group, True)
        for hit in hit_zombie:
            power_bullet.kill()
            special_zombie.kill()
# code that causes the special zombie to be killed if the player fires a power bullet at it

    hit_player = pygame.sprite.spritecollide(player, special_zombie_group, True)
    for hit in hit_player:
        lives -= 3
        player_scream_sound.play()
# code that causes the player to lose 3 lives if a power-down zombie falls on it

    for enemy in enemy_group:
        count += 1
# adds to the zombie count for each zombie there is

    if player.rect.x >= screen_width - 5 and player.image == bat_image:
        count = 0
# code that causes the zombie count to equal 0 if the player is at the right hand side of the screen

    if lives <= 0:
        game_over_lost()
        done = True
    # if the player has 0 lives or less, the game over screen appears and then the game ends

    if player.rect.x >= screen_width - 50:  # if the player is at the very right side of the screen, you level up
        level += 1
        cut_screen3()  # projects function which is a level marker
        bullet_group.empty()
        all_sprite_groups.empty()
        enemy_group.empty()
        power_up_group.empty()
        power_down_group.empty()
        apple_group.empty()  # empties all sprite groups
        player.rect.x = 0
        player.change_x = 0  # resets player position, speed, and bullets used
        player.image = player_image  # resets player form to the human one
        all_sprite_groups.add(player)
        for i in range(5 * level):
            new_block = Enemy()
            new_block.change_x *= (level / 3)
            all_sprite_groups.add(new_block)  # creates new zombies and makes them move faster
            enemy_group.add(new_block)
            if random.randrange(0, 10) == 2:
                new_power_up = PowerUp()
                all_sprite_groups.add(new_power_up)
                power_up_group.add(new_power_up)  # adds a power-up at random
            if random.randrange(1, 10) == 2:
                new_power_down = PowerDown()
                all_sprite_groups.add(new_power_down)
                power_down_group.add(new_power_down)  # adds a power-down at random
            new_apple = Apple()
            all_sprite_groups.add(new_apple)
            apple_group.add(new_apple)  # creates new apples

        if level >= 6 and apple_score <= 40:
            game_over_apples_lost()
            done = True
# causes the game_over_apples_lost() screen to play if the player has 40 apples or less but has finished the game

        if level >= 6 and apple_score > 40:
            game_over_won()
            done = True
# causes the player to win if they have finished the game and have more than 40 apples



    # --- Drawing code should go here
    screen.fill(WHITE)
    screen.blit(background_image_list[level - 1], [0, 0])  # blits background image (help was provided here)

    all_sprite_groups.draw(screen)  # draws all sprite groups

    draw_grass()  # draws the grass

    screen.blit(gravestone1_image, [500, screen_height / 2 + 30])
    screen.blit(gravestone2_image, [90, (screen_height / 2) + 20])
    screen.blit(gravestone1_image, [130, (screen_height / 2) + 25])
    screen.blit(gravestone2_image, [600, (screen_height / 2) + 40])
    screen.blit(gravestone1_image, [210, (screen_height / 2) + 30])
    screen.blit(gravestone2_image, [270, (screen_height / 2) + 50])
    screen.blit(gravestone1_image, [320, (screen_height / 2) + 80])
    screen.blit(gravestone2_image, [20, (screen_height / 2) + 110])
    screen.blit(gravestone2_image, [470 + 10, (screen_height + 100)])  # projects different gravestones for decoration

    my_text2 = my_font.render("Lives: " + str(lives), True, BLACK)
    screen.blit(my_text2, [40, 40])  # projects your score to see how many lives you have left

    my_text11 = my_font.render("Apples: " + str(apple_score), True, BLACK)
    screen.blit(my_text11, [40, 60])  # projects the score to see how many apples you've gotten

    my_text13 = my_font.render("Bullets Used: " + str(bullets_used), True, BLACK)
    screen.blit(my_text13, [40, 80])  # projects the score to see how many bullets you've used

    my_text22 = my_font.render("Power-Ups Stored: " + str(power_up_count), True, BLACK)
    screen.blit(my_text22, [40, 100])  # projects the score to see how many power-ups you have stored

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# help was provided 4 times

