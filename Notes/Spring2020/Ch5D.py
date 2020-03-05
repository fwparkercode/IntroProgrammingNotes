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
WIDTH = 800
HEIGHT = 600
done = False

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas
    # line(surface, color, [x0, y0], [x1, y1], optional_width)
    pygame.draw.line(screen, BLACK, [0, 0], [WIDTH, HEIGHT], 3)
    pygame.draw.line(screen, BLACK, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT])
    pygame.draw.line(screen, BLACK, [WIDTH // 2, HEIGHT // 2], [WIDTH, 0], 5)  # center to top right

    # rect(surface, color, [top_leftx, top_lefty, width, height], optional_thickness)
    pygame.draw.rect(screen, GREEN, [0, 0, 100, 50], 2)  # optional_thick not filled in
    pygame.draw.rect(screen, BLUE, [200, 400, 300, 100])
    pygame.draw.rect(screen, GREEN, [200, 400, 50, 50])

    # ellipse(surface, color, [top_leftx, top_lefty, width, height], optional_thickness)
    pygame.draw.ellipse(screen, RED, [0, 0, 100, 50])
    pygame.draw.ellipse(screen, YELLOW, [300, 50, 100, 100])

    # Drawing with loops
    # pinstripes
    for x in range(0, WIDTH, 20):
        pygame.draw.line(screen, MAGENTA, [x, 0], [x, HEIGHT], 5)

    for x in range(0, WIDTH, 20):
        pygame.draw.line(screen, CYAN, [0, 0], [x, HEIGHT], 5)

    # tiles
    for x in range(0, WIDTH, 100):
        for y in range(0, HEIGHT, 100):
            pygame.draw.rect(screen, RED, [x, y, 50, 50])

    # polygon
    # circle
    # text

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
