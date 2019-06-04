"""
Final Game

by emma manley 2019

This game is a platform game based off of the big idea of high school.
To play, you have to hit the space button to jump. You want to collect the A+s and avoid the Fs
You also can collect an iced coffee to regain half a life.

You use the space key to do most everything unless otherwise stated

I used the Pygame base template to start the code.

I sorted out the code with the comments so you can see my thought process

it's sorted out by:
resources
    within resources is sound, text, and image resources
    I also include variables and lists

classes
    this includes the player, coins, and platforms

functions
    this makes platforms, resets the groups and lists at levels, and has cut screens for levels and game over

program loop
    where it happens!


Where I got help:
Making the coins show up properly
Making the platforms keep duplicating and then also not ending up on top of each other
Other small fixes for errors
got some help for the error at the end of the game but I ultimately figured it out

"""
# always have to import pygame
import pygame
import random


# Define some colors  - all caps bc constants  (Red, green, blue)
# I don't really need any of these colors except black and blue2 but they were there when I made the template

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLUE2 = (200, 200, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 200, 255)
CYAN = (0, 255, 255)
ORANGE = (250, 150, 0)
PURPLE = (150, 50, 200)
GRAY = (127, 127, 127)
LAVENDER = (230, 175, 255)
PINK = (242, 164, 211)
pygame.init()  # do not put anything in pygame above this line

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Emma's Final Game")  # what it says at the top of the screen window

# Loop until the user clicks the close button.
done = False  # condition for game loop

""" 
RESOURCES

This is where I made all my players and coins and noises and everything
 
 """
# image resources
player_image = pygame.image.load("player.PNG")
a_image = pygame.image.load("A.PNG")
f_image = pygame.image.load("F.PNG")
coffee_image = pygame.image.load("coffee.PNG")
background_image = pygame.image.load("schoolpic.PNG")


# sound resources
# Background music
background_music = pygame.mixer.Sound("background.ogg")
background_music.set_volume(0.7)
background_music.play(-1)  # plays forever

# sound effects
jump_sound = pygame.mixer.Sound("zapThreeToneDown.ogg")  # this plays when the player jumps
coin_sound = pygame.mixer.Sound("threeTone2.ogg")
cheer_sound = pygame.mixer.Sound("cheer-copy.ogg")  # this plays at each new level
coffee_sound = pygame.mixer.Sound("zap1.ogg")
fail_sound = pygame.mixer.Sound("phaseJump2.ogg")

# font resources
my_font = pygame.font.SysFont("comicsansms", 25, True, False)
my_font2 = pygame.font.SysFont("comicsansms", 50, True, False)


# setting lists and variables

platform_list = []
level = 1
faster = False
speed = 4 + level
can_power_up = True
double_coin = 1
can_double = False
power_up_type = "none"
can_play = False
game_over = False


# Used to manage how fast the screen updates
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

'''
CLASSES
This is where I set up my various classes

I have a player class, a coin class that has child classes for "fail" coins and "coffee" coins
I also have a platform class. 

'''


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = player_image  # this accesses the image file i loaded under resources

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.rect.x = 50
        self.rect.y = 0
        self.change_x = 0
        self.change_y = 0

        # setting gravity so that the player doesnt just go straight up
        self.gravity = 0.2

        # setting score for the game
        # this will show on the screen
        self.score = 0
        self.health = 5

        # List of sprites we can bump against
        self.level = None
        self.can_jump = False
        self.coin = coin_group
        self.platform = platform_group

    def update(self):
        self.change_y += self.gravity
        self.rect.y += self.change_y

        # this is so that when you hit a platform you don't go straight through

        hit_list = pygame.sprite.spritecollide(self, self.platform, False)
        # for platform in hit_list:
        if self.change_y > 0:
            self.can_jump = False
            global platform
            for platform in hit_list:
                if self.rect.bottom - platform.rect.bottom < 10:
                    # it only matters on the y axis because the platforms are moving sideways and the player is not
                    self.rect.bottom = platform.rect.top
                    self.change_y = 0
                    self.can_jump = True  # this is so that you can't jump when you are falling

        # this is to collect the coins and gain points!
        coin_hit_list = pygame.sprite.spritecollide(self, self.coin, False)
        for coin in coin_hit_list:
            if coin.rect.centerx + self.rect.centerx > 10 > coin.rect.centerx - self.rect.centerx:
                if coin.num == 1:
                    global double_coin  # I set each type of coin to a number lower down so I could access it here
                    coin_sound.play()  # this is the A+ coin
                    player.score += 5 * double_coin
                    coin.kill()
                elif coin.num == 2:  # this is the fail coin
                    player.score -= 5
                    player.health -= 2
                    fail_sound.play()
                    coin.kill()
                elif coin.num == 3:  # this is the coffee coin
                    global speed
                    global can_power_up
                    global can_double
                    global power_up_type
                    global level
                    coffee_sound.play()
                    number = random.randrange(5)
                    if number == 1:  # this makes it so that there are different power ups to make the game interesting
                        double_coin = 2
                        speed = 4 + level
                        for platform in platform_group:
                            platform.change_x = speed
                            speed = 4 + level
                        power_up_type = "double points"
                        # power_up = double score
                    elif number == 2:
                        if can_power_up is True:
                            power_up_type = "faster"
                            double_coin = 1
                            speed += 2
                            for i in range(10):
                                for platform in platform_group:
                                    platform.change_x = speed
                                    can_power_up = False
                    else:
                        power_up_type = "+1 health"
                        self.health += 1
                        speed = 4 + level
                        for platform in platform_group:
                            platform.change_x = speed
                            speed = 4 + level
                        double_coin = 1
                        # power up is lives

                    coin.kill()

        '''
        I decided that I didnt need this code
        
        
        elif self.change_y < 0:
            self.rect.top = platform.rect.bottom
            self.can_jump = True
        '''


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = a_image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.change_x = 0
        self.change_y = 0
        self.num = 1


