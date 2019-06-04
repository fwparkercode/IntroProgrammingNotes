"""
Coding Final
Spring 2019
Alex Ostrom
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (15, 63, 140)
PURPLE = (83, 13, 96)
NAVY = (10, 3, 35)
NEON_GREEN = (62, 237, 18)
BROWN = (102, 37, 0)
DARK_RED = (102, 37, 0)


pygame.init()# starts pygame

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
center_x = 350
center_y = 250

# Set the caption (different each project)
pygame.display.set_caption("My Game")


done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

stars_list = []


# code for the stars
for i in range(500):
    x = random.randrange(0, screen_width - 5)
    y = random.randrange(0, screen_width - 5)
    stars_list.append([x, y])

#print(stars_list)

#Classes
class Alien(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(color)
        self.image = pygame.image.load("alien.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(-screen_height, 0)
        self.change_x = random.randrange(1, 2)
        self.change_y = random.randrange(1, 2)

    def update(self):
        self.rect.x += self.change_x
        if self.rect.right > screen_width or self.rect.left < 0:
            self.change_x *= -1
        self.rect.y += self.change_y
        if self.rect.top > screen_height:
            self.rect.bottom = 0
            player.health -= 1
            #print(player.health)

class Mega_alien(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(color)
        self.image = pygame.image.load("megaalien.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(-screen_height, 0)
        self.change_x = random.randrange(1, 2)
        self.change_y = random.randrange(1, 2)
        self.health = 5

    def update(self):
        self.rect.x += self.change_x
        if self.rect.right > screen_width or self.rect.left < 0:
            self.change_x *= -1
        self.rect.y += self.change_y
        if self.rect.top > screen_height:
            self.rect.bottom = 0
            player.health -= 1
            #print(player.health)

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.image.load("astronaut.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.bottom = screen_height
        self.change_x = random.randrange(-1, 2)
        self.change_y = 0
        self.health = 10

    def update(self):
        self.rect.x += self.change_x
        if self.rect.right > screen_width or self.rect.left < 0:
            self.change_x *= -1
        self.rect.y += self.change_y
        if self.rect.top > screen_height:
            self.rect.bottom = 0
#bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 8])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 8
        if self.rect.bottom < 0:
            self.kill()

player = Player(BLACK)
player.rect.x = 0
player.rect.bottom = screen_height


# sprites groups
all_sprites_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
all_sprites_group.add(player)
bullet_group = pygame.sprite.Group()
mega_alien_group = pygame.sprite.Group()


#making the alien
for i in range(5):
    new_alien = Alien(RED)
    all_sprites_group.add(new_alien)
    alien_group.add(new_alien)

#making the mega alien
for i in range(1):
    new_mega_alien = Mega_alien(BLUE)
    all_sprites_group.add(new_mega_alien)
    mega_alien_group.add(new_mega_alien)

#fonts
score_font = pygame.font.SysFont("Calibri", 30, True, False)
text_font = pygame.font.SysFont("Calibri", 30, True, False)
welcome_font = pygame.font.SysFont("Calibri", 60, True, False)

# music resources
shooting_sound = pygame.mixer.Sound("shooting.wav")
intro_music = pygame.mixer.Sound("intro_music.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")

#score, level, health
score = 0
level = 1
health = 10

#Functions

#welcome screen
def cut_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            intro_music.play()
            if event.type == pygame.KEYDOWN:
                done = True
        for i in range(len(stars_list)):
            stars_list[i][0] += 0.2
            if stars_list[i][0] > screen_width:
                stars_list[i][0] = -2

        screen.fill(NAVY)
        for star in stars_list:
            pygame.draw.ellipse(screen, WHITE, [star[0], star[1], 5, 5])
        text = welcome_font.render("Welcome to Space Invasion!", True, WHITE)
        screen.blit(text, [20, 100])
        text2 = text_font.render("Your objective in this game is to kill all the aliens!", True, WHITE)
        screen.blit(text2, [45, 150])
        text3 = text_font.render("Do NOT let the aliens touch you or let them get past you.", True, WHITE)
        screen.blit(text3, [10, 180])
        text4 = welcome_font.render("GOOD LUCK!!!", True, WHITE)
        screen.blit(text4, [180, 400])
        text5 = text_font.render("Your health goes down if the aliens past you.", True, WHITE)
        screen.blit(text5, [80, 210])
        text6 = text_font.render("Once your health is 0 you will have lost the game.", True, WHITE)
        screen.blit(text6, [55, 240])

        astronaut_image2 = pygame.image.load("astronaut.png")
        screen.blit(astronaut_image2, [60, 375])
        screen.blit(astronaut_image2, [560, 375])

        pygame.display.flip()
        clock.tick(60)

# other screens
def cut_screen2():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            intro_music.play()
            if event.type == pygame.KEYDOWN:
                done = True
        for i in range(len(stars_list)):
            stars_list[i][0] += 0.2
            if stars_list[i][0] > screen_width:
                stars_list[i][0] = -2

        screen.fill(NAVY)
        for star in stars_list:
            pygame.draw.ellipse(screen, WHITE, [star[0], star[1], 5, 5])

        text = welcome_font.render("You have completed", True, WHITE)
        screen.blit(text, [120, 100])
        text3 = welcome_font.render("this level!", True, WHITE)
        screen.blit(text3, [220, 150])
        text2 = text_font.render("Click to move onto the next level", True, WHITE)
        screen.blit(text2, [160, 400])
        astronaut_image2 = pygame.image.load("astronaut.png")
        screen.blit(astronaut_image2, [60, 375])
        screen.blit(astronaut_image2, [560, 375])


        pygame.display.flip()
        clock.tick(60)
#ending screen
def cut_screen3():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            intro_music.play()
            if event.type == pygame.KEYDOWN:
                done = True
        for i in range(len(stars_list)):
            stars_list[i][0] += 0.2
            if stars_list[i][0] > screen_width:
                stars_list[i][0] = -2
        screen.fill(NAVY)
        for star in stars_list:
            pygame.draw.ellipse(screen, WHITE, [star[0], star[1], 5, 5])
        last_text = welcome_font.render("You are dead!:(", True, WHITE)
        screen.blit(last_text, [175, 150])
        last_text2 = welcome_font.render("Thank you for playing!", True, WHITE)
        screen.blit(last_text2, [89, 200])
        pygame.display.flip()
        clock.tick(60)


cut_screen()
intro_music.stop()


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_bullet = Bullet()
            new_bullet.rect.center = player.rect.center
            all_sprites_group.add(new_bullet)
            bullet_group.add(new_bullet)
            shooting_sound.play()
    if player.health <= 0:
        done = True
        cut_screen3()

    # --- Game logic should go here
    mouse_pos = pygame.mouse.get_pos()
    player.rect.centerx = mouse_pos[0]
    alien_group.update()
    bullet_group.update()
    mega_alien_group.update()

    hit_list = pygame.sprite.spritecollide(player, alien_group, True)
    hit_list2 = pygame.sprite.spritecollide(player, mega_alien_group, True)



    for hit in hit_list:
        cut_screen3()
        done = True

    for hit in hit_list2:
        cut_screen3()
        done = True
    count = 0
    for enemy in alien_group:
        count += 1

    if count <= 0:
        # go to the next level
        intro_music.play()
        cut_screen2()
        intro_music.stop()
        level += 1
        bullet_group.empty()
        all_sprites_group.empty()
        all_sprites_group.add(player)
        player.rect.centerx = screen_width / 2

        for i in range(1):
            new_mega_alien = Mega_alien(BLUE)
            all_sprites_group.add(new_mega_alien)
            mega_alien_group.add(new_mega_alien)

        for i in range(5 * level):
            new_block = Alien(RED)
            new_block.change_y *= level / 3 + 1
            new_block.change_x = random.randrange(1, 2)
            all_sprites_group.add(new_block)
            alien_group.add(new_block)

     #collision
    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, alien_group, True)
        for hit in hit_list:
            bullet.kill()
            score += 1
            #print(score)
            explosion_sound.play()
    for bullet in bullet_group:
        hit_list2 = pygame.sprite.spritecollide(bullet, mega_alien_group, False)
        for hit in hit_list2:
            bullet.kill()
            hit.health -= 1
            if hit.health <= 0:
                new_mega_alien.kill()
                score += 1
            #print(score)
            explosion_sound.play()

    # code for the stars
    for i in range(len(stars_list)):
        stars_list[i][0] += 0.2
        if stars_list[i][0] > screen_width:
            stars_list[i][0] = -2

    # --- Drawing code should go here
    screen.fill(NAVY)

#very background--- number 1
    #drawing code for the stars
    for star in stars_list:
        pygame.draw.ellipse(screen, WHITE, [star[0], star[1], 5, 5])
#---- number 2
    # drawing code for the planet
    pygame.draw.ellipse(screen, BROWN, [0, 435, screen_width, 115])

#---- number 3
    all_sprites_group.draw(screen)
    text = score_font.render("Score:" + str(score), True, WHITE)
    screen.blit(text, [30, 30])
    text2 = score_font.render("Health:" + str(player.health), True, WHITE)
    screen.blit(text2, [30, 50])

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
