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

def draw_stick(x, y, color):
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

# Mouse variables
stick_x = 0
stick_y = 0
stick_color = RED

# keyboard variables
key_x = 0
key_y = 0
key_changex = 0
key_changey = 0

pygame.mouse.set_visible(False)  # turn the cursor arrow off

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            #print(event.pos)  # event.pos is the mouse position as a tuple
            stick_x, stick_y = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # pressed the mouse button down
            stick_color = GREEN
            print(event.button, event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            # lifted my finger off the button
            stick_color = RED
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                key_changex = 3
            elif event.key == pygame.K_LEFT:
                key_changex = -3
            elif event.key == pygame.K_UP:
                key_changey = -3
            elif event.key == pygame.K_DOWN:
                key_changey = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                key_changex = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                key_changey = 0


    # --- Game logic should go here
    key_x += key_changex
    key_y += key_changey

    # boundary checks
    if stick_x > WIDTH - 11:
        stick_x = WIDTH - 11

    if key_x < 0:
        key_x = 0

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas

    draw_stick(stick_x, stick_y, stick_color) # mouse control
    draw_stick(key_x, key_y, RED)  # key control

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
