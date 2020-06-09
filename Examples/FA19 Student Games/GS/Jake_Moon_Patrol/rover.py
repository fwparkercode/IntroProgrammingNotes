'''
Rover class for Moon-Pytrol
Contains rover, bullets, and explosions. Rover class takes in gravity and speed from main program.
'''

import pygame

WHITE = (255, 255, 255)

class Rover(pygame.sprite.Sprite):

    def __init__(self, grav, ground_pos):
        super().__init__()
        self.image = pygame.image.load("assets/rover.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.origleftwheel = pygame.image.load("assets/leftwheel.png")
        self.origrightwheel = pygame.image.load("assets/rightwheel.png")
        self.leftwheel = self.origleftwheel
        self.rightwheel = self.origrightwheel
        self.leftwheelx = 0
        self.lefwheely = 0


        self.angle = 20
        self._leftwheel = self.leftwheel
        self.change_y = 0
        self.grav = grav
        self.ground_pos = ground_pos
        self.counter = 0
        self.status = "alive"
        self.jump_sfx = pygame.mixer.Sound("assets/sounds/jump.wav")

    def update(self, speed):
        if self.status == "alive":
            self.speed = speed
            self.rect.x += self.speed
            self.rect.y += self.change_y
        #self.jiggle()

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += self.grav
 
        # See if we are on the ground.
        if self.rect.bottom >= self.ground_pos - 7 and self.change_y >= 0:
            self.change_y = 0
            self.rect.bottom = self.ground_pos - 7
 
    def jump(self):
        # If rover is on the ground, move up, else don't
        if self.rect.bottom == self.ground_pos - 7:
            self.change_y = -4
            pygame.mixer.Channel(1).play(self.jump_sfx)

    def blitWheels(self, screen):
        if self.status == "alive":
            screen.blit(self.leftwheel, [self.rect.x + 3.5, self.rect.y + 30])
            screen.blit(self.rightwheel, [self.rect.x + 23.4, self.rect.y + 30])
            screen.blit(self.leftwheel, [self.rect.x + 42, self.rect.y + 30])

    def jiggle(self):
        if self.counter <= 5:
            self.rect.y += 0.5
            self.counter += 1
        if self.counter > 5:
            self.rect.y -= 0.5
            self.counter -= 1
        if self.counter == 11:
            self.counter = 0

'''
Classes for rover bullets (sideways single and upwards infinite)
'''

class UpBullet(pygame.sprite.Sprite):

    def __init__(self, rover):
        super().__init__()
        self.image = pygame.Surface([2, 13])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centery = rover.rect.centery - 10
        self.rect.centerx = rover.rect.centerx - 13

    def update(self):
        self.rect.y -= 8 # Move the bullets up
        if self.rect.bottom < 0: # off the top of the SCREEN_WIDTH
            self.kill()

class SideBullet(pygame.sprite.Sprite):

    def __init__(self, rover):
        super().__init__()
        self.image = pygame.image.load("assets/sidebullet_smaller.png")
        self.rect = self.image.get_rect()
        self.call_pos = rover.rect.centerx
        self.rect.x = rover.rect.centerx + 7
        self.rect.y = rover.rect.centery - 4
        self.sfx = pygame.mixer.Sound("assets/sounds/shoot.wav")
        self.sfx.set_volume(0.2)
        pygame.mixer.Channel(2).play(self.sfx)

    def update(self):
        self.rect.x += 5
        if self.rect.left >= self.call_pos + 145:
            self.kill()

'''
Explosion upon rover death. List is of explosion frames for cycling.
'''

class Explosion(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.explosion_image_list = ["assets/explosion5.png", 
                        "assets/explosion4.png", 
                        "assets/explosion3.png", 
                        "assets/explosion2.png", 
                        "assets/explosion1.png"]
        self.explosion_image_index = 0
        self.image = pygame.image.load(self.explosion_image_list[0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame = 0 # Keep track of time
        self.last_update = pygame.time.get_ticks()
        self.speed = 60 # How fast images should cycle

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.speed:
            self.last_update = now
            self.frame += 1
        if self.frame == len(self.explosion_image_list):
            self.kill() # If explosion is over, kill
        else:
            self.image = pygame.image.load(self.explosion_image_list[self.frame]) # Cycle image
            self.rect = self.image.get_rect(center=self.rect.center) # Keeps explosion centered

# -------- Main Program Loop -----------

if __name__ == "__main__":

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    angle = 0
    ground_pos = 240
    rover_speed = 0.5
    rover_gravity = 0.4

    pygame.init()
    
    all_sprites_list = pygame.sprite.Group()
    bullet_sprites_list = pygame.sprite.Group()

    rover = Rover(rover_gravity, ground_pos)
    rover.rect.x = 320
    rover.rect.y = 200

    all_sprites_list.add(rover)

    pygame.display.set_caption("Rover Class")
    screen_width = 640
    screen_height = 300
    screen = pygame.display.set_mode([screen_width, screen_height])
    done = False
    clock = pygame.time.Clock()

    bg_music = pygame.mixer.Sound("assets/sounds/theme_bigger.wav")


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                new_bullet = UpBullet(rover) # make new bullet sprite
                new_side_bullet = SideBullet(rover)
                all_sprites_list.add(new_bullet) # adding it to the container to be drawn
                all_sprites_list.add(new_side_bullet)
                bullet_sprites_list.add(new_bullet)
                bullet_sprites_list.add(new_side_bullet)

        # Clear the screen
        screen.fill(BLACK)

        # Draw stuff
        all_sprites_list.draw(screen)
        rover.blitWheels(screen)
        rover.calc_grav()
        rover.update(rover_speed)

        bullet_sprites_list.update()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
