"""
Pygame base template
by Aaron Lee 2020
"""
import random

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

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# CLASSES
class Circle():
    def __init__(self):
        self.diameter = random.randrange(20, 100)
        self.x = random.randrange(WIDTH - self.diameter)
        self.y = random.randrange(HEIGHT - self.diameter)
        gb = random.randrange(256)
        self.color = (255, gb, gb)
        self.change_x = random.randrange(1, 6)

    def draw_me(self):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.diameter, self.diameter])

    def update(self):
        self.x += self.change_x
        if self.x > WIDTH:
            # randomize my balloon
            self.diameter = random.randrange(20, 100)
            self.x = random.randrange(WIDTH - self.diameter)
            self.y = random.randrange(HEIGHT - self.diameter)
            self.change_x = random.randrange(1, 6)
            # move it to left side (wrap)
            self.x = -self.diameter


class Bubble(Circle):  # Bubble is a child of the Circle class. (Circle is the parent class)
    def __init__(self):
        super().__init__()  # runs the constructor on the parent  super() means parent (Circle in this case)
        rg = random.randrange(256)
        self.color = (rg, rg, 255)
        self.change_x = 0
        self.change_y = random.randrange(1, 4)

    def update(self):
        self.y += self.change_y



circle_list = []

for i in range(100):
    my_circle = Circle()
    my_bubble = Bubble()
    circle_list.append(my_circle)
    circle_list.append(my_bubble)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            my_bubble = Bubble()
            my_bubble.x, my_bubble.y = event.pos
            circle_list.append(my_bubble)

    # --- Game logic should go here
    for my_circle in circle_list:
        my_circle.update()

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas

    for my_circle in circle_list:
        my_circle.draw_me()

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
