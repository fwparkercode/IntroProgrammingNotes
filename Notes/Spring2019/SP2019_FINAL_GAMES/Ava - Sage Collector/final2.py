import pygame
import random
import datetime

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (127,  127, 127)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (200, 125, 0)
PURPLE = (150, 50, 0)

screen_width = 1280
screen_height = 720
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False  # condition for my game loop

# Used to manage how fast the screen updates
clock = pygame.time.Clock() # used to manage how fast the screen updates
time = 1800  # 30fps
score = 0

background_image = pygame.image.load("ocean.png")
item_image = pygame.image.load("item.png")
player_image = pygame.image.load("player.png")

background_music = pygame.mixer.Sound("background.ogg")
background_music.set_volume(.5)
background_music.play(-1)

item_sound = pygame.mixer.Sound("good.ogg")
collide_sound = pygame.mixer.Sound("bad.ogg")

my_font = pygame.font.SysFont('Calibri', 40, True, False)

#time = datetime.datetime(
#print(time)
#start_time = time.now().second
#print(start_time)


def start_screen():
    done = False
    text = my_font.render("Press any key to Start!!", True, WHITE)
    text2 = my_font.render("Collect all the Sage's in under 60 seconds", True, WHITE)
    text3 = my_font.render("Avoid the walls and try to pass each level", True, WHITE)
    text4 = my_font.render("Made by Ava Rosenberg", True, CYAN)
    text5 = my_font.render("Use the control keys to move", True, WHITE)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(BLACK)

        screen.blit(text, [screen_width // 2 - text.get_rect().width // 2, screen_height // 2 - text.get_rect().height // 2 + 100])
        screen.blit(text2, [screen_width // 2 - text2.get_rect().width // 2, screen_height // 2 - text2.get_rect().height // 2 - 20])
        screen.blit(text3, [screen_width // 2 - text3.get_rect().width // 2, screen_height // 2 - text3.get_rect().height // 2 + 20])
        screen.blit(text5, [screen_width // 2 - text5.get_rect().width // 2, screen_height // 2 - text5.get_rect().height // 2 + 60])
        screen.blit(text4, [screen_width // 2 - text4.get_rect().width // 2, screen_height // 2 - text4.get_rect().height // 2 + 140])

        pygame.display.flip()

        clock.tick(60)


class Item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("item.png")
        self.image.get_rect()
        self.rect = self.image.get_rect()  # grabs the rect based on the image
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(screen_height - self.rect.height)
        self.speed = random.randrange(-8, 9)
        self.change_y = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.change_y
        if self.rect.bottom >= screen_height:
            self.change_y *= -1
        if self.rect.top <= 0:
            self.change_y *= -1


class Wall(pygame.sprite.Sprite):
    def __init__(self, wall_rect):
        super().__init__()
        self.wallnumber = 0
        self.image = pygame.Surface([wall_rect[2], wall_rect[3]])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = wall_rect[0]
        self.rect.y = wall_rect[1]

def cut_screen():
    done = False
    textc = my_font.render("NEW LEVEL!!", True, WHITE)
    textc2 = my_font.render("press an key to continue", True, WHITE)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(BLACK)

        screen.blit(textc, [screen_width // 2 - textc.get_rect().width // 2, screen_height // 2 - textc.get_rect().height // 2 - 20])
        screen.blit(textc2, [screen_width // 2 - textc2.get_rect().width // 2, screen_height // 2 - textc2.get_rect().height // 2 + 20])

        pygame.display.flip()
        clock.tick(60)

def end_screen():
    done = False
    texte = my_font.render("Game Over :(", True, WHITE)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(BLACK)

        screen.blit(texte, [screen_width // 2 - texte.get_rect().width // 2, screen_height // 2 - texte.get_rect().height // 2 - 20])

        pygame.display.flip()
        clock.tick(60)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.rect.center = (screen_width//2, screen_height//2)

        if self.rect.x > 1280:
            self.rect.x = 1280
        if self.rect.y > 720:
            self.rect.y = 720


    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x
        wall_list = pygame.sprite.spritecollide(self, self.walls, False)
        #print(wall_list)
        for wall in wall_list:
            if self.change_x > 0:
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right

            collide_sound.play()

        self.rect.y += self.change_y
        wall_list = pygame.sprite.spritecollide(self, self.walls, False)
        #print(wall_list)
        for wall in wall_list:
            if self.change_y > 0:
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom

            collide_sound.play()




all_sprites_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

player = Player()
all_sprites_group.add(player)

item_group = pygame.sprite.Group()

wall_group = pygame.sprite.Group()

level_walls = [[300, 200, 200, 15], [800, 500, 200, 15], [400, 400, 200, 20], [[600, 600, 15, 200], [200, 750, 200, 15]], [[850, 400, 200, 15], [400, 620, 200, 15]]]

wall1 = Wall([300, 100, 200, 15])
all_sprites_group.add(wall1)
wall_group.add(wall1)

wall2 = Wall([150, 300, 15, 200])
all_sprites_group.add(wall2)
wall_group.add(wall2)

wall3 = Wall([300, 600, 100, 15])
all_sprites_group.add(wall3)
wall_group.add(wall3)

wall4 = Wall([1000, 500, 200, 15])
all_sprites_group.add(wall4)
wall_group.add(wall4)

wall5 = Wall([800, 300, 15, 200])
all_sprites_group.add(wall5)
wall_group.add(wall5)

wall6 = Wall([1000, 175, 200, 15])
all_sprites_group.add(wall6)
wall_group.add(wall6)

player.walls = wall_group


for i in range(50):
    new_coin = Item()
    all_sprites_group.add(new_coin)
    item_group.add(new_coin)

#pygame.set_visible(False)

start_screen()

level = 1

# -------- Main Program Loop -----------
while not done:
# --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-6, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(6, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -6)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 6)
            elif event.key == pygame.K_q:
                done = True

            # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(6, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-6, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 6)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -6)


            # --- Game logic should go here
    #x, y = player.changespeed()
    #player.rect.center = pygame.mouse.get_pos()
    all_sprites_group.update()
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])
    # screen.blit(item_image, [x, y])
    #Sprite.draw()

    # Blit images here (blit background first!)
    hit_list = pygame.sprite.spritecollide(player, item_group, True)
    for hit in hit_list:
        score += 1
        #print(score)
        item_sound.play()

    # --- Game logic should go here
    if player.rect.x < 0:
        player.rect.x = 0

    if player.rect.right > screen_width:
        player.rect.right = screen_width

    if player.rect.y < 0:
        player.rect.y = 0

    if player.rect.bottom > screen_height:
        player.rect.bottom = screen_height

    if (len(item_group)) == 0:
        level += 1
        cut_screen()

        new_wall = Wall(level_walls[level - 1])
        #new_wall.change_y *= level
        # new_wall.health *= level
        all_sprites_group.add(new_wall)
        wall_group.add(new_wall)

        for i in range(50):
            new_coin = Item()
            all_sprites_group.add(new_coin)
            item_group.add(new_coin)

        time += 1800

    #if player.rect.y

    # --- Screen-clearing code goes here
    time -= 1
    if time <= 0:
        end_screen()
        done = True

    #print(time // 60)
    time_text = my_font.render("time:" + str(time//30 + 1), True, WHITE)
    screen.blit(time_text, [20, 50])

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # screen.fill(WHITE)
    #all_sprites_list.update()
    # --- Drawing code should go here
    all_sprites_group.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()  # update the screen with what we've drawn

    #time = 3600 // 2
    # --- Limit to 60 frames per second
    clock.tick(30)  # frames per seconds


# Close the window and quit.
pygame.quit()
