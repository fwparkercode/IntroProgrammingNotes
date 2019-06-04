import pygame

# GLOBAL VARIABLES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
fps = pygame.time.Clock()


# CLASSES
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([20, 80])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""

        self.rect.y += self.change_y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

class Ball(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()

        # -- Attributes
        # Set speed vector
        self.change_x = 4
        self.change_y = 4

        self.player1_score = 0
        self.player2_score = 0



    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        if self.rect.left > screen_width:
            self.rect.center = [screen_width // 2, screen_height // 2]
            self.player2_score +=1
            print("Player 2:", self.player2_score, "Player 1:", self.player1_score)
        if self.rect.right < 0:
            self.rect.center = [screen_width // 2, screen_height // 2]
            self.player1_score += 1
            print("Player 2:", self.player2_score, "Player 1:", self.player1_score)

        self.rect.y += self.change_y
        if self.rect.top < 0:
            self.change_y *= -1
        if self.rect.bottom > screen_height:
            self.change_y *= -1


# SETUP THE GAME
pygame.init()
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Calibri', 70, False, False)

def cut_screen():
    done = False
    text = my_font.render("Press any key to Start!!", True, YELLOW)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(BLACK)

        screen.blit(text, [screen_width // 2 - text.get_rect().width // 2, screen_height // 2 - text.get_rect().height // 2])
        pygame.display.flip()
        clock.tick(60)



def game_over(winner):
    done = False
    text = my_font.render(winner + " wins! ", True, YELLOW)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(BLACK)

        screen.blit(text, [screen_width // 2 - text.get_rect().width // 2, screen_height // 2 - text.get_rect().height // 2])
        pygame.display.flip()
        clock.tick(60)

cut_screen()

#Bounce Sound
bounce = pygame.mixer.Sound("bounce.wav")


# Create an 800x600 sized screen


# Set the title of the window
pygame.display.set_caption('Epic Pong Game')


# CREATE OBJECTS
player2 = Player()
player2.rect.left = 0
player = Player()
player.rect.right = screen_width

ball = Ball()
ball.rect.center = [screen_width//2, screen_height//2]




# Background
background = pygame.image.load("soccer.jpg")

# GROUPS
all_sprites_list = pygame.sprite.Group()  # holds all my sprites
player_list = pygame.sprite.Group()
all_sprites_list.add(ball)
all_sprites_list.add(player)
player_list.add(player)
all_sprites_list.add(player2)
player_list.add(player2)

clock = pygame.time.Clock()
done = False

background_music = pygame.mixer.Sound("backgroundmusic.wav")
background_music.play(-1)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
            elif event.key == pygame.K_w:
                player2.changespeed(0, -3)
            elif event.key == pygame.K_s:
                player2.changespeed(0, 3)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player2.changespeed(0, 3)
            elif event.key == pygame.K_s:
                player2.changespeed(0, -3)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    # --- Game logic

    # This calls update on all the sprites
    all_sprites_list.update()

    hit_list = pygame.sprite.spritecollide(ball, player_list, False)

    for hit in hit_list:
        ball.change_x *= -1
        bounce.play()
    if ball.player1_score >= 7:
        game_over("Player 1")
        done = True
    elif ball.player2_score >= 7:
        game_over("Player 2")
        done = True



    # -- Draw everything
    # Clear screen
    screen.fill(WHITE)
    screen.blit(background, [0, 0])

    # Draw sprites
    all_sprites_list.draw(screen)

    score_text = my_font.render(str(ball.player2_score), True, WHITE)

    screen.blit(score_text, [screen_width // 2 - score_text.get_rect().width - 10,0])

    score_text = my_font.render(str(ball.player1_score), True, WHITE)

    screen.blit(score_text, [screen_width // 2 - score_text.get_rect().width + 50, 0])





    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()