class Fail(Coin):
    def __init__(self):
        super().__init__()
        self.image = f_image
        self.num = 2


class Coffee(Coin):
    def __init__(self):
        super().__init__()
        self.image = coffee_image
        self.num = 3


class Platform(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, width, height):  # this takes some info that is given in the new_platform function
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()  # grabs the rect based on the image
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.change_x = speed  # each level it goes faster
        self.change_y = 0
        self.coin = coin_group
        self.coin_list = []
        self.duplicate = False  # this is so they don't start stacking

    def update(self):
        self.rect.x -= self.change_x  # so the platform moves

        if self.rect.right <= 0:  # delete the platform when its off the screen
            self.kill()

        for coin in self.coin_list:  # so the coins move on the platform too
            coin.rect.x -= self.change_x


'''
FUNCTIONS

These are mostly functions for new screens
'''


def cut_screen():  # we made this one in class
        done = False
        while not done:
            global event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        done = True
                    else:
                        done = True
                        pygame.quit()

            screen.fill(BLUE2)

            my_text = my_font.render("Welcome to my game! I hope you like it!", True, WHITE)
            my_text1 = my_font.render("Click space to jump.", True, WHITE)
            my_text10 = my_font.render("To collect points, collect the A+ coins.", True, WHITE)
            my_text11 = my_font.render("Try to avoid the F coins!", True, WHITE)
            my_text12 = my_font.render("For power ups, collect the coffee coins.", True, WHITE)
            my_text13 = my_font.render("Click space to start and space to jump.", True, WHITE)

            screen.blit(my_text, [10, 50])
            screen.blit(my_text1, [10, 75])
            screen.blit(my_text10, [10, 100])
            screen.blit(my_text11, [10, 125])
            screen.blit(my_text12, [10, 150])
            screen.blit(my_text13, [10, 175])

            pygame.display.flip()
            clock.tick(60)


def end_screen():  # this is based off of the one we made in class just for the end
    done = False
    while not done:
        global event
        global game_over
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    done = True
                if event.key == pygame.K_DOWN:
                    done = True
                    game_over = True
                else:
                    pass
        screen.fill(BLUE2)
        my_text = my_font.render("GAME OVER. PLAY AGAIN?", True, WHITE)
        my_text2 = my_font.render("IF SO, HIT UP. ", True, WHITE)
        my_text3 = my_font.render("IF NOT, HIT DOWN. ", True, WHITE)
        screen.blit(my_text, [10, 50])
        screen.blit(my_text2, [10, 80])
        screen.blit(my_text3, [10, 110])
        my_text1 = my_font.render("Score: " + str(player.score) + " Level: " + str(level), True, WHITE)
        # yay you can see the final score
        screen.blit(my_text1, [10, 135])

        pygame.display.flip()
        clock.tick(60)
    return game_over


def new_level_screen():  # also based off of the cut screen but for a new level!
    done = False
    global event
    global game_over
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True
                else:
                    done = True
                    game_over = True

        screen.fill(BLUE2)
        my_text = my_font.render("LEVEL UP YAY. Click space to start.", True, WHITE)
        my_text1 = my_font.render("Score: " + str(player.score) + " Level: " + str(level), True, WHITE)

        screen.blit(my_text, [10, 50])
        screen.blit(my_text1, [10, 75])

        pygame.display.flip()
        clock.tick(60)
    return game_over

