"""
Pygame - Class Final
June 2019
by Zach Wrubel
"""
# --- Game overview ---
# This is a multi-level shooting game where the user controls the player with the arrow keys and uses the space bar to
# fire bullets to kill advancing enemies.  To win, kill enough enemies to gather 500 points or run out of lives and die.

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)  # (red, green, blue)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.init()  # starts pygame. do not put anything pygame above this line

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Final Project")

done = False  # condition for the game loop

clock = pygame.time.Clock()

# --- Image resources ---
background_image = pygame.image.load("grass00.png")
car_image = pygame.image.load("pitstop_car_3_left.png")  # car image
enemy_image = pygame.image.load("pitstop_car_1_right.png")
road_sign_image = pygame.image.load("smoko_0.png")
keyboard_image = pygame.image.load("KeyboardButtons.png")

# --- Sound resources ---
background_music = pygame.mixer.Sound("345. Street Justice.wav")  # S in Sound is uppercase
bullet_impact = pygame.mixer.Sound("laser.wav")
collision_sound = pygame.mixer.Sound("qubodup-crash.wav")

background_music.play(-1)

count = 0


# --- Player class ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = car_image  # loads car image file
        self.rect = self.image.get_rect()  # grabs the rectangle based on the surface/image size
        self.rect.x = random.randrange(345, 356)
        self.rect.y = random.randrange(-35, -5)
        self.change_x = random.randrange(-1, 9)
        self.change_y = random.randrange(2, 6)

    def update(self):
        self.rect.x += self.change_x
        if self.rect.right > 450 or self.rect.left < 250:
            self.change_x *= -1

        self.rect.y += self.change_y
        if self.rect.top > screen_height:
            self.rect.bottom = 0


# --- Enemy class ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image  # loads enemy image file
        self.rect = self.image.get_rect()  # grabs the rectangle based on the surface/image size
        self.rect.x = random.randrange(271, 390)  # random x starting position of the enemy
        self.rect.y = random.randrange(-35, -5)  # starts the enemies above the field of view to give time to come down
        self.change_x = random.randrange(-5, 3)  # random x speed of the enemy
        self.change_y = random.randrange(2, 10)  # random y speed of the enemy

    def update(self):
        self.rect.x += self.change_x
        if self.rect.right >= 450:  # keeps the enemies from going too far off the right side of the road
            self.rect.right = 450
            self.change_x *= -1

        if self.rect.left <= 250:  # keep the enemies from going too far off the left side of the road
            self.rect.left = 250
            self.change_x *= -1

        self.rect.y += self.change_y
        if self.rect.top > screen_height:  # brings the enemies to the top after they've passed the bottom of the screen
            self.rect.bottom = random.randrange(-10, 0)

        if count > 15:
            self.change_x += .25  # adds .25 speed to the enemies if there are more than 15 of them
            self.change_y += .25


# --- Bullet class ---
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([8, 8])  # size of the bullet
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 18  # speed of the bullet
        if self.rect.bottom < 0:
            self.kill()  # removes from every Group


# --- Obstacle class ---
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = road_sign_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(280, 380)  # random x position of the obstacle
        self.rect.y = random.randrange(-55, -20)  # random starting y position of the obstacle
        self.change_x = 0
        self.change_y = 8

    def update(self):
        self.rect.y += self.change_y
        if self.rect.top > screen_height:  # returns the obstacle to the top of the screen
            self.rect.bottom = 0


player = Player()
enemy = Enemy()
bullet = Bullet()
obstacle = Obstacle()
player.rect.x = random.randrange(345, 356)  # initial x position of the player at the start
player.rect.bottom = screen_height  # initial y position of the player at the start

# --- Make my sprite groups ---
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(player)
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()

# --- make my blocks ---
for i in range(5):  # 5 enemies
    new_enemy = Enemy()
    all_sprites_group.add(new_enemy)
    enemy_group.add(new_enemy)

# --- make obstacle ---
for i in range(1):
    new_obstacle = Obstacle()
    all_sprites_group.add(new_obstacle)
    obstacle_group.add(new_obstacle)

score = 0
level = 1
lives = 10

# --- FONTS ---
score_font = pygame.font.SysFont("Calibri", 30, True, False)
lives_font = pygame.font.SysFont("Calibri", 30, True, False)
level_font = pygame.font.SysFont("Calibri", 30, True, False)
pit_font = pygame.font.SysFont("Calibri", 22, True, False)
intro_font = pygame.font.SysFont("Calibri", 30, True, False)


