"""
Pygame base template
by Aaron Lee 2020
"""

import pygame

# Define global varibles
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
WIDTH = 600
HEIGHT = 500
done = False

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#  images
bg_image = pygame.image.load("trees.jpg")
squirrel_image = pygame.image.load('squirrel.png')

# sound files
bg_music = pygame.mixer.Sound("bgmusic.ogg")
bg_music.set_volume(0.01)  # float between 0 and 1 (0 to 100%)
# bg_music.play()  # play through one time
#bg_music.play(0)  # one time  (start with 0 in programming)
#bg_music.play(1)  # two time
bg_music.play(-1)  # play forever (loop)

glass_sound = pygame.mixer.Sound('glass.ogg')
cheer_sound = pygame.mixer.Sound('cheer-crowd.ogg')

# animation variables
sq_x = 0
sq_y = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            # sq_x = event.pos[0]
            # sq_y = event.pos[1]
            # or use
            sq_x, sq_y = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            glass_sound.play()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                cheer_sound.play()

    # --- Game logic should go here
    if sq_x <= 0:
        sq_x = 0
        glass_sound.play()


    # --- Drawing code should go here
    #screen.fill(WHITE)  # paint the blank canvas
    screen.blit(bg_image, [0, 0])  # images are moved by top left corner

    screen.blit(squirrel_image, [sq_x, sq_y])

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
