"""
 Tennis Stars
 by Max Samuels 2019
 In this game the player uses the right and left arrow keys to run back and forth along the court and hit the ball.
 The goal is to get the highest score possible and essentially could go on forever. This will ot happen because the ball
 gets faster every five scores. The player has one life so there is no room for mistakes. Have Fun!
"""
import pygame
import random

pygame.init()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TENNIS_GREEN = (108, 191, 73)
TENNIS_BLUE = (213, 87, 70)
TENNIS_BALL_YELLOW = (255, 255, 0)

screen_height = 588
screen_width = 500
size = (screen_width, screen_height)  # width, height
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tennis Stars")

# Classes
# class for the player the user controls


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_list = [pygame.image.load("playerdown_5left.png"),
                           pygame.image.load("playerdown_8left.png"),
                           pygame.image.load("playerdown_8.png"),
                           pygame.image.load("playerdown_5.png"),
                           pygame.image.load("playerdown_12.png")]  # hit sprite
        self.image = pygame.image.load("playerdown_1.png")  # player's starting position sprite
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = screen_height - 85
        self.frame = 0
        self.change_x = 0

    def update(self):  # walking code
        self.frame += 1
        self.rect.x += self.change_x
        if self.change_x > 0:
            if self.frame % 30 < 15:
                self.image = self.image_list[2]
            else:
                self.image = self.image_list[3]
        elif self.change_x < 0:
            if self.frame % 30 < 15:
                self.image = self.image_list[0]
            else:
                self.image = self.image_list[1]


