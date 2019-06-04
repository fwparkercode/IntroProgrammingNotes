"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/


This game is similar to Galaga. You are Mickey Mouse, and Pete
wants to keep you and your friends from the party and from having
a good time. You have to stop him. Mickey starts and can move
with the arrow keys and shoot. You start with three lives, and you
can shoot at all of the Pete's. Pete's can shoot back. They are
placed on the screen at random and move randomly. As the levels increase,
you get more player and more enemies, and the enemies get more health and bullets.
"""

import pygame
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MOSS = (100, 155, 0)
YELLOW = (255, 255, 0)
DARKGREEN = (5, 25, 0)
DARKBLUE = (1, 1, 60)
GREY = (80, 80, 80)
PERYWINKLE = (70, 70, 180)
PINK = (170, 10, 150)
PURPLE = (110, 10, 190)
SEAFOAM = (0, 220, 195)
TEAL = (0, 80, 80)
SKYBLUE = (80, 140, 255)
GRASS = (0, 155, 0)
BEIGE = (250, 250, 200)
DISNEYBLUE = (10, 10, 205)
INDISEMOUTH = (48, 0, 0)
PLUTO = (255, 171, 10)
ORANGE = (255, 100, 0)

pygame.init()

screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
level = 1
my_font = pygame.font.SysFont("Calibri", 40, True, False)
my_font2 = pygame.font.SysFont("Calibri", 28, False, False)

# all needed images
'''
background_image = pygame.image.load("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/mickey_mouse_clubhouse.png")
first_image = pygame.image.load("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/firstimage.png")
bullet_image = pygame.image.load("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/mickey_head.png")
enemy_image = pygame.image.load("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/pete.png")
wrench_image = pygame.image.load("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/wrench.png")
mickey_image = pygame.image.load("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/mickey.png")
minnie_image = pygame.image.load("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/minnie.png")
pluto_image = pygame.image.load("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/pluto.png")
goofy_image = pygame.image.load("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/goofy.png")
donald_image = pygame.image.load("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/donald.png")
daisy_image = pygame.image.load("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/daisy.png")
'''
background_image = pygame.image.load("mickey_mouse_clubhouse.png")
first_image = pygame.image.load("firstimage.png")
bullet_image = pygame.image.load("mickey_head.png")
enemy_image = pygame.image.load("pete.png")
wrench_image = pygame.image.load("wrench.png")
mickey_image = pygame.image.load("mickey.png")
minnie_image = pygame.image.load("minnie.png")
pluto_image = pygame.image.load("pluto.png")
goofy_image = pygame.image.load("goofy.png")
donald_image = pygame.image.load("donald.png")
daisy_image = pygame.image.load("daisy.png")

# all needed sound
'''
background_sound = pygame.mixer.Sound("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/background.wav")
background_sound.set_volume(0.7)
background_sound.play(-1)
shot_sound = pygame.mixer.Sound("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/laser.wav")
hit_you_sound = pygame.mixer.Sound("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/clank.wav")
hit_me_sound = pygame.mixer.Sound("/Users/aliciaberger/PycharmProjects/Computer programing 1/Labs/final2/canon.wav")
shot_sound.set_volume(0.2)
hit_you_sound.set_volume(1)
hit_me_sound.set_volume(0.8)
'''
background_sound = pygame.mixer.Sound("background.wav")
background_sound.set_volume(0.7)
background_sound.play(-1)
shot_sound = pygame.mixer.Sound("laser.wav")
hit_you_sound = pygame.mixer.Sound("clank.wav")
hit_me_sound = pygame.mixer.Sound("canon.wav")
shot_sound.set_volume(0.2)
hit_you_sound.set_volume(1)
hit_me_sound.set_volume(0.8)


# order they come in in the game
image_list = [mickey_image, donald_image, goofy_image, pluto_image, minnie_image, daisy_image, daisy_image]

# Main player, moves with arrow keys and shoots with space bar.

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = mickey_image




        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()



        self.rect.x = x
        self.rect.y = y


        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.wellbeing = 3
        self.player_list = []

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        for extra_player in self.player_list:
            extra_player.changespeed(x,y)
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

# players bullets that release when space bar is hit. They kill the enemy
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 8
        if self.rect.y < 0:
            self.kill()

# Enemies bullets. Fired at random and they take away player health till the player dies
class Shrapnil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = wrench_image
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 8

        if self.rect.y > 500:
            self.kill()

# Pete. Starts with 5 and increases per level. Move around screen but not off and can't go below the player. They die if their helth is 0
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # calling sprite class
        self.image = enemy_image
        self.rect = self.image.get_rect() # grabs the rect based on the image



        self.rect.x = random.randrange(0, 700 - self.rect.width) # moving the rectangle is moving the sprite
        self.rect.y = random.randrange(0, 250)





        self.health = 1
        self.change_x = random.randrange(-7,10)
        self.change_y = random.randrange(-7, 10)

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right >= screen_width:
            self.change_x *= -1
        if self.rect.left <= 0:
            self.change_x *= -1

        if self.rect.bottom >= 445:
            self.change_y *= -1
        if self.rect.top <= 0:
            self.change_y *= -1


bullet_group = pygame.sprite.Group()
shrapnil_group = pygame.sprite.Group()




# Create the player object
player = Player(325, 375)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
enemy_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player_group.add(player)

# creates enemies
for i in range(5):
    new_enemy = Block()
    all_sprites_list.add(new_enemy)
    enemy_group.add(new_enemy)





clock = pygame.time.Clock()
done = False

# first cut screen. Main background on game
def cut_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_c:
                    done = True
        screen.fill(DARKBLUE)
        screen.blit(background_image, [0, 0])


        my_text = my_font.render("Welcome to Mickey Mouse Friend Rescue!", True, BLACK)
        my_text2 = my_font2.render("Mickey Mouse's Friends have been captured by Pete who wants to take", True, BLACK)
        my_text7 = my_font2.render("all of their fun and it's up to you to get them back so they can go", True, BLACK)
        my_text3 = my_font2.render("to the party. Every time you defeat the all of the Petes one of ", True, BLACK)
        my_text4 = my_font2.render("Mickey's friends will return to you and help you. But if you lose ", True, BLACK)
        my_text5 = my_font2.render("all of your health you will be captured and the game will be over.",True, BLACK)
        my_text6 = my_font.render("Click c to continue.", True, BLACK)
        screen.blit(my_text, [30, 100])
        screen.blit(my_text7, [50, 200])
        screen.blit(my_text2, [15, 150])
        screen.blit(my_text3, [65, 250])
        screen.blit(my_text4, [50, 300])
        screen.blit(my_text5, [80, 350])
        screen.blit(my_text6, [190, 450])


        pygame.display.flip()
        clock.tick(60)
# second cut screen. tells how to play
def cut_screen2():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        done = True
        screen.fill(DARKBLUE)
        screen.blit(background_image, [0, 0])



        my_text = my_font.render("How to play", True, BLACK)
        my_text2 = my_font2.render("Use the arrow keys to move the players to the right and left", True, BLACK)
        my_text3 = my_font2.render("to hit Pete press down the space bar, soemtimes you will have to hit him", True, BLACK)
        my_text4 = my_font2.render("more then once. If he hits you too many times your health will go 0", True, BLACK)
        my_text5 = my_font2.render("and you will be captured and the game will be over. GOOD LUCK!",True, BLACK)
        my_text6 = my_font.render("Click c to continue.", True, BLACK)
        screen.blit(my_text, [30, 50])
        screen.blit(my_text2, [50, 150])
        screen.blit(my_text3, [15, 200])
        screen.blit(my_text4, [50, 250])
        screen.blit(my_text5, [60, 300])
        screen.blit(my_text6, [190, 450])

        pygame.display.flip()
        clock.tick(60)
# cut screen for when you die
def end_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        done = True
        screen.fill(DARKBLUE)
        screen.blit(background_image, [0, 0])
        background_sound



        my_text = my_font.render("Oh No!", True, BLACK)
        my_text2 = my_font2.render("It seems like Pete was able to capture you.", True, BLACK)
        my_text3 = my_font2.render("Now you won't be able to go to the party.", True, BLACK)
        my_text6 = my_font.render("Better luck next time!", True, BLACK)
        my_text7 = my_font.render("Press q to quit.", True, BLACK)
        screen.blit(my_text, [315, 50])
        screen.blit(my_text2, [150, 100])
        screen.blit(my_text3, [160, 150])
        screen.blit(my_text6, [180, 320])
        screen.blit(my_text7, [240, 350])

        pygame.display.flip()
        clock.tick(60)
# cut screen for if you win
def end_screen2():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        done = True
        screen.fill(DARKBLUE)
        screen.blit(background_image, [0, 0])



        my_text = my_font.render("Yay!", True, BLACK)
        my_text2 = my_font2.render("You beat Pete!", True, BLACK)
        my_text3 = my_font2.render("Now you will be able to go to the party.", True, BLACK)
        my_text6 = my_font.render("Congratulations!", True, BLACK)
        my_text7 = my_font.render("Press q to quit.", True, BLACK)
        screen.blit(my_text, [290, 50])
        screen.blit(my_text2, [250, 150])
        screen.blit(my_text3, [155, 200])
        screen.blit(my_text6, [210, 320])
        screen.blit(my_text7, [230, 350])

        pygame.display.flip()
        clock.tick(60)
# Middle screen between levels. Gets player to lift hands off of the key board
def middle_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3, 0)

                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3, 0)
                elif event.key ==  pygame.K_c:
                    done = True

            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)



        screen.fill(DARKBLUE)
        screen.blit(background_image, [0, 0])


        my_text = my_font.render("You have now rescued another friend!", True, BLACK)
        my_text2 = my_font2.render("They will now help you rescue the others.", True, BLACK)
        my_text6 = my_font.render("Click c to continue.", True, BLACK)
        screen.blit(my_text, [60, 100])
        screen.blit(my_text2, [165, 150])
        screen.blit(my_text6, [190, 450])


        pygame.display.flip()
        clock.tick(60)


cut_screen()
cut_screen2()
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if player.wellbeing <= 0:
            done = True

        # Set the speed based on the key pressed


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)

            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)

            # shoots bullets from rect center
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet()
                all_sprites_list.add(new_bullet)
                bullet_group.add(new_bullet)
                new_bullet.rect.center = player.rect.center
                shot_sound.play()
                for extra in player.player_list:
                    new_bullet = Bullet()
                    all_sprites_list.add(new_bullet)
                    bullet_group.add(new_bullet)
                    new_bullet.rect.center = extra.rect.center


            elif event.key == pygame.K_q:
                done = True

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)



    # sets for next level increases challenge and resets sets new player in game

    if len(enemy_group) == 0:
        if level == 6:
            end_screen2()
            done = True
        else:
            middle_screen()
        level += 1
        new_player = Player(0,0)
        new_player.image = image_list[level-1]
        if len(player.player_list) > 0:
            new_player.rect.left = player.player_list[-1].rect.right - 35
            new_player.rect.y = player.rect.y
        else:
            new_player.rect.left = player.rect.right - 30
            new_player.rect.y = player.rect.y
        player.player_list.append(new_player)
        all_sprites_list.add(new_player)
        player_group.add(new_player)
        player.wellbeing = 3 + level

        # numbers for levels.

        for i in range(4 * level - level):
            new_enemy = Block()
            new_enemy.change_x += level
            new_enemy.health += level
            all_sprites_list.add(new_enemy)
            enemy_group.add(new_enemy)


# kill factor for the bullets
    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, False)
        for hit in hit_list:
            bullet.kill()
            hit.health -= 1
            hit_you_sound.play()
            if hit.health <= 0:
                hit.kill()
# kill factor for enemy group
    for new_enemy in enemy_group:
        if random.randrange(3360 / level) == 0:
            new_shrapnil = Shrapnil()
            all_sprites_list.add(new_shrapnil)
            shrapnil_group.add(new_shrapnil)
            new_shrapnil.rect.center = new_enemy.rect.center
    for new_enemy in enemy_group:
        if random.randrange(3360 / level) == 1:
            new_shrapnil = Shrapnil()
            all_sprites_list.add(new_shrapnil)
            shrapnil_group.add(new_shrapnil)
            new_shrapnil.rect.center = new_enemy.rect.center

# kill factor for characters

    for character in player.player_list:
        hit_list = pygame.sprite.spritecollide(character, shrapnil_group, True)
        for hit in hit_list:
            hit_me_sound.play()
            player.wellbeing -= 1
            print(player.wellbeing)
            if player.wellbeing <= 0:
                end_screen()
                done = True
# kill factor for players

    hit_list = pygame.sprite.spritecollide(player, shrapnil_group, True)
    for hit in hit_list:
        player.wellbeing -= 1
        print(player.wellbeing)
        if player.wellbeing <= 0:
            end_screen()
            done = True


# win screen
    if level == 8:
        end_screen2()
        done = True


    # Calls update on all the sprites
    all_sprites_list.update()

    # -- Draw everything
    # Clear screen
    screen.fill(WHITE)
    screen.blit(first_image, [0, 0])
    # Draw sprites
    all_sprites_list.draw(screen)
    # shows player health
    my_text = my_font.render("Your health : " + str(player.wellbeing), True, BLACK)
    screen.blit(my_text, [10, 10])
    # how many people you have left to save
    my_text2 = my_font.render("Friends left : " + str(6 - level), True, BLACK)
    screen.blit(my_text2, [450, 10])
    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()
