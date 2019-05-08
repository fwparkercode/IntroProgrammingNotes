"""
Pygame base template
by Aaron Lee 2019
"""
import random

import pygame
pygame.init()  # do not put anything pygame above this line

# Define some colors (red, green, blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen_width = 700
screen_height = 500
size = (screen_width, screen_height)  # width, height
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Window Bar Name")

done = False  # condition for my game loop

clock = pygame.time.Clock() # Used to manage how fast the screen updates

# CLASSES
class Ball():
    def __init__(self):
        print("A new ball is born")
        gb = random.randrange(256)
        self.color = (255, gb, gb)
        self.size = random.randrange(30, 100)
        self.x = random.randrange(0, screen_width - self.size)
        self.y = random.randrange(0, screen_height - self.size)
        self.change_x = random.random() * 8
        self.change_y = 0

    def draw(self):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.size, self.size])
        pygame.draw.ellipse(screen, BLACK, [self.x, self.y, self.size, self.size], 2)

    def move(self):
        self.x += self.change_x
        if self.x > screen_width:
            self.x = -self.size

        self.y += self.change_y

class Bubble(Ball):
    def __init__(self):
        super().__init__()
        rg = random.randrange(256)
        self.color = (rg, rg, 255)
        self.change_x = 0
        self.change_y = random.random() - 0.5

ball_list = []

for i in range(100):
    ball = Ball()  # create an instance of the Ball class
    ball_list.append(ball)



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop  (user inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            bubble = Bubble()
            bubble.x = x
            bubble.y = y
            ball_list.append(bubble)

    # --- Game logic should go here
    for ball in ball_list:
        ball.move()

    # --- Drawing code should go here
    screen.fill(WHITE)

    for ball in ball_list:
        ball.draw()

    pygame.display.flip() # Update the screen with what we've drawn.

    clock.tick(60)  # frames per second

# Close the window and quit.
pygame.quit()