# class for ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.change_y = 3
        self.image = pygame.image.load("ball.00.png")
        self.ball_bounce = pygame.image.load("ball.02.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(140, 360)  # randomizes x position
        self.rect.y = 5  # starts at baseline opposite the player

    def update(self):
        self.image = pygame.image.load("ball.00.png")
        self.rect.y += self.change_y

    def hit(self):
        self.change_y *= -1  # changes direction of ball when it collides with player

    def bounce(self):
        self.image = self.ball_bounce


# background image
background_image = pygame.image.load("tennisfield.jpg")

# Shadow image
shadow_ball_image = pygame.image.load("ball.shadow.png")

# Sound effects / music
tennis_ball_hit = pygame.mixer.Sound("tennis_hit.wav")
background_music = pygame.mixer.Sound("easyjoy.wav")
tennis_point = pygame.mixer.Sound("Rise03.wav")

# set volumes
background_music.set_volume(.5)
tennis_point.set_volume(.8)
tennis_ball_hit.set_volume(10)

# play background music
background_music.play(-1)

# variables for switching between two sprites to walk
frame = 0
frame2 = 0


# function with intro screen, end screen, variables for both screens and
def main():

    all_sprites_group = pygame.sprite.Group()  # create groups
    ball = Ball()
    player = Player()

    all_sprites_group.add(ball)
    all_sprites_group.add(player)

    my_font = pygame.font.SysFont("Calibri", 30, True, False)  # font for words to be blit to screen

    score = 0  # variable to keep track of score
    score_counter = 1  # variable to increase speed of ball based on score

    done = False
    clock = pygame.time.Clock()  # manages how fast the screen updates

    # into screen function
    def intro_screen():
        done = False
        # words for into screen
        text3 = my_font.render("Press any key to Start!", True, WHITE)
        text2 = my_font.render("Use left and right arrow keys to move", True, WHITE)
        text4 = my_font.render("Have fun!", True, WHITE)
        text = my_font.render("Welcome to Tennis Stars", True, WHITE)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # closes window
                if event.type == pygame.KEYDOWN:
                    done = True  # continues to game
                if event.type == pygame.MOUSEBUTTONDOWN:
                    done = True  # continues to game
            screen.fill(BLACK)  # background of into screen
            # code to center text
            screen.blit(text, [screen_width // 2 - text.get_rect().width // 2,
                               screen_height // 2 - text.get_rect().height // 2 - 100])
            screen.blit(text2, [screen_width // 2 - text2.get_rect().width // 2,
                                screen_height // 2 - text2.get_rect().height // 2 - 50])
            screen.blit(text3, [screen_width // 2 - text3.get_rect().width // 2,
                                screen_height // 2 - text3.get_rect().height // 2])
            screen.blit(text4, [screen_width // 2 - text4.get_rect().width // 2,
                                screen_height // 2 - text4.get_rect().height // 2 + 50])
            pygame.display.flip()

    # end screen function
    def end_screen():
        done = False
        # end screen text
        text = my_font.render("Game Over. Your score was " + str(score), True, WHITE)
        text2 = my_font.render("Press R to restart or Q to quit", True, WHITE)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # quits window
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main()  # goes back to intro screen if r key is pressed
                    if event.key == pygame.K_q:
                        pygame.quit()  # quits window if q key is pressed

            screen.fill(BLACK)  # background for end screen
            # code to center text
            screen.blit(text, [screen_width // 2 - text.get_rect().width // 2,
                               screen_height // 2 - text.get_rect().height // 2 - 50])
            screen.blit(text2, [screen_width // 2 - text.get_rect().width // 2,
                                screen_height // 2 - text.get_rect().height // 2])
            pygame.display.flip()
    intro_screen()

    # main program loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # quits window
            # code that controls the movement of the player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.change_x += 1.3
                if event.key == pygame.K_LEFT:
                    player.change_x += -1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.change_x = 0
                if event.key == pygame.K_LEFT:
                    player.change_x = 0

        if pygame.sprite.collide_rect(player, ball):
            ball.hit()  # changes direction of the ball
            player.image = player.image_list[4]  # hitting sprite  # CHANGE THE LIST
            tennis_ball_hit.play()  # plays hitting sound
            ball.rect.y -= 11  # Before if you the ball with the side of the player the ball would bounce
            # forward and backward rapidly. Now it goes faster when it hits the player so it won't glitch'''

        # Game logic

        if ball.rect.y <= -20:  # code for when the ball crosses the top of the screen after hit by the player
            ball.rect.x = random.randrange(140, 360)  # puts the ball in a random location along the top of the screen
            ball.rect.y = 5
            ball.change_y *= -1  # sends the ball in its new position back towards the player
            ball.rect.y += ball.change_y
            score += 1  # adds one point to the score
            tennis_point.play()  # plays point sound effect

        # code to increase speed of ball every 5 scores
        if score / 5 == score_counter:  # score counter starts at 1
            ball.change_y += 1  # increases speed of ball
            score_counter += 1  # adds one so when the score is ten and is divided by 5 the answer will be 2.

        if ball.rect.y >= screen_height:  # if the ball passes the player
            end_screen()  # the player loses and it goes to the end screen

        all_sprites_group.update()  # allows the sprites to move

        # Drawing code
        # background image
        screen.blit(background_image, [0, 0])

        # code for the ball to bounce
        if 370 <= ball.rect.y <= 420 and ball.change_y == abs(ball.change_y):
            ball.bounce()
            screen.blit(shadow_ball_image, [ball.rect.x, ball.rect.y])
        elif 120 <= ball.rect.y <= 170 and ball.change_y * -1 == abs(ball.change_y):
            ball.bounce()
            screen.blit(shadow_ball_image, [ball.rect.x, ball.rect.y])
        else:
            screen.blit(shadow_ball_image, [ball.rect.x, ball.rect.y + 10])

        all_sprites_group.draw(screen)  # draws all sprites

        my_text = my_font.render("Score: " + str(score), True, WHITE)  # displays player's score
        screen.blit(my_text, [5, 5])

        pygame.display.flip()  # updates the screen

        clock.tick(60)  # frames per second
    pygame.quit()


# call to start the game, it opens the intro screen first
main()
