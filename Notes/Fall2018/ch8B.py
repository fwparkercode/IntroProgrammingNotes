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
speed_x = 3
speed_y = 3

car_x = 0
car_y = 300
car_speed_x = 5

health = 600

red = 0
r_speed = 1

ball_y = 300
ball_speed_y = -5
ball_accel_y = 0.1

my_font = pygame.font.SysFont("Calibri", 30, True, False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    # bouncing ball
    ball_speed_y += ball_accel_y
    ball_y += ball_speed_y

    if ball_y >= screen_height - 50:
        ball_y = screen_height - 50
        ball_speed_y *= -0.9
    if ball_speed_y < 0.05 and ball_speed_y > -0.05:
        ball_speed_y = 0

    # health bar
    health -= 1
    if health < 0:
        health = 0

    # bouncing rectangle
    box_x += speed_x
    box_y += speed_y

    if box_x > screen_width - 50:
        box_x = screen_width - 50
        speed_x *= -1
    if box_x < 0:
        box_x = 0
        speed_x *= -1
    if box_y > screen_height - 50:
        box_y = screen_height - 50
        speed_y *= -1
    if box_y < 0:
        box_y = 0
        speed_y *= -1

    # wrapping car
    car_x += car_speed_x
    if car_x > screen_width:
        car_x = -100

    # color shift
    red += r_speed
    if red >= 255 or red <= 0:
        r_speed *= -1

    screen.fill(WHITE)
    # --- Drawing code should go here
    # bouncing ball
    pygame.draw.ellipse(screen, BLUE, [0, ball_y, 50, 50])
    # health bar
    pygame.draw.rect(screen, RED, [50, 50, health, 20])
    # bouncing box
    pygame.draw.rect(screen, RED, [box_x, box_y, 50, 50])
    # car wrapping
    pygame.draw.rect(screen, (red, 0, 0), [car_x, car_y, 100, 50])
    pygame.draw.ellipse(screen, BLACK, [car_x, car_y + 35, 25, 25])
    pygame.draw.ellipse(screen, BLACK, [car_x + 75, car_y + 35, 25, 25])

    my_text = my_font.render("Score: " + str(health), True, BLACK)
    screen.blit(my_text, [50, 80])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()