"""
Asteroids clone just for fun
Aaron Lee - 2019
"""

from sprite_classes import *

# Classes
class Game():
    # creates instance of the game
    def __init__(self):
        self.create_globals()
        self.initialize_pygame()
        self.create_sprite_groups()
        self.initialize_level()

    def create_globals(self):
        # all game globals
        self.frame_rate = 60
        self.done = False  # game loop condition
        self.level = 1
        self.frame = 0

    def initialize_pygame(self):
        pygame.init()
        self.screen = screen = pygame.display.set_mode([screen_width, screen_height])  # Screen object we draw to
        self.clock = pygame.time.Clock()  # Used to manage how fast the screen updates

    def create_sprite_groups(self):
        #only for pygame sprite Group class creation
        self.all_sprites = pygame.sprite.Group()
        self.asteroid_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.power_sprites = pygame.sprite.Group()

    def initialize_level(self):
        # first level and beyond
        # creates and sets player.
        # creates asteroids according to level
        self.player = Player(screen_width // 2, screen_height // 2)
        self.all_sprites.add(self.player)

        for i in range(level):
            asteroid = Asteroid(100)
            self.all_sprites.add(asteroid)
            self.asteroid_sprites.add(asteroid)

    def event_loop(self):
        # USER INPUTS HERE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.change_angle_speed(-0.1)
                if event.key == pygame.K_RIGHT:
                    self.player.change_angle_speed(0.1)
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(self.player.angle, self.player.rect.center)
                    self.all_sprites.add(new_bullet)
                    self.bullet_sprites.add(new_bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.change_angle_speed(0.1)
                if event.key == pygame.K_RIGHT:
                    self.player.change_angle_speed(-0.1)


    def update_code(self):
        # ALL UPDATE CODE GOES HERE
        self.frame += 1
        self.all_sprites.update()
        self.collisions()

    def draw_code(self):
        #  ALL DRAW CODE GOES HERE
        self.screen.fill(BLACK)
        self.draw_asteroids()  # draw on my asteroid images
        self.player.draw_me(self.screen) #  draw on my player image
        self.all_sprites.draw(self.screen)  # blit all the images

        pygame.display.flip()  # update the screen with what we've drawn.
        self.clock.tick(self.frame_rate)  # limit to 60 frames per second

    def draw_asteroids(self):
        for asteroid in self.asteroid_sprites:
            asteroid.draw_me(self.screen)

    def collisions(self):
        pass

    def quit(self):
        self.done = True




def midpoint(point1, point2):
    x = (point1[0] + point2[0]) // 2
    y = (point1[1] - point2[1]) // 2
    return x, y



if __name__ == "__main__":
    my_game = Game()
    while not my_game.done:
        my_game.event_loop()
        my_game.update_code()
        my_game.draw_code()
        print(int(my_game.frame / 60))
    pygame.quit()  # safely close pygame