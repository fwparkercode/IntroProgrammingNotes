"""
Pygame base template - Period D
by Aaron Lee 2019
"""

import pygame
pygame.init()  # do not put anything pygame above this line

# Define some colors (red, green, blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen_width = 700
screen_height = 500
size = (screen_width, screen_height)  # width, height
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Window Bar Name")

done = False  # condition for my game loop

clock = pygame.time.Clock() # Used to manage how fast the screen updates

#  Animation variables
blue_x = 0
blue_y = 100
red_x = 0
red_y = 200
red_change_x = 5  # speed of the red rect
red_change_y = 3

black_x = 100  # bouncing ball
black_y = 100
black_change_x = 4
black_change_y = -2
black_accel_y = 0.1

health = 500

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop  (user inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here
    health -= 1

    blue_x += 2
    if blue_x > screen_width:
        blue_x = -50  # wraps back to left

    red_x += red_change_x
    if red_x > screen_width - 50:
        red_change_x *= -1
    if red_x < 0:
        red_change_x *= -1

    red_y += red_change_y
    if red_y > screen_height - 50:
        red_change_y *= -1
    if red_y < 0:
        red_change_y *= -1

    black_x += black_change_x
    if black_x > screen_width - 50:
        black_change_x *= -1
    if black_x < 0:
        black_change_x *= -1

    black_change_y += black_accel_y
    black_y += black_change_y
    if black_y > screen_height - 50:
        black_change_y *= -1
    if black_y < 0:
        black_change_y *= -1

    # --- Drawing code should go here

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, [blue_x, blue_y, 50, 50])
    pygame.draw.rect(screen, RED, [red_x, red_y, 50, 50])
    pygame.draw.ellipse(screen, BLACK, [black_x, black_y, 50, 50])


    if health <= 0:
        pass
    elif health < 100:
        pygame.draw.line(screen, RED, [50, 50], [50 + health, 50], 30)
    else:
        pygame.draw.line(screen, GREEN, [50, 50], [50 + health, 50], 30)


    pygame.display.flip() # Update the screen with what we've drawn.

    clock.tick(60)  # frames per second

# Close the window and quit.
pygame.quit()
