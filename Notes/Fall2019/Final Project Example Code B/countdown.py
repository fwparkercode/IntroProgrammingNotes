"""
This program contains a function called centered_text.
You don't have to use a function to do text centering though.
After rendering, you can run the get_width() or get_height() methods
on your rendered text object.  This allows you to center up your
text or place it in alignment with other things on the screen

Important steps:
1) make a font... my_font = pygame.font.SysFont("fontName", size, bold, italics)
2) render the text... my_text = my_font.render("my message", antialias, color)
3) get the width/height...   my_text.get_width() or my_text.get_height()
4) calculate an x and y to place your text based on width/height info
5) blit the rendered text...  screen.blit(my_text, [x, y])

Aaron Lee - 2019
"""

import pygame
import random
pygame.init()  # initializes pygame (necessary before any pygame functions)


# Global Variables
BLACK = (0, 0, 0)  # red, green, blue (RGB)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 200, 200)
MAROON = (100, 0, 0)
ORANGE = (255, 150, 0)
PURPLE = (150, 50, 200)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)  # Screen object we draw to

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates


my_font = pygame.font.SysFont("Calibri", 80, True)

def centered_text(screen, message, color):
    my_text = my_font.render(message, True, color)
    x = SCREEN_WIDTH // 2 - my_text.get_width() // 2
    y = SCREEN_HEIGHT // 2 - my_text.get_height() // 2
    screen.blit(my_text, [x, y])


time = 30 * 60  # 30 second timer at 60fps


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    time -= 1

    # --- Draw to screen
    screen.fill(WHITE)

    centered_text(screen, str(time // 60 + 1), RED)

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.