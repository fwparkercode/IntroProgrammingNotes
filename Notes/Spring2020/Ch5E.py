"""
pygame base template
by Aaron Lee 2020
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (120, 120, 120)
ORANGE = (255, 150, 0)
PINK = (255, 200, 200)
MAROON = (100, 0, 0)
MY_GREEN = (72, 110, 19)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
done = False

# Starts up pygame (don't do any pygame stuff before this)
pygame.init()

# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Template")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Font Step 1
# SysFont("font_name", size, Bold, Italics)
my_font = pygame.font.SysFont("Calibri", 40, True, False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    screen.fill(WHITE)
    # --- Drawing code should go here
    # line(surface, color, [x0, y0], [x1, y1], optional_width)
    pygame.draw.line(screen, BLACK, (0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), 3)
    pygame.draw.line(screen, BLACK, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # drawing multiple shapes with a loop
    for x in range(0, SCREEN_WIDTH, 10):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT), 1)

    # for x in range(0, SCREEN_WIDTH, 50):
    #     for y in range(0, SCREEN_HEIGHT, 50):
    #         pygame.draw.rect(screen, GREEN, [x, y, 25, 25])

    # rect(surface, color, [top_leftx, top_lefty, width, height], optional_width)
    pygame.draw.rect(screen, BLUE, [100, 0, 100, 50])
    pygame.draw.rect(screen, RED, [150, 20, 50, 50])
    pygame.draw.rect(screen, CYAN, [300, 200, 50, 50], 3)

    # ellipse(surface, color, [top_leftx, top_lefty, width, height], optional_width)
    pygame.draw.ellipse(screen, MAGENTA, [200, 200, 100, 100])
    pygame.draw.rect(screen, MAGENTA, [200, 200, 100, 100], 3)  # defining rect
    pygame.draw.ellipse(screen, YELLOW, [400, 400, 200, 100])

    # polygon(surface, color, [[x0, y0], [x1, y1], [x2, y2]...], optional_width)
    pygame.draw.polygon(screen, RED, [[100, 100], [200, 100], [150, 200]])

    # circle(surface, color, [centerx, centery], radius, optional_width)
    pygame.draw.circle(screen, YELLOW, [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], 50)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()