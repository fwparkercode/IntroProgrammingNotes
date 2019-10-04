"""
Pygame base template
Aaron Lee - 2019
"""
import random

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
score = 0


size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game!")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

# Define Font
# SysFont(name, size, bold, italics)
# go to console and type pygame.font.get_fonts()
my_font = pygame.font.SysFont("spaceobsessed", 30, False, False)  # Step 1 of 3


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    if random.randrange(100) == 0:
        score += 10


    # --- Drawing code goes here
    screen.fill(WHITE)

    #  rect(surface, color, [top_left_x, top_left_y, width, height], optional_thickness)
    # optional thickness is for border only object
    pygame.draw.rect(screen, RED, [0, 0, 200, 100])
    pygame.draw.rect(screen, BLUE, [100, 50, 200, 100], 0)
    pygame.draw.rect(screen, BLACK, [100, 50, 200, 100], 3)

    # ellipse(surface, color, [top_left_x, top_left_y, width, height], optional_thickness)
    # ellipse is circumscribed inside the defined rectangle
    pygame.draw.rect(screen, GRAY, [300, 300, 100, 50])
    pygame.draw.ellipse(screen, YELLOW, [300, 300, 100, 50])
    pygame.draw.ellipse(screen, PURPLE, [200, 200, 100, 100])  # I'm a circle

    # line(surface, color, [x1, y1], [x2, y2], optional_thickness)
    # default thickness is 1
    pygame.draw.line(screen, BLACK, [200, 200], [300, 300], 5)
    pygame.draw.line(screen, PURPLE, [SCREEN_WIDTH // 2, 0],[SCREEN_WIDTH // 2, SCREEN_HEIGHT], 5)

    # loops to make repeat objects
    for y in range(0, SCREEN_HEIGHT, 20):
        pygame.draw.line(screen, GREEN, [0, y], [SCREEN_WIDTH, y], 5)
        pygame.draw.line(screen, ORANGE, [0, 0], [SCREEN_WIDTH, y], 3)

    '''
    for rg in range(256):
        pygame.draw.line(screen, (rg, rg, 255), [0, rg * 2], [SCREEN_WIDTH, rg * 2], 2)
    '''

    # polygon(screen, color, ([x1, y1], [x2, y2], [x3, y3]...)
    pygame.draw.polygon(screen, MAROON, ([0, 0], [200, 0], [100, 200]))

    # draw text
    # render(string, anti_alias, color
    my_text = my_font.render("Score: " + str(score), True, WHITE)  # Step 2 of 3
    screen.blit(my_text, [50, 50])  # Step 3 of 3

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second


pygame.quit()  # Close the window and quit.