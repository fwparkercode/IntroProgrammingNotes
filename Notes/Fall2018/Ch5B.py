"""
 Pygame base template
 Intro to Programming

 Aaron Lee 2018
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

pygame.init()  # starts pygame

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Template")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# fonts
#  SysFont("font", font_size, bold, italics)
my_font = pygame.font.SysFont("Calibri", 30, True, False)

score = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here
    screen.fill(WHITE)

    # --- Drawing code should go here
    # rect(surface, color, [top_left_x, top_left_y, width, height], optional width)
    pygame.draw.rect(screen, RED, [0, 0, 200, 100])
    pygame.draw.rect(screen, GREEN, [200, 100, 200, 100], 3)

    # ellipse(surface, color, [top_left_x, top_left_y, width, height], optional width)
    # ellipse is circumscribed on inside of the defined rectangle
    pygame.draw.ellipse(screen, RED, [200, 100, 200, 100])
    pygame.draw.ellipse(screen, BLUE, [0, 0, 100, 100])

    # line(surface, color, [x1, y1], [x2, y2], width)
    pygame.draw.line(screen, BLACK, [0, 0], [200, 100], 3)
    pygame.draw.line(screen, BLACK, [100, 0], [100, screen_height], 3)  # vertical
    pygame.draw.line(screen, BLACK, [0, 100], [screen_width, 100], 3)  # horizontal

    # repeating shapes
    for x in range(20, screen_width, 20):
        pygame.draw.line(screen, BLUE, [x, 0], [x, screen_height], 1)  # vertical

    for y in range(20, screen_height, 20):
        pygame.draw.line(screen, BLUE, [0, y], [screen_width, y], 1)  # vertical

    #  polygon
    #  polygon(surface, color, [[x1, y1], [x2, y2], [x3, y3]...], optional_width]
    pygame.draw.polygon(screen, MAGENTA, [[0, 0], [0, 200], [200, 100]])

    #  text
    #  step 1:  make a font (usually outside the loop)
    #  step 2:  render your text in the font (usually inside the loop)
    #  render(text, anti-alias, color)
    score += 1
    my_text = my_font.render("Score: " + str(score), True, BLACK)

    #  step 3:  blit the text object to the screen
    # blit(text_object, [top_left_x, top_left_y])
    screen.blit(my_text, [20, 20])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    clock.tick(60)

# Close the window and quit.
pygame.quit()