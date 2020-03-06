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
score = 0
ball_x = 0

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Define fonts  (if you want to see available fonts >>> pygame.font.get_fonts())
my_font = pygame.font.SysFont("Calibri", 40, True, False)  # step 1

x_offset = -50

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    score += 1
    ball_x += 1

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas
    # line(surface, color, [x0, y0], [x1, y1], optional_width)
    pygame.draw.line(screen, BLACK, [0, 0], [WIDTH, HEIGHT], 3)
    pygame.draw.line(screen, BLACK, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT])
    pygame.draw.line(screen, BLACK, [WIDTH // 2, HEIGHT // 2], [WIDTH, 0], 5)  # center to top right

    # rect(surface, color, [top_leftx, top_lefty, width, height], optional_thickness)
    pygame.draw.rect(screen, GREEN, [0, 0, 100, 50], 2)  # optional_thick not filled in
    pygame.draw.rect(screen, BLUE, [200, 400, 300, 100])
    pygame.draw.rect(screen, GREEN, [200, 400, 50, 50])

    # ellipse(surface, color, [top_leftx, top_lefty, width, height], optional_thickness)
    pygame.draw.ellipse(screen, RED, [0, 0, 100, 50])
    pygame.draw.ellipse(screen, YELLOW, [300, 50, 100, 100])

    # Drawing with loops
    # pinstripes
    for x in range(0, WIDTH, 20):
        pygame.draw.line(screen, MAGENTA, [x, 0], [x, HEIGHT], 5)

    for x in range(0, WIDTH, 20):
        pygame.draw.line(screen, CYAN, [0, 0], [x, HEIGHT], 5)

    # tiles
    for x in range(0, WIDTH, 100):
        for y in range(0, HEIGHT, 100):
            pygame.draw.rect(screen, YELLOW, [x, y, 50, 50])

    # polygon(screen, color, [[x0, y0], [x1, y1], [x2, y2] ...], optional_width)
    pygame.draw.polygon(screen, RED, [[100, 100], [200, 100], [150, 200]])

    # circle(screen, color, [x, y], radius, optional_width)
    pygame.draw.circle(screen, GREEN, [ball_x, 400], 50)

    # text
    my_text = my_font.render("Score: " + str(score), True, BLACK) # step 2 render
    screen.blit(my_text, [40, 40]) # step 3 blit the text

    # screen.fill(WHITE)
    #
    # for x in range(0, WIDTH, 100):
    #     pygame.draw.circle(screen, YELLOW, [100 + x + x_offset, 100], 50)
    #     pygame.draw.circle(screen, BLACK, [80 + x + x_offset, 80], 5)
    #     pygame.draw.circle(screen, BLACK, [120 + x + x_offset, 80], 5)


    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
