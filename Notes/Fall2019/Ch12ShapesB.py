"""
Pygame base template
Aaron Lee - 2019
"""

import pygame
import random
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

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)  # Screen object we draw to

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates


# CLASSES
class Circle():
    def __init__(self):
        self.diameter = random.randrange(10, 100)
        self.x = 0
        self.y = 0
        gb = random.randrange(256)  # random green and blue color
        self.color = (255, gb, gb)
        self.change_x = random.randrange(1, 6)

    def draw(self):
        pygame.draw.ellipse(screen, BLACK, [self.x - 2, self.y - 2, self.diameter + 4, self.diameter + 4])
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.diameter, self.diameter])

    def update(self):
        self.x += self.change_x
        if self.x > SCREEN_WIDTH:
            self.x = -self.diameter

class Ball(Circle):
    def __init__(self):
        super().__init__()
        rg = random.randrange(256)  # random green and blue color
        self.color = (rg, rg, 255)



shape_list = []

for i in range(100):
    my_circle = Circle()
    my_circle.x = random.randrange(SCREEN_WIDTH - my_circle.diameter)
    my_circle.y = random.randrange(SCREEN_HEIGHT - my_circle.diameter)
    shape_list.append(my_circle)

    my_ball = Ball()
    my_ball.x = random.randrange(SCREEN_WIDTH - my_ball.diameter)
    my_ball.y = random.randrange(SCREEN_HEIGHT - my_ball.diameter)
    shape_list.append(my_ball)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    for shape in shape_list:
        shape.update()

    # --- Draw to screen
    screen.fill(WHITE)

    for shape in shape_list:
        shape.draw()

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second

pygame.quit()  # Close the window and quit.