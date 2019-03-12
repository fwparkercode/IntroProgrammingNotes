"""
Pygame Base Template
Spring 2019
by Aaron Lee
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 150, 0)
PURPLE = (150, 0, 200)


pygame.init()  # starts pygame (Vroom!)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)  # surface to draw to

pygame.display.set_caption("Mr. Lee's Game")

done = False  # condition for the game loop

clock = pygame.time.Clock()
ellipse_x = 0
score = 0

# text objects
# font.SysFont("font name", size, Bold, Italic)
my_font = pygame.font.SysFont("Calibri", 40, True, False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here
    # --- Drawing code should go here
    screen.fill(WHITE)

    #  draw.line(surface, color, [x1, y1], [x2, y2], width)
    pygame.draw.line(screen, PURPLE, [0, 0], [100, 100], 3)
    pygame.draw.line(screen, GREEN, [0, screen_height], [screen_width, 0], 5)

    for x in range(0, screen_width, 50):
        pygame.draw.line(screen, BLACK, [x, 0], [x, screen_height], 5)

    # draw.rect(surface, color, [top_left_x, top_left_y, width, height], optional_border)
    pygame.draw.rect(screen, RED, [100,100,200,100])
    pygame.draw.rect(screen, BLUE, [200,200,50,50], 3)

    # draw.ellipse(surface, color, [top_left_x, top_left_y, width, height], optional_border)
    # ellipse draws inside the rectangle (circumscribed inside)
    pygame.draw.ellipse(screen, YELLOW, [100,100,200,100])
    pygame.draw.ellipse(screen, MAGENTA, [ellipse_x,200,50,50], 3)
    ellipse_x += 0.1

    # draw.polygon(surface, color, [[x1,y1],[x2,y2],[x3,y3]...[xn,yn]], optional thickness
    pygame.draw.polygon(screen, ORANGE, [[400,100],[500,100],[450,200]])

    # render the text
    #  render("text", anti-alias, color)
    score += 1
    my_text = my_font.render("Score: " + str(score), True, BLACK)
    screen.blit(my_text, [50, 50])

    pygame.display.flip()  #update the screen
    clock.tick(60)  #60 frames per second

pygame.quit()  #Close the window and quit.