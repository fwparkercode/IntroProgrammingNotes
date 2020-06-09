"""
Max Brenner
WELCOME TO SPACE SHOOTERS!!! in this game the goal is to stay alive for as long as possible. Move your ship aroiund by
using the mosue pad you can attack the enemy ship by pressing the space bar.
Remember to avoid the enemys bullets and Meteors! an enemys bullet will remove .5 lifes and a meteor will remove 2
you get 10 lifes to start
You can blow up meteors by using a meteor blaster. fire those by pressing B but beware you only get so many. if you hit zero you cant fire any more
So stay alive and have fun
watch out it gets pretty fast real quick
"""
import random
import pygame
pygame.init()  # initializes pygame (need to do this before you use it)
font = pygame.font.SysFont("signpainter", 24, True, True)

font1 = pygame.font.SysFont("signpainter", 70, True, True)
font2 = pygame.font.SysFont("signpainter", 50, True, True)
# Global Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 150, 150)
MAROON = (100, 0, 0)
ORANGE = (255, 150, 0)
PURPLE = (100, 50, 150)

background_speed = 1
gunnership_sound = pygame.mixer.Sound("explosion.wav")
background_sound = pygame.mixer.Sound("space.wav")
metor_expolsion = pygame.mixer.Sound("Cannon.wav")
enemy_bullet_sound = pygame.mixer.Sound("laser1.wav")
background_sound.play(-1)
level = 1
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
done = False  # Loop until the user clicks the close button.
player_x = 0
player_y = 0
mk = 7
size = (1400, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)
Lifes = 10
pygame.display.set_caption("My Game!")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates
enemy_dmg = 100


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(). __init__()
        self.image = pygame.image.load("player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.right > SCREEN_WIDTH - 200:
            self.rect.right = SCREEN_WIDTH - 200


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(). __init__()
        self.image = pygame.image.load("enemy_ship.png")
        self.rect = self.image.get_rect()
        self.change_x = 5 * level

    def update(self):
        self.rect.x += self.change_x
        if self.rect.right >= SCREEN_WIDTH - 200:
            self.rect.right = SCREEN_WIDTH - 200
            self.change_x *= -1
        if self.rect.left <= 0:
            self.rect.left = 0
            self.change_x *= -1
        if random.randrange (27) == 0:   #because the speed increase the bullets become less of an obstacle so you have to increase the rate they apear
            new_enemy_bullet = enemy_bullets()
            new_enemy_bullet.rect.midtop = enemy.rect.midbottom
            all_sprites.add(new_enemy_bullet)
            enemy_bullets_sprites.add(new_enemy_bullet)
            enemy_bullet_sound.play(0)
        if level >= 3:
            if random.randrange (25) == 0:
                new_enemy_bullet = enemy_bullets()
                new_enemy_bullet.rect.midtop = enemy.rect.midbottom
                all_sprites.add(new_enemy_bullet)
                enemy_bullets_sprites.add(new_enemy_bullet)
                enemy_bullet_sound.play(0)
        if level >= 5:
            if random.randrange (15) == 0:
                new_enemy_bullet = enemy_bullets()
                new_enemy_bullet.rect.midtop = enemy.rect.midbottom
                all_sprites.add(new_enemy_bullet)
                enemy_bullets_sprites.add(new_enemy_bullet)
                enemy_bullet_sound.play(0)
        if level >= 7:
            if random.randrange (10) == 0:
                new_enemy_bullet = enemy_bullets()
                new_enemy_bullet.rect.midtop = enemy.rect.midbottom
                all_sprites.add(new_enemy_bullet)
                enemy_bullets_sprites.add(new_enemy_bullet)
                enemy_bullet_sound.play(0)
        if level >= 10:
            if random.randrange (7) == 0:
                new_enemy_bullet = enemy_bullets()
                new_enemy_bullet.rect.midtop = enemy.rect.midbottom
                all_sprites.add(new_enemy_bullet)
                enemy_bullets_sprites.add(new_enemy_bullet)
                enemy_bullet_sound.play(0)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.change_y = -10 * level / 2
        if level == 1:
            self.change_y = -10

    def update(self):
        self.rect.y += self.change_y
        if self.rect.bottom < 0:
            self.kill()


class Health_bar(pygame.sprite.Sprite):
    def __init__(self):
        super(). __init__()
        pygame.draw.rect(screen, ORANGE, [1300, 400, 100, 400])


class Metor(pygame.sprite.Sprite):
    def __init__(self):
        super(). __init__()
        self.image = pygame.image.load("metor_1.png")
        self.rect = self.image.get_rect()
        self.change_x = 20 * level + 5
        self.change_y = 7 * level
        self.rect.x = random.randrange(0, 948)
        self.rect.y = random.randrange(-252, -253, -1)
    def update(self):
        self.rect.y += self.change_y
        if self.rect.top > 800:
            self.kill()


class Metor_killer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("metor_killer.png")
        self.rect = self.image.get_rect()
        self.change_y = -10 * level / 2
        if level == 1:
            self.change_y = - 10
    def update(self):
        self.rect.y += self.change_y
        if self.rect.bottom < 0:
            self.kill()


class enemy_bullets(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.change_y = 10 * level / 2
        if level == 1:
            self.change_y = 10

    def update(self):
        self.rect.y += self.change_y
        if self.rect.bottom > 800:
            self.kill()


# groups
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
metor_killer_sprites = pygame.sprite.Group()
level_group_sprites = pygame.sprite.Group()
enemy_bullets_sprites = pygame.sprite.Group()
Metor_sprites = pygame.sprite.Group()

# instances
player = Player()
all_sprites.add(player)
enemy = Enemy()
metor = Metor()
all_sprites.add(enemy)
enemy_sprites.add(enemy)
Metor_sprites.add(metor)
player_list = pygame.sprite.Group()
player_list.add(player)
all_sprites.add(player_list)
bg_image = pygame.image.load("space1.png")
bg_pos = 0


def intro_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        for x in range(-200, 1400, 200):
            for y in range(-200, 800, 200):
                screen.blit(bg_image, [x, y + bg_pos])
        text_6 = font1.render(("SPACE SHOOTERS"), True, RED)
        text_7 = font.render(("Press Space to shoot bullets"), True, RED)
        text_8 = font.render(("Press B to shoot Meteor Blasters, use them wisely"), True, RED)
        text_9 = font.render(("Avoid the Meteors and enemy Bullets"), True, RED)
        text_10 = font.render(("AND STAY ALIVE!!"), True, RED)
        text_11 = font2.render(("(PRESS SPACE TO START)"), True, RED)
        text_12 = font.render(("Move your ship with the mouse pad"), True, RED)
        text_13 = font.render(("Move the enemys health bar to zero to ge to the next level"), True, RED)
        screen.blit(text_6, [480, 330])
        screen.blit(text_7, [0, 0])
        screen.blit(text_8, [0, 25])
        screen.blit(text_12, [0, 50])
        screen.blit(text_9, [0, 75])
        screen.blit(text_13, [0, 100])
        screen.blit(text_10, [0, 125])
        screen.blit(text_11, [480, 650])

        pygame.display.flip()

        clock.tick(60)


def level_screen():
    '''
    five second cut screen
    '''
    done = False
    for i in range(300):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        if done:
            break


def End_screen():
    screen.fill((RED))
    text_4 = font1.render(("GAME OVER!!"), True, BLACK)
    screen.blit(text_4, [480, 330])
    pygame.display.flip()
    clock.tick(60)

if mk > 0:
    if level == 5 or level == 7 or level == 10:
        Lifes = Lifes + 2

intro_screen()
frame = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:   # bullet shooting code
                new_bullet = Bullet()
                new_bullet.rect.midtop = player.rect.midtop
                all_sprites.add(new_bullet)
                bullet_sprites.add(new_bullet)
                gunnership_sound.play(0)
            if mk > 0:   # cotnrols how many meteor killers you get and where they fire from
                if event.key == pygame.K_b:
                    new_metor_killer = Metor_killer()
                    new_metor_killer.rect.midtop = player.rect.midtop
                    all_sprites.add(new_metor_killer)
                    metor_killer_sprites.add(new_metor_killer)
                    mk -= 1
    # --- Game logic should go here
    screen.fill(BLACK)
    all_sprites.update()
    frame += 1
    if frame% 300 - level * 2  == 0:   #controls amount of meteors
        metor = Metor()
        all_sprites.add(metor)
        Metor_sprites.add(metor)

    for metor_killer in metor_killer_sprites:   #metor killer code
        metor_killer_hit_list = pygame.sprite.spritecollide(metor_killer, Metor_sprites, True)
        for hit in metor_killer_hit_list:
            metor_killer.kill()   #mr lee helped me
            metor_expolsion.play(0)

    for metor in Metor_sprites:
        metor_hit_list = pygame.sprite.spritecollide(metor, player_list, False)
        for hit in metor_hit_list:
            Lifes -= 2   #MR Lee helped me

    for bullet in bullet_sprites:    # player bullets code
       hit_list = pygame.sprite.spritecollide(bullet, enemy_sprites, False)
       for hit in hit_list:
            bullet.kill()
            enemy_dmg += 50 / level + 10

    metor_hit_list = pygame.sprite.spritecollide(player, Metor_sprites, True)   # metor hitting player code
    for hit in metor_hit_list:
        Lifes -= 2

    enemy_hit_list = pygame.sprite.spritecollide(player, enemy_bullets_sprites, True)   # enemy bullet code
    for hit in enemy_hit_list:
        Lifes -= 0.5

    if 800 - enemy_dmg <= 0:  # controls levels and the enemy health bar
        level += 1
        if level >= 3:
            mk += 1
        enemy.kill()
        enemy = Enemy()
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
        level_screen()
        for x in bullet_sprites:
            x.kill()
        for x in enemy_bullets_sprites:
            x.kill()
        enemy_dmg = 100  
        print ("level")

    bg_pos += 1 * level + 1  # Background speed code
    if bg_pos > 200:
        bg_pos = 0   #mr lee helped me
    # --- Drawing code goes here
    for x in range(-200, 1200, 200):   # Scrolling background code
        for y in range(-200, 800, 200):
            screen.blit(bg_image, [x, y + bg_pos])
    all_sprites.draw(screen)
    pygame.draw.rect(screen, ORANGE, [1350, 0, 50, 800 - enemy_dmg])  #enemy health bar
    if Lifes <= 0:
        End_screen()
        player.kill()
        enemy.kill()

    text = font.render(str("Enemy health:"), True, RED) # signifes enemy healh bar
    screen.blit(text, [1200, 0])

    text_2 = font.render(("Lifes: " + str(Lifes)), True, RED)  # Signifies player lifes
    screen.blit(text_2, [1200, 50])

    text_3 = font.render(("Level: " + str(level)), True, RED)  # Signifes curent Level
    screen.blit(text_3, [1200, 100])

    text_5 = font.render(("Meteor blasters:" + str(mk)), True, RED)  # Signifes amount of Meteor Blasters
    screen.blit(text_5, [1200, 150])

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second


pygame.quit()  # Close the window and quit.