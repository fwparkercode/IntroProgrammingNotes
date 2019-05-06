import random

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()  # starts pygame (Vroom!)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mr. Lee's Game")

done = False  # condition for the game loop

clock = pygame.time.Clock()


# CLASSES
class Ball():
    def __init__(self):
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
        if self.y > screen_height:
            self.y = -self.size

class Bubble(Ball):
    def __init__(self):
        super().__init__()
        self.change_x = 0
        self.change_y = random.random()
        rg = random.randrange(256)
        self.color = (rg, rg, 255)


ball_list = []

for i in range(100):
    ball = Ball()
    ball_list.append(ball)



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
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

    pygame.display.flip()  #update the screen
    clock.tick(60)  #60 frames per second

pygame.quit()  #Close the window and quit.

