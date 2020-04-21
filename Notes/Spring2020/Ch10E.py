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

def draw_stick(x, y):
    x -= 95
    y -= 83

    # Head
    pygame.draw.ellipse(screen, BLACK, [96 + x, 83 + y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [100 + x, 100 + y], [105 + x, 110 + y], 2)
    pygame.draw.line(screen, BLACK, [100 + x, 100 + y], [95 + x, 110 + y], 2)

    # Body
    pygame.draw.line(screen, RED, [100 + x, 100 + y], [100 + x, 90 + y], 2)

    # Arms
    pygame.draw.line(screen, RED, [100 + x, 90 + y], [104 + x, 100 + y], 2)
    pygame.draw.line(screen, RED, [100 + x, 90 + y], [96 + x, 100 + y], 2)


stick_x = 0
stick_y = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas
    draw_stick(stick_x, stick_y)

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
