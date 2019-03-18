"""
Pygame base template
by Aaron Lee 2019
"""

import pygame
pygame.init()  # do not put anything pygame above this line

# Define some colors (red, green, blue)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (200, 125, 0)
PURPLE = (150, 50, 200)

screen_width = 700
screen_height = 500
size = (screen_width, screen_height)  # width, height
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Window Bar Name")

done = False  # condition for my game loop

clock = pygame.time.Clock() # Used to manage how fast the screen updates

x_pos = 0

my_font = pygame.font.SysFont("Calibri", 30, True, False)

x_offset = -200


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop  (user inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code should go here
    screen.fill(BLUE)

    # draw.line(surface, color, [x1, y1], [x2, y2], optional_width)
    pygame.draw.line(screen, BLACK, [0, 0], [screen_width, screen_height], 3)
    pygame.draw.line(screen, BLACK, [0, screen_height // 2], [screen_width, screen_height // 2], 3)
    pygame.draw.line(screen, BLACK, [0, screen_height], [screen_width, 0], 3)



    for x in range(0, screen_width, 30):
        pygame.draw.line(screen, BLACK, [x, 0], [x, screen_height], 15)
        pygame.draw.line(screen, CYAN, [x + 15, 0], [x + 15, screen_height], 15)

    screen.fill(WHITE)

    # draw.rect(surface, color, [top_leftx, top_lefty, width, height], optional_width)
    pygame.draw.rect(screen, BLUE, [400, 50, 200, 100])
    pygame.draw.rect(screen, BLACK, [400, 50, 200, 100], 3)  #border

    x_pos += 1
    pygame.draw.rect(screen, RED, [x_pos, 100, 20, 200])
    pygame.draw.rect(screen, PURPLE, [300, 300, 50, 100], 3)


    # draw.ellipse(surface, color, [top_leftx, top_lefty, width, height], optional_width)
    # ellipse is circumscribed inside the defined rectangle
    pygame.draw.ellipse(screen, PURPLE, [300 + x_offset, 400, 50, 50])
    pygame.draw.rect(screen, PURPLE, [300 + x_offset, 400, 50, 50], 5)  # Circle

    # draw.polygon(surface, color, [[x1,y1],[x2,y2]...[xn,yn]], opt_width)
    pygame.draw.polygon(screen, RED, [[300,100],[400,100],[350,200]])

    # my_font.render("text to render", anti_alias, color)
    my_text = my_font.render("Score: " + str(x_pos), True, BLACK)
    screen.blit(my_text, [50, 50])

    for i in range(256):
        pygame.draw.line(screen, (i, i, 255), [0, 0 + i], [screen_width, 0 + i])



    y = 0
    for x in range(200, 301, 20):
        pygame.draw.polygon(screen, WHITE, [[0 + x,6 + y],[12 + x,6 + y],[6 + x,9 + y]])
        pygame.draw.polygon(screen, WHITE, [[1 + x,12 + y],[6 + x,0 + y],[9 + x,6 + y]])
        pygame.draw.polygon(screen, WHITE, [[11 + x,12 + y],[6 + x,0 + y],[3 + x,6 + y]])
    y = 16
    for x in range(210, 301, 20):
        pygame.draw.polygon(screen, WHITE, [[0 + x,6 + y],[12 + x,6 + y],[6 + x,9 + y]])
        pygame.draw.polygon(screen, WHITE, [[1 + x,12 + y],[6 + x,0 + y],[9 + x,6 + y]])
        pygame.draw.polygon(screen, WHITE, [[11 + x,12 + y],[6 + x,0 + y],[3 + x,6 + y]])

    y = 32
    for x in range(200, 301, 20):
        pygame.draw.polygon(screen, WHITE, [[0 + x, 6 + y], [12 + x, 6 + y], [6 + x, 9 + y]])
        pygame.draw.polygon(screen, WHITE, [[1 + x, 12 + y], [6 + x, 0 + y], [9 + x, 6 + y]])
        pygame.draw.polygon(screen, WHITE, [[11 + x, 12 + y], [6 + x, 0 + y], [3 + x, 6 + y]])
    y = 16

    for x in range(0, screen_width, 50):
        for y in range(0, screen_height, 50):
            pygame.draw.rect(screen, GREEN, [x, y, 20, 20])


    pygame.display.flip() # Update the screen with what we've drawn.

    clock.tick(60)  # frames per second

# Close the window and quit.
pygame.quit()















