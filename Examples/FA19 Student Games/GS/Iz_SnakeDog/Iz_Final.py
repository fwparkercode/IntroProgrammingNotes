"""
This game is based off of the 90s game Snake, though rather than a snake eating
dots its a Dachshund eating hotdogs with the same basic goal. With every hotdog
it eats the longer the dog gets, and the dog dies when it runs into itself or
the fence surrounding the edge of the screen. The player controls the dog by
using the arrow keys and gains points by eating the hotdogs.
"""
import pygame
import random

from pygame.sprite import Group

pygame.init()  # italializes pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FENCE_BROWN = (156, 119, 68)
GRASS_GREEN = (100, 227, 106)
DOG_BROWN = (161, 91, 48)

# make dog blocks
dog_width = 25
dog_height = 25

# set dog speed
x_change = dog_width
y_change = 0
frame_rate = 5

# set hotdog variables
hotdog_x = random.randrange(40, 661)
hotdog_y = random.randrange(40, 661)

# Sprite Groups
all_sprites_list: Group = pygame.sprite.Group()
dog_sprites_list = pygame.sprite.Group()  # keeps dog blocks in one list
hotdog_sprites_list = pygame.sprite.Group()  # keeps all of the hotdogs in one list
hit_sprites_list = pygame.sprite.Group()  # keeps all collision blocks in one lsit
dog_segment_list = pygame.sprite.Group()  # keeps all dog parts in one list

# Intro Screen
opening_img = pygame.image.load("opening.png")

