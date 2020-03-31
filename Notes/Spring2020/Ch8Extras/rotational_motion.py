"""
Pygame base template
by Aaron Lee 2020
"""
import math

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

# variables
radius = 200
angle = 0  # radians
x = WIDTH // 2
y = HEIGHT // 2
delta_x = 0
delta_y = 0
center = [x, y]

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    angle += 0.05

    delta_x = math.cos(angle) * radius
    delta_y = -math.sin(angle) * radius

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas

    pygame.draw.line(screen, RED, center, [x + delta_x, y + delta_y], 3)
    pygame.draw.circle(screen, RED, [int(x + delta_x), int(y + delta_y)], 10)


    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
