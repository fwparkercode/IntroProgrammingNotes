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

x_offset = 200
score = 0

# make my font(s)
# SysFont('font_name', font_size, bold, italics)
my_font = pygame.font.SysFont('helvetica', 30, True, False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    screen.fill(WHITE)
    # --- Drawing code should go here

    # Rectangle
    # rect(surface, color, [top_left_x, top_left_y, width, height], optional width)
    pygame.draw.rect(screen, RED, [100, 50, 200, 100])
    pygame.draw.rect(screen, BLUE, [150, 150, 200, 100], 3)

    # Ellipse
    # ellipse(surface, color, [top_left_x, top_left_y, width, height], optional width)
    # ellipse is circumscribed to the inside of the rect
    pygame.draw.ellipse(screen, GREEN, [150, 150, 200, 100])

    # Line
    # line(surface, color, [x1, y1], [x2, y2], width)
    pygame.draw.line(screen, BLACK, [0, 0], [150, 250], 2)
    pygame.draw.line(screen, BLACK, [0, 0], [150, 150], 2)

    # Repeating objects
    for x in range(10, screen_width, 20):
        pygame.draw.line(screen, BLUE, [x, 0], [x, screen_height], 1)
        #pygame.draw.line(screen, RED, [x + 10, 0], [x + 10, screen_height], 10)
    for y in range(10, screen_height, 20):
        pygame.draw.line(screen, BLUE, [0, y], [screen_width, y], 1)

    # Polygon
    # polygon(surface, color, [[x1, y1], [x2, y2], [x3, y3]...], optional_width)
    #x_offset += 1
    pygame.draw.polygon(screen, RED, [[0 + x_offset, 0], [200 + x_offset, 0], [100 + x_offset, 200]])

    # Text
    # make a font (usually outside the loop)
    # render the text (usually inside the loop)
    # render(text, anti_alias, color)
    score += 1
    my_text = my_font.render("Score: " + str(score), True, BLACK)

    # blit the text to the screen.
    #  blit(text_object, [top_left_x, top_left_y])
    screen.blit(my_text, [20, 20])







    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()