def intro_screen():
    done = False
    my_font = pygame.font.SysFont("DIN Condensed", 50, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(WHITE)
        screen.blit(opening_img, [0, 0])
        text = my_font.render("Welcome to hotDOG", True, BLACK)
        text_2 = my_font.render("Click any key to begin!", True, BLACK)
        screen.blit(text, [200, 100])
        screen.blit(text_2, [150, 150])
        pygame.display.flip()
        clock.tick(60)

# instruction screen
keys = pygame.image.load("keys.png")
def instructions():
    done = False
    my_font = pygame.font.SysFont("DIN Condensed", 50, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(GRASS_GREEN)

        text= my_font.render("Control the dog using:", True, WHITE)
        text_2 = my_font.render("Eat hotdogs to gain points!", True, WHITE)
        text_3 = my_font.render("Avoid yourself and the fence!", True, WHITE)
        text_4 = my_font.render("click any key to play", True, WHITE)
        text_5 = my_font.render("GOOD LUCK!!", True, WHITE)
        screen.blit(text, [50, 50])
        screen.blit(keys, [450, 20])
        screen.blit(text_2, [50, 150])
        screen.blit(text_3, [50, 250])
        screen.blit(text_4, [50, 350])
        screen.blit(text_5, [50, 450])
        pygame.display.flip()
        clock.tick(60)



# Game over Screen
outro_img = pygame.image.load("outro.png")
def outro_screen():
    done = False
    my_font = pygame.font.SysFont("DIN Condensed", 50, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(WHITE)
        screen.blit(outro_img, [0, 0])
        text = my_font.render("Oh no you lost!", True, BLACK)
        text_2 = my_font.render("Thanks for playing", True, BLACK)
        screen.blit(text, [200, 100])
        screen.blit(text_2, [150, 150])
        pygame.display.flip()
        clock.tick(60)


# Dog sprite
class Dog(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(DOG_BROWN)
        self.rect = self.image.get_rect()
        self.speed = 3
        self.change_x = self.rect.width
        self.change_y = 0
        self.dog_parts = []
        self.direction = "E"

    def update(self, *args):
        self.rect.x += self.change_x
        self.rect.y += self.change_y




# subclass for the dog parts
class DogSegment(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(DOG_BROWN)
        self.rect = self.image.get_rect()
        self.direction = "E"



# screen dimensions
SCREEN_WITDTH = 700
SCREEN_HIEGHT = 700

pygame.init()  # starting up game
done = False  # condition for game
# Set the width and height of the screen [width, height]
size = (SCREEN_WITDTH, SCREEN_HIEGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Iz Bruozis, Final Game: hotDOG")


# creates hotdog as a sprite
class Hotdog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("hotdog.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(60, 641)
        self.rect.y = random.randrange(60, 641)


# Puts Fence on screen
class Fence(pygame.sprite.Sprite):  # makes the fence and dog dies when it hits fence
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(FENCE_BROWN)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


# puts fence on edge of screen

fence_list = pygame.sprite.Group()
dog_part_group = pygame.sprite.Group()  # For dog segments

fence = Fence(0, 0, 700, 20)
fence_list.add(fence)
all_sprites_list.add(fence)

fence_2 = Fence(680, 0, 20, 700)
fence_list.add(fence_2)
all_sprites_list.add(fence_2)

fence_3 = Fence(0, 680, 700, 20)
fence_list.add(fence_3)
all_sprites_list.add(fence_3)

fence_4 = Fence(0, 0, 20, 700)
fence_list.add(fence_4)
all_sprites_list.add(fence_4)

# creates dog
dog = Dog(DOG_BROWN, 25, 25)  # head of the dog
dog.rect.x = 400
dog.rect.y = 400
dog.change_x = dog.rect.width
all_sprites_list.add(dog)

for i in range(3):
    dog_part = DogSegment(DOG_BROWN, 25, 25)
    dog.dog_parts.append(dog_part)
    dog_part.rect.x = dog.rect.x - dog.rect.width * (i + 1)
    dog_part.rect.y = dog.rect.y
    all_sprites_list.add(dog_part)
    dog_part_group.add(dog_part)


# Loop until the user clicks the close button.
done = False

clock = pygame.time.Clock()  # creates a clock object that manages updates

# brings first hotdog on screen
hotdog = Hotdog()
all_sprites_list.add(hotdog)
hotdog_sprites_list.add(hotdog)

# runs the into screen & instructions
intro_screen()
instructions()
# creates score
score = 0

# sounds
munch = pygame.mixer.Sound("munch.wav")
game_over = pygame.mixer.Sound("sad puppy.wav")
bg_music = pygame.mixer.Sound("puppy.wav")
bg_music.play(-1)
bg_music.set_volume(0.5)

# Main event loop

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:  # Makes the dog move
            if event.key == pygame.K_LEFT:
                dog.change_x = -dog.rect.width
                dog.change_y = 0
                dog.direction = "W"
            if event.key == pygame.K_RIGHT:
                dog.change_x = dog.rect.width
                dog.change_y = 0
                dog.direction = "E"
            if event.key == pygame.K_UP:
                dog.change_y = -dog.rect.width
                dog.change_x = 0
                dog.direction = "N"
            if event.key == pygame.K_DOWN:
                dog.change_y = dog.rect.width
                dog.change_x = 0
                dog.direction = "S"

# keeps track of the last position of the head
    last_pos = dog.rect.topleft
    all_sprites_list.update()

    #Gets rid of last dog
    move_me = dog.dog_parts.pop(-1)
    last_tail_pos = move_me.rect.topleft
    move_me.rect.topleft = last_pos
    move_me.direction = dog.direction

    dog.dog_parts.insert(0, move_me)




    # places new segment


    # colliding code
# when dog eat hotdog it adds a dogpart to the dog
    hit_sprites_list = pygame.sprite.spritecollide(dog, hotdog_sprites_list, True)
    for hit in hit_sprites_list:
        score += 1
        frame_rate += 0.5
        munch.play()
        hotdog = Hotdog()

        dog_part = DogSegment(DOG_BROWN, 25, 25)
        all_sprites_list.add(dog_part)
        dog_segment_list.add(dog_part)
        dog.dog_parts.append(dog_part)
        dog_part.rect.topleft = last_tail_pos
        dog_part.direction = dog.dog_parts[-1].direction

        # draws new hotdog
        all_sprites_list.add(hotdog)
        hotdog_sprites_list.add(hotdog)
# dog dies when it runs into itself
    hit_sprites_list = pygame.sprite.spritecollide(dog, dog_segment_list, False)
    for hit in hit_sprites_list:
        bg_music.stop()
        game_over.play()
        outro_screen()
        done = True
#dog dies when it runs into fence
    hit_sprites_list = pygame.sprite.spritecollide(dog, fence_list, False)
    for hit in hit_sprites_list:
        bg_music.stop()
        game_over.play()
        outro_screen()
        done = True

    screen.fill(GRASS_GREEN)
    all_sprites_list.draw(screen)
# places the tail in the correct orientation for the direction
    tail_seg = dog.dog_parts[-1]
    if tail_seg.direction == "E":
        pygame.draw.line(screen, DOG_BROWN, tail_seg.rect.center, [tail_seg.rect.left - 20, tail_seg.rect.centery], 3)
    elif tail_seg.direction == "S":
        pygame.draw.line(screen, DOG_BROWN, tail_seg.rect.center, [tail_seg.rect.centerx, tail_seg.rect.top - 20], 3)
    elif tail_seg.direction == "W":
        pygame.draw.line(screen, DOG_BROWN, tail_seg.rect.center, [tail_seg.rect.right + 20, tail_seg.rect.centery], 3)
    else:
        # NORTH

        pygame.draw.line(screen, DOG_BROWN, tail_seg.rect.center, [tail_seg.rect.centerx, tail_seg.rect.bottom + 20], 3)
# places the head in correct orientation for the directions

#ellipse
    if dog.direction == "E":
        pygame.draw.ellipse(screen, DOG_BROWN, [dog.rect.centerx, dog.rect.top, 50, 25])
        pygame.draw.ellipse(screen, DOG_BROWN, [dog.rect.centerx + dog.rect.width, dog.rect.centery - dog.rect.height, 10, 55])
        pygame.draw.ellipse(screen, BLACK, [dog.rect.centerx + (dog.rect.width + 17), dog.rect.centery - 4, 10, 10])
    elif dog.direction == "S":
        pygame.draw.ellipse(screen, DOG_BROWN, [dog.rect.left, dog.rect.centery, 25, 50])
        pygame.draw.ellipse(screen, DOG_BROWN, [dog.rect.centerx - dog.rect.width, dog.rect.centery + dog.rect.height, 55, 10])
        pygame.draw.ellipse(screen, BLACK, [dog.rect.centerx - 4, dog.rect.centery + (dog.rect.height + 17), 10, 10])
    elif dog.direction == "W":
        pygame.draw.ellipse (screen, DOG_BROWN, [dog.rect.centerx - (dog.rect.width + 20), dog.rect.top, 40, 25])
        pygame.draw.ellipse(screen, DOG_BROWN, [dog.rect.centerx - (dog.rect.width + 10), dog.rect.centery - dog.rect.height, 10, 55])
        pygame.draw.ellipse(screen, BLACK,[dog.rect.centerx - (dog.rect.width + 23), dog.rect.centery - 4, 10, 10] )
    else: #NORTH
        pygame.draw.ellipse(screen, DOG_BROWN, [dog.rect.left, dog.rect.centery - (dog.rect.height + 20), 25, 40])
        pygame.draw.ellipse(screen, DOG_BROWN, [dog.rect.centerx - dog.rect.width, dog.rect.centery - dog.rect.height, 55, 10])
        pygame.draw.ellipse(screen, BLACK, [dog.rect.centerx - 4, dog.rect.centery - (dog.rect.height + 23), 10, 10])



    my_font = pygame.font.SysFont("DIN Condensed", 30, True, False)
    text = my_font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [10, 10])



    pygame.display.flip()  # updates the screen

    clock.tick(int(frame_rate))  # frames per second

pygame.quit()  # Close the window and quit
