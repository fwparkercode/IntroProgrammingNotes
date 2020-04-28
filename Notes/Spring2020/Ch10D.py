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

def draw_stickman(x, y, color):
    x -= 95
    y -= 83

    # Head
    pygame.draw.ellipse(screen, BLACK, [96 + x, 83 + y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [100 + x, 100 + y], [105 + x, 110 + y], 2)
    pygame.draw.line(screen, BLACK, [100 + x, 100 + y], [95 + x, 110 + y], 2)

    # Body
    pygame.draw.line(screen, color, [100 + x, 100 + y], [100 + x, 90 + y], 2)

    # Arms
    pygame.draw.line(screen, color, [100 + x, 90 + y], [104 + x, 100 + y], 2)
    pygame.draw.line(screen, color, [100 + x, 90 + y], [96 + x, 100 + y], 2)

# mouse controlled player
stick_x = 0
stick_y = 0
color = RED

# key controlled player
stick_keyx = 100
stick_keyy = 0
stick_changex = 0
stick_changey = 0

pygame.mouse.set_visible(False)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            stick_x, stick_y = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print(event.button)
            color = GREEN
        elif event.type == pygame.MOUSEBUTTONUP:
            color = MAGENTA
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                stick_changex = -3
            elif event.key == pygame.K_RIGHT:
                stick_changex = 3
            elif event.key == pygame.K_DOWN:
                stick_changey = 3
            elif event.key == pygame.K_UP:
                stick_changey = -3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                stick_changex = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                stick_changey = 0

    # --- Game logic should go here
    stick_keyx += stick_changex
    if stick_keyx < 0:
        stick_keyx = 0
    if stick_keyx > WIDTH - 10:
        stick_keyx = WIDTH - 10

    stick_keyy += stick_changey

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas

    draw_stickman(stick_x, stick_y, color)  # mouse controlled

    draw_stickman(stick_keyx, stick_keyy, RED)  # key controlled

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
