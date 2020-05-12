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

class Rectangle():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def update(self):
        pass  # you fill it in

my_shapes = []

for i in range(100):
    color = [random.randrange(256), random.randrange(256), random.randrange(256)]
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    width = random.randrange(20, 50)
    height = random.randrange(20, 50)
    my_rect = Rectangle(x, y, width, height, color)
    my_shapes.append(my_rect)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    for shape in my_shapes:
        shape.update()

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas
    for shape in my_shapes:
        shape.draw()

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
