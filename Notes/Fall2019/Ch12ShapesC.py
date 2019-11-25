"""
Pygame Template
Aaron Lee - 2019
"""

import pygame
import math
import random

pygame.init()  #  initializes pygame


# Define variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
GRAY = (100, 100, 100)
PINK = (255, 200, 200)
ORANGE = (255, 150, 0)
MAROON = (100, 0, 0)
BROWN = (100, 50, 50)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
done = False  # condition for my game loop


# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mr. Lee's Game")

clock = pygame.time.Clock()  # creates a clock object that manages updates

# CLASSES
class Circle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.diameter = 20
        self.color = GREEN

    def draw(self):
        pygame.draw.ellipse(screen, BLACK, [self.x - 2, self.y - 2, self.diameter + 4, self.diameter + 4])
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.diameter, self.diameter])

    def update(self):
        pass


class Bouncies(Circle):
    def __init__(self):
        super().__init__()
        self.diameter = random.randrange(10, 100)
        self.color = (random.randrange(256), random.randrange(256), random.randrange(256))
        self.x = random.randrange(SCREEN_WIDTH - self.diameter)
        self.y = random.randrange(SCREEN_HEIGHT - self.diameter)
        self.change_x = random.randrange(-10, 10)
        self.change_y = random.random() * 6 - 3

    def update(self):
        # move in x
        self.x += self.change_x

        # move in y
        self.y += self.change_y


shape_list = []

for i in range(100):
    my_circle = Circle()
    my_circle.x = random.randrange(SCREEN_WIDTH - my_circle.diameter)
    my_circle.y = random.randrange(SCREEN_HEIGHT - my_circle.diameter)
    my_circle.diameter = random.randrange(10, 100)
    rb = random.randrange(200)
    my_circle.color = (rb, 200, rb)
    shape_list.append(my_circle)

    my_bouncy = Bouncies()
    shape_list.append(my_bouncy)



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard, controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    for shape in shape_list:
        shape.update()

    # --- Drawing code goes here
    screen.fill(WHITE)

    for shape in shape_list:
        shape.draw()

    pygame.display.flip()  # updates the screen

    clock.tick(60) # frames per second

pygame.quit() # Close the window and quit.
