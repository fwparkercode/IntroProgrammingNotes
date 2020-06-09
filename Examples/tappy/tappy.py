"""
Pygame base template
Aaron Lee - 2019
"""

import random
from globals import *
from classes import *

class Game():
    def __init__(self):
        pygame.init()  # initializes pygame (necessary before any pygame functions)
        self.done = False  # Loop until the user clicks the close button.
        self.screen_width = 600
        self.screen_height = 400
        self.size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(self.size)  # Screen object we draw to
        pygame.display.set_caption("my_game")
        self.clock = pygame.time.Clock()  # Used to manage how fast the screen updates

    def events(self):
        # --- Main event loop (input from user keyboard, mouse, game controller)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)

    def commit_loop(self):
        pygame.display.flip()  # Go ahead and update the screen with what we've drawn.
        self.clock.tick(60)  # limit to 60 frames per second




if __name__ == "__main__":
    my_game = Game()
    my_game.done = False

    while not my_game.done:
        my_game.events()
        my_game.update()
        my_game.draw()
        my_game.commit_loop()

    pygame.quit()
