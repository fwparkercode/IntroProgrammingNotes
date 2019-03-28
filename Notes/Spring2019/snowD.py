"""
Pygame base template
by Aaron Lee 2019
"""
import random
import pygame
pygame.init()  # do not put anything pygame above this line

# Define some colors (red, green, blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen_width = 700
screen_height = 500
size = (screen_width, screen_height)  # width, height
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Window Bar Name")

done = False  # condition for my game loop
clock = pygame.time.Clock() # Used to manage how fast the screen updates

snow_list = []

for i in range(500):
    x = random.randrange(screen_width)
    y = random.randrange(screen_height)
    snow_list.append([x, y])

print(snow_list)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop  (user inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code should go here
    screen.fill(BLACK)

    pygame.draw.ellipse(screen, WHITE, [x, y, 7, 7])

    pygame.display.flip() # Update the screen with what we've drawn.

    clock.tick(60)  # frames per second

# Close the window and quit.
pygame.quit()















