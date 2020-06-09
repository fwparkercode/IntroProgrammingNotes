"""
Asteroids clone just for fun
Aaron Lee - 2019
"""
from GS_Sprites import *


class Game():
    # creates instance of the game
    def __init__(self):
        self.create_globals()
        self.initialize_pygame()
        self.create_sprite_groups()
        self.initialize_level()

    def create_globals(self):
        # all game globals
        self.volume = 50
        self.frame_rate = 60
        self.done = False  # game loop condition
        self.level = 1
        self.frame = 0
        self.score = 0
        self.paused = False
        self.game_over = False
        self.star_list = [[random.randrange(screen_width), random.randrange(screen_height)] for x in range(200)]
        #self.star_list = []  # temp to test no stars
        self.twinkle_list = [[random.randrange(5000, 10000), random.randrange(5000, 10000), random.randrange(5000)] for i in range(len(self.star_list))]  # frame on off
        self.fps_tracking = []


    def initialize_pygame(self):
        pygame.init()
        #self.screen = pygame.display.set_mode([screen_width, screen_height])  # Screen object we draw to

        self.screen = pygame.display.set_mode([screen_width, screen_height])


        self.clock = pygame.time.Clock()  # Used to manage how fast the screen updates
        self.game_font = pygame.font.Font("Hyperspace Bold.otf", 14)
        self.power_font = pygame.font.Font("Hyperspace Bold.otf", 10)

        self.fire_sound = pygame.mixer.Sound("fire.wav")

        self.thrust_sound = pygame.mixer.Sound("thrust.wav")

        self.bg = pygame.mixer.Sound(
            "bg.wav")
        self.bg.play(-1)

        self.life_sound = pygame.mixer.Sound(
            "positive.wav")
        pygame.mouse.set_visible(False)
        intro_screen(self.screen, self.clock)

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
        if self.level == 1:
            self.player = Player(screen_width // 2, screen_height // 2)
            self.all_sprites.add(self.player)
            self.player.asteroid_sprites = self.asteroid_sprites
            self.power_up_list = [[self.player.triple, "3x"],
                                  [self.player.shield, "shield"],
                                  [self.player.laser, "laser"]]
            self.player.broken_sprites = self.broken_sprites

        else:
            self.all_sprites.empty()
            self.bullet_sprites.empty()
            self.asteroid_sprites.empty()
            self.power_sprites.empty()
            self.all_sprites.add(self.player)
            #self.player.rect.center = (screen_width // 2, screen_height // 2)
            #self.player.x, self.player.y = self.player.rect.center
            #self.bullet_sprites.empty()
            self.frame = 1
            self.player.shield_time = 100
            #self.player.shield = False
            #self.player.change_x = 0
            #self.player.change_y = 0
            #self.player.angle = -math.pi / 2

        for i in range(max(self.level, 2)):
            asteroid = Asteroid(random.randrange(30, 30 + self.level * 10), self.player)
            self.all_sprites.add(asteroid)
            self.asteroid_sprites.add(asteroid)

    def event_loop(self):
        # USER INPUTS HERE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.change_angle_speed(-0.05)
                elif event.key == pygame.K_RIGHT:
                    self.player.change_angle_speed(0.05)
                elif event.key == pygame.K_j:
                    if self.game_over or not self.player.active: break
                    self.fire_sound.play()
                    new_bullet = Bullet(self.player.angle, self.player.rect.center)
                    self.all_sprites.add(new_bullet)
                    self.bullet_sprites.add(new_bullet)
                    if self.player.triple:
                        new_bullet = Bullet(self.player.angle - 0.3, self.player.rect.center)
                        self.all_sprites.add(new_bullet)
                        self.bullet_sprites.add(new_bullet)
                        new_bullet = Bullet(self.player.angle + 0.3, self.player.rect.center)
                        self.all_sprites.add(new_bullet)
                        self.bullet_sprites.add(new_bullet)
                elif event.key == pygame.K_UP:
                    self.player.thrust_on = True
                elif event.key == pygame.K_k:
                    self.player.shield = True
                elif event.key == pygame.K_RETURN and self.game_over:
                    self.game_over = False
                    self.all_sprites.empty()
                    self.asteroid_sprites.empty()
                    self.broken_sprites.empty()
                    self.bullet_sprites.empty()
                    self.level = 1
                    self.initialize_level()
                elif event.key == pygame.K_ESCAPE:
                    if self.game_over or self.paused:
                        self.quit()
                    else:
                        self.paused = True

                elif event.key == pygame.K_RETURN and self.paused:
                    self.paused = False
                elif event.key == pygame.K_SPACE:
                    self.set_volume(-10)
                elif event.key == pygame.K_RETURN and not self.game_over:
                    self.set_volume(10)



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.change_angle_speed(0.05)
                elif event.key == pygame.K_RIGHT:
                    self.player.change_angle_speed(-0.05)
                elif event.key == pygame.K_UP:
                    self.player.thrust_on = False
                elif event.key == pygame.K_k:
                    self.player.shield = False


    def update_code(self):
        # ALL UPDATE CODE GOES HERE
        if self.paused: return
        self.frame += 1
        self.all_sprites.update()
        self.collisions()
        if self.frame % 1800 == 0:
            self.add_powerup()
        self.level_check()



    def draw_code(self):
        #  ALL DRAW CODE GOES HERE
        self.screen.fill(BLACK)
        self.draw_stars()
        self.draw_powerups()

        self.draw_asteroids()  # draw on my asteroid images
        self.player.draw_me(self.screen) #  draw on my player image
        self.draw_broken()  # broken ship parts if any
        self.all_sprites.draw(self.screen)  # blit all the images
        self.draw_gui()  # score and lives

        pygame.display.flip()  # update the screen with what we've drawn.
        self.clock.tick(self.frame_rate)  # limit to 60 frames per second

    def draw_powerups(self):
        for powerup in self.power_sprites:
            powerup.draw_me(self.screen)

    def draw_stars(self):
        for i in range(len(self.star_list)):
            pygame.draw.line(self.screen, WHITE, self.star_list[i], self.star_list[i], linewidth)

    def draw_broken(self):
        for line in self.broken_sprites:
            line.draw_me(self.screen)

    def draw_asteroids(self):
        for asteroid in self.asteroid_sprites:
            asteroid.draw_me(self.screen)

    def collisions(self):
        self.bullet_collision()
        self.player_collision()
        self.power_collision()

    def power_collision(self):
        for power in self.power_sprites:
            if pygame.sprite.collide_rect(power, self.player):
                if power.power == "3x":
                    self.player.triple = True
                    self.player.power_time = 500
                power.kill()


    def player_collision(self):
        # collision between player and asteroids
        if not self.player.active: return
        for asteroid in self.asteroid_sprites:
            if pygame.sprite.collide_circle(self.player, asteroid):
                if self.player.shield:
                    angle = math.atan2( asteroid.y - self.player.y, asteroid.x - self.player.x)
                    self.player.change_x -= math.cos(angle) / 10
                    self.player.change_y -= math.sin(angle) / 10
                    asteroid.change_x += math.cos(angle) / asteroid.radius
                    asteroid.change_y += math.sin(angle) / asteroid.radius
                else:
                    self.player.lives -= 1
                    self.player.angle = -math.pi / 2
                    self.player.thrust_on = False
                    self.player.change_x = 0
                    self.player.change_y = 0
                    self.player.thrust_x = 0
                    self.player.thrust_y = 0
                    self.player.active = False
                    self.player.shield_time = 100
                    self.break_ship()
        if self.player.lives <= 0:
            self.game_over = True
            self.player.rect.center = (-1000, -1000)
            self.player.active = False
            self.player.dead = True

    def break_ship(self):
        # create ship pieces when you die
        midpoint1 = midpoint(self.player.nose, self.player.tail1)
        midpoint2 = midpoint(self.player.nose, self.player.tail2)
        midpoint_tail = midpoint(self.player.tail1, self.player.tail2)

        line = BrokenParts(self.player.nose, midpoint1, self.player.change_x, self.player.change_y)
        self.all_sprites.add(line)
        self.broken_sprites.add(line)

        line = BrokenParts(self.player.nose, midpoint2, self.player.change_x, self.player.change_y)
        self.all_sprites.add(line)
        self.broken_sprites.add(line)

        line = BrokenParts(self.player.tail1, midpoint1, self.player.change_x, self.player.change_y)
        self.all_sprites.add(line)
        self.broken_sprites.add(line)

        line = BrokenParts(self.player.tail2, midpoint2, self.player.change_x, self.player.change_y)
        self.all_sprites.add(line)
        self.broken_sprites.add(line)

        line = BrokenParts(self.player.tail1, midpoint_tail, self.player.change_x, self.player.change_y)
        self.all_sprites.add(line)
        self.broken_sprites.add(line)

        line = BrokenParts(self.player.tail2, midpoint_tail, self.player.change_x, self.player.change_y)
        self.all_sprites.add(line)
        self.broken_sprites.add(line)

    def bullet_collision(self):
        # bullets vs asteroids
        for bullet in self.bullet_sprites:
            for asteroid in self.asteroid_sprites:
                if pygame.sprite.collide_circle(bullet, asteroid):
                    bullet.kill()
                    old_score = self.score
                    self.score += int(asteroid.radius) + 100
                    if old_score % 20000 > self.score % 20000 or old_score < 10000 and self.score > 10000:
                        self.player.lives += 1
                        self.life_sound.play()
                    if asteroid.radius > 8:
                        self.make_babies(asteroid)
                    asteroid.kill()
                    break

    def make_babies(self, asteroid):
        for i in range(random.randrange(2, 4)):
            baby = Asteroid(int(asteroid.radius * (random.random()/5 + 0.4)), self.player)
            baby.rect.center = asteroid.rect.center
            baby.rect.centerx += random.randrange(-int(asteroid.radius * 3 / 4), int(asteroid.radius * 3 / 4))
            baby.rect.centery += random.randrange(-int(asteroid.radius * 3 / 4), int(asteroid.radius * 3 / 4))
            baby.x = baby.rect.centerx
            baby.y = baby.rect.centery
            baby.change_x += asteroid.change_x * 2 / 3
            baby.change_y += asteroid.change_y * 2 / 3
            self.all_sprites.add(baby)
            self.asteroid_sprites.add(baby)

    def draw_gui(self):
        # score and lives
        my_score = self.game_font.render("Score: " + str(self.score), True, WHITE)
        my_lives = self.game_font.render("Lives: " + str(max(0, self.player.lives - 1)), True, WHITE)
        my_shield = self.game_font.render("Shield:", True, WHITE)
        my_level = self.game_font.render("Level: " + str(self.level), True, WHITE)


        fps = self.clock.get_fps()
        self.fps_tracking.append(fps)
        if len(self.fps_tracking) > 100:
            self.fps_tracking.pop(0)
        fps = int(sum(self.fps_tracking) / len(self.fps_tracking))
        my_fps = self.power_font.render("FPS: " + str(fps), True, WHITE)

        # DRAW MY STATS
        self.screen.blit(my_score, [10, 5])
        self.screen.blit(my_lives, [10, 20])
        self.screen.blit(my_fps, [screen_width - my_fps.get_width(), screen_height - my_fps.get_height()])
        #self.screen.blit(my_level, [10, 40])

        if self.player.shield_time > 10 or self.frame % 30 > 10:
            self.screen.blit(my_shield, [10, 35])
            for x in range(my_shield.get_width() + 10, my_shield.get_width() + 10 + int((self.player.shield_time) / 2), 5):
                pygame.draw.line(self.screen, WHITE, [x, 40], [x, 48], linewidth)

            pygame.draw.rect(self.screen, WHITE, [my_shield.get_width() + 10, 40, 51, 8], linewidth)  # shield power

        if self.game_over == True:
            self.game_over_message()

        if self.paused:
            self.pause_message()

    def game_over_message(self):
        centered_text(self.screen, self.game_font, "GAME OVER", WHITE, -15)
        centered_text(self.screen, self.game_font, "SCORE:" + str(self.score), WHITE, 15)

        centered_text(self.screen, self.game_font, "Press START to play again", WHITE, 30)
        centered_text(self.screen, self.game_font, "Press MENU to quit", WHITE, 45)

    def pause_message(self):
        centered_text(self.screen, self.game_font, "PAUSED", WHITE, -15)

        centered_text(self.screen, self.game_font, "Press START to continue", WHITE, 30)
        centered_text(self.screen, self.game_font, "Press MENU to quit", WHITE, 45)


    def level_check(self):
        if len(self.asteroid_sprites) == 0:
            self.level += 1
            self.initialize_level()
            self.screen.fill(BLACK)
            pygame.display.flip()  # update the screen with what we've drawn.

    def add_powerup(self):
        #new_powerup = random.choice(self.power_up_list)
        #my_power = self.power_up_list[0]  # grab random item from list
        new_powerup = PowerUp("3x", self.player, self.power_font)  # position 1 is the message
        self.all_sprites.add(new_powerup)
        self.power_sprites.add(new_powerup)

        #my_power[0] = True  # position 0 is the attribute to turn it on.

    def draw_stars(self):
        for i in range(len(self.star_list)):
            self.twinkle_list[i][0] += 1
            if self.twinkle_list[i][0] % self.twinkle_list[i][1] > self.twinkle_list[i][2]:
                pygame.draw.line(self.screen, WHITE, self.star_list[i], self.star_list[i])

    def quit(self):
        self.done = True

    def set_volume(self, change):
        self.volume += change

        if self.volume > 100:
            self.volume = 100
        if self.volume < 0:
            self.volume = 0

        float_volume = min(1, self.volume / 100)
        self.bg.set_volume(float_volume)
        self.thrust_sound.set_volume(float_volume)
        self.fire_sound.set_volume(float_volume)
        self.life_sound.set_volume(float_volume)
        self.player.volume = float_volume


def centered_text(screen, font, message, color, y_offset):
    w, h = screen.get_size()
    my_text = font.render(message, True, color)
    x = w // 2 - my_text.get_width() // 2
    y = h // 2 - my_text.get_height() // 2 + y_offset
    screen.blit(my_text, [x, y])

def intro_screen(screen, clock):
    done = False
    can_click = True
    star_list = [[random.randrange(screen_width), random.randrange(screen_height)] for x in range(500)]
    star_list = []
    my_font = pygame.font.Font(
        "Hyperspace Bold.otf", 30)
    small_font = pygame.font.Font(
        "Hyperspace Bold.otf", 14)
    smaller_font = pygame.font.Font(
        "Hyperspace Bold.otf", 14)
    frame = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and can_click:
                if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                    can_click = False
                else:
                    done = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    can_click = True

        frame +=1
        screen.fill(BLACK)
        for star in star_list:
            pygame.draw.line(screen, WHITE, star, star)
        centered_text(screen, my_font, "Frankie and", WHITE, -100)
        centered_text(screen, my_font, "Benton's Game", WHITE, -50)

        centered_text(screen, small_font, "Controls", WHITE, -10)
        pygame.draw.line(screen, WHITE, [screen_width // 2 - 100, screen_height // 2 + 2],
                         [screen_width // 2 + 100, screen_height // 2 + 2], linewidth)
        centered_text(screen, smaller_font, "Left/right to rotate", WHITE, 20)
        centered_text(screen, smaller_font, "A to fire", WHITE, 40)
        centered_text(screen, smaller_font, "B for shields", WHITE, 60)
        if frame % 120 > 60:
            centered_text(screen, small_font, "Press any key to continue", WHITE, 180)


        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    my_game = Game()
    while not my_game.done:
        my_game.event_loop()
        my_game.update_code()
        my_game.draw_code()
    pygame.quit()  # safely close pygame