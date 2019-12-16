"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""

import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.change_y = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.change_y

        if self.rect.top > screen_height:
            self.rect.bottom = 0



class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
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
        self.rect.x += self.change_x
        self.rect.y += self.change_y


# Call this function so the Pygame library can initialize itself
pygame.init()

screen_width = 800
screen_height = 600

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption('Test')

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.

for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height - 200)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)



# Font
my_font = pygame.font.SysFont("Calibri", 25, True, False)

# Create the player object
player = Player(50, 50)
player.rect.bottom = screen_height
all_sprites_list.add(player)

clock = pygame.time.Clock()
done = False
score = 0
lives = 5

while not done:

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
                player.changespeed(0, 0)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 0)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 0)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 0)

    # --- Game logic

    # This calls update on all the sprites
    all_sprites_list.update()

    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # Check the list of collisions.
    for block in blocks_hit_list:
        lives -= 1
        player.rect.centerx = screen_width // 2
        for block in block_list:
            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randrange(- 200, screen_height - 400)


    if lives < 0:
        done = True  # maybe replace with a game over screen.

    # -- Draw everything
    # Clear screen
    screen.fill(WHITE)

    # Draw sprites
    all_sprites_list.draw(screen)

    my_text = my_font.render("Lives: " + str(lives), True, BLACK)
    screen.blit(my_text, [20, 20])
    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()