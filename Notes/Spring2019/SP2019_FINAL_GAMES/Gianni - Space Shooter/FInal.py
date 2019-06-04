
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 150, 0)
PURPLE = (150, 0, 200)


pygame.init() # starts pygame (Vroom!)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Gianni's Game")

done = False # condition for the game loop


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

background_music = pygame.mixer.Sound("music.wav")
background_music.play(-1)

gun_sound = pygame.mixer.Sound("gun.wav")


class Enemy(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(color)
        self.image = pygame.image.load("ship2.png")
        self.rect = self.image.get_rect()
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
class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.bottom = screen_height
        self.change_x = 0
        self.lives = 5


    def update(self):
        self.rect.x += self.change.x
        if self.rect.right > screen_width or self.rect.lect < 0:
            self.change_x *= -1
        self.rect.y += self.change_y
        if self.rect.top > screen_height:
            self.rect.bottom = 0

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 8])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 8
        if self.rect.bottom < 0:
            self.kill()  # removes from every Group


player = Player(WHITE)
player.rect.x = 0
player.rect.bottom = screen_height


# Make my sprite groups
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(player)
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()


# make my blocks

for i in range(10):
    new_enemy = Enemy(WHITE)
    all_sprites_group.add(new_enemy)
    enemy_group.add(new_enemy)

score = 0
lives = 5
level = 1

# FONTS
score_font = pygame.font.SysFont("Calibri", 30, True, False)
lives_font = pygame.font.SysFont("Calibri", 30, True, False)
background_image = pygame.image.load("space.png")



# FUNCTIONS
def cut_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(WHITE)
        text = score_font.render("Welcome space invader!", True, BLACK)
        screen.blit(text, [215, 250])
        pygame.display.flip()  # Updates the screen
        clock.tick(60)  # 60 frames per second

def cut_screen2():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(WHITE)
        text2 = score_font.render("Next Level click any button to continue!", True, BLACK)
        screen.blit(text2, [125, 250])
        pygame.display.flip()  # Updates the screen
        clock.tick(60)  # 60 frames per second


def end_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(WHITE)
        text = score_font.render("You ran out of lives!", True, BLACK)
        screen.blit(text, [215, 250])
        pygame.display.flip()  # Updates the screen
        clock.tick(60)  # 60 frames per second


cut_screen()


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
            gun_sound.play()
    if player.lives <= 0:
        done = True
        end_screen()



    # --- Game logic should go here
    mouse_pos = pygame.mouse.get_pos()
    player.rect.centerx = mouse_pos[0]
    bullet_group.update()
    enemy_group.update()

    hit_list = pygame.sprite.spritecollide(player, enemy_group, True)

    for hit in hit_list:
        lives -= 1
    if lives <= 0:
        end_screen()
        done = True



    count = 0
    for enemy in enemy_group:
        count += 1

    if count <= 0:
        cut_screen2()
        level += 1
        bullet_group.empty()
        all_sprites_group.empty()
        all_sprites_group.add(player)
        for i in range(10 * level):
            new_block = Enemy(RED)
            new_block.change_y *= 1.5
            new_block.change_x = random.randrange(-level, level + 1)
            all_sprites_group.add(new_block)
            enemy_group.add(new_block)




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

    text = score_font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [30, 30])
    text2 = lives_font.render("Lives: " + str(lives), True, WHITE)
    screen.blit(text2, [30, 50])

    pygame.display.flip()  # Updates the screen
    clock.tick(60)  # 60 frames per second


pygame.quit()