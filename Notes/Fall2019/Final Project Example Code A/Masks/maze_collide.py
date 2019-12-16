"""
Maze game with sprite mask
"""

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Maze(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("maze.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.image.load("circle.png").convert()
        self.image.set_colorkey(BLACK)
        self.mask = pygame.mask.from_surface(self.image)

        # Make our top-l# See if the player block has collided with anything.
        #     blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
        #
        #     # Check the list of collisions.
        #     for block in blocks_hit_list:
        #         score += 1
        #         print(score)eft corner the passed-in location.
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

# Create an 800x600 sized screen
screen = pygame.display.set_mode([540, 540])

# Set the title of the window
pygame.display.set_caption('Test')

# Create the player object
player = Player(0, 0)
maze = Maze()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
all_sprites_list.add(maze)

clock = pygame.time.Clock()
done = False


# image
vero = pygame.image.load("vero.jpg")
timer = 0
show = False

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
                player.changespeed(0, -3)
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

    # --- Game logic


    # This calls update on all the sprites
    all_sprites_list.update()

    if pygame.sprite.collide_mask(player, maze):
        show = True

    if show:
        screen.blit(vero, [0, 0])
        timer += 1
    else:
        screen.fill(WHITE)
        all_sprites_list.draw(screen)

    if timer > 100:
        done = True

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()