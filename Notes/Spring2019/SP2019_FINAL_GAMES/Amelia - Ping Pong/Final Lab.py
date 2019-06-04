import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CAR_RED = (240, 41, 41)
YELLOW = (255, 255, 0)
SKY_BLUE = (83, 145, 244)
BROWN = (147, 81, 22)
PINK = (243, 123, 198)
GREY = (151, 149, 150)
DARK_GREEN = (31, 124, 37)
DARK_GREY = (79, 86, 79)
NEON_GREEN = (68, 236, 68)
LIGHT_BLUE = (146, 196, 240)
TAILLIGHT= (171, 12, 12)
FRONT_LIGHT = (245, 234, 169)
WINDOW = (112, 140, 171)
CAR_GREEN = (55, 144, 61)
SUN = (255, 237, 83)
NAVY = (37, 84, 171)
PING = (11, 79, 151)
DARK_BLUE = (5, 48, 93)

pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 600)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode(size)
y_offset = 0
paddle_y = 0
topleft = (100, 100)
top = 0


my_font = pygame.font.SysFont('Calibri', 70, True, False)
my_startfont = pygame.font.SysFont('Verdana', 50, True, False)
my_directionfont = pygame.font.SysFont('Verdana', 30, True, False)
my_instructions = pygame.font.SysFont('Calibri', 40, True, False)
paddles_image = "paddles.png"





ball_hit = pygame.mixer.Sound("ballhit.wav")

background_music = pygame.mixer.Sound("song.wav")
background_music.play(-1)


pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("player1racket.png")
        self.rect = self.image.get_rect()
        self.change_y = 0
        self.rect.x = x
        self.score_1 = 0
        self.score_2 = 0


    def update(self):

        self.rect.y += self.change_y
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 500:
            self.rect.y = 500






class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ball.png")
        self.rect = self.image.get_rect()
        self.change_x = random.randrange(1, 3)
        self.change_y = 3.5
        self.color = WHITE
        self.rect = self.image.get_rect()



    def draw(self):
        self.image = pygame.Surface([20,20])
        self.rect = self.image.get_rect()
        self.x = 200
        self.rect.y = 200



    def update(self):

        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.bottom > 495:
            self.change_y *= -1
        if self.rect.top < 100:
            self.change_y *= -1





all_sprites_list = pygame.sprite.Group()
paddle_group = pygame.sprite.Group()


player_1 = Paddle(10, 0)
player_1.name = "Player 1"
all_sprites_list.add(player_1)
paddle_group.add(player_1)
score_1 = 0


player_2 = Paddle(720, 0)
player_2.name = "Player 2"
all_sprites_list.add(player_2)
paddle_group.add(player_2)
score_2 = 0

ball = Ball()
ball.rect.center = [screen_width//2, screen_height//2]
ball.name = "Ball"
all_sprites_list.add(ball)



# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def cut_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(NAVY)
        text = my_font.render("WELCOME TO PING PONG", True, WHITE)
        screen.blit(text, [50, 60])
        text3 = my_directionfont.render("(Do NOT let the ball get "
                                        "past your paddle)", True, WHITE)
        screen.blit(text3, [50, 470])
        text4 = my_startfont.render("press spacebar to play", True, WHITE)
        screen.blit(text4, [85, 400])

        instructions = my_instructions.render("player 1: tab and shift    player 2: return an shift", True, DARK_BLUE)
        screen.blit(instructions, [25, 530])
        paddles = pygame.image.load("paddles.png")
        screen.blit(paddles, [110, 45])



        
        pygame.display.flip()
        clock.tick(60)
cut_screen()
# -------- Main Program Loop -----------

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                player_1.change_y = -5
            if event.key == pygame.K_LSHIFT:
                player_1.change_y = 5

            if event.key == pygame.K_RETURN:
                player_2.change_y = -5
            if event.key == pygame.K_RSHIFT:
                player_2.change_y = 5

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_TAB or event.key == pygame.K_LSHIFT:
                player_1.change_y = 0
            if event.key == pygame.K_RETURN or event.key == pygame.K_RSHIFT:
                player_2.change_y = 0

    # --- Game logic should go here

    all_sprites_list.update()

    hit_list = pygame.sprite.spritecollide(ball, paddle_group, False)
    for hit in hit_list:

        if ball.change_x > 0:
            ball.rect.right = hit.rect.left

        else:
            ball.rect.left = hit.rect.right

        ball.change_x *= -1.3
        ball_hit.play()



    if ball.rect.left > screen_width:
        ball.rect.center = [screen_width // 2, screen_height // 2]
        ball.change_x *= -1
        ball.change_x = -3
        score_1 += 1





    if ball.rect.right < 0:
        ball.rect.center = [screen_width // 2, screen_height // 2]
        ball.change_x *= -1
        ball.change_x = -3
        score_2 += 1

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(PING)

    # --- Drawing code should go here

    pygame.draw.line(screen, LIGHT_BLUE, [0, 0], [800, 0], 196)  # GROUND TOP BORDER
    pygame.draw.line(screen, LIGHT_BLUE, [0, 600], [800, 600], 196)  # GROUND BOTTOM BORDER
    pygame.draw.line(screen, LIGHT_BLUE, [50, 98], [50, 502], 15)  # WHITE LEFT BORDER
    pygame.draw.line(screen, LIGHT_BLUE, [0, 98], [0, 502], 100)  # WHITE LEFT BORDER
    pygame.draw.line(screen, LIGHT_BLUE, [800, 98], [800, 502], 100)  # WHITE RIGHT BORDER

    pygame.draw.line(screen, WHITE, [50, 105], [750, 105], 15)  # WHITE TOP BORDER
    pygame.draw.line(screen, WHITE, [50, 495], [750, 495], 15)  # WHITE BOTTOM BORDER
    pygame.draw.line(screen, WHITE, [50, 98], [50, 502], 15)  # WHITE LEFT BORDER
    pygame.draw.line(screen, WHITE, [750, 98], [750, 502], 15)  # WHITE RIGHT BORDER
    pygame.draw.line(screen, WHITE, [50, 305], [750, 305], 3)  # WHITE HORIZONTAL MIDDLE
    pygame.draw.line(screen, BLACK, [395, 113], [395, 487], 6)  # WHITE CENTER BORDER


    all_sprites_list.draw(screen)





    my_text = my_font.render(" PING PONG ", True, DARK_BLUE)
    screen.blit(my_text, [232, 30])
    my_text = my_font.render(" PING PONG ", True, WHITE)
    screen.blit(my_text, [226, 30])

    my_text = my_font.render("Score: " + str(score_1), True, DARK_BLUE)  # creates a rendered graphical object my_text
    screen.blit(my_text, [115, 520])
    my_text = my_font.render("Score: " + str(score_1), True, WHITE)  # creates a rendered graphical object my_text
    screen.blit(my_text, [110, 520])
    my_text = my_font.render("Score: " + str(score_2), True, DARK_BLUE)  # creates a rendered graphical object my_text
    screen.blit(my_text, [485, 520])
    my_text = my_font.render("Score: " + str(score_2), True, WHITE)  # creates a rendered graphical object my_text
    screen.blit(my_text, [480, 520])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)



# Close the window and quit.
pygame.quit()
