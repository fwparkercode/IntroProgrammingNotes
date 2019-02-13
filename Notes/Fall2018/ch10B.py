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

def draw_stickman(x, y, color):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, color, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, color, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, color, [5 + x, 7 + y], [1 + x, 17 + y], 2)

pygame.mouse.set_visible(False)
color = RED

player_x = 0
player_y = 0
player_xspeed = 0
player_yspeed = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            color = GREEN
        elif event.type == pygame.MOUSEBUTTONUP:
            color = RED
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_xspeed = 3
            if event.key == pygame.K_LEFT:
                player_xspeed = -3
            if event.key == pygame.K_UP:
                player_yspeed = -3
            if event.key == pygame.K_DOWN:
                player_yspeed = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_xspeed = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_yspeed = 0


    # --- Game logic should go here
    mouse_x, mouse_y = pygame.mouse.get_pos()  # returns x,y position of mouse
    player_x += player_xspeed
    player_y += player_yspeed

    screen.fill(WHITE)

    # --- Drawing code should go here
    draw_stickman(mouse_x, mouse_y, GREEN)
    draw_stickman(player_x, player_y, RED)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()