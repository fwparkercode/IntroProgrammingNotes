'''
Pygame Base Template C Period
Spring 2019
by Aaron Lee

Animation
Moving
Wrapping
Bouncing
Growing
Color Shift
Snow
'''

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 150, 0)
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

# Animation variables
rect_x = 0
rect_y = 100

ellipse_x = 0
ellipse_y = 200
ellipse_change_x = 5
ellipse_change_y = -1
ellipse_accel_y = 0.1

health = 500

r = 0
g = 0
b = 0

frame = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here
    frame += 1

    rect_x += 4
    if rect_x > screen_width:
        # wraps around to left hand side of screen
        rect_x = -50

    ellipse_x += ellipse_change_x
    if ellipse_x > screen_width - 50:
        ellipse_change_x *= -1
    if ellipse_x < 0:
        ellipse_change_x *= -1

    ellipse_change_y += ellipse_accel_y
    ellipse_y += ellipse_change_y
    if ellipse_y > screen_height - 50:
        ellipse_change_y *= -1
    if ellipse_y < 0:
        ellipse_change_y *= -1

    health -= 1

    if r < 255:
        r += 1

    # --- Drawing code should go here
    screen.fill((r, 255, 255))

    if frame % 20 < 10:
        pygame.draw.rect(screen, RED, [rect_x, rect_y, 50, 50])
    else:
        pygame.draw.rect(screen, BLUE, [rect_x, rect_y, 50, 50])


    pygame.draw.ellipse(screen, GREEN, [ellipse_x, ellipse_y, 50, 50])

    if health < 100:
        pygame.draw.line(screen, RED, [0, 50], [health, 50], 10)  # health bar
    else:
        pygame.draw.line(screen, GREEN, [0, 50], [health, 50], 10)  # health bar

    pygame.display.flip()  #update the screen
    clock.tick(60)  #60 frames per second

pygame.quit()  #Close the window and quit.
