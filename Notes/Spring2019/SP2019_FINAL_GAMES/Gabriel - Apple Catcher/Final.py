
import pygame
import random

# Creating a cut screen for the different levels
# Adding text to the cut screen
# quitting game when 3 rotten apples are hit

# VARIABLES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
done = False
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
APPLE_SIZE = 25
BAD_APPLE_SIZE = 30
level = 1
health = 3
pygame.init()

APPLE = pygame.image.load("apple.png")
Village = pygame.image.load("countryvillage.png")
BADAPPLE = pygame.image.load("rotten_apple.png")
BASKET = pygame.image.load("basket.png")
FOREST = pygame.image.load("forest.png")
heart_image = pygame.image.load('heart.png')


background_music = pygame.mixer.Sound("Backgroundsound.wav")
background_music.set_volume(0.5)
background_music.play(-1)
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# CLASSES




# FUNCTIONS
def cut_screen():
    done = False
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                done = True





        # background image.



        screen.fill(WHITE)
        screen.blit(Village, [-95, 0])

        # --- Drawing code should go here

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)










# Speed and direction of apple



class BadApple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.change_y = random.randrange(2, 4)
        #self.image = APPLE
        self.image = BADAPPLE
        #
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += self.change_y
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-SCREEN_HEIGHT, 0)


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.change_y = random.randrange(2, 4)
        #self.image = pygame.Surface([30, 30])
        #self.image.fill(RED)
        self.image = APPLE
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.change_y
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-SCREEN_HEIGHT, 0)





class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.image = BASKET
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.change_x




# Logic

def intro_screen():
    done = False
    frame = 0
    my_font = pygame.font.SysFont('Helvetica', 40, True, False)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                done = True
                frame = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        frame += 1
        if frame > 600:
            done = True
        screen.fill(BLACK)
        my_text = my_font.render('Click to start.', True, WHITE)
        my_text_2 = my_font.render('Welcome to APPLE DROP', True, WHITE)
        my_text_3 = my_font.render('The goal is to collect', True, WHITE)
        my_text_7 = my_font.render('100 RIPE apples', True, WHITE)
        my_text_4 = my_font.render('But don\'t collect any rotten ones', True, WHITE)
        my_text_5 = my_font.render('you have 3 lives', True, WHITE)
        my_text_6 = my_font.render('each level gets harder.', True, WHITE)
        screen.blit(my_text, [230, 440 - 10])
        screen.blit(my_text_2, [180, 80 - 10])
        screen.blit(my_text_3, [100, 140 - 10])
        screen.blit(my_text_7, [150,200 - 10])
        screen.blit(my_text_4, [60, 260 - 10])
        screen.blit(my_text_5, [210, 320 - 10])
        screen.blit(my_text_6, [150, 380 - 10])

        pygame.display.flip()
        clock.tick(60)




def out_screen():
    done = False
    frame = 0
    my_font = pygame.font.SysFont('Helvetica', 40, True, False)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                done = True
                frame = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        frame += 1
        if frame > 600:
            done = True
        screen.fill(BLACK)
        my_text = my_font.render('Im sorry. You have lost', True, WHITE)
        my_text_2 = my_font.render('GAME OVER!', True, WHITE)
        my_text_3 = my_font.render('Too many rotten apples', True, WHITE)
        my_text_7 = my_font.render('granny does not approve', True, WHITE)
        my_text_4 = my_font.render('', True, WHITE)
        my_text_5 = my_font.render('', True, WHITE)
        my_text_6 = my_font.render('', True, WHITE)
        screen.blit(my_text, [230, 440 - 10])
        screen.blit(my_text_2, [180, 80 - 10])
        screen.blit(my_text_3, [100, 140 - 10])
        screen.blit(my_text_7, [150,200 - 10])
        screen.blit(my_text_4, [60, 260 - 10])
        screen.blit(my_text_5, [210, 320 - 10])
        screen.blit(my_text_6, [150, 380 - 10])

        pygame.display.flip()
        clock.tick(60)

