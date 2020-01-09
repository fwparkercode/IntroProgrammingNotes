"""
Pygame base template
Aaron Lee - 2019
"""

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


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
done = False  # Loop until the user clicks the close button.


size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the 30 and 10 of the screen [30, 10]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game!")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

def draw_car(x, y, color):
    '''
    draws a car to the screen at position x, y (top left corner of car body)
    '''
    pygame.draw.rect(screen, BLACK, [x + 10, y, 10, 5], 1) # windows
    pygame.draw.rect(screen, color, [x + 5, y, 6, 5]) # windows
    pygame.draw.ellipse(screen, BLACK, [x + 2, y + 6, 9, 9], 3) # wheel
    pygame.draw.ellipse(screen, BLACK, [x + 18, y + 6, 9, 9], 3) # wheel
    pygame.draw.rect(screen, color, [x, y + 4, 30, 5]) # body


def draw_player(x, y, color):
    # draw a player
    pygame.draw.ellipse(screen, color, [x + 3, y, 5, 5])  # player's head
    pygame.draw.line(screen, color, [x + 5, y], [x + 5, y + 10])  # player's body
    pygame.draw.line(screen, color, [x + 5, y + 10], [x + 8, y + 20])  # player's right leg
    pygame.draw.line(screen, color, [x + 5, y + 10], [x + 2, y + 20])  # player's left leg
    pygame.draw.line(screen, color, [x + 5, y + 3], [x + 10, y + 11])  # player's right arm
    pygame.draw.line(screen, color, [x + 5, y + 3], [x, y + 11])  # player's left arm


car_color = RED
car_x = 0
car_y = 0
car_change_x = 0
car_change_y = 0
car_width = 30
car_height = 14
car_color = RED
player_x = 0
player_y = 0
player_width = 10
player_height = 20
car_speed = 5

pygame.mouse.set_visible(False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                car_change_y = -car_speed
            if event.key == pygame.K_DOWN:
                car_change_y = car_speed
            if event.key == pygame.K_RIGHT:
                car_change_x = car_speed
            if event.key == pygame.K_LEFT:
                car_change_x = -car_speed
            if event.key == pygame.K_r:
                car_color = RED
            if event.key == pygame.K_b:
                car_color = BLUE

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                car_change_y = 0
            if event.key == pygame.K_DOWN:
                car_change_y = 0
            if event.key == pygame.K_RIGHT:
                car_change_x = 0
            if event.key == pygame.K_LEFT:
                car_change_x = 0



    # --- Game logic should go here
    car_y += car_change_y
    car_x += car_change_x

    if car_x > SCREEN_WIDTH - car_width:
        car_x = SCREEN_WIDTH - car_width
    if car_y > SCREEN_HEIGHT - car_height:
        car_y = SCREEN_HEIGHT - car_height
    if car_x < 0:
        car_x = 0
    if car_y < 0:
        car_y = 0

    player_x, player_y = pygame.mouse.get_pos()
    if player_x > SCREEN_WIDTH - player_width:
        player_x = SCREEN_WIDTH - player_width
    if player_y > SCREEN_HEIGHT - player_height:
        player_y = SCREEN_HEIGHT - player_height


    # --- Drawing code goes here
    screen.fill(WHITE)

    draw_player(player_x, player_y, BLACK)

    draw_car(car_x, car_y, car_color)

    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second


pygame.quit()  # Close the window and quit.