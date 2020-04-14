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
my_color = [0, 0, 0]

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
rect_x = 100
rect_y = 100
change_x = 5
change_y = 5


r = 0
r_speed = 1

health = WIDTH

frame = 0


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    frame += 1
    health -= 1

    rect_x += change_x
    rect_y += change_y

    r += r_speed
    if r >= 255:
        r_speed *= -1
    if r <= 0:
        r_speed *= -1

    my_color = [r, 0, 0]

    # wrapping around the screen
    # if rect_x > WIDTH:
    #     rect_x = -50

    # bounce off edges
    if rect_x > WIDTH - 50:
        # change_x *= -1 # alternate way to write it
        change_x = change_x * -1
    if rect_x < 0:
        change_x *= -1

    if rect_y > HEIGHT - 50:
        change_y *= -1
    if rect_y < 0:
        change_y *= -1



    # --- Drawing code should go here
    screen.fill(my_color)  # paint the blank canvas
    screen.fill(WHITE)

    # blinking
    if frame % 120 < 60:
        pygame.draw.rect(screen, YELLOW, [200, 200, 50, 50])

    if frame < 300:
        pygame.draw.circle(screen, RED, [400, 400], 50)

    pygame.draw.rect(screen, BLUE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, GREEN, [0, 0, health, 40])

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
