"""
Final Project
Zach Joseph -- 2019/2020
"""

# Welcome to Rapid Runner! In this game, the player is continuously running through the city, and avoiding obstacles
# such as trash cans along the way. To regain their health, the player can pick up batteries, which they can find at
# random times during the game. As time progresses, the game gets faster and faster, meaning the player has to be
# just as fast as the program. Good luck!
import pygame
import random

pygame.init()

# GENERAL VARIABLES USED THROUGHOUT GAME
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
done = False

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

health_list = pygame.sprite.Group()

heal_list = pygame.sprite.Group()

pygame.display.set_caption("Final Project")

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

intro_font = pygame.font.SysFont("Pythagoras", 30, True, False)
end_font = pygame.font.SysFont("CG Times", 50, True, False)
game_font = pygame.font.SysFont("Pythagoras", 50, True, False)

background_image = pygame.image.load("city.png")
bg_x = 0

bg_music = pygame.mixer.Sound("background.Wav")
bg_music.set_volume(0.5)
bg_music.play(-1)

jump_sound = pygame.mixer.Sound("jump.wav")

collide_sound = pygame.mixer.Sound("collide.wav")

collect_sound = pygame.mixer.Sound("battery_collect.wav")
collect_sound.set_volume(10)

health = 2
enemy_move = -8
frame = 0

frame_rate = 60
start_time = 0


# INTRO SCREEN -- creates an intro screen function that can be closed out by the player
def intro_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(BLUE)
        my_text1 = intro_font.render("Welcome to Rapid Runner!", True, WHITE)
        screen.blit(my_text1, [350, 40])

        my_text2 = intro_font.render("Use the up arrow to vault over enemy obstacles.", True, WHITE)
        screen.blit(my_text2, [230, 130])

        my_text3 = intro_font.render("Each time you touch a garbage can, you lose a life.", True, WHITE)
        screen.blit(my_text3, [210, 230])

        my_text4 = intro_font.render("Try to make it as far as you can without losing all your lives.", True, WHITE)
        screen.blit(my_text4, [150, 330])

        my_text5 = intro_font.render("Collect battery packs to regenerate your lives!", True, WHITE)
        screen.blit(my_text5, [240, 430])

        my_text6 = intro_font.render("Press any key to begin!", True, WHITE)
        screen.blit(my_text6, [350, 520])
        pygame.display.flip()
        clock.tick(60)


intro_screen()


# GAME OVER FUNCTION -- creates a game over screen that ends the game and shows the player's end time
def game_over():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(WHITE)
        end_text = end_font.render("GAME OVER!", True, BLACK)
        end_time = end_font.render(("YOUR TIME: " + str(time)), True, BLACK)
        screen.blit(end_text, [380, 220])
        screen.blit(end_time, [320, 300])
        pygame.display.flip()
        clock.tick(60)


# CLASSES

# PLAYER CLASS -- defines the player's attributes, as well as its image and allows it to update and jump
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("run1.png")
        self.image_list = [pygame.image.load("run1.png"),
                           pygame.image.load("run2.png"),
                           pygame.image.load("run3.png"),
                           pygame.image.load("run4.png")]
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT
        self.change_y = 0
        self.acceleration = 0.5
        self.frame = 0
        self.image_index = 0

    def update(self):  # allows the player to jump and come back down to the screen, and also updates the frames in
        # order to constantly switch between the images of the player to make it seem like it is running
        self.change_y += self.acceleration
        self.rect.y += self.change_y
        self.frame += 1

        # UPDATING PLAYER IMAGE -- uses the frames to cycle through a list of all possible images player can have to
        # appear like it is running
        if self.frame % 2.5 == 0:
            self.image_index += 1
            self.image = self.image_list[self.image_index % len(self.image_list)]

        # KEEPING PLAYER BACK ON BOTTOM OF SCREEN -- makes sure that the player goes back to the bottom of the screen
        # after jumping
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.change_y = 0


