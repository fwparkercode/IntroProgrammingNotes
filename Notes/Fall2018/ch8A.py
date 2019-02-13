"""
 Pygame base template for opening a window

 Intro to Programming
 Aaron Lee 2018
"""

import pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)  # (red, green, blue)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (120, 120, 120)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Template")

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# variables
box_x = 100
box_y = 100
box_speed_x = 3
box_speed_y = 3

car_x = 0
car_y = 300

health = 700

gb = 0
gb_speed = 1

ball_x = 0
ball_y = 450
ball_speed_y = -5
ball_accel_y = 0.05

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    # --- Game logic should go here
    # accelerating ball
    ball_speed_y += ball_accel_y
    ball_y += ball_speed_y

    if ball_y >= screen_height - 50:
        ball_y = screen_height - 50
        ball_speed_y *= -1

    # car color shift
    gb += gb_speed
    if gb >= 255 or gb <= 0:
        gb_speed *= -1

    # health
    health -= 1
    if health < 0:
        health = 0

    # car wrapping
    car_x += 3

    if car_x > screen_width:
        car_x = -100

    # bouncing box
    box_x += box_speed_x
    box_y += box_speed_y
    if box_x > screen_width - 50:
        box_x = screen_width - 50
        box_speed_x *= -1
    if box_x < 0:
        box_x = 0
        box_speed_x *= -1
    if box_y > screen_height - 50:
        box_y = screen_height - 50
        box_speed_y *= -1
    if box_y < 0:
        box_y = 0
        box_speed_y *= -1

    screen.fill(WHITE)
    # --- Drawing code should go here

    # bouncing ball
    pygame.draw.ellipse(screen, MAGENTA, [ball_x, ball_y, 50, 50])
    # bouncing box
    pygame.draw.rect(screen, RED, [box_x, box_y, 50, 50])
    # car wrapping
    pygame.draw.rect(screen, (255, gb, gb), [car_x, car_y, 100, 50])
    pygame.draw.ellipse(screen, BLACK, [car_x, car_y+40, 25, 25])
    pygame.draw.ellipse(screen, BLACK, [car_x+75, car_y+40, 25, 25])
    # health bar
    pygame.draw.rect(screen, BLACK, [18, 18, 704, 24])
    pygame.draw.rect(screen, RED, [20, 20, health, 20])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()