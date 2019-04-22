"""
Pygame base template
by Aaron Lee 2019
"""

import pygame
pygame.init()  # do not put anything pygame above this line

# Define some colors (red, green, blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen_width = 700
screen_height = 500
size = (screen_width, screen_height)  # width, height
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Window Bar Name")

done = False  # condition for my game loop

clock = pygame.time.Clock() # Used to manage how fast the screen updates

pygame.mouse.set_visible(False)

def stick_man(x, y):
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

background = WHITE

key_x = 0
key_y = 0
change_x = 0
change_y = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop  (user inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            background = GREEN
            print(event.pos)
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
            if event.key == pygame.K_RIGHT:
                change_x = 0
            elif event.key == pygame.K_LEFT:
                change_x = 0
            elif event.key == pygame.K_UP:
                change_y = 0
            elif event.key == pygame.K_DOWN:
                change_y = 0

    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    #x, y = pygame.mouse.get_pos() # alternate way
    key_x += change_x
    key_y += change_y

    if key_x < 0:
        key_x = 0  # keep from going off left
    if key_x > screen_width - 15:
        key_x = screen_width - 15  # keep from going off right


    # --- Drawing code should go here
    screen.fill(background)

    stick_man(pos[0], pos[1])
    stick_man(key_x, key_y)

    pygame.display.flip() # Update the screen with what we've drawn.

    clock.tick(60)  # frames per second

# Close the window and quit.
pygame.quit()

