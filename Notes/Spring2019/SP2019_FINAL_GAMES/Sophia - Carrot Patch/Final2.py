import pygame

import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (167, 223, 232)
ORANGE = (255, 140, 0)
PINK = (255, 209, 236)
GREY = (140, 140, 140)

count = 9
pygame.init()  # starts pygame

block_list = pygame.sprite.Group()
my_font = pygame.font.SysFont('Calibri', 25, True, False)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Sophia's Final")

done = False  # condition for the game loop

# images and Sounds
sound_effect = pygame.mixer.Sound("foom_0.wav")
background_music = pygame.mixer.Sound("awesomeness.wav")
cut_screen_music = pygame.mixer.Sound("wind1.wav")


rabbit = pygame.image.load("PeterRabbit.bmp") # HELP from Mr. Lee - Finding a good image easy to crop
carrot = pygame.image.load("carrot.png")
hammy = pygame.image.load("hammy.png")
background_image = pygame.image.load("grass03.png")

background_music.play(-1) # Replays background music

clock = pygame.time.Clock()

# Character Classes
class Block(pygame.sprite.Sprite): #Enemy
    def __init__(self, color):
        super().__init__()
        self.image = hammy
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

class Player(pygame.sprite.Sprite): # Rabbit
    def __init__(self, color):
        super().__init__()
        self.image = rabbit
        self.rect = self.image.get_rect()  # grabs a rect based on image
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(-screen_height, 0)
        self.change_x = random.randrange(-1, 2)
        self.change_y = random.randrange(1, 3)



class Bullet(pygame.sprite.Sprite): # Bullet
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 8])
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 8
        if self.rect.bottom < 0:
            self.kill()  # removes from every Group


class Carrots(pygame.sprite.Sprite): # Carrots (at bottom of screen)
    def __init__(self, color):
        super().__init__()
        self.image = carrot # HELP from Mr. Lee - getting it to be image not block
        self.rect = self.image.get_rect()  # grabs a rect based on image
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(-screen_height, 0)
        self.change_x = random.randrange(-1, 2)
        self.change_y = random.randrange(1, 3)




player = Player(PINK)
player.rect.x = 0
player.rect.bottom = 450

# Make my sprite groups
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(player)
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
carrots_group = pygame.sprite.Group()


# make my blocks
for i in range(2):
    new_block = Block(GREY)
    all_sprites_group.add(new_block)
    enemy_group.add(new_block)

for x in range(0, screen_width, 80):

    # This represents a block
    block = Carrots(ORANGE)

    block.rect.x = x
    block.rect.bottom = screen_height
    carrots_group.add(block)
    all_sprites_group.add(block)
# HELP from Mr. Lee - creating a line of orange blocks at bottom of screen

score = 0
level = 1

# FONTS
score_font = pygame.font.SysFont("Calibri", 30, True, False)



#  FUNCTIONS
def cut_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            cut_screen_music.play() # playing wind

            if event.type == pygame.KEYDOWN:
                done = True
                print("Next Level")
                print("your score is", score)


        # Printed Instructions
        screen.fill(BLUE)
        my_text1 = my_font.render("Bunnies and Carrots!", True, BLACK)
        screen.blit(my_text1, [30, 30])

        my_text1 = my_font.render("Click the space bar to continue", True, BLACK)
        screen.blit(my_text1, [50, 50])

        my_text1 = my_font.render("Drag the mouse across the screen to move the bunny", True, WHITE)
        screen.blit(my_text1, [20, 100])

        my_text1 = my_font.render("click the mouse pad to shoot.", True, WHITE)
        screen.blit(my_text1, [20, 120])

        my_text1 = my_font.render("Don't get hit by the enemy", True, RED)
        screen.blit(my_text1, [20, 150])

        my_text1 = my_font.render("You are the rabbit and you are protecting your carrots", True, WHITE)
        screen.blit(my_text1, [20, 200])

        my_text1 = my_font.render("from Over the Hedge's very own rabid Hammy", True, WHITE)
        screen.blit(my_text1, [20, 220])

        my_text1 = my_font.render("Sometimes you just have to sacrifice a carrot to survive", True, RED)
        screen.blit(my_text1, [20, 280])

        my_text1 = my_font.render("How many Hammys can you stop before getting caught ", True, BLACK)
        screen.blit(my_text1, [20, 300])

        my_text1 = my_font.render("or before you lose all your carrots?", True, BLACK)
        screen.blit(my_text1, [20, 320])

        pygame.display.flip()  # update the screen
        clock.tick(60)  # 60 frames per second

# Game Over Screen
def game_over_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                done = True
                print("Next Level")
                print("your score is", score)

        screen.fill(BLACK)
        my_text1 = my_font.render("Game Over", True, RED)
        screen.blit(my_text1, [30, 30])
        pygame.display.flip()  # update the screen
        clock.tick(60)  # 60 frames per second

# HELP from Mr. Lee - getting game over screen to appear at end of game
# previously the game would just freeze


cut_screen()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            print("Game Over")
            print("your final score is", score)

        if event.type == pygame.MOUSEBUTTONDOWN:
            new_bullet = Bullet()
            new_bullet.rect.center = player.rect.center
            all_sprites_group.add(new_bullet)
            bullet_group.add(new_bullet)
            sound_effect.play() # playing shooting through air noise

    # --- Game logic should go here
    mouse_pos = pygame.mouse.get_pos()
    player.rect.centerx = mouse_pos[0]
    bullet_group.update()
    enemy_group.update()

    for enemy in enemy_group:
        pygame.sprite.spritecollide(enemy, carrots_group, True)





    hit_list = pygame.sprite.spritecollide(player, enemy_group, True) # Bullet colliding with enemy

    for hit in hit_list:
        game_over_screen()
        done = True
        print("Game Over")
        print("your final score is", score)

    count = 0
    for enemy in enemy_group:
        count += 1

    if count <= 0:
        # go to next level
        cut_screen()
        level += 1
        bullet_group.empty()  # gets rid of everything in group
        all_sprites_group.empty()
        all_sprites_group.add(player)
        for carrot in carrots_group:
            all_sprites_group.add(carrot)
        for i in range(2 * level):
            new_block = Block(GREY)
            new_block.change_x *= (level / 2)  # Makes enemy faster each level
            # new_block.change_y *= level
            # new_block.change_x = random.randrange(-level, level + 1)
            all_sprites_group.add(new_block)
            enemy_group.add(new_block)
            new_carrot = Block(ORANGE)

    if len(carrots_group) == 0:
        game_over_screen()
        done = True
        print("Game Over")
        print("your final score is", score)

    # check for collision between bullets and enemy
    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, True)
        for hit in hit_list:
            bullet.kill()
            score += 1
            print(score)

    # --- Drawing code should go here
    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])
    all_sprites_group.draw(screen)


    text = score_font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [30, 30])



    pygame.display.flip()  #update the screen
    clock.tick(60)  #60 frames per second

pygame.quit()  #Close the window and quit.