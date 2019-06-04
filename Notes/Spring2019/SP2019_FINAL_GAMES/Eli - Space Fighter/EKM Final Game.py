#do write up, test for bugs, done
'''
Multiline Comment --
This is a space fighter game. The focus is on protecting earth, which the player does
through shooting comets and aliens. To make the game harder satellites
are flying at you, which you most avoid in order to live on (you can not destroy them). There are a
limited amount of bullets -- so make sure to hit your shots. the player
moves through the arrow keys, with shooting happening at the press of the
space bar. Have Fun and Make sure to save the earth!
'''
# parts  Adapted from move_sprite_keyboard_smooth.py
# parts adapted from Chapter 13 Notes -- Ball shot Game


# Made by Eli Kraft Moog
import random
import pygame

pygame.init()  # do not put anything pygame above this line

# Define some colors (red, green, blue)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (200, 125, 0)
PURPLE = (150, 50, 200)
SILVER = (192, 192, 192)

screen_width = 600 # changed size bc of image-- want it to look like mobile game
screen_height = 960 # changed size bc of image
size = (screen_width, screen_height)  # width, height
screen = pygame.display.set_mode(size)
## (0,0), pygame.FULLSCREEN) for me bc mac is broken
# or just (size)



pygame.display.set_caption("Eli Kraft Moog Final Game") ## this is my title of screen

done = False  # condition for my game loop

clock = pygame.time.Clock() # Used to manage how fast the screen updates

background_image = pygame.image.load("background.png") # this is calling my background image


# random variables
frame = 1
level = 1 ## define what level is
bullet_count = 50 - level
frame = 0 ## my timer
earth_health = 400 + (level * 50)
enemy_left = 30 + 2 * level
spaceship_health = 10 - level

## Adapted from move_sprite_keyboard_smooth.py

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png") # loading my image
        self.rect = self.image.get_rect()
        self.rect.x = 200  # starting location x
        self.rect.y = 350   # starting location y
        self.change_x = 0 # what mouse moves by x
        self.change_y = 0  # what mouse moves by y

    ## Adapted from move_sprite_keyboard_smooth.py

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # ship boundary for right side
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        # ship boundary for left side
        if self.rect.left <= 0:
            self.rect.left = 0
        # ship boundary for earth side
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
        # ship boundary for left side
        if self.rect.top <= 0:
            self.rect.top = 0

## my bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y



    def update(self):
        self.rect.y -= 7 + level
        if self.rect.y < 50:
            self.kill() # killing it if its to high -- so it wont kill something going on screen or off screen

# creating enemy class
class Aliens(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ufo alien.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, 300)
        self.rect.y = -100


    def update(self):
        self.rect.y += 4 + (level * 0.5)
## creating comet class
class Comet(Aliens):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("comet.png")
## creating spacex
class Spacex(Aliens):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spacex.png")
        self.rect.centery = random.randrange(150, 600) # making random y location
        self.rect.centerx = -100 # getting it off screen


    def update(self):
        self.rect.x += 4 # moving it

## getting more ammo
class More_Ammo(Aliens):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rockets.png")
        self.rect.centery = random.randrange(150, 600)
        self.rect.centerx = screen_width


    def update(self):
        self.rect.x -= 4


# Text resources
my_font = pygame.font.SysFont('Merriweather', 30, True, False) #creates usable object named my_font

## have sound on half way please
# Sound Resources
shot_sound = pygame.mixer.Sound("shot.wav")
shot_sound.set_volume(0.1)


background_music = pygame.mixer.Sound("fornite.wav")
background_music.set_volume(2.7)
background_music.play(-1)

# sound for win screen
win_music = pygame.mixer.Sound("win_cap_usa.wav")
win_music.set_volume(0.3) ## sorry if its bad audio quility -- i got it from youtube, into mp3, into wav

# Making my sprites
player = Spaceship()

# Create Sprite
comet_group = pygame.sprite.Group()
extra_ammo_group = pygame.sprite.Group()
spacex_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

#  aliens stager
alien_list = []
stagger_aliens = 10
for i in range(10 + level): # creates instance of the alien class
    alien = Aliens()
    alien.rect.y = 10 - (20 * stagger_aliens)
    stagger_aliens += 50 / level
    alien_group.add(alien)

#comet's stagger
comet_list = []
stagger_comet = 10
for i in range(20 + level): # creates instance of the comet class
    comet = Comet()
    comet.rect.y = 10 - (20 * stagger_comet)
    stagger_comet += 20 / level
    comet_group.add(comet)
# spacex ships stagger
spacex_list = []
stagger_spacex = 10
for i in range(25 + level): # creates instance of the spacex class
    space_x = Spacex()
    space_x.rect.x = 10 - (20 * stagger_spacex)
    stagger_spacex += 20 / (level * 0.5)
    spacex_group.add(space_x)
    all_sprites_group.add(space_x)
