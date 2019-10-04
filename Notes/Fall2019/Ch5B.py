"""
Pygame base template
Aaron Lee - 2019
"""

import pygame
pygame.init()  # initializes pygame (necessary before any pygame functions)


# Global Variables
BLACK = (0, 0, 0)  # red, green, blue (RGB)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 200, 200)
MAROON = (100, 0, 0)
ORANGE = (255, 150, 0)
PURPLE = (150, 50, 200)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.
score = 0

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)  # Screen object we draw to

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

# define fonts
# SysFont(name, size, bold, italics)
# pygame.font.get_fonts() to find what fonts you have
my_font = pygame.font.SysFont("signpainter", 40, True, True)  # step 1 of drawing text



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    score += 1

    # --- Draw to screen
    screen.fill(WHITE)
    # rect(surface, color, [top_left_x, top_left_y, width, height], optional_thickness)
    pygame.draw.rect(screen, ORANGE, [400, 100, 50, 100])
    pygame.draw.rect(screen, BLACK, [400, 100, 50, 100], 2)
    pygame.draw.rect(screen, GREEN, [600, 400, 100, 100])
    pygame.draw.rect(screen, CYAN, [550, 350, 100, 100])
    pygame.draw.rect(screen, BLACK, [0, 0, 50, 50], 3)

    # ellipse(surface, color, [top_left_x, top_left_y, width, height], optional_thickness)
    # ellipse is circumscribed on the inside of the defined rect
    pygame.draw.ellipse(screen, PURPLE, [0, 0, 50, 50])
    pygame.draw.ellipse(screen, MAROON, [300, 250, 200, 50])

    # line(surface, color, [x1, y1], [x2, y2], thickness)
    pygame.draw.line(screen, (0, 100, 0), [0, 0], [SCREEN_WIDTH, SCREEN_HEIGHT], 3)

    # loops to make lots of objects
    for x in range(0, SCREEN_WIDTH, 50):
        pygame.draw.line(screen, BLACK, [x, 0], [x, SCREEN_HEIGHT], 5)
        pygame.draw.line(screen, RED, [0, 0], [x, SCREEN_HEIGHT], 2)

    for y in range(0, SCREEN_HEIGHT, 30):
        for x in range(0, SCREEN_WIDTH, 30):
            pygame.draw.rect(screen, BLUE, [x, y, 20, 20])

    # polygon(surface, color, ([x1, y1], [x2, y2], [x3, y3]...))
    pygame.draw.polygon(screen, RED, ([0, 0], [200, 0], [100, 200]))

    # draw text to screen
    #  render(string, antialias, color)
    my_text = my_font.render("Score: " + str(score), True, BLACK)  # step 2
    screen.blit(my_text, [50, 50])  # step 3


    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.