# ENEMY CLASS -- defines the enemy's attributes, as well as its image and allows it to continuously update and move
# as the game goes on
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("garbage.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.right = SCREEN_WIDTH
        self.change_x = enemy_move

    def update(self):  # allows the enemy to move down the screen
        self.rect.x += self.change_x

        # SPAWNING NEW ENEMIES -- when the enemy goes off the screen, a new enemy is spawned, and its speed is
        # slightly faster than the previous one -- Mr. Lee helped give me the idea for spawning new enemies for each
        # collision
        if self.rect.right < 0:
            new = Enemy()
            new.change_x = self.change_x
            new.change_x -= 0.5
            all_sprites.add(new)
            trash_sprites.add(new)
            self.kill()


# BATTERY CLASS -- defines the battery's attributes, as well as its appearance, and constantly creates and spawns new
# batteries
class Battery(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("battery.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.right = SCREEN_WIDTH + 60
        self.change_x = enemy_move
        self.active_timer = random.randrange(120, 240)

    def update(self):  # counts down the random timer and when it reaches zero, the battery moves along the screen
        self.active_timer -= 1
        if self.active_timer < 0:
            self.rect.x += self.change_x

        # SPAWNING MORE BATTERIES -- if the battery goes off the screen, it is sent back to the right hand side to
        # start the process all over again -- Mr. Lee helped me create the active_timer, as I did not know how to do
        # it, and I worked with it from there
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH + 60
            self.active_timer = random.randrange(120, 240)
            self.change_x -= 0.5


# GROUPS -- defines all three groups a sprite can be in, and will allow all of the sprites to be interacted with and
# be drawn onto the screen
all_sprites = pygame.sprite.Group()
trash_sprites = pygame.sprite.Group()
battery_sprites = pygame.sprite.Group()

# INSTANCES -- add the player, enemies, and battery to instances, which allow these sprites to be interacted with and
# moved with simple commands as the game moves on
player = Player()
all_sprites.add(player)

trash = Enemy()
all_sprites.add(trash)
trash_sprites.add(trash)

battery = Battery()
battery_sprites.add(battery)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # CONTROLS FOR JUMPING -- allows the player to jump using the up arrow and change its position
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player.rect.bottom == SCREEN_HEIGHT:  # Matthew Garchik suggested that I
                # add the player.rect.bottom == SCREEN_HEIGHT so the player can only jump once at a time
                player.change_y = -10
                jump_sound.play()

    # TRIGGERING GAME OVER SCREEN -- ends the game except for a game over screen that tells the final time of the player
    if health == 0:
        game_over()
        done = True

    # CREATING A CLOCK -- uses frame rate to create a clock, which is then displayed for the player
    # to see and record as an incentive to keep playing
    timing = frame // frame_rate

    minutes = timing // 60

    second = timing % 60

    time = "{0:02}:{1:02}".format(minutes, second)

    # GAME LOGIC

    # MAKING SPRITES MOVE
    all_sprites.update()
    battery_sprites.update()

    # MAKING BACKGROUND UPDATE AND MOVE
    frame += 1

    bg_x -= 2.5
    if bg_x < -1000:
        bg_x = 0

    # COLLIDING AND HEALTH INFO -- creates lists for when player collides with either the enemy or the battery
    health_list = pygame.sprite.spritecollide(player, trash_sprites, False)
    heal_list = pygame.sprite.spritecollide(player, battery_sprites, False)

    # HEALTH DECREASING FOR ENEMY -- uses the list where player hits enemy to decrease the health of the player,
    # play a sound, and reset the enemy's x position
    for enemy in health_list:
        health -= 1
        collide_sound.play()
        enemy.rect.x += SCREEN_WIDTH

    # HEALTH INCREASING FOR BATTERY -- uses the list where player hits battery to increase the health of the player,
    # play a sound, and reset the battery's position
    for battery in heal_list:
        health += 1
        collect_sound.play()
        battery.active_timer = random.randrange(120, 240)
        battery.rect.x += SCREEN_WIDTH + 60
        battery.change_x -= 0.5

    # DRAWING CODE

    # MOVING THE BACKGROUND -- continuously moves the background's x position to appear that it is endlessly continuing
    screen.fill(WHITE)
    for i in range(2):
        screen.blit(background_image, [bg_x + 1000 * i, 0])

    # DRAWING THE HEALTH INFO -- displays the player's health info, and continuously updates as the player collides
    # with enemies and batteries
    my_text = game_font.render("Health: " + str(health), True, RED)
    screen.blit(my_text, [20, 20])

    # DRAWING THE TIMER -- displays the timer of the game, and continuously updates as time moves on
    time_text = game_font.render("Time: " + str(time), True, RED)
    screen.blit(time_text, [20, 70])

    all_sprites.draw(screen)  # draws every sprite in this list to the screen and makes them behave in the way they
    # are programmed to
    battery_sprites.draw(screen)  # draws the battery sprites to the screen so they can move and appear at random times

    pygame.display.flip()  # updates the screen with what the code contains

    clock.tick(60)  # sets the clock time

pygame.quit()  # adds a quit function