def new_platform(x_position, y_position, width, height):  # this takes in width and height which puts it into the class
    platform = Platform(x_position, y_position, width, height)
    platform.coin = coin_group
    platform_group.add(platform)
    platform_list.append(platform)
    all_sprites_group.add(platform)

    for i in range(1, 4):
        number = random.randrange(20)  # this randomizes what kind of coin is
        for platform in platform_group:
            if number == 1:
                coin = Coffee()
                coin.rect.bottom = platform.rect.top
            elif number == 2 + level:  # there are more fail coins as the levels get higher
                coin = Fail()
                coin.rect.bottom = platform.rect.top
            else:  # this makes it so its mostly As
                coin = Coin()
                coin.rect.bottom = platform.rect.top

        coin.rect.bottom = platform.rect.top
        coin.rect.right = platform.rect.left + 10 + platform.rect.width // 3 * i
        all_sprites_group.add(coin)
        coin_group.add(coin)
        platform.coin_list.append(coin)

# these are my reset screens for when the game is over or if you need to reset for a new level


def reset():
    global speed
    global can_power_up
    global double_coin
    global power_up_type
    global can_play
    all_sprites_group.empty()
    coin_group.empty()
    platform_group.empty()
    player.coin.empty()
    platform.coin.empty()
    player.platform.empty()

    player.score = 0
    player.health = 5
    player.change_y = 0

    speed = 4 + level
    can_power_up = True
    double_coin = 1
    power_up_type = "none"
    can_play = False

    all_sprites_group.add(player)
    player.rect.x = 50
    player.rect.y = 0

    new_platform(200, 290, 200, 50)

    new_platform(550, random.randrange(250, 400), 200, 50)

    if can_play is False:
        global start_text
        pygame.draw.rect(screen, BLUE2, [150, 150, 500, 100])
        start_text = my_font2.render("Hit space to start!", True, WHITE)
        screen.blit(start_text, [160, 160])

    # new_platform(600, random.randrange(300, 500), 200, 50)


def new_level():
    global speed
    global can_power_up
    global double_coin
    global power_up_type
    global can_play
    new_level_screen()
    all_sprites_group.empty()
    coin_group.empty()
    platform_group.empty()
    player.coin.empty()
    platform.coin.empty()
    player.platform.empty()

    all_sprites_group.add(player)
    player.rect.x = 50
    player.rect.y = 0
    double_coin = 1

    speed = 4 + level
    can_power_up = True
    power_up_type = "none"
    can_play = False

    player.score = 0
    player.health = 5

    new_platform(200, 290, 200, 50)

    new_platform(550, random.randrange(250, 400), 200, 50)

    if can_play is False:
        global start_text
        pygame.draw.rect(screen, BLUE2, [150, 150, 500, 100])
        start_text = my_font2.render("Hit space to start!", True, WHITE)
        screen.blit(start_text, [160, 160])

    # new_platform(600, random.randrange(300, 500), 200, 50)

    # all_sprites_group.update()


all_sprites_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()

cut_screen()

player = Player()

# add players
all_sprites_group.add(player)
player.coin = coin_group

new_platform(200, 290, 200, 50)

new_platform(550, random.randrange(250, 400), 200, 50)
# new_platform(600, random.randrange(100, 400), 200, 50)


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if can_play is False:
                can_play = True
            if player.can_jump is True:
                jump_sound.play()
                player.change_y = -6
                player.can_jump = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.KEYUP:
            pass
    x, y = pygame.mouse.get_pos()

    if player.rect.y > SCREEN_HEIGHT:  # you want to avoid jumping off the screen
        end_screen()
        level = 1
        reset()
    if player.health <= 0:  # so if you have no health you die
        end_screen()
        level = 1
        reset()

    if player.score < 0:  # so you can't go negative
        player.score = 0

    for platform in platform_group:
        if platform.rect.right < 300 and platform.duplicate is False:
            platform.duplicate = True
            new_platform(SCREEN_WIDTH, random.randrange(300, 500), 200, 50)
        if platform.rect.right < 0:
            platform.kill()

    if len(platform_list) > 20 + level:  # this makes the levels end eventually and start a new level
        level += 1
        cheer_sound.play()
        new_level()
        platform_list = []

    if can_play is True:
        all_sprites_group.update()

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    screen.fill(BLUE2)
    screen.blit(background_image, [0, 0])

    all_sprites_group.draw(screen)
    if can_play is False:
        pygame.draw.rect(screen, BLUE2, [150, 150, 500, 100])
        start_text = my_font2.render("Hit space to start!", True, WHITE)
        screen.blit(start_text, [160, 160])

    # this writes the score!
    my_text4 = my_font.render("Score: " + str(player.score), True, WHITE)
    screen.blit(my_text4, [10, 10])
    my_text5 = my_font.render("Health: " + str(player.health), True, WHITE)
    screen.blit(my_text5, [10, 35])
    my_text6 = my_font.render("Level: " + str(level), True, WHITE)
    screen.blit(my_text6, [10, 60])
    my_text7 = my_font.render("Power up: " + power_up_type, True, WHITE)
    screen.blit(my_text7, [10, 85])

    for platform in platform_list:
        if platform.rect.top == player.rect.bottom:
            player.can_jump = True

    if game_over is True:
        done = True

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
