'''
World Generation-related classes for Moon-Pytrol. Provides ground, foreground, and background generation and scrolling.
Also provides rock and hole generation with varying sizes. Most classes take in ground position and speed of scroll.
'''

import pygame

class WorldGen():

    def __init__(self, scroll_speed, y_shift, ground_pos):
        self.foreground = pygame.image.load("assets/front-hills.png")
        self.background = pygame.image.load("assets/back-mountains.png")
        self.ground = pygame.image.load("assets/ground.png")
        self.bg_x = 0
        self.fg_x = 0
        self.scroll_speed = scroll_speed
        self.y_shift = y_shift
        self.ground_pos = ground_pos

    def drawBackground(self, screen):

        # Moving the background across the screen
        self.bg_x -= self.scroll_speed
        if self.bg_x < -640:
            self.bg_x = 0

        for i in range(2):
            screen.blit(self.background, [self.bg_x + 640 * i, 45 + self.y_shift])
    
    def drawForeground(self, screen):

        # Moving the foreground across the screen
        self.fg_x -= self.scroll_speed + 0.5
        if self.fg_x < -640:
            self.fg_x = 0

        for i in range(2):
            screen.blit(self.foreground, [self.fg_x + 640 * i, 100 + self.y_shift])
    
    def drawGround(self, screen):

        # Ground is just an image color matched to holes
        screen.blit(self.ground, [0, self.ground_pos + self.y_shift])


holefiles = ["assets/smallhole.png", "assets/mediumhole.png", "assets/hugehole.png"]

class GenHole(pygame.sprite.Sprite):

    def __init__(self, scroll_speed, y_shift, ground_pos, x, size):
        super().__init__()
        self.image = pygame.image.load(holefiles[size])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = ground_pos + y_shift
        self.rect.x = x
        self.speed = scroll_speed

    def update(self):
        self.rect.x -= self.speed + 3

        if self.rect.x <= -60:
            self.kill()

rockfiles = ["assets/tinyrock.png", "assets/mediumrock.png", "assets/bigrock.png", "assets/hugerock.png"]

class Rock(pygame.sprite.Sprite):

    def __init__(self, scroll_speed, y_shift, ground_pos, x, size):
        super().__init__()
        self.image = pygame.image.load(rockfiles[size])
        self.rect = self.image.get_rect()
        self.rect.bottom = ground_pos + y_shift
        self.rect.x = x
        self.speed = scroll_speed
        self.death_sound = pygame.mixer.Sound("assets/sounds/rock_kill.wav")

    def update(self):
        self.rect.x -= self.speed + 3

        if self.rect.x <= -60:
            self.kill()

    def death(self):
        pygame.mixer.Channel(4).set_volume(1)
        pygame.mixer.Channel(4).play(self.death_sound)
        self.kill()

# -------- Main Program Loop -----------
if __name__ == "__main__":

    GROUND_POS = 240
    WORLD_SPEED = 0.8

    pygame.init()
    WHITE = (255, 255, 255)
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 340
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)
    done = False
    clock = pygame.time.Clock()

    worldGen = WorldGen(WORLD_SPEED, 30, GROUND_POS)


    hole_list = pygame.sprite.Group()
    hole = GenHole(WORLD_SPEED, 30, GROUND_POS, 400, 0)
    hole_list.add(hole)

    rock_list = pygame.sprite.Group()
    rock = Rock(WORLD_SPEED, 30, GROUND_POS, 400, 0)
    rock_list.add(rock)

    while not done:
        # --- Main event loop (input from user mouse, keyboard, etc)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Game logic

        # --- Drawing code
        screen.fill(WHITE)

        worldGen.drawBackground(screen)
        worldGen.drawForeground(screen)
        worldGen.drawGround(screen)

        hole_list.draw(screen)
        hole_list.update()

        rock_list.draw(screen)
        rock_list.update()

        pygame.display.flip()  # updates the screen

        clock.tick(60)  # frames per second

    pygame.quit()  # Close the window and quit.