"""
Pygame Template
Aaron Lee - 2019
"""
import math

import pygame

pygame.init()  #  initializes pygame


# Define variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
GRAY = (100, 100, 100)
PINK = (255, 200, 200)
ORANGE = (255, 150, 0)
MAROON = (100, 0, 0)
BROWN = (100, 50, 50)
score = 2



SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # condition for my game loop

# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mr. Lee's Game")

clock = pygame.time.Clock()  # creates a clock object that manages updates

# FONTS
# SysFont(name, size, bold, italics)
# in console pygame.font.get_fonts()
my_font = pygame.font.SysFont("signpainter", 40, False, False)  # step 1 of 3


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard, controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    score += 2

    # --- Drawing code goes here
    screen.fill(WHITE)

    # rect(surface, color, [top_left_x, top_left_y, width, height], optional_thickness)
    pygame.draw.rect(screen, RED, [0, 0, 100, 50])
    pygame.draw.rect(screen, BLACK, [0, 0, 100, 50], 3)
    pygame.draw.rect(screen, GREEN, [600, 400, 100, 100])
    pygame.draw.rect(screen, CYAN, [550, 350, 100, 100])

    # ellipse(surface, color, [top_left_x, top_left_y, width, height], optional_thickness)
    # ellipse is drawn inside (circumscribed) the defined rectangle
    pygame.draw.rect(screen, ORANGE, [200, 200, 100, 100])
    pygame.draw.ellipse(screen, PINK, [200, 200, 100, 100])
    pygame.draw.ellipse(screen, MAROON, [SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 100, 400, 100])

    # line(surface, color, [x1, y1], [x2, y2], thickness)
    pygame.draw.line(screen, BLACK, [200, 100], [SCREEN_WIDTH, SCREEN_HEIGHT], 3)

    # drawing with loops
    for x in range(0, SCREEN_WIDTH, 10):
        pygame.draw.line(screen, BLACK, [0, 0], [x, SCREEN_HEIGHT], 2)

    for x in range(0, SCREEN_WIDTH, 40):
        for y in range(0, SCREEN_HEIGHT, 40):
            pygame.draw.rect(screen, MAGENTA, [x, y, 30, 30])

    screen.fill(WHITE)
    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, math.pi / 2, 2)
    pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], math.pi / 2, math.pi, 2)
    pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], math.pi, 3 * math.pi / 2, 2)
    pygame.draw.arc(screen, RED, [20, 220, 250, 200], 3 * math.pi / 2, 2 * math.pi, 2)

    # polygon(surface, color, ([x1, y1], [x2, y2], [x3, y3]...), optional_thickness)
    pygame.draw.polygon(screen, RED, ([0, 0], [200, 0], [100, 200]))

    # draw text
    my_text = my_font.render("Score: " + str(score), True, BLACK)  # render(string, antialias, color) (step 2 of 3)
    screen.blit(my_text, [50, 50])  # blit(rendered_text_object, [x, y])

    pygame.display.flip()  # updates the screen

    clock.tick(60) # frames per second

pygame.quit() # Close the window and quit.