# extra bullets stagger
more_ammo_list = []
stagger_ammo = 10
supply_drop = 2 + level
for i in range(supply_drop): # creates instance of the more ammo class
    more_ammo = More_Ammo()
    more_ammo.rect.x = screen_width + (20 * stagger_ammo)
    stagger_ammo += 20 / (level * 0.5)
    extra_ammo_group.add(more_ammo)



# add player to sprite
all_sprites_group.add(player)# add player so that its infront of bullet


## create end screen-- call it later on
clock = pygame.time.Clock()
done = False
## text for all my screens
my_end_screen = my_font.render("GAME OVER: YOU LOSE ", True, WHITE)
my_level_screen = my_font.render("Congrats on advancing! [Press E to Continue]", True, WHITE)
my_start_screen = my_font.render("Welcome to Space Fighter!", True, WHITE)
my_start2_screen = my_font.render("Credits:", True, WHITE)
my_start3_screen = my_font.render("GamePlay Advice: ", True, WHITE)
my_start4_screen = my_font.render("Play Game", True, WHITE)
my_c_screen = my_font.render("Press C to Continue!", True, WHITE)
my_cend_screen = my_font.render("Press C to End the Game!", True, WHITE)


# loss screen
def end_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    done = True
        screen.fill(BLACK)
        screen.blit(my_end_screen, [screen_width * 1/2 - 150, screen_height * 1/2])
        screen.blit(my_cend_screen, [screen_width * 1 / 2 - 150, screen_height - 200])
        pygame.display.flip()
        clock.tick(60)
# screen in between levels
def level_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    done = True

        screen.fill(BLACK)
        screen.blit(my_level_screen, [screen_width * 1/2 - 280, screen_height * 1/2 - 100])

        pygame.display.flip()
        clock.tick(60)

# text for credit screen -- smaller text
my_font_small = pygame.font.SysFont('Merriweather', 25, True, False) #creates usable object named my_font
## text for credit screen

credits_line1 = my_font.render("Game Developer: Eli Kraft Moog", True, WHITE)
credits_line2 = my_font_small.render("With Help From: Mr. Lee and Program Arcade Games", True, WHITE)
credits_line3 = my_font_small.render("Partially Adapted From: move_sprite_keyboard_smooth.py", True, WHITE)
credits_line4 = my_font.render("&", True, WHITE)
credits_line5 = my_font.render("Chapter 13 Notes - Ball Shot Game ", True, WHITE)

def credit_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    done = True
        screen.fill(BLACK)
        screen.blit(my_start2_screen, [screen_width * 1/2 - 40, (screen_height * 1/2) - 100])
        screen.blit(credits_line1, [screen_width * 1 / 2 - 170, (screen_height * 1 / 2) - 50])
        screen.blit(credits_line2, [screen_width * 1 / 2 - 250, (screen_height * 1 / 2) - 10])
        screen.blit(credits_line3, [screen_width * 1 / 2 - 270, (screen_height * 1 / 2) + 25])
        screen.blit(credits_line4, [screen_width * 1 / 2, (screen_height * 1 / 2) + 60])
        screen.blit(credits_line5, [screen_width * 1 / 2 - 190, (screen_height * 1 / 2) + 90])
        screen.blit(my_c_screen, [screen_width * 1 / 2 - 120, screen_height - 200])

        pygame.display.flip()
        clock.tick(60)


## text for game tips
gametip_1 = my_font.render("The Goal of the Game is to Protect Earth!", True, WHITE)
gametip_2 = my_font.render("Comets and Aliens do damage to earth,", True, WHITE)
gametip_8 = my_font.render("and Satellites do damage to the Spaceship.", True, WHITE)
gametip_3 = my_font.render("Press Space to shoot (aim for Comets and Aliens)!", True, WHITE)
gametip_11 = my_font.render("Use the Arrow Keys to move the spaceship!", True, WHITE)
gametip_4 = my_font_small.render("Satellites cannot be damaged, so you must avoid them.", True, WHITE)
gametip_5 = my_font.render("You have limited Ammo,", True, WHITE)
gametip_9 = my_font.render("however can get more in supply packages.", True, WHITE)
gametip_6 = my_font_small.render("Spaceship Health, Earth Health, # of Bullets, Enemies Left, &", True, WHITE)
gametip_10 = my_font_small.render("# of Supply packages left are all displayed on the bottom.", True, WHITE)
gametip_7 = my_font.render("If you survive 6 whole rounds you WIN!", True, CYAN)
def game_tips_screen():

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    done = True
        screen.fill(BLACK)
        screen.blit(my_start3_screen, [screen_width * 1/2 - 100, (screen_height * 1/2) - 450])
        screen.blit(gametip_1, [screen_width * 1 / 2 - 250, (screen_height * 1 / 2) - 400])
        screen.blit(gametip_2, [screen_width * 1 / 2 - 250, (screen_height * 1 / 2) - 350])
        screen.blit(gametip_8, [screen_width * 1 / 2 - 250, (screen_height * 1 / 2) - 300])
        screen.blit(gametip_3, [screen_width / 2 - 290, (screen_height * 1 / 2) - 250])
        screen.blit(gametip_11, [screen_width / 2 - 250, (screen_height * 1 / 2) - 200])
        screen.blit(gametip_4, [screen_width * 1 / 2 - 250, (screen_height * 1 / 2) - 160])
        screen.blit(gametip_5, [screen_width * 1 / 2 - 125, (screen_height * 1 / 2) - 120])
        screen.blit(gametip_9, [screen_width * 1 / 2 - 225, (screen_height * 1 / 2) - 80])
        screen.blit(gametip_6, [screen_width * 1 / 2 - 280, (screen_height * 1 / 2) - 40])
        screen.blit(gametip_10, [screen_width * 1 / 2 - 280, (screen_height * 1 / 2) - 0])
        screen.blit(gametip_7, [screen_width * 1 / 2 - 250, (screen_height * 1 / 2) + 40])
        screen.blit(my_c_screen, [screen_width * 1 / 2 - 120, screen_height - 200])



        pygame.display.flip()
        clock.tick(60)