def outwin_screen():
    done = False
    frame = 0
    my_font = pygame.font.SysFont('Helvetica', 40, True, False)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                done = True
                frame = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        frame += 1
        if frame > 600:
            done = True
        screen.fill(BLACK)
        my_text = my_font.render('YOU HAVE WON!!', True, WHITE)
        my_text_2 = my_font.render('GOLD STAR', True, WHITE)
        my_text_3 = my_font.render('100 ripe apples!', True, WHITE)
        my_text_7 = my_font.render('great job', True, WHITE)
        my_text_4 = my_font.render('', True, WHITE)
        my_text_5 = my_font.render('', True, WHITE)
        my_text_6 = my_font.render('', True, WHITE)
        screen.blit(my_text, [230, 440 - 10])
        screen.blit(my_text_2, [180, 80 - 10])
        screen.blit(my_text_3, [100, 140 - 10])
        screen.blit(my_text_7, [150,200 - 10])
        screen.blit(my_text_4, [60, 260 - 10])
        screen.blit(my_text_5, [210, 320 - 10])
        screen.blit(my_text_6, [150, 380 - 10])

        pygame.display.flip()
        clock.tick(60)
all_sprites_group = pygame.sprite.Group()
apple_group = pygame.sprite.Group()
bad_apple_group = pygame.sprite.Group()

score = 0
basket = Basket()
health = 3
basket.rect.bottom = SCREEN_HEIGHT
basket.rect.centerx = SCREEN_WIDTH//2
all_sprites_group.add(basket)
intro_screen()
my_font = pygame.font.SysFont('Helvetica', 30, True, False)


for i in range(level * 2 + 3):


    apple = Apple()
    apple.rect.x = random.randrange(0, SCREEN_WIDTH - apple.rect.width)
    apple.rect.y = random.randrange(-SCREEN_HEIGHT, 0)
    all_sprites_group.add(apple)
    apple_group.add(apple)

    bad_apple = BadApple()
    bad_apple.rect.x = random.randrange(0, SCREEN_WIDTH - bad_apple.rect.width)
    bad_apple.rect.y = random.randrange(-SCREEN_HEIGHT, 0)
    all_sprites_group.add(bad_apple)
    bad_apple_group.add(bad_apple)







# -------- Main Program Loop -----------






while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True




    if len(apple_group) == 0:
        level += 1
        health += 1
        cut_screen()
        all_sprites_group.empty()
        bad_apple_group.empty()
        apple_group.empty()
        all_sprites_group.add(basket)
        for i in range(level * 2 + 3):
            apple = Apple()
            apple.rect.x = random.randrange(0, SCREEN_WIDTH - apple.rect.width)
            apple.rect.y = random.randrange(-SCREEN_HEIGHT, 0)
            all_sprites_group.add(apple)
            apple_group.add(apple)

            bad_apple = BadApple()
            bad_apple.rect.x = random.randrange(0, SCREEN_WIDTH - bad_apple.rect.width)
            bad_apple.rect.y = random.randrange(-SCREEN_HEIGHT, 0)
            all_sprites_group.add(bad_apple)
            bad_apple_group.add(bad_apple)


    # updates (game logic)




    basket.rect.x = pygame.mouse.get_pos()[0]
    all_sprites_group.update()


    apple_group_hit_list = pygame.sprite.spritecollide(basket, apple_group, True)

    for apple in apple_group_hit_list:
        score += 1
        print(score)

    bad_apple_group_hit_list = pygame.sprite.spritecollide(basket, bad_apple_group, True)

    for bad_apple in bad_apple_group_hit_list:
        health -= 1
        print(health)


    if health <= 0:
        out_screen()
        done = True




    screen.blit(FOREST, [0,0])

    all_sprites_group.draw(screen)
    my_text_22 = my_font.render("Score: " + str(score), True, WHITE)
    screen.blit(my_text_22, [20, 80])

    my_text_23 = my_font.render("Lives:", True, WHITE)
    screen.blit(my_text_23, [20, 50])

    for x in range(20 + my_text_23.get_rect().width, 20 + heart_image.get_rect().width * (health + 1), heart_image.get_rect().width):
        screen.blit(heart_image, [x, 50])


    if score >= 100:
        outwin_screen()
        done = True

    pygame.display.flip()
    clock.tick(60)

# Close the window and quit.
pygame.quit()

