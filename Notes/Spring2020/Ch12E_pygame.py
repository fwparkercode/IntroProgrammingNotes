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

class Balloon():
    def __init__(self):
        self.diameter = random.randrange(40, 100)
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
            self.x = -self.diameter

class Bubble(Balloon):
    def __init__(self):
        super().__init__()
        rg = random.randrange(256)
        self.color = (rg, rg, 255)
        self.change_x = 0
        self.change_y = random.randrange(1, 4)

    def update(self):
        self.y += self.change_y


balloon_list = []

for i in range(100):
    balloon = Balloon()
    bubble = Bubble()
    balloon_list.append(balloon)
    balloon_list.append(bubble)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bubble = Bubble()
            bubble.x, bubble.y = event.pos
            balloon_list.append(bubble)

    # --- Game logic should go here
    for balloon in balloon_list:
        balloon.update()

    # --- Drawing code should go here
    screen.fill(WHITE)  # paint the blank canvas

    for balloon in balloon_list:
        balloon.draw_me()

    pygame.display.flip()  # show the updated drawing

    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
