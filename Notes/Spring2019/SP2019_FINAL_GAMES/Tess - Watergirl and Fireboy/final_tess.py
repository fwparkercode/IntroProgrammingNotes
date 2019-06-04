import pygame
import random

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SKY_BLUE = (135, 206, 250)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
SLATE_GREY = (112, 128, 144)

pygame.init()

# screen width and height of the screen [width, height]
screen_width = 700
screen_height = 700
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)


# loop until the user clicks the close button.
done = False

# how fast the screen updates
clock = pygame.time.Clock()

# variables
score = 0
level = 3
gem_limit = 0

# classes

class Water(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("watergirl.png")
        self.rect = self.image.get_rect()  # grabs a rect based on image
        self.rect.x = 0
        self.rect.bottom = screen_height - 60
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.friendly = None
        self.friend = None
        self.gravity = 0.5
        self.jumping = False

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        if pygame.sprite.collide_rect(self, self.friend):
            if self.change_x > self.friend.change_x:
                self.rect.right = self.friend.rect.left
            else:
                self.rect.left = self.friend.rect.right

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # did this update cause us to hit a "friendly" block?

        block_hit_list = pygame.sprite.spritecollide(self, self.friendly, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.change_y += self.gravity
        self.rect.y += self.change_y


        # Check and see if we hit anything

        if pygame.sprite.collide_rect(self, self.friend):
            if self.change_y > self.friend.change_y:
                self.rect.bottom = self.friend.rect.top
                self.jumping = False
            else:
                self.rect.top = self.friend.rect.bottom

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.change_y = 0
                self.rect.bottom = block.rect.top
                self.jumping = False
            else:
                self.change_y = 0
                self.rect.top = block.rect.bottom

        # did this update cause us to hit a "friendly" block?
        block_hit_list = pygame.sprite.spritecollide(self, self.friendly, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.change_y = 0
                self.rect.bottom = block.rect.top
                self.jumping = False
            elif self.change_y < 0:
                self.change_y = 0
                self.rect.top = block.rect.bottom

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y


class Fire(Water):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("fireboy.png")
        self.rect.bottom = screen_height - 100


class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height, color):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a black wall
        self.image = pygame.Surface([width, height])
        self.color = color
        self.image.fill(self.color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Gem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("blue_gem.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y


class Fire_Gem(Gem):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("red_gem.png")


class Door(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("blue_door.png")
        self.rect = self.image.get_rect()  # grabs a rect based on image
        self.rect.x = screen_width - 160
        self.rect.bottom = 125


class Fire_Door(Door):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("red_door.png")
        self.rect.x = screen_width - 80


class Water_Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = RED
        self.image.fill(self.color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Fire_Enemy(Water_Enemy):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = BLUE
        self.image.fill(BLUE)


# objects/sprites
watergirl = Water()
fireboy = Fire()
fire_door = Fire_Door()
water_door = Door()

# sprite groups
water_gem_group = pygame.sprite.Group()
fire_gem_group = pygame.sprite.Group()
water_enemy_group = pygame.sprite.Group()
fire_enemy_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

# wall group
wall_list = pygame.sprite.Group()

# outline walls
wall0 = Wall(0, 690, 700, 100, WHITE)
wall_list.add(wall0)
all_sprites_group.add(wall0)

wall1 = Wall(0, 0, 10, 700, WHITE)
wall_list.add(wall1)
all_sprites_group.add(wall1)

wall2 = Wall(10, 0, 790, 10, WHITE)
wall_list.add(wall2)
all_sprites_group.add(wall2)

wall3 = Wall(10, 200, 100, 10, WHITE)
wall_list.add(wall3)
all_sprites_group.add(wall3)

wall4 = Wall(screen_height - 10, 0, 10, screen_width - 10, WHITE)
wall_list.add(wall4)
all_sprites_group.add(wall4)

wall5 = Wall(screen_width - 180, fire_door.rect.bottom, 170, 15, WHITE)
wall_list.add(wall5)
all_sprites_group.add(wall5)

fire_door.rect.bottom = wall5.rect.top
water_door.rect.bottom = wall5.rect.top

# walls to jump off of
# change color level 2
wall6 = Wall(0, 585, 70, 10, WHITE)
wall_list.add(wall6)
all_sprites_group.add(wall6)

wall7 = Wall(150, 400, 80, 10, WHITE)
wall_list.add(wall7)
all_sprites_group.add(wall7)

# change color level 3
wall8 = Wall(570, 350, 60, 10, WHITE)
wall_list.add(wall8)
all_sprites_group.add(wall8)

wall9 = Wall(400, 290, 90, 10, WHITE)
wall_list.add(wall9)
all_sprites_group.add(wall9)

# change color level 4
wall10 = Wall(350, 630, 80, 10, WHITE)
wall_list.add(wall10)
all_sprites_group.add(wall10)

wall11 = Wall(630, 565, 70, 10, WHITE)
wall_list.add(wall11)
all_sprites_group.add(wall11)

# extra walls
wall12 = Wall(350, 470, 70, 10, WHITE)
wall_list.add(wall12)
all_sprites_group.add(wall12)

wall13 = Wall(210, 150, 70, 10, WHITE)
wall_list.add(wall13)
all_sprites_group.add(wall13)

# initial gems, gem group randomized
for i in range(10):
    water_gem = Gem(random.randrange(60, screen_width - 60), random.randrange(80, screen_height - 60))
    water_gem_group.add(water_gem)
    all_sprites_group.add(water_gem)
    fire_gem = Fire_Gem(random.randrange(60, screen_width - 60), random.randrange(80, screen_height - 60))
    fire_gem_group.add(fire_gem)
    all_sprites_group.add(fire_gem)

# wall + gem collisions
for wall in wall_list:
    hit_list = pygame.sprite.spritecollide(water_gem, wall_list, True)
    for hit in hit_list:
        water_gem.kill()
for wall in wall_list:
    hit_list = pygame.sprite.spritecollide(fire_gem, wall_list, True)
    for hit in hit_list:
        fire_gem.kill()

# obstacle + gem collisions
for wall in wall_list:
    hit_list = pygame.sprite.spritecollide(water_gem, water_enemy_group, True)
    for hit in hit_list:
        water_gem.kill()
for wall in wall_list:
    hit_list = pygame.sprite.spritecollide(fire_gem, fire_enemy_group, True)
    for hit in hit_list:
        fire_gem.kill()

# define self.walls and self.friendly and self.friend
watergirl.walls = wall_list
fireboy.walls = wall_list

watergirl.friendly = fire_enemy_group
fireboy.friendly = water_enemy_group

watergirl.friend = fireboy
fireboy.friend = watergirl

# add to all sprites group
all_sprites_group.add(fire_door)
all_sprites_group.add(water_door)

all_sprites_group.add(watergirl)
all_sprites_group.add(fireboy)

# image resources
score_font = pygame.font.SysFont("Calibri", 30, True, False)

# sound resources
level_music = pygame.mixer.Sound("level_up.wav")
gem_sound1 = pygame.mixer.Sound("powerUp5.ogg")
gem_sound2 = pygame.mixer.Sound("powerUp7.ogg")
game_over = pygame.mixer.Sound("GameOver.wav")


# functions
def cut_screen():
    done = False
    cut_font = pygame.font.SysFont("Times New Roman", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(GREY)
        cut_text = cut_font.render("Welcome to", True, BLUE)
        cut2_text = cut_font.render("Fireboy and Watergirl", True, RED)
        instructions_text = cut_font.render("Collect all the gems and then jump to the doors!", True, WHITE)
        instructions2_text = cut_font.render("Watergirl is controlled by W, A, S, and D.", True, BLUE)
        instructions3_text = cut_font.render("She collects blue gems & is killed by red platforms.", True, WHITE)
        instructions4_text = cut_font.render("Fireboy is controlled by the arrows.", True, RED)
        instructions5_text = cut_font.render("He collects red gems & is killed by blue platforms.", True, WHITE)
        instructions6_text = cut_font.render("Collaboration is key!", True, WHITE)
        instructions7_text = cut_font.render("Use your partner as a platform.", True, WHITE)
        instructions8_text = cut_font.render("Leveling up = more gems & obstacles.", True, WHITE)
        instructions9_text = cut_font.render("Press 'Q' to quit and enjoy the 4 levels!", True, WHITE)
        screen.blit(cut_text, [30, 30])
        screen.blit(cut2_text, [185, 30])
        screen.blit(instructions_text, [30, 100])
        screen.blit(instructions2_text, [30, 170])
        screen.blit(instructions3_text, [30, 240])
        screen.blit(instructions4_text, [30, 310])
        screen.blit(instructions5_text, [30, 380])
        screen.blit(instructions6_text, [30, 450])
        screen.blit(instructions7_text, [30, 520])
        screen.blit(instructions8_text, [30, 590])
        screen.blit(instructions9_text, [30, 660])
        pygame.display.flip()
        clock.tick(60)


def end_screen():
    done = False
    cut_font = pygame.font.SysFont("Times New Roman", 50, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(GREY)
        end_text = cut_font.render("You Lost :(", True, RED)
        end2_text = cut_font.render("Better luck next time!", True, BLUE)
        end3_text = cut_font.render("Gems earned: " + str(score), True, WHITE)
        screen.blit(end_text, [0, 0])
        screen.blit(end2_text, [0, 100])
        screen.blit(end3_text, [0, 200])
        pygame.display.flip()
        clock.tick(60)

def win_screen():
    done = False
    cut_font = pygame.font.SysFont("Times New Roman", 50, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(GREY)
        win_text = cut_font.render("You won!", True, BLUE)
        win2_text = cut_font.render("Gems earned: " + str(score), True, RED)
        screen.blit(win_text, [0, 0])
        screen.blit(win2_text, [0, 100])
        pygame.display.flip()
        clock.tick(60)

# cut screen before main program loop
cut_screen()

#  Main Program Loop -----------
while not done:

    # ----------- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                watergirl.changespeed(-3, 0)
            elif event.key == pygame.K_d:
                watergirl.changespeed(3, 0)
            elif event.key == pygame.K_w:
                if not watergirl.jumping:
                    watergirl.change_y = -15
                    watergirl.jumping = True
            elif event.key == pygame.K_LEFT:
                fireboy.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                fireboy.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                if not fireboy.jumping:
                    fireboy.jumping = True
                    fireboy.change_y = -15
            elif event.key == pygame.K_q:
                done = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                watergirl.changespeed(3, 0)
            elif event.key == pygame.K_d:
                watergirl.changespeed(-3, 0)
            elif event.key == pygame.K_LEFT:
                fireboy.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                fireboy.changespeed(-3, 0)

    # --- Game logic should go here

    all_sprites_group.update()

    # level system - empty gem group AND reach doors
    if len(water_gem_group) == 0 and len(fire_gem_group) == 0 and pygame.sprite.collide_rect(fireboy, fire_door) and pygame.sprite.collide_rect(watergirl, water_door):
        level += 1
        gem_limit = 0

        # level two
        if level == 2:
            level_music.play(1)
            # new obstacle for water
            obstacle1 = Water_Enemy(wall6.rect.left, wall6.rect.top - 10, 70, 10)
            wall6.kill()
            water_enemy_group.add(obstacle1)
            all_sprites_group.add(obstacle1)
            # new obstacle for fire
            obstacle2 = Fire_Enemy(wall7.rect.left, wall7.rect.top - 10, 80, 10)
            wall7.kill()
            fire_enemy_group.add(obstacle2)
            all_sprites_group.add(obstacle2)
            # more gems
            for i in range(15):
                if gem_limit <= 30:
                    water_gem = Gem(random.randrange(60, screen_width - 60), random.randrange(80, screen_height - 60))
                    water_gem_group.add(water_gem)
                    gem_limit += 1
                    all_sprites_group.add(water_gem)
                    fire_gem = Fire_Gem(random.randrange(60, screen_width - 60), random.randrange(80, screen_height - 60))
                    fire_gem_group.add(fire_gem)
                    gem_limit += 1
                    all_sprites_group.add(fire_gem)

        # level three
        if level == 3:
            level_music.play(1)
            for i in range(20):
                # new obstalcle for water
                obstacle3 = Water_Enemy(wall8.rect.left, wall8.rect.top - 10, 70, 10)
                wall8.kill()
                water_enemy_group.add(obstacle3)
                all_sprites_group.add(obstacle3)
                # new obstacle for fire
                obstacle4 = Fire_Enemy(wall9.rect.left, wall9.rect.top - 10, 80, 10)
                wall9.kill()
                fire_enemy_group.add(obstacle4)
                all_sprites_group.add(obstacle4)
                # more gems
                if gem_limit <= 40:
                    water_gem = Gem(random.randrange(60, screen_width - 60), random.randrange(80, screen_height - 60))
                    water_gem_group.add(water_gem)
                    all_sprites_group.add(water_gem)
                    gem_limit += 1
                    fire_gem = Fire_Gem(random.randrange(60, screen_width - 60), random.randrange(80, screen_height - 60))
                    fire_gem_group.add(fire_gem)
                    all_sprites_group.add(fire_gem)
                    gem_limit += 1

        # level four
        if level == 4:
            # new obstacle for water
            obstacle5 = Water_Enemy(wall10.rect.left, wall10.rect.top - 10, 70, 10)
            wall10.kill()
            water_enemy_group.add(obstacle5)
            all_sprites_group.add(obstacle5)
            # new obstacle for fire
            obstacle6 = Fire_Enemy(wall11.rect.left, wall11.rect.top - 10, 80, 10)
            wall11.kill()
            fire_enemy_group.add(obstacle6)
            all_sprites_group.add(obstacle6)

            # more gems
            for i in range(25):
                if gem_limit <= 50:
                    water_gem = Gem(random.randrange(30, screen_width - 30), random.randrange(30, screen_height - 30))
                    water_gem_group.add(water_gem)
                    all_sprites_group.add(water_gem)
                    gem_limit += 1
                    fire_gem = Fire_Gem(random.randrange(30, screen_width - 30), random.randrange(30, screen_height - 30))
                    fire_gem_group.add(fire_gem)
                    all_sprites_group.add(fire_gem)
                    gem_limit += 1

        # win game
        if level == 5:
            win_screen()
            done = True

    # check for collisions

    for wall in water_enemy_group:
        hit_list = pygame.sprite.spritecollide(watergirl, water_enemy_group, False)
        for hit in hit_list:
            watergirl.kill()
            game_over.play(1)
            end_screen()
            done = True

    for wall in fire_enemy_group:
        hit_list = pygame.sprite.spritecollide(fireboy, fire_enemy_group, False)
        for hit in hit_list:
            fireboy.kill()
            game_over.play(1)
            end_screen()
            done = True

    for gem in water_gem_group:
        hit_list = pygame.sprite.spritecollide(watergirl, water_gem_group, True)
        for hit in hit_list:
            gem_sound2.play(1)
            score += 1

    for gem in fire_gem_group:
        hit_list = pygame.sprite.spritecollide(fireboy, fire_gem_group, True)
        for hit in hit_list:
            gem_sound1.play(1)
            score += 1


    # --- Screen-clearing code goes here
    screen.fill(GREY)

    # --- Drawing code should go below here!!
    all_sprites_group.draw(screen)
    score_text = score_font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, [30, 30])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()