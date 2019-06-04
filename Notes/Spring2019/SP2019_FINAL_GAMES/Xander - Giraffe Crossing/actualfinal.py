"""
Frogger
by Xander Mesires 2019

The objective of this game is to move the giraffe to the other side of the roads.
Once you reach the other end, you will move on to the next level.
With each level the speed of the cars increases, making it harder to make it across.
Use WASD to control the player.
W - foreward
A - left
S - backwards
D - right
"""
level = 1
import pygame
import random
pygame.init()

# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (102, 51, 0)
YELLOW = (255, 255, 0)


# Defining images for the variation of cars
truck1 = pygame.image.load("car1.png")
truck2 = pygame.image.load("car2.png")
truck3 = pygame.image.load("car3.png")
truck4 = pygame.image.load("car4.png")
truck5 = pygame.image.load("car5.png")
textbk = pygame.image.load("text copy.jpg")

background_image = pygame.image.load("truebkground.png")

# Defining music / sound effects
background_music = pygame.mixer.Sound("bkground.wav")
background_music.set_volume(0.5)
background_music.play()

accel = pygame.mixer.Sound("accel.wav")

speed = pygame.mixer.Sound("foom.wav")

my_font = pygame.font.SysFont("cochin", 20, True, False)


# Creating classes, one for the player, & 2 for the cars
# Player class
class Player(pygame.sprite.Sprite):  # The class is the player-controlled sprite

    # -- Methods
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        self.lives = 5

        # Image for the player
        self.image = pygame.image.load("beete.png")

        # Creates the actual sprite and where it goes
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = 355

        # Attributes
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        # Change the speed of the player
        self.change_x += x
        self.change_y += y

    def update(self):
        # Find a new position for the player
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.lives <= 0:
            cut_screen3()


# First car class, for cars moving across the screen to the right
class Enemy(pygame.sprite.Sprite):
    def __init__(self, y, image):
        # defining some terms for the cars and their positions
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = -25
        self.rect.y = y
        self.change_x = random.randrange(1,4)

    def update(self):
        # new position for the cars
        self.rect.x += self.change_x
        if self.rect.x > 325:
            self.rect.x = -25

# 2nd car class, for cars moving across the screen to the left
class Car(pygame.sprite.Sprite):
    def __init__(self, y, image):
        # defining some terms for the cars and their positions
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width)
        self.rect.y = y
        self.change_x = random.randrange(-4, -1)
        
    def update(self):
        # new position for the cars
        self.rect.x += self.change_x
        if self.rect.right < 0:
            self.rect.left = screen_width


pygame.init()

# Setting the size of the screen
screen_width = 300
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the title of the window
pygame.display.set_caption('Frogger')

# Groups for the player & car classes
# Adding them to the all sprites list
player_group = pygame.sprite.Group()
player = Player(50, 50)
player_group.add(player)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
enemy_group = pygame.sprite.Group()
new_car = Enemy(325, truck1)
enemy_group.add(new_car)
all_sprites_list.add(new_car)
car = Car(275, truck2)
enemy_group.add(car)
all_sprites_list.add(car)
new_car2 = Enemy(225, truck3)
enemy_group.add(new_car2)
all_sprites_list.add(new_car2)
car2 = Car(145, truck4)
enemy_group.add(car2)
all_sprites_list.add(car2)
new_car3 = Enemy(95, truck5)
enemy_group.add(new_car3)
all_sprites_list.add(new_car3)
car3 = Car(40, truck2)
enemy_group.add(car3)
all_sprites_list.add(car3)


clock = pygame.time.Clock()
done = False

# Defining cut screens to go in between certain parts of the game
# Intro screen
def cut_screen():
    my_font = pygame.font.SysFont('Britannic', 19, True, False)
    text = my_font.render("Try to move the giraffe", True, BLACK)
    text5 = my_font.render("across the road and make it to", True, BLACK)
    text2 = my_font.render("the other end without", True, BLACK)
    text6 = my_font.render("getting hit by any cars.", True, BLACK)
    text9 = my_font.render("Try to make it past level 3.", True, BLACK)
    text8 = my_font.render("You start off with 5 lives.", True, RED)
    text3 = my_font.render("Use WASD to control the player.", True, BLACK)
    my_font2 = pygame.font.SysFont('Britannic', 23, True, False)
    text4 = my_font2.render("Press the spacebar to start", True, RED)


    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True

        screen.fill(BLACK)
        screen.blit(textbk, [0, -65])

        rect = text.get_rect()
        screen.blit(text, [3, 100])
        screen.blit(text5, [3, 120])
        screen.blit(text2, [3, 140])
        screen.blit(text6, [3, 160])
        screen.blit(text9, [3, 180])
        screen.blit(text8, [3, 200])
        screen.blit(text3, [3, 235])
        screen.blit(text4, [3, 250])


        pygame.display.flip()
        clock.tick(60)

