"""
Pygame base template
Aaron Lee - 2019
"""

import pygame
pygame.init()  # initializes pygame (need to do this before you use it)


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


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
done = False  # Loop until the user clicks the close button.


size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game!")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

pygame.mouse.set_visible(False)

# Images
background_image = pygame.image.load("bgCave.bmp")
dragon_image = pygame.image.load("dragon.png")

# Sounds
bg_music = pygame.mixer.Sound("bgMusic.wav")
bg_music.set_volume(0.5)  # float from 0 to 1
bg_music.play(-1)  # -1 makes it play forever on loop

fireball_sound = pygame.mixer.Sound("fireball.wav")
# fireball_sound.play(2)

# control variables
dragon_x = 0
dragon_y = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            fireball_sound.play()


    # --- Game logic should go here
    dragon_x, dragon_y = pygame.mouse.get_pos()

    if dragon_x > SCREEN_WIDTH - 135:
        dragon_x = SCREEN_WIDTH - 135

    # --- Drawing code goes here
    #screen.fill(WHITE)
    screen.blit(background_image, [0, 0])
    screen.blit(dragon_image, [dragon_x, dragon_y])

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second


pygame.quit()  # Close the window and quit.