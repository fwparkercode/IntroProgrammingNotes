"""
Pygame base template
by Aaron Lee 2019
"""

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

def draw_stickman(x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

stick_x = 0
stick_y = 0

key_x = 0
key_y = 0
change_x = 0
change_y = 0

background = WHITE

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            print(event.rel, event.pos, event.buttons)
        elif event.type ==  pygame.MOUSEBUTTONDOWN:
            background = GREEN
            print(event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONUP:
            background = WHITE
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_x = 3
            elif event.key == pygame.K_LEFT:
                change_x = -3
            elif event.key == pygame.K_UP:
                change_y = -3
            elif event.key == pygame.K_DOWN:
                change_y = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                change_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                change_y = 0

    # --- Game logic should go here
    stick_x, stick_y = pygame.mouse.get_pos()
    key_x += change_x
    key_y += change_y

    if key_x < 0:
        key_x = 0 # prevents from going off left side
    if key_x > screen_width - 10:
        key_x = screen_width - 10

    # --- Drawing code should go here
    screen.fill(background)

    draw_stickman(stick_x, stick_y)
    draw_stickman(key_x, key_y)

    pygame.display.flip()  #update the screen
    clock.tick(60)  #60 frames per second

pygame.quit()  #Close the window and quit.