# Getting hit by a car screen
def cut_screen1():
    my_font = pygame.font.SysFont('Britannic', 19, True, False)
    text = my_font.render("You got hit by a car.", True, WHITE)
    text2 = my_font.render("Press the spacebar to reset the level", True, RED)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True

                    # Set the speed based on the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_d:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_w:
                    player.changespeed(0, -3)
                elif event.key == pygame.K_s:
                    player.changespeed(0, 3)

                # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_d:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_w:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_s:
                    player.changespeed(0, -3)

        screen.fill(BLACK)

        rect = text.get_rect()
        screen.blit(text, [3, 100])
        screen.blit(text2, [3, 120])

        pygame.display.flip()
        clock.tick(60)

# Completing a level screen
def cut_screen2():
    my_font = pygame.font.SysFont('Britannic', 19, True, False)
    text = my_font.render("You completed level" + str(level), True, WHITE)
    text2 = my_font.render("Moving on to level" + str(level + 1), True, WHITE)
    text3 = my_font.render("Press space to continue", True, RED)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True

            # Set the speed based on the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_d:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_w:
                    player.changespeed(0, -3)
                elif event.key == pygame.K_s:
                    player.changespeed(0, 3)

            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_d:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_w:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_s:
                    player.changespeed(0, -3)

        screen.fill(BLACK)

        rect = text.get_rect()
        screen.blit(text, [3, 50])
        screen.blit(text2, [3, 70])
        screen.blit(text3, [3, 95])

        pygame.display.flip()
        clock.tick(60)

# Game over screen
def cut_screen3():
    my_font = pygame.font.SysFont('Britannic', 19, True, False)
    text = my_font.render("You ran out of lives.", True, BLACK)
    text2 = my_font.render("Game over.", True, RED)


    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    done = True

        screen.fill(BLACK)
        screen.blit(textbk, [0, -65])

        rect = text.get_rect()
        screen.blit(text, [3, 100])
        screen.blit(text2, [3, 120])

        pygame.display.flip()
        clock.tick(60)


cut_screen()


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user inputs)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        # What happens when a certain key is pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_d:
                player.changespeed(3, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, -3)
            elif event.key == pygame.K_s:
                player.changespeed(0, 3)


        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed(3, 0)
            elif event.key == pygame.K_d:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, 3)
            elif event.key == pygame.K_s:
                player.changespeed(0, -3)

    # --- Game logic should go here

    # This calls update on all the sprites
    all_sprites_list.update()

    hit_list = pygame.sprite.spritecollide(player, enemy_group, False)

    for hit in hit_list:
        accel.play()
        player.lives -= 1
        player.rect.x = screen_width // 2
        player.rect.y = 355
        cut_screen1()



        # -- Attributes
        player.change_x = 0
        player.change_y = 0

    # The code for what happens when a player makes it to the other side
    if player.rect.y < 15:
        cut_screen2()
        level += 1
        player.rect.x = screen_width // 2
        player.rect.y = 355
        speed.play()
        # Increasing the speed of the cars since a new level is coming
        # Mr. Lee provided help with the #'s for movement
        new_car.change_x += random.randrange(1, 3)
        new_car2.change_x += random.randrange(1, 3)
        new_car3.change_x += random.randrange(1, 3)
        car.change_x += random.randrange(-2, 0)
        car2.change_x += random.randrange(-2, 0)
        car3.change_x += random.randrange(-2, 0)




    # --- Drawing code should go here
    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])

    # The text displayed on the screen for levels & lives
    my_text = my_font.render("Lives:" + str(player.lives), True, WHITE)
    my_text2 = my_font.render("Level:" + str(level), True, WHITE)
    screen.blit(my_text, [0, screen_height - 20])
    screen.blit(my_text2, [0, 18])

    # Draw sprites
    all_sprites_list.draw(screen)

    pygame.display.flip()  #Go ahead and update the screen with what we've drawn

    clock.tick(60)  # frames per second


# Close the window and quit.
pygame.quit()
