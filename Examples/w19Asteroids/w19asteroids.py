"""
Asteroids clone just for fun
Aaron Lee - 2019
"""
from sprite_classes import *


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
        self.score = 0

    def initialize_pygame(self):
        pygame.init()
        self.screen = screen = pygame.display.set_mode([screen_width, screen_height])  # Screen object we draw to
        self.clock = pygame.time.Clock()  # Used to manage how fast the screen updates
        self.game_font = pygame.font.Font("/Users/alee/PycharmProjects/IntroProgramming/Examples/w19Asteroids/Hyperspace Bold.otf", 30)


    def create_sprite_groups(self):
        #only for pygame sprite Group class creation
        self.all_sprites = pygame.sprite.Group()
        self.asteroid_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.power_sprites = pygame.sprite.Group()
        self.broken_sprites = pygame.sprite.Group()

    def initialize_level(self):
        # first level and beyond
        # creates and sets player.
        # creates asteroids according to level
        self.player = Player(screen_width // 2, screen_height // 2)
        self.all_sprites.add(self.player)
        self.player.asteroid_sprites = self.asteroid_sprites

        for i in range(level + 2):
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
                elif event.key == pygame.K_RIGHT:
                    self.player.change_angle_speed(0.1)
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(self.player.angle, self.player.rect.center)
                    self.all_sprites.add(new_bullet)
                    self.bullet_sprites.add(new_bullet)
                elif event.key == pygame.K_UP:
                    self.player.thrust_on = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.change_angle_speed(0.1)
                elif event.key == pygame.K_RIGHT:
                    self.player.change_angle_speed(-0.1)
                elif event.key == pygame.K_UP:
                    self.player.thrust_on = False


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
        self.draw_broken()  # broken ship parts if any
        self.all_sprites.draw(self.screen)  # blit all the images
        self.draw_gui()  # score and lives

        pygame.display.flip()  # update the screen with what we've drawn.
        self.clock.tick(self.frame_rate)  # limit to 60 frames per second

    def draw_broken(self):
        for line in self.broken_sprites:
            line.draw_me(self.screen)

    def draw_asteroids(self):
        for asteroid in self.asteroid_sprites:
            asteroid.draw_me(self.screen)

    def collisions(self):
        self.bullet_collision()
        self.player_collision()

    def player_collision(self):
        # collision between player and asteroids
        for asteroid in self.asteroid_sprites:
            if pygame.sprite.collide_circle(self.player, asteroid):
                self.player.lives -= 1
                self.player.angle = math.pi / 2
                self.player.thrust_on = False
                self.player.change_x = 0
                self.player.change_y = 0
                self.player.thrust_x = 0
                self.player.thrust_y = 0
                self.player.active = False
                self.break_ship()

    def break_ship(self):
        # create ship pieces when you die
        line = BrokenParts(self.player.nose, self.player.tail1, self.player.change_x, self.player.change_y)
        self.all_sprites.add(line)
        self.broken_sprites.add(line)

        line = BrokenParts(self.player.nose, self.player.tail2, self.player.change_x, self.player.change_y)
        self.all_sprites.add(line)
        self.broken_sprites.add(line)

        line = BrokenParts(self.player.tail1, self.player.tail2, self.player.change_x, self.player.change_y)
        self.all_sprites.add(line)
        self.broken_sprites.add(line)

    def bullet_collision(self):
        # bullets vs asteroids
        for bullet in self.bullet_sprites:
            for asteroid in self.asteroid_sprites:
                if pygame.sprite.collide_circle(bullet, asteroid):
                    bullet.kill()
                    self.score += int(asteroid.radius) + 100
                    if asteroid.radius >= 10:
                        self.make_babies(asteroid)
                    asteroid.kill()

    def make_babies(self, asteroid):
        for i in range(2, 5):
            baby = Asteroid(asteroid.radius // 2)
            baby.rect.center = asteroid.rect.center
            baby.rect.x += random.randrange(-asteroid.radius // 2, asteroid.radius // 2)
            baby.rect.y += random.randrange(-asteroid.radius // 2, asteroid.radius // 2)
            baby.x = baby.rect.centerx
            baby.y = baby.rect.centery
            baby.change_x += asteroid.change_x / 2
            baby.change_y += asteroid.change_y / 2
            self.all_sprites.add(baby)
            self.asteroid_sprites.add(baby)

    def draw_gui(self):
        # score and lives
        my_score = self.game_font.render("Score: " + str(self.score), True, WHITE)
        my_lives = self.game_font.render("Lives: " + str(self.player.lives), True, WHITE)
        self.screen.blit(my_score, [20, 20])
        self.screen.blit(my_lives, [20, 50])


    def quit(self):
        self.done = True





if __name__ == "__main__":
    my_game = Game()
    while not my_game.done:
        my_game.event_loop()
        my_game.update_code()
        my_game.draw_code()
    pygame.quit()  # safely close pygame