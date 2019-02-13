"""
 Pygame base template for opening a window

 Intro to Programming
 Aaron Lee 2018
"""

import pygame
import random
pygame.init()

# Define some colors
BLACK = (0, 0, 0)  # (red, green, blue)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (120, 120, 120)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Template")

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Ball():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = random.randrange(30, 150)
        self.brightness = random.randrange(256)
        self.color = (255, self.brightness, self.brightness)
        self.speed_x = 0
        self.speed_y = 0
    def draw(self):
        pygame.draw.ellipse(screen, BLACK, [self.x - 2, self.y - 2, self.size + 4, self.size + 4])
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.size, self.size])
    def update(self):
        self.x += self.speed_x
        if self.x > screen_width:
            self.x = -self.size
        self.y += self.speed_y

class Bubble(Ball):
    def update(self):
        self.y += self.speed_y
        self.speed_y += (random.random() - 0.5) / 3


ball_list = []

for i in range(100):
    ball = Ball()
    ball.x = random.randrange(screen_width - ball.size)
    ball.y = random.randrange(screen_height - ball.size)
    ball.speed_x = random.randrange(1, 7)
    ball_list.append(ball)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_bubble = Bubble()
            new_bubble.color = (new_bubble.brightness, new_bubble.brightness, 255)
            new_bubble.x, new_bubble.y = event.pos
            new_bubble.x -= new_bubble.size / 2
            new_bubble.y -= new_bubble.size / 2

            ball_list.append(new_bubble)


    # --- Game logic should go here
    for ball in ball_list:
        ball.update()

    screen.fill(WHITE)
    # --- Drawing code should go here
    for ball in ball_list:
        ball.draw()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()