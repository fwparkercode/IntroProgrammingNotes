'''
Sprite classes for asteroids
'''

import math
import random
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
board_width = 10000
board_height = 10000
screen_width = 1000
screen_height = 700
level = 1


class Player(pygame.sprite.Sprite):
    # my ship
    def __init__(self, x, y):
        super().__init__()
        self.radius = 20
        self.image = pygame.Surface([20,20])
        self.image.set_colorkey(BLACK)  # using pygame primitives instead
        self.rect = self.image.get_rect()
        self.angle = math.pi / 2  # start facing up
        self.angle_speed = 0  # start with no rotation
        self.length = 15  # referenced in pygame drawing
        self.thrust_on = False  # show flame and add speed
        self.thrust = 0.1  # how much speed we add
        self.thrust_x = 0  # trig components of accel
        self.thrust_y = 0
        self.x = x  # real location of ship (used for float precision)
        self.y = y
        self.change_x = 0  # component vector of speed
        self.change_y = 0
        self.triple = False  # do I have triple shot power up
        self.power_time = 0  # time remaining on powerup
        self.dead = False
        self.dead_timer = 150
        self.dead_speed = [[random.random() + 0.5, random.random() + 0.5] for x in range(3)]
        self.lives = 3
        self.dead_flag = False
        self.broken_parts_list = [[[0, 0], [0, 0]]]
        self.active = True
        self.asteroid_sprites = None

    def update(self):
        if not self.active:
            self.rect.center = (screen_width // 2, screen_height // 2)
            for asteroid in self.asteroid_sprites:
                if pygame.sprite.collide_circle_ratio(3)(self, asteroid):
                    self.rect.center = (-1000, -1000)
                    return
            else:
                self.active = True
                self.x = self.rect.x
                self.y = self.rect.y

        self.power_time -= 1  # clock to countdown how long we have a power.

        self.angle += self.angle_speed  # spin me

        if self.thrust_on:
            self.thrust_x = math.cos(self.angle) * self.thrust
            self.thrust_y = math.sin(self.angle) * self.thrust
        else:
            self.thrust_x = 0
            self.thrust_y = 0

        # move in x
        self.change_x += self.thrust_x
        self.x += self.change_x
        self.rect.centerx = self.x  # update the rect with true value

        # wrap horizontal
        if self.rect.left > screen_width:
            self.rect.right = 0
            (self.x, self.y) = self.rect.center

        if self.rect.right < 0:
            self.rect.left = screen_width
            (self.x, self.y) = self.rect.center

        # move in y
        self.change_y += self.thrust_y
        self.y += self.change_y
        self.rect.centery = self.y

        # wrap vertical
        if self.rect.top > screen_height:
            self.rect.bottom = 0
            (self.x, self.y) = self.rect.center

        if self.rect.bottom < 0:
            self.rect.top = screen_height
            (self.x, self.y) = self.rect.center


        # if self.dead_timer < 0 and self.dead_flag:
        #     player.rect.center = (screen_width // 2, screen_height // 2)
        #     for asteroid in asteroid_sprites:
        #         if asteroid.rect.centerx > screen_width // 2 - 100 and asteroid.rect.centerx < screen_width // 2 + 100 and asteroid.rect.centery > screen_height // 2 - 100 and asteroid.rect.centery < screen_height // 2 + 100:
        #             break
        #     else:
        #         self.dead_timer = 150
        #         self.dead = False



    def change_angle_speed(self, val):
        self.angle_speed += val

    def draw_me(self, screen):
        # grab local x, y from rect value
        if not self.active: return

        x, y = self.rect.center

        # where is the nose of my craft (pair)
        self.nose = (x + math.cos(self.angle) * self.length, y + math.sin(self.angle) * self.length)

        # left tail pair
        self.tail1 = (x + math.cos(self.angle + 2.4) * self.length, y + math.sin(self.angle + 2.4) * self.length)

        # right tail pair
        self.tail2 = (x + math.cos(self.angle - 2.4) * self.length, y + math.sin(self.angle - 2.4) * self.length)

        # draw my ship using pairs
        pygame.draw.line(screen, WHITE, self.nose, self.tail1, 3)
        pygame.draw.line(screen, WHITE, self.nose, self.tail2, 3)
        pygame.draw.line(screen, WHITE, self.tail1, self.tail2, 3)


        # if the thruster is on, draw the thruster
        if self.thrust_on:
            self.draw_thrust(screen, x, y)

    def draw_thrust(self, screen, x, y):
        flamenose = [x - math.cos(self.angle) * self.length * 1.5, y - math.sin(self.angle) * self.length * 1.5]
        flamelen = self.length * 0.8
        flame1 = [x - math.cos(self.angle - 0.3) * flamelen,
                  y - math.sin(self.angle - 0.3) * flamelen]
        flame2 = [x - math.cos(self.angle + 0.3) * flamelen,
                  y - math.sin(self.angle + 0.3) * flamelen]
        pygame.draw.polygon(screen, WHITE, [flamenose, flame1, flame2], 3)
        #pygame.draw.line(screen, WHITE, flamenose, flamenose, 10)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle, center):
        super().__init__()
        self.radius = 2
        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.angle = angle
        self.speed = 10
        self.change_x = math.cos(self.angle) * self.speed
        self.change_y = math.sin(self.angle) * self.speed
        self.x = center[0]
        self.y = center[1]
        self.rect.center = [self.x, self.y]
        self.health = 50
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.x += self.change_x
        self.rect.centerx = self.x
        if self.rect.left > screen_width:
            self.rect.right = 0
            (self.x, self.y) = self.rect.center

        if self.rect.right < 0:
            self.rect.left = screen_width
            (self.x, self.y) = self.rect.center

        self.y += self.change_y
        self.rect.centery = self.y
        if self.rect.top > screen_height:
            self.rect.bottom = 0
            (self.x, self.y) = self.rect.center

        if self.rect.bottom < 0:
            self.rect.top = screen_height
            (self.x, self.y) = self.rect.center

        self.health -= 1
        if self.health < 0:
            self.kill()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, radius):
        super().__init__()
        self.image = pygame.Surface([radius * 2, radius * 2])
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = radius
        self.spokes = random.randrange(5, 10)
        self.spoke_angles = [x * (2 * math.pi) / self.spokes + random.random() - 0.5 for x in range(self.spokes)]
        self.spoke_lengths = [random.randrange(self.radius - self.radius // 3, self.radius) for x in range(self.spokes)]
        self.polygon = [[self.rect.width/2 + math.cos(self.spoke_angles[i]) * self.spoke_lengths[i], self.rect.height/2 + math.sin(self.spoke_angles[i]) * self.spoke_lengths[i]] for i in range(self.spokes)]
        #print(self.spoke_angles)
        #self.image.fill(WHITE)
        print(self.spokes, self.spoke_angles, self.spoke_lengths, self.polygon)
        pygame.draw.polygon(self.image, WHITE, self.polygon, 3)
        self.angle = 0
        self.angle_speed = random.random() / 20 - 0.025

        self.change_x = random.random() * 3 - 1.5
        self.change_y = random.random() * 3 - 1.5
        if random.randrange(2):
            self.x, self.y = random.randrange(screen_width // 3), random.randrange(screen_height)
        else:
            self.x, self.y = random.randrange(screen_width - screen_width // 3, screen_width), random.randrange(screen_height)



    def update(self):
        self.angle += self.angle_speed
        for i in range(len(self.polygon)):
            self.polygon[i] = [self.rect.width/2 + math.cos(self.spoke_angles[i] + self.angle) * self.spoke_lengths[i], self.rect.height/2 + math.sin(self.spoke_angles[i] + self.angle) * self.spoke_lengths[i]]

        self.x += self.change_x
        self.rect.centerx = self.x
        if self.rect.left > screen_width:
            self.rect.right = 0
            (self.x, self.y) = self.rect.center

        if self.rect.right < 0:
            self.rect.left = screen_width
            (self.x, self.y) = self.rect.center

        self.y += self.change_y
        self.rect.centery = self.y
        if self.rect.top > screen_height:
            self.rect.bottom = 0
            (self.x, self.y) = self.rect.center

        if self.rect.bottom < 0:
            self.rect.top = screen_height
            (self.x, self.y) = self.rect.center

    def draw_me(self, screen):
        self.image.fill(BLACK)
        pygame.draw.polygon(self.image, WHITE, self.polygon, 3)


class TripleShot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 600
        self.image = pygame.Surface([40, 20])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont("Calibri", 20, True, False)
        self.message = self.font.render("x3", True, WHITE)
        if random.randrange(2):
            self.x, self.y = random.randrange(screen_width // 3), random.randrange(screen_height)
        else:
            self.x, self.y = random.randrange(screen_width - screen_width // 3, screen_width), random.randrange(screen_height)
        self.rect.center = (self.x, self.y)

    def update(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()

    def draw_me(self, screen):
        screen.blit(self.message, self.rect.topleft)


class BrokenParts(pygame.sprite.Sprite):
    def __init__(self, point1, point2, change_x, change_y):
        super().__init__()
        self.health = 300
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.center = midpoint(point1, point2)
        self.x = self.center[0]
        self.y = self.center[1]
        self.rect.center = (self.x, self.y)
        self.change_x = change_x + random.random() - 0.5
        self.change_y = change_y + random.random() - 0.5
        self.angle = 0
        self.angle_speed = random.random() / 10
        self.length = 10
        self.point1 = [point1[0], point1[1]]
        self.point2 = [point2[0], point2[1]]

    def update(self):
        self.health -= 1
        if self.health < 0:
            self.kill()
        self.x += self.change_x
        self.y += self.change_y
        self.angle += self.angle_speed
        self.point1[0] = self.x + math.cos(self.angle) * self.length
        self.point1[1] = self.y + math.sin(self.angle) * self.length
        self.point2[0] = self.x + math.cos(self.angle + math.pi) * self.length
        self.point2[1] = self.y + math.sin(self.angle + math.pi) * self.length
        self.rect.center = (self.x, self.y)


    def draw_me(self, screen):
        pygame.draw.line(screen, WHITE, self.point1, self.point2, 3)



def midpoint(point1, point2):
    x = (point1[0] + point2[0]) // 2
    y = (point1[1] + point2[1]) // 2
    return x, y

if __name__ == "__main__":
    pass