def start_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    done = True
        screen.fill(BLACK)
        screen.blit(my_start_screen, [screen_width * 1/2 - 150, (screen_height * 1/2) - 100])
        screen.blit(my_c_screen, [screen_width * 1 / 2 - 120, screen_height - 200])

        pygame.display.flip()
        clock.tick(60)

win_sc_1 = my_font.render("You WON -- CONGRATS!!", True, CYAN)
win_sc_2 = my_font.render("The citizens of Earth thank you", True, CYAN)
win_sc_3 = my_font.render("\"Your a hero\" -- POTUS", True, CYAN)


def win_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    done = True
        screen.fill(BLACK)
        screen.blit(win_sc_1, [(screen_width * 1 / 2) - 130, screen_height / 2])
        screen.blit(win_sc_2, [(screen_width * 1 / 2) - 180, (screen_height / 2) + 50])
        screen.blit(win_sc_3, [(screen_width * 1 / 2) - 110, (screen_height / 2) + 100])
        background_music.set_volume(0.0)
        win_music.play(0)
        screen.blit(my_cend_screen, [screen_width * 1 / 2 - 150, screen_height - 200])

        pygame.display.flip()
        clock.tick(60)
## calls my all my start screens
start_screen()
credit_screen()
game_tips_screen()


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop  (user inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

            # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-8, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(8, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -8)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 8)
            elif event.key == pygame.K_q:
                done = True

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(8, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-8, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 8)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -8)


            ## getting it so it can move and shot (play sound, ect.)
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet()
                shot_sound.play(0)
                new_bullet.rect.center = player.rect.center
                new_bullet.rect.y = player.rect.y - 50
                all_sprites_group.add(new_bullet) # so it draws
                bullet_group.add(new_bullet)
                bullet_count = bullet_count - 1
                if bullet_count < 0:
                    bullet_count = -1
                shot_sound.set_volume(0.1)


    ## code that makes my levels
    if enemy_left == 0 and spaceship_health > 0:
        for bullet in bullet_group:
            bullet.kill()
        for space_x in spacex_group:
            space_x.kill()
        level = level + 1
        if level > 6:
            done = True
        if level < 6.1:
            level_screen()
        player.change_y = 0
        player.change_x = 0
        earth_health = 400 + (level * 50)
        enemy_left = 30 + (2 * level)
        bullet_count = 50 - level
        spaceship_health = 10 - level
        if spaceship_health <= 2:
            spaceship_health = 2
        alien_list = []
        stagger_aliens = 10
        for i in range(10 + level):  # create 10 instance of the alien class
            alien = Aliens()
            alien.rect.y = 10 - (20 * stagger_aliens)
            stagger_aliens += 50 / level
            alien_group.add(alien)
        player.rect.x = 200  # starting location x
        player.rect.y = 350  # starting location y
        comet_list = []
        stagger_comet = 10
        for i in range(20 + level):  # create 20 instance of the comet class
            comet = Comet()
            comet.rect.y = 10 - (20 * stagger_comet)
            stagger_comet += 20 / (level * 0.5)
            comet_group.add(comet)
            # draw spacex
        spacex_list = []
        stagger_spacex = 10
        for i in range(25 + level):  # creates instance of the spacex class
            space_x = Spacex()
            space_x.rect.x = 10 - (20 * stagger_spacex)
            stagger_spacex += 20 / level
            spacex_group.add(space_x)
            # draw ammo
        more_ammo_list = []
        stagger_ammo = 10
        supply_drop = 2 + level
        for i in range(supply_drop):  # creates instance of the more ammo class
            more_ammo = More_Ammo()
            more_ammo.rect.x = screen_width + (20 * stagger_ammo)
            stagger_ammo += 20 / (level * 0.5)
            extra_ammo_group.add(more_ammo)

    # --- Game logic should go here
    ## when player hits ammo drops -- they die and player gets ammo
    for more_ammo in extra_ammo_group:
        hit_list = pygame.sprite.spritecollide(player, extra_ammo_group, True)
        for hit in hit_list:
            more_ammo.kill()
            if bullet_count >= 0:
                bullet_count = bullet_count + 3
            if bullet_count < 0:
                bullet_count += 4
            supply_drop = supply_drop - 1
    # updating everything
    bullet_group.update()
    player.update()
    alien_group.update()
    comet_group.update()
    extra_ammo_group.update()
    spacex_group.update()


    # set up everything to be written
    my_bullet_text = my_font.render("Bullets Left: " + str(bullet_count), True, WHITE)
    my_earth_health = my_font.render("Earth Health: " + str(earth_health), True, WHITE)
    my_player_health = my_font.render("Spaceship Health: " + str(spaceship_health), True, WHITE)
    my_enemies_left = my_font.render("Enemies Left:  " + str(enemy_left), True, WHITE)
    my_ammo_airdrop = my_font.render("Supply Drops Left: " + str(supply_drop), True, WHITE)
    my_level = my_font.render("Level:  " + str(level), True, WHITE)

    ## making it so earth will take damage
    for alien in alien_group:
        if alien.rect.y >= 530:
            alien.kill()
            earth_health -= 100
            enemy_left = enemy_left - 1

    ## if it goes off the screen it just kills itself
    for space_x in spacex_group:
        if space_x.rect.x >= screen_width:
            space_x.kill()
    ## getting it so extra ammo dies after its past screen
    for more_ammo in extra_ammo_group:
        if more_ammo.rect.x <= 0:
            more_ammo.kill()
            supply_drop = supply_drop - 1

    ##making it so comet dies and does damage to earth
    for comet in comet_group:
        if comet.rect.y >= 530:
            comet.kill()
            earth_health -= 100
            enemy_left = enemy_left - 1
            # killing bullet
    # must be two different ones so it still shots last shot
    if bullet_count < 0:
        new_bullet.kill()
        shot_sound.set_volume(0)
        bullet_count = -1

    ## making text red and changing test
    if bullet_count < 1:
        my_bullet_text = my_font.render("NO BULLETS LEFT", True, RED)


    ## ends game if earth has no health
    if earth_health < 1:
        done = True
    # ends gam if spaceship doesnt have enough health
    if spaceship_health < 1:
        done = True


    # adapted from Chapter 13 Notes -- Ball shot Game


    ## if bullet hits alien, both die and enemies left goes down
    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, alien_group, True)
        for hit in hit_list:
            bullet.kill()
            enemy_left = enemy_left - 1

    ## if bullet hits comet, both die and enemies left goes down
    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, comet_group, True)
        for hit in hit_list:
            bullet.kill()
            enemy_left = enemy_left - 1

    ## the normal collide stuff wasn't working so I changed it to this -- with 50 of center spacx -- not perfect but works pretty well
    for space_x in spacex_group:
        if space_x.rect.centerx - 50 <= player.rect.centerx <= space_x.rect.centerx + 50 and space_x.rect.centery - 50 <= player.rect.centery <= space_x.rect.centery + 50:
            space_x.kill()
            spaceship_health = spaceship_health - 1

    ## has supply graphic go off of screen
    if supply_drop == 0:
        my_ammo_airdrop = my_font.render("", True, RED)




            # --- Drawing code should go here
    screen.fill(WHITE) # clear screen)
    screen.blit(background_image, [0, 0]) # my image
    all_sprites_group.draw(screen) # draw my sprites
    spacex_group.draw(screen)
    extra_ammo_group.draw(screen)

    screen.blit(my_bullet_text, [30, 770]) # text - is 870
    screen.blit(my_earth_health, [30, 800]) # text - is 900
    screen.blit(my_enemies_left, [30, 830]) # text - is 930
    screen.blit(my_level, [30, 30]) # text
    screen.blit(my_player_health, [300, 770])
    screen.blit(my_ammo_airdrop, [300, 800])




    alien_group.draw(screen) # alien
    comet_group.draw(screen) # and comet draw on screen)


    # draw.line(surface, color, [x1, y1], [x2, y2], optional_width)

    pygame.display.flip() # Update the screen with what we've drawn.

    clock.tick(60)  # frames per second

# makes it so it will either call end screen or win screen - depending on level
if level <= 6:
    end_screen()
if level > 6:
    win_screen()
# Close the window and quit.
pygame.quit()