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
BROWN = (150, 100, 50)

screen_width = 700
screen_height = 500
size = (screen_width, screen_height)  # width, height
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Window Bar Name")

done = False  # condition for my game loop
clock = pygame.time.Clock() # Used to manage how fast the screen updates

snow_list = []

for i in range(500):
    x = random.randrange(screen_width)
    y = random.randrange(screen_height)
    speed = random.randrange(1, 5)
    snow_list.append([x, y, speed])

print(snow_list)
depth = 0

def draw_tree(x, y):
    pygame.draw.rect(screen, BROWN, [60 + x, 400 -230 + y, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150 + x, 400 - 230 + y], [75 + x, 250 - 230 + y], [x, 400 - 230 + y]])
    pygame.draw.polygon(screen, GREEN, [[140 + x, 350 - 230 + y], [75 + x, y], [10 + x, 350 - 230 + y]])

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop  (user inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code should go here
    screen.fill(BLACK)
    for x in range(0, screen_width, 200):
        draw_tree(x, 300)



    for i in range(len(snow_list)):
        snow_list[i][1] += snow_list[i][2]
        if snow_list[i][1] > screen_height:
            snow_list[i][1] = -7
            snow_list[i][0] = random.randrange(screen_width)
            depth += 0.01

        pygame.draw.ellipse(screen, WHITE, [snow_list[i][0], snow_list[i][1], 2 * snow_list[i][2] , 2 * snow_list[i][2]])

    pygame.draw.rect(screen, WHITE, [0, screen_height - depth, screen_width, depth + 1])

    pygame.display.flip() # Update the screen with what we've drawn.

    clock.tick(60)  # frames per second

# Close the window and quit.
pygame.quit()















