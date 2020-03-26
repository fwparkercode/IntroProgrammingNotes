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

# animation variables
rect_x = 0
change_x = 5
rect_y = 0
change_y = 5

red = 0

frame = 0  # how many frames have we been running this program


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    frame += 1

    rect_x += change_x
    rect_y += change_y

    # wrap around the screen
    # if rect_x > WIDTH:
    #     rect_x = -50

    # bounce off sides
    if rect_x >= WIDTH - 50:
        change_x *= -1
    if rect_x <= 0:
        change_x *= -1

    if rect_y >= HEIGHT - 50:
        change_y *= -1
    if rect_y <= 0:
        change_y *= -1

    # color shift
    red += 1
    if red > 255:
        # color values cannot go less than 0 or greater than 255 and must be int
        red = 0


    # --- Drawing code should go here
    screen.fill((red, red, red))  # paint the blank canvas

    # blinking
    if frame % 300 >= 60:
        pygame.draw.ellipse(screen, BLUE, [200, 200, 50, 50])
    else:
        pygame.draw.ellipse(screen, RED, [200, 200, 50, 50])


    pygame.draw.rect(screen, BLUE, [rect_x, rect_y, 50, 50])

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
