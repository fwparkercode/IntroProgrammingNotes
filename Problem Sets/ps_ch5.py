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


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.


size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Chapter 5 Problem Set")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

my_font = pygame.font.SysFont("Calibri", 40, True, False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code goes here
    screen.fill((100,100,255))


    pygame.draw.rect(screen, GREEN, [0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, 500])
    pygame.draw.line(screen, BLACK, [0, SCREEN_HEIGHT // 2], [SCREEN_WIDTH, SCREEN_HEIGHT // 2], 3)

    pygame.draw.ellipse(screen, YELLOW, [SCREEN_WIDTH - 100, 0, 100, 100])

    pygame.draw.rect(screen, RED, [SCREEN_WIDTH // 2 - 100, 200, 200, 200])
    pygame.draw.polygon(screen, BLACK, [[SCREEN_WIDTH // 2 - 100, 200],[SCREEN_WIDTH // 2 + 100, 200],[SCREEN_WIDTH // 2, 100]])
    pygame.draw.rect(screen, BLACK, [SCREEN_WIDTH // 2 - 20, 400 - 80, 40, 80])


    text = my_font.render("Your Name", True, WHITE)
    screen.blit(text, [50, 50])



    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second


pygame.quit()  # Close the window and quit.