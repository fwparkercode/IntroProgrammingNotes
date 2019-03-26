'''
Pygame Base Template C Period
Spring 2019
by Aaron Lee
'''
import random

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()  # starts pygame (Vroom!)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mr. Lee's Game")

done = False  # condition for the game loop

clock = pygame.time.Clock()

snow_list = []

for i in range(500):
    x = random.randrange(0, screen_width - 5)
    y = random.randrange(0, screen_height - 5)
    snow_list.append([x, y])

print(snow_list)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here
    for i in range(len(snow_list)):
        snow_list[i][1] += 1
        if snow_list[i][1] > screen_height:
            snow_list[i][1] = -5

    # --- Drawing code should go here
    screen.fill(BLACK)

    for flake in snow_list:
        pygame.draw.ellipse(screen, WHITE, [flake[0], flake[1], 5, 5])

    pygame.display.flip()  #update the screen
    clock.tick(60)  #60 frames per second

pygame.quit()  #Close the window and quit.
