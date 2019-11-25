"""
Pygame base template
Aaron Lee - 2019
"""
import random

import pygame
pygame.init()  # initializes pygame (need to do this before you use it)


# Global Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 150, 150)
MAROON = (100, 0, 0)
ORANGE = (255, 150, 0)
PURPLE = (100, 50, 150)


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.


size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game!")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

# CLASSES
class Circle():
    def __init__(self):
        self.diameter = 10
        self.color = RED
        self.change_x = random.randrange(1, 10)
        self.change_y = 0
        self.x = 0
        self.y = 0
        self.gravity = 0.2
        self.elasticity = 0.8

    def draw(self):
        pygame.draw.ellipse(screen, BLACK, [self.x - 2, self.y - 2, self.diameter + 4, self.diameter + 4])
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.diameter, self.diameter])

    def update(self):
        self.x += self.change_x
        if self.x > SCREEN_WIDTH - self.diameter:
            self.x = SCREEN_WIDTH - self.diameter
            self.change_x *= -self.elasticity
        if self.x < 0:
            self.x = 0
            self.change_x *= -self.elasticity

        self.change_y += self.gravity
        self.y += self.change_y
        if self.y > SCREEN_HEIGHT - self.diameter:
            if self.change_y > 1:
                self.color = (random.randrange(256), random.randrange(256), random.randrange(256))
            self.y = SCREEN_HEIGHT - self.diameter
            self.change_y *= -self.elasticity
            self.change_x *= self.elasticity


shape_list = []
for i in range(20):
    my_circle = Circle()
    bg = random.randrange(256)
    my_circle.color = (255, bg, bg)
    my_circle.diameter = random.randrange(10, 100)  # dot notation outside of class
    my_circle.x = random.randrange(SCREEN_WIDTH - my_circle.diameter)
    my_circle.y = random.randrange(SCREEN_HEIGHT - my_circle.diameter)
    shape_list.append(my_circle)

#print(shape_list)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
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


    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second


pygame.quit()  # Close the window and quit.