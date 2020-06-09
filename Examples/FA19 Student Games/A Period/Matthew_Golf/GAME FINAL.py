"""
 GOLF
 Matthew Garchik - 2019

 Aid From Mr. Lee on order and indentation levels
"""
import random
import math

import pygame
pygame.init()  # initializes pygame (need to do this before you use it)

# Global Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE = (200, 200, 255)
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

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.

# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game!")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

my_font = pygame.font.SysFont("Calibri", 30, True, False)

level = 0

ball_size = 20

strokes = 0

mode = 1

grass_image = pygame.image.load("grass.png")

splash = pygame.mixer.Sound("Water Drop-SoundBible.com-2039669379.wav")

hole_sound = pygame.mixer.Sound("glass_ping-Go445-1207030150 (1).wav")

launch_sound = pygame.mixer.Sound("Golf Club Swing-SoundBible.com-1724786007.wav")
#  Classes

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("golf_ball.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - 50
        self.initial_x = 50
        self.initial_y = SCREEN_HEIGHT - 50
        self.change_y = 0
        self.change_x = 0
        self.gravity = .5
        self.elasticity = 0.5
        self.x = self.rect.x
        self.y = self.rect.y
        self.rect = self.image.get_rect()
        self.last_x = self.initial_x
        self.last_y = self.initial_y

    def launch(self, stroke):
        if -.0001 < self.change_x < .0001:
            launch_sound.play()
            (x, y) = pygame.mouse.get_pos()
            self.change_y = max(-(self.y - y) / 10, -21)
            print(self.change_y)
            if x - self.x >= 0:
                self.change_x = min((x - self.x) / 10, 10)
                stroke += 1
                print(stroke)
            else:
                self.change_x = max(((x - self.x) / 10), -10)
                stroke += 1
                print(stroke)
        return stroke

    def update(self):
        self.change_y += self.gravity
        if self.change_y < (SCREEN_HEIGHT - 50) - self.y:
            self.y += self.change_y
        else:
            self.y += (SCREEN_HEIGHT - 50) - self.y
            self.y = SCREEN_HEIGHT - 50
            self.change_x *= self.elasticity
            self.change_y *= -self.elasticity

        self.x += self.change_x
        self.rect.x, self.rect.y = (self.x, self.y)

        if self.y > SCREEN_HEIGHT - 50:
            self.y = SCREEN_HEIGHT - 50
            self.change_x *= self.elasticity
            self.change_y *= -self.elasticity

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH - 1
#            self.change_x *= -self.elasticity
            self.change_x *= -1

        if self.x <= 0:
            self.x = 0
#            self.change_x *= -self.elasticity
            self.change_x *= -1

        if -.0001 < self.change_x < .0001:
            self.last_x, self.last_y = self.x, self.y

    def draw_line(self):
        start_x, start_y = self.rect.center
        x, y = pygame.mouse.get_pos()
        if y > start_y:
            y = start_y
        if -.0001 < self.change_x < .0001:
            if x - start_x >= 0:
                pygame.draw.line(screen, BLACK, (start_x, start_y), (min(((x - start_x) / 2) + start_x, start_x + 150),
                                                                     max(y + ((start_y - y) / 2),
                                                                         SCREEN_HEIGHT - 150 - (
                                                                                 SCREEN_HEIGHT - start_y))), 5)
            else:
                pygame.draw.line(screen, BLACK, (start_x, start_y), (max(((x - start_x) / 2) + start_x, start_x - 150),
                                                                     max(y + ((start_y - y) / 2),
                                                                         SCREEN_HEIGHT - 150 - (
                                                                                     SCREEN_HEIGHT - start_y))), 5)


class Hole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 5])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(200, SCREEN_WIDTH - 40)
        self.rect.y = SCREEN_HEIGHT - 40

    def draw(self):
        pygame.draw.ellipse(screen, BLACK, [self.rect.x - 15, SCREEN_HEIGHT - 60 + ball_size, 40, 24])


