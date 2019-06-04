import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

player_x = 0
player_y = 0
change_x = 0
change_y = 0


background_image = pygame.image.load("bam.png")
cactus_image = pygame.image.load("who.png")




class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.image.load("oomp.png")


        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.gravity = 0.2





    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x
        hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in hit_list:
            if self.change_x > 0:
                self.rect.right = wall.rect.left
            elif self.change_x < 0:
                self.rect.left = wall.rect.right


        self.change_y += self.gravity
        self.rect.y += self.change_y
        hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in hit_list:
            if self.change_y > 0:
                self.change_y = 0
                self.rect.bottom = wall.rect.top
            elif self.change_y < 0:
                self.rect.top = wall.rect.bottom

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()


        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Finish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("who.png")
        self.rect = self.image.get_rect() # grabs a rect based on image
        self.rect.x = screen_width - 80
        self.rect.bottom = screen_height


def one_win_screen():
    done = False
    cut_font = pygame.font.SysFont("Times New Roman", 60, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                pygame.quit()
        screen.fill(BLACK)
        click_sound2.play(0)
        win_text = cut_font.render("Player 1 won!", True, WHITE)
        screen.blit(win_text, [240, 250])
        pygame.display.flip()
        clock.tick(60)

def two_win_screen():
    done = False
    cut_font = pygame.font.SysFont("Times New Roman", 60, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                pygame.quit()
        screen.fill(BLACK)
        click_sound2.play(0)
        win_text = cut_font.render("Player 2 won!", True, WHITE)
        screen.blit(win_text, [240, 250])
        pygame.display.flip()
        clock.tick(60)

def open_screen():
    done = False
    cut_font = pygame.font.SysFont("Times New Roman", 28, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(BLACK)
        win_text = cut_font.render("Welcome to desert race!", True, WHITE)
        win_text_2 = cut_font.render("Race your friend!", True, WHITE)
        win_text_3 = cut_font.render("Player one uses arrow keys to move, and player two uses WASD", True, WHITE)
        win_text_4 = cut_font.render("You are a snake looking for a new home, so claim ", True, WHITE)
        win_text_5 = cut_font.render("the cactus before your opponent does, ", True, WHITE)
        win_text_6 = cut_font.render("and be sure to jump over any obstacles!", True, WHITE)
        win_text_7 = cut_font.render("PRESS SPACE TO PLAY", True, WHITE)
        screen.blit(win_text, [270, 200])
        screen.blit(win_text_2, [310, 240])
        screen.blit(win_text_3, [15, 275])
        screen.blit(win_text_4, [100, 310])
        screen.blit(win_text_5, [185, 350])
        screen.blit(win_text_6, [170, 390])
        screen.blit(win_text_7, [255, 450])
        pygame.display.flip()
        clock.tick(60)


# Call this function so the Pygame library can initialize itself
pygame.init()


background_music = pygame.mixer.Sound("Lil Nas X - Old Town Road (ft. Billy Ray Cyrus) [Instrumental].ogg")
background_music.set_volume(0.5)
background_music.play(-1)
click_sound = pygame.mixer.Sound("SFX_Jump_07.wav")
click_sound.set_volume(0.5)

click_sound2 = pygame.mixer.Sound("zapThreeToneUp.ogg")
click_sound2.set_volume(0.5)

# Create an 800x600 sized screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the title of the window
pygame.display.set_caption('Desert Run')

# Create groups
all_sprites_list = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

# Create the objects
player = Player(50, 50)
all_sprites_list.add(player)
player2 = Player(50, 50)
all_sprites_list.add(player2)
cactus = Finish()
all_sprites_list.add(cactus)


wall1 = Wall(0, 130, 700, 10)
wall2 = Wall(100, 245, 900, 10)
wall3 = Wall(0, 360, 700, 10)
wall4 = Wall(100, 480, 900, 10)
wall5 = Wall(0, 599, 900, 10)
wall6 = Wall(200, 450, 40, 40)
wall7 = Wall(300, 205, 40, 40)
wall8 = Wall(280, 330, 40, 40)
wall9 = Wall(450, 330, 40, 40)
wall10 = Wall(-40, 0, 40, 800)
wall11 = Wall(800, 0, 40, 800)
wall12 = Wall(0, -40, 800, 40)


all_sprites_list.add(wall1)
all_sprites_list.add(wall2)
all_sprites_list.add(wall3)
all_sprites_list.add(wall4)
all_sprites_list.add(wall5)
all_sprites_list.add(wall6)
all_sprites_list.add(wall7)
all_sprites_list.add(wall8)
all_sprites_list.add(wall9)
all_sprites_list.add(wall10)
all_sprites_list.add(wall11)
all_sprites_list.add(wall12)
wall_group.add(wall1)
wall_group.add(wall2)
wall_group.add(wall3)
wall_group.add(wall4)
wall_group.add(wall5)
wall_group.add(wall6)
wall_group.add(wall7)
wall_group.add(wall8)
wall_group.add(wall9)
wall_group.add(wall10)
wall_group.add(wall11)
wall_group.add(wall12)
player.walls = wall_group
player2.walls = wall_group


clock = pygame.time.Clock()
done = False

open_screen()
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-4, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(4, 0)
            elif event.key == pygame.K_UP:
                player.change_y = -7
                click_sound.play(0 )
            elif event.key == pygame.K_a:
                player2.changespeed(-4, 0)
            elif event.key == pygame.K_d:
                player2.changespeed(4, 0)
            elif event.key == pygame.K_w:
                player2.change_y = -7
                click_sound.play(0)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(4, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-4, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 4)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 4)
            if event.key == pygame.K_a:
                player2.changespeed(4, 0)
            elif event.key == pygame.K_d:
                player2.changespeed(-4, 0)
            elif event.key == pygame.K_w:
                player2.changespeed(0, 4)
            elif event.key == pygame.K_s:
                player2.changespeed(0, 4)


    # --- Game logic

    # This calls update on all the sprites
    all_sprites_list.update()

    # check for collisions
    if pygame.sprite.collide_rect(player, cactus):
        one_win_screen()
    if pygame.sprite.collide_rect(player2, cactus):
        two_win_screen()
    # -- Draw everything
    # Clear screen
    screen.fill(WHITE)

    screen.blit(background_image, [0, 0])

    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()
