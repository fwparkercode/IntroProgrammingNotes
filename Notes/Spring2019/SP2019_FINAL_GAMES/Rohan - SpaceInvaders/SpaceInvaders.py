"""
 Pygame base template
 Spring 2019
 by Rohan Jain

"""
import pygame
import random

# Define some colors
# (Red, Green, Blue)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()  # starts pygame (Vroom!)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button
done = False  # condition for the game loop

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Image resources
player_image = pygame.image.load("player.png")
enemy_image1 = pygame.image.load("spacealien.png")
enemy_image2 = pygame.image.load("spacealien2.png")

# Sound resources
shoot_sound = pygame.mixer.Sound("laser1.wav")
explosion_sound = pygame.mixer.Sound("invaderkilled.wav")
player_explosion_sound = pygame.mixer.Sound("explosion.wav")
background_music = pygame.mixer.Sound("spaceinvaders1.wav")
background_music.play()


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        super().__init__()

        self.image = player_image
        self.image_list = []
        self.image_list.append(self.image)


        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(-screen_height, 0)
        self.change_x = 0
        self.change_y = 0
        self.frame = 0

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += 0

    def update(self):
        """ Find a new position for the player"""
        self.frame += 1

        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # Player Restrictions
        if self.rect.right > screen_width:
            self.rect.right = screen_width

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 8])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.change_y = -8

    def update(self):
        self.rect.y += self.change_y
        if self.rect.bottom < 0:
            self.kill()  # removes from every Group
        if self.rect.top > screen_height:
            self.kill()


class Block(pygame.sprite.Sprite):
    # Enemy Class
    def __init__(self, color, x, y):
        super().__init__()

        self.image = pygame.image.load("spacealien.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(-screen_height, 0)
        self.change_x = 1
        self.change_y = 0
        self.frame = 0

    def update(self):
        # Animates Player
        self.frame += 1
        if self.frame % 30 < 15:
            self.image = enemy_image1
        else:
            self.image = enemy_image2
        if self.frame % 10 == 0:
            self.rect.x += self.change_x

        if self.rect.right > screen_width or self.rect.left < 0:
            self.rect.x -= self.change_x
            for enemy in self.my_group:
                enemy.change_x *= -1
                enemy.rect.y += 50

class Enemy_Bullet(Bullet):
    # Adds bullets for the enemy to shoot
    def __init__(self):
        super().__init__()
        self.change_y = 4


player = Player(0, 0)
player.rect.x = 0
player.rect.bottom = screen_height


# Make my sprite groups
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(player)
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()

score = 0
level = 1
lives = 3

score_font = pygame.font.SysFont("Calibri", 30, True, False)

#  FUNCTIONS
def cut_screen(my_text):
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(BLUE)
        text = score_font.render(my_text, True, BLACK)
        screen.blit(text, [(screen_width/2) - 100, screen_height/2])
        pygame.display.flip()
        clock.tick(60)

cut_screen("SPACE INVADERS")

for y in range(50, min(100 * level, 400), 30):
    for x in range(50, 650, 40):
        new_block = Block(RED, 20, 15)
        new_block.change_x *= level
        new_block.rect.x = x
        new_block.rect.y = y
        all_sprites_group.add(new_block)
        enemy_group.add(new_block)
        new_block.my_group = enemy_group

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
            elif event.key == pygame.K_SPACE:
                bullet = Bullet()
                bullet.rect.center = player.rect.center
                all_sprites_group.add(bullet)
                bullet_group.add(bullet)



        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)


    # --- Game logic should go here

    mouse_pos = pygame.mouse.get_pos()
    bullet_group.update()
    player.update()
    enemy_group.update()
    enemy_bullet_group.update()

    hit_list = pygame.sprite.spritecollide(player, enemy_bullet_group, True)

    ""
    # Executes collision
    for hit in hit_list:
        lives -= 1
        player.rect.centerx = screen_width/2
        for bullet in enemy_bullet_group:
            bullet.kill()
        for bullet in bullet_group:
            bullet.kill()


    count = 0
    for enemy in enemy_group:
        if enemy.rect.bottom > screen_height:
            cut_screen("GAME OVER")
            done = True
        if random.randrange(1500) == 0:
            new_bullet = Enemy_Bullet()
            new_bullet.rect.center = enemy.rect.center
            all_sprites_group.add(new_bullet)
            enemy_bullet_group.add(new_bullet)
        count += 1


    if count <= 0:
        # go to next level
        level += 1
        player.change_x = 0
        cut_screen("Level: " + str(level))



        bullet_group.empty()  # gets rid of everything in the group
        all_sprites_group.empty()
        all_sprites_group.add(player)
        for y in range (50, min(30 * level, 400), 30):
            for x in range(50, 650, 40):
                new_block = Block(RED, 20, 15)
                new_block.change_x *= level
                new_block.rect.x = x
                new_block.rect.y = y
                all_sprites_group.add(new_block)
                enemy_group.add(new_block)
                new_block.my_group = enemy_group


    if lives <= 0:
        player_explosion_sound.play()
        cut_screen("GAME OVER!     Score = " + str(score) )
        done = True

    for bullet in bullet_group:
        shoot_sound.play()
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, True)
        for hit in hit_list:
            bullet.kill()
            score += 1
            explosion_sound.play()
            print(score)
            for enemy in enemy_group:
                enemy.change_x *= 1.02

    # --- Drawing code should go here
    screen.fill(WHITE)

    all_sprites_group.draw(screen)

    text = score_font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [30, 30])

    text = score_font.render("Lives: " + str(lives), True, BLACK)
    screen.blit(text, [300, 30])

    pygame.display.flip()   # --- Go ahead and update the screen with what we've drawn.
    clock.tick(60)  # 60 frames per second

pygame.quit() # Close the window and quit