# --- Functions ---
def cut_screen():
    done = False
    while not done:  # move the end and lose game cut screens here?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                done = True

        screen.fill(RED)
        text = score_font.render("Level " + str(level), True, BLACK)  # prints the next level to the screen
        screen.blit(text, [screen_width // 2 - 35, screen_height // 2])  # location of the text on the screen
        if level == 1:  # if statement for beginning of game instructions
            text = intro_font.render("Objective: Shoot all the enemies and avoid collisions", True, BLACK)
            screen.blit(text, [screen_width // 2 - 300, 100])
            text = intro_font.render("before you run out of lives.", True, BLACK)
            screen.blit(text, [screen_width // 2 - 300, 130])
            text = intro_font.render("Target score is 500 points.", True, BLACK)
            screen.blit(text, [screen_width // 2 - 300, 160])
            text = intro_font.render("Use the arrow keys to move and the space bar to fire.", True, BLACK)  # directions
            screen.blit(text, [screen_width // 2 - 310, screen_height // 2 + 45])  # location of the text on the screen
            screen.blit(keyboard_image, [screen_width // 7, screen_height // 1.75])  # location of the keyboard image
            pygame.draw.rect(screen, BLACK, [screen_width // 1.8, screen_height // 1.25, 275, 50])  # space bar image
            screen.blit(car_image, [screen_width - 80, screen_height // 3 + 38])  # sample player image
            screen.blit(enemy_image, [screen_width - 75, screen_height // 3 - 40])  # sample enemy image
        text = intro_font.render("Press any key to continue", True, BLACK)
        screen.blit(text, [screen_width // 3.25, screen_height - 30])
        pygame.display.flip()  # update the screen with what we've drawn
        clock.tick(60)  # 60 frames per second


cut_screen()


def win_game():  # function that plays when the player wins the game
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                done = True
                

        if level > 2:
            screen.fill(GREEN)
            bullet_impact.play(3)

            text = score_font.render("You Won!", True, BLACK)
            screen.blit(text, [screen_width // 2 - 50, screen_height // 2])
            text = score_font.render("Score: " + str(score), True, BLACK)
            screen.blit(text, [20, screen_height // 2 - 30])
            text = lives_font.render("Lives: " + str(lives), True, BLACK)
            screen.blit(text, [20, screen_height // 2])
            text = level_font.render("Level: " + str(level), True, BLACK)
            screen.blit(text, [20, screen_height // 2 + 30])
            #print("The player reached the intended score of 500")
            pygame.display.flip()  # update the screen with what we've drawn
            clock.tick(60)  # 60 frames per second


win_game()


def lose_game():  # function that plays when the player loses the game
    done = False
    while not done:  # move the end and lose game cut screens here?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                done = True

    if lives < 1:
        screen.fill(BLACK)
        background_music.stop()
        text = score_font.render("You Lost!", True, WHITE)
        screen.blit(text, [screen_width // 2 - 50, screen_height // 2])
        text = score_font.render("Score: " + str(score), True, WHITE)
        screen.blit(text, [20, screen_height // 2 - 30])
        text = lives_font.render("Lives: 0", True, WHITE)
        screen.blit(text, [20, screen_height // 2])
        text = level_font.render("Level: " + str(level), True, WHITE)
        screen.blit(text, [20, screen_height // 2 + 30])
        #print("The player ran out of lives and lost")
        pygame.display.flip()  # update the screen with what we've drawn
        clock.tick(60)  # 60 frames per second


lose_game()

change_x = 0
change_y = 0
key_x = 0
key_y = screen_height
yellow_y = 0
pit_y = 400

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet()
                new_bullet.rect.center = player.rect.center
                all_sprites_group.add(new_bullet)
                bullet_group.add(new_bullet)
                #print("Fire!")
            elif event.key == pygame.K_RIGHT:  # car speed
                change_x = 10
            elif event.key == pygame.K_LEFT:  # car speed
                change_x = -10
            elif event.key == pygame.K_UP:  # car speed
                change_y = -10
            elif event.key == pygame.K_DOWN:  # car speed
                change_y = 10
            elif event.key == pygame.K_q:
                done = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:  # stops car movement when button is released
                change_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # stops car from moving when button is released
                change_y = 0

    # --- Game logic should go here ---
    yellow_y += 8
    if yellow_y > 70:
        yellow_y = 0

    if pit_y > screen_height + 100:
        pit_y = 0

    key_x += change_x
    key_y += change_y

    if key_x < 270:
        key_x = 270  # prevents from going off the left side
    if key_y > 440 < 460 and key_x > 430:  # make a pit stop/rest area on the right
        key_x = 475
        key_y = 450
        #print("Player is in pit stop")
    if key_x == 475 and key_y == 450:
        change_x = 0
        change_y = 0
    elif key_x > 430:
        key_x = 430  # prevents from going off the right side
    if key_y < 0:
        key_y = 0  # prevents from going off the top
    if key_y > screen_height - 20:
        key_y = screen_height - 20  # prevents from going off the bottom

    # main road boundaries are between 270 and 430 on the x axis for the player
    # main road boundaries are between 0 and screen_height on the y axis for the player

    player.rect.centerx = key_x
    player.rect.centery = key_y
    player_group.update()
    bullet_group.update()
    enemy_group.update()
    obstacle_group.update()

    hit_list = pygame.sprite.spritecollide(player, enemy_group, True)  # true destroys the object run into
    hit_list2 = pygame.sprite.spritecollide(player, obstacle_group, True)  # player is hit by obstacle and loses life

    count = 0
    for enemy in enemy_group:  # count is the number of enemies at a given time
        count += 1

    for hit in hit_list:
        collision_sound.play()
        lives -= 1
        #print("Player was hit: Lives remaining:", lives)

    for hit in hit_list2:
        collision_sound.play()
        lives -= 1

    if count <= 0:
        # go to the next level
        level += 1
        if level + 1:
            count += 5
            cut_screen()
        bullet_group.empty()  # gets rid of everything in group
        all_sprites_group.empty()
        all_sprites_group.add(player)
        for i in range(level * 2 + level):  # level * 2 + level
            new_enemy = Enemy()
            all_sprites_group.add(new_enemy)
            enemy_group.add(new_enemy)
        for i in range(1):  # adds an obstacle to each level
            new_obstacle = Obstacle()
            all_sprites_group.add(new_obstacle)
            obstacle_group.add(new_obstacle)

    # --- check for collision between bullets and enemy ---
    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, True)
        for hit in hit_list:
            bullet.kill()
            score += 1
            bullet_impact.play(1)  # plays the bullet impact sound when an enemy is hit
            #print("Hit! Player score is:", str(score))

    # --- Drawing code should go here ---
    screen.fill(WHITE)

    # --- Blit images here ---
    screen.blit(background_image, [0, 0])  # blits the background image to the screen before everything else

    pygame.draw.rect(screen, GRAY, [250, 0, 200, screen_height])  # Street

    # --- Yellow lane markers ---
    for y in range(-30, screen_height, 75):
        pygame.draw.line(screen, YELLOW, [315, yellow_y + y], [315, yellow_y + 30 + y], 5)  # lines on left side
    for y in range(-30, screen_height, 75):
        pygame.draw.line(screen, YELLOW, [385, yellow_y + y], [385, yellow_y + 30 + y], 5)  # lines on right side

    pygame.draw.rect(screen, GRAY, [430, 0, 70, screen_height])  # pit stop
    pygame.draw.line(screen, WHITE, [450, 0], [450, screen_height], 2)  # pit stop line

    all_sprites_group.draw(screen)

    # --- Render the score and lives text ---
    text = score_font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [30, 30])

    text = lives_font.render("Lives: " + str(lives), True, BLACK)
    screen.blit(text, [30, 60])

    text = level_font.render("Level: " + str(level), True, BLACK)
    screen.blit(text, [30, 90])

    text = pit_font.render("Pit Lane", True, BLACK)
    screen.blit(text, [500, pit_y - 30])

    text = pit_font.render("Pit below here", True, BLACK)
    screen.blit(text, [500, pit_y - 15])

    # --- Check if game has ended ---
    if score >= 500:  # ends the game if score is = or greater than 500, player wins
        win_game()
        bullet_group.empty()  # gets rid of everything in group
        all_sprites_group.empty()  # deletes all the sprites
        pygame.display.flip()  # update the screen with what we've drawn
        clock.tick(30)  # 60 frames per second

    if lives < 1:  # ends the game if lives are less than 1, player loses
        collision_sound.play(2)
        lose_game()
        bullet_group.empty()
        all_sprites_group.empty()  # deletes all the sprites
        pygame.display.flip()  # update the screen with what we've drawn
        clock.tick(30)  # 60 frames per second

    #print(key_x, key_y)

    pygame.display.flip()  # update the screen with what we've drawn
    clock.tick(30)  # 60 frames per second

pygame.quit()  # Close the window and quit.