class Water(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pond-transparent-3.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = random.randrange(375, SCREEN_WIDTH - 265)
        self.rect.y = SCREEN_HEIGHT - 70


class Walls(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


#  Functions
def get_par(level):
    if level == 1:
        this_par = 1
    if level == 2:
        this_par = 2
    if level > 2:
        this_par = 1
    return this_par


def centered_text(screen, message, color):
    my_text = my_font.render(message, True, color)
    x = SCREEN_WIDTH // 2 - my_text.get_width() // 2
    y = SCREEN_HEIGHT // 2 - my_text.get_height() // 2
    screen.blit(my_text, [x, y])


def level_screen():
    # 5 second cut screen
    done = False
    for i in range(300):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                done = True

        if done:
            break

        screen.fill(WHITE)

        if level == 2:
            my_text = my_font.render("Press Space To Exit Cut Screens", True, BLACK)
            screen.blit(my_text, [10, 10])

        centered_text(screen, "Hole " + str(level), BLACK)

        pygame.display.flip()
        clock.tick(60)


def intro_screen():
    intro_done = False
    mode = 0
    while not intro_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro_done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    intro_done = True
                    mode = 1
                elif event.key == pygame.K_2:
                    intro_done = True
                    mode = 2
                if mode == 1 or mode == 2:
                    return mode
        screen.fill(WHITE)

        centered_text(screen, "Press 1 For 9 Holes or 2 For 18 Holes", BLACK)

        pygame.display.flip()
        clock.tick(60)


def end_screen():
    end_done = False
    while not end_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_done = True
        if mode == 1 and level > 9:
            screen.fill(WHITE)
            centered_text(screen, "You Shot " + str(strokes) + " On 9 Holes", BLACK)
        elif mode == 2 and level > 18:
            screen.fill(WHITE)
            centered_text(screen, "You Shot " + str(strokes) + " On 18 Holes", BLACK)
        else:
            screen.fill(WHITE)
            centered_text(screen, "You Quit!", BLACK)

        pygame.display.flip()
        clock.tick(60)


def water_screen():
    done = False
    for i in range(300):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                done = True

        if done:
            break

        screen.fill(WHITE)

        centered_text(screen, "SPLASH! +1 Stroke", BLUE)

        pygame.display.flip()
        clock.tick(60)


mode = intro_screen()
level += 1

print("mode", mode)

all_sprites_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
water_list = pygame.sprite.Group()

player = Player()
all_sprites_list.add(player)
player_list.add(player)

hole = Hole()
all_sprites_list.add(hole)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            end_screen()

        if event.type == pygame.MOUSEBUTTONDOWN:
            strokes = player.launch(strokes)

    # --- Game logic should go here

    all_sprites_list.update()
    ball_in_hole_collision = pygame.sprite.spritecollide(hole, player_list, False)

    for hit in ball_in_hole_collision:
        hole_sound.play()
        level += 1

        if mode == 1 and level > 9:
            done = True
            end_screen()
        elif mode == 2 and level > 18:
            done = True
            end_screen()

        if mode == 1 and level < 10 or mode == 2 and level < 19:
            level_screen()
            if level > 3:
                hole.rect.x = random.randrange(525, SCREEN_WIDTH - 40)

            else:
                hole.rect.x = random.randrange(100, SCREEN_WIDTH - 40)

            if level > 3:
                if level == 4:
                    water = Water()
                    all_sprites_list.add(water)

                water.rect.y = SCREEN_HEIGHT - 70
                water.rect.x = random.randrange(220, SCREEN_WIDTH - 275)

            hole.rect.y = SCREEN_HEIGHT - 40

            ball_in_hole_collision.clear()
            player.x = player.initial_x
            player.y = player.initial_y
            player.change_x = 0
            player.change_y = 0

    if level > 3:
        if pygame.sprite.collide_mask(player, water):
            splash.play()

            strokes += 1
            player.x = player.last_x
            player.y = player.last_y
            player.change_x = 0
            player.change_y = 0
            water_screen()

    par = get_par(level)

    # --- Drawing code goes here
    screen.fill(WHITE)
    screen.blit(grass_image, [0, SCREEN_HEIGHT - 304])

    all_sprites_list.draw(screen)
    hole.draw()
    player.draw_line()

    my_text = my_font.render("Hole:" + str(level), True, BLACK)
    screen.blit(my_text, [10, 10])
    my_text = my_font.render("Par:" + str(par), True, BLACK)
    screen.blit(my_text, [10, 40])
    my_text = my_font.render("Strokes:" + str(strokes), True, BLACK)
    screen.blit(my_text, [10, 70])

    if level == 1:
        centered_text(screen, "Click Mouse To Launch", BLACK)
    if level == 4:
        centered_text(screen, "Water Sends You To Your Last Position And +1 Stroke", BLUE)

    pygame.display.flip()  # --- Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # --- Limit to 60 frames per second

pygame.quit()

