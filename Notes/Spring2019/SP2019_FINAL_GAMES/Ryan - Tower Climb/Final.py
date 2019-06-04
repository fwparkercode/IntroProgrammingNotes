# This is a tower-climb game where the objective is to reach the "princess"(the girl) at the top of the tower. Watch out! Bullets will be flying out from the top of the screen and will loop down to try and take away your 3 lives! Your goal is to wrap around the screen/tower to reach the princess and get a high-score. Good luck!
# Controls : RIGHT ARROW KEY - go right, LEFT ARROW KEY - go left, UP ARROW KEY - Jump

import random
import pygame
pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY_BLUE = (130, 170, 255)
YELLOW = (255, 255, 0)

# Character movement variables
key_x = 0
key_y = 0
change_x = 0
change_y = 0

clock = pygame.time.Clock()

# Winning sound
win_sound = pygame.mixer.Sound("Win_sound.wav")
win_sound.set_volume(1.5)
start = False
level = 1
#  background music

backgroundMusic = pygame.mixer.Sound("UpBeatFunk.wav")
backgroundMusic.set_volume(.8)
backgroundMusic.play()

# Jump Sound Effect
jump_sound = pygame.mixer.Sound("JumpSound.wav")
jump_sound.set_volume(5)


my_font = pygame.font.Font("MyFont.ttf", 60)  # My custom font
my_font2 = pygame.font.SysFont("Calibri", 60, True, False)
my_font3 = pygame.font.Font("MyFont.ttf", 137)
my_font4 = pygame.font.SysFont("Calibri", 200, True, False)





# Set the width and height of the screen [width, height]
screen_width = 800
screen_height = 600
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("The Final: Climb The Tower")
done = False
#CLASSES
floor_image = pygame.image.load("Floor.jpg")

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([100, 50])
        self.image = floor_image


        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        for x in range(0, self.rect.width, 100):
            self.image.blit(floor_image, [x, self.rect.y])



class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = -2 * (level)

    def update(self):
        self.rect.x += self.change_x
        if self.rect.right < 0:
            self.rect.left = screen_width
            self.rect.y += 200
        if self.rect.y > screen_height:
            self.kill()



player_image = pygame.image.load("Bunny.png")




class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Set height, width
        self.image = player_image

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        self.health = 3
        self.gravity = 0.2
        # Set speed vector
        self.change_x = 0
        self.change_y = 0


    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""

        self.change_y += self.gravity
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        hit_list = pygame.sprite.spritecollide(self, self.floors, False)
        for floor in hit_list:
            if self.change_y > 0:
                self.change_y = 0
                self.rect.bottom = floor.rect.top
            elif self.change_y < 0:
                self.rect.top = floor.rect.bottom
        if self.rect.x < 0:
            self.rect.x = 0  # keep from going off left
        if self.rect.x > screen_width - 20:
            self.rect.x = screen_width - 20  # keep from going off right
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > screen_height - 20:
            self.rect.y = screen_height - 20
        if self.rect.left > screen_width - 21:
            self.rect.right = 0
            self.rect.y -= 200



win = pygame.image.load("princess.png")

class Princess(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = win
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#Background Image
background = pygame.image.load("Wallpaper.png")

# Cut Screen
def cut_screen():
    done = False
    start_text = my_font.render("Press the Space Bar to", False, WHITE)
    start_text_2 = my_font.render("start the climb!", False, WHITE)
    my_text = my_font3.render("Climb The Tower", False, YELLOW)
    my_text_inst = my_font2.render("(arrow keys to move)", False, YELLOW)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                done = True

            screen.fill(BLACK)
            screen.blit(my_text, [0, 150])
            screen.blit(start_text, [150, screen_height // 2])
            screen.blit(start_text_2, [240, screen_height // 2 + 75])
            screen.blit(my_text_inst, [130, screen_height // 2 + 150])

            pygame.display.flip()
            clock.tick(60)


cut_screen()

def end_screen():
    end_text = my_font3.render("You Died", False, YELLOW)
    end_text_2 = my_font3.render("You got to level", False, WHITE)
    end_text_3 = my_font4.render(str(level), False, WHITE)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                done = True

        screen.fill(BLACK)
        screen.blit(end_text, [150, 75])
        screen.blit(end_text_2, [25, 225])
        screen.blit(end_text_3, [screen_width // 2 - 50, 350])


        pygame.display.flip()
        clock.tick(60)




# Groups
all_sprites_list = pygame.sprite.Group()
floor_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

#Player/Object creation
player = Player(10, 540)

all_sprites_list.add(player)

princess = Princess(650, 75)

all_sprites_list.add(princess)
bullet = Bullet(600, random.randrange(40, 135))







for x in range(0, screen_width, 100):
    floor1 = Floor(x, 550, 0, 0)
    all_sprites_list.add(floor1)
    floor_group.add(floor1)
for x in range(0, screen_width, 100):
    floor2 = Floor(x, 350, 0, 0)
    all_sprites_list.add(floor2)
    floor_group.add(floor2)
for x in range(0, screen_width, 100):
    floor3 = Floor(x, 150, 0, 0)
    all_sprites_list.add(floor3)
    floor_group.add(floor3)




all_sprites_list.add(bullet)
bullet_group.add(bullet)


player.floors = floor_group


#  Collision





# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                jump_sound.play()
                player.changespeed(0, -6)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

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

    if random.randrange(60 // (level / 2)) == 0:
        new_bullet = Bullet(screen_width - 20, random.randrange(40, 140))
        all_sprites_list.add(new_bullet)
        bullet_group.add(new_bullet)

    hit_list = pygame.sprite.spritecollide(player, bullet_group, True)
    for hit in hit_list:
        player.health -= 1
        bullet.kill()
    # End game
    if player.health <= 0:
        end_screen()
        done = True
        break




    # This calls update on all the sprites
    all_sprites_list.update()



    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    my_text_1 = my_font.render("Level", False, BLACK)
    my_text_2 = my_font.render("Health ", False, BLACK)
    my_text_3 = my_font2.render(":", False, BLACK)
    my_text_4 = my_font2.render(str(player.health), False, BLACK)
    my_text_5 = my_font2.render(str(level), False, BLACK)
    screen.blit(background, [0, 0])
    all_sprites_list.draw(screen)
    # Level Text
    screen.blit(my_text_1, [100, 550])
    screen.blit(my_text_3, [225, 550])
    screen.blit(my_text_5, [250, 555])

    # Health Text
    screen.blit(my_text_2, [500, 550])
    screen.blit(my_text_3, [650, 550])
    screen.blit(my_text_4, [675, 555])

    if pygame.sprite.collide_rect(princess, player):
        level += 1
        win_sound.play()

        player.rect.x = 10
        player.rect.y = 540

        for bullet in bullet_group:
            bullet.kill()





    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()