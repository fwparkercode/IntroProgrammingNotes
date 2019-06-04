import random

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (230, 0, 0)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
ORANGE = (200, 125,0 )
PURPLE = (150, 50, 200)
BLUE = (0, 0, 255)

# Call this function so the Pygame library can initialize itself
pygame.init ()

class Enemy ( pygame.sprite.Sprite ):
    def __init__(self):
        super ().__init__ ()
        self.image = pygame.image.load("hot_dog.png")
        #self.image.fill ( RED )
        self.rect = self.image.get_rect ()
        self.changey = random.randrange (1, 10)

    def update(self):
        self.rect.y += self.changey

class Player ( pygame.sprite.Sprite ):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super ().__init__ ()

        # Set height, width
        #self.image = pygame.Surface ( [15, 15] )
        #self.image.fill ( BLACK )
        self.image = pygame.image.load("weinerdog.png")
        self.image_left = pygame.image.load("weinerdog.png")
        self.image_right = pygame.image.load("weinerdog_right.png")

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect ()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        if self.change_x > 0:
            self.image = self.image_right
        elif self.change_x < 0:
            self.image = self.image_left
        self.rect.x += self.change_x
        self.rect.y += self.change_y




# Create an 800x600 sized screen
screen_width = 741
screen_height = 481
screen = pygame.display.set_mode ( [screen_width, screen_height] )

# Set the title of the window
pygame.display.set_caption ( 'Hungry Dachsund' )

# Create the player object


clock = pygame.time.Clock()
done = False
# image resources
background_image = pygame.image.load("kitchen_cut.png")
background_image2 = pygame.image.load("kitchenbackground.png")

dog_image = pygame.image.load ("dog.png")
end_image = pygame.image.load ("endscreen.png")

background_music = pygame.mixer.Sound("mushroom dance_0.ogg")
background_music.set_volume(0.5)
background_music.play(-1)

eating_sound = pygame.mixer.Sound("chomp.ogg")


def cut_screen():
    done = False
    while not done:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(RED)
        screen.blit(background_image, [0,0])
        # Flip screen
        pygame.display.flip ()

        # Pause
        clock.tick ( 60 )

def end_screen():
    done = False
    while not done:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.blit(end_image, [0,0])
        # Flip screen
        pygame.display.flip ()

        # Pause
        clock.tick ( 60 )




# Create my pygame group
all_sprites_list = pygame.sprite.Group ()
enemy_list = pygame.sprite.Group ()



for i in range ( 50 ):
    new_enemy = Enemy ()
    new_enemy.rect.x = random.randrange ( screen_width - new_enemy.rect.width )
    new_enemy.rect.y = random.randrange ( -new_enemy.changey * screen_height * 5, 0 )
    all_sprites_list.add ( new_enemy )
    enemy_list.add ( new_enemy )

score = 0


cut_screen()

player = Player(15,10)
all_sprites_list.add ( player )
player.rect.bottom = screen_height

while not done:

    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed ( -5, 0 )
            elif event.key == pygame.K_RIGHT:
                player.changespeed ( 5, 0 )
            elif event.key == pygame.K_UP:
                player.changespeed ( 0, -5 )
            elif event.key == pygame.K_DOWN:
                player.changespeed ( 0, 5 )

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed ( 5, 0 )
            elif event.key == pygame.K_RIGHT:
                player.changespeed ( -5, 0 )
            elif event.key == pygame.K_UP:
                player.changespeed ( 0, 5 )
            elif event.key == pygame.K_DOWN:
                player.changespeed ( 0, -5 )






    # --- Game logic

    all_sprites_list.update()

    hit_list = pygame.sprite.spritecollide ( player, enemy_list, False )
    for enemy in hit_list:
        score += 1
        print ( score )
        enemy.kill ()
        eating_sound.play ( 0 )

    if score >= 20:
        done = True
        player.kill()



    screen.fill(YELLOW)
    screen.blit ( background_image2, [0, 0] )
    #screen.blit ( , [x, y] )
    all_sprites_list.draw(screen)

    my_font = pygame.font.SysFont ( "Helvetica", 40, True, False )
    my_text = my_font.render ( 'score ' +str ( score ), True, RED )
    screen.blit ( my_text, [10, 10])

    pygame.display.flip ()

    clock.tick ( 60 )

end_screen()
pygame.quit ()

