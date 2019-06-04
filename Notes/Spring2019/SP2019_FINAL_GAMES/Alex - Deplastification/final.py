import random
import pygame

# Initialize the game engine
pygame.init()

# Defined  colors, used from various assignments from this class
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARKBLUE = (92, 107, 242)


screen_width = 1000
screen_height = 667
level = 0

# Set the height and width of the screen
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Alex Carlin FINAL!?")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Global Variables
score = 0

# Text resources
my_font = pygame.font.SysFont('Calibri', 40, True, False)

# Image resources
background_image = pygame.image.load("background.jpeg")
entrancescreen_image = pygame.image.load("background2.png")
happyearth_image = pygame.image.load("happyearth.png")
waterbottle_image = pygame.image.load("waterbottle2.png")
paddle_image = pygame.Surface([400, 100])
paddle_image.fill(RED)
greenorb_image = pygame.image.load("orb for screen.png")
endbottle_image = pygame.image.load("angry water bottle end.png")
people_image = pygame.image.load("people.jpeg")

# Sound resources
background_music = pygame.mixer.Sound("bensound-epic.wav")
plastic_sound = pygame.mixer.Sound("plastic_sound.wav")
bounce_sound = pygame.mixer.Sound("bounce.wav")
background_music.set_volume(0.5)



'''
This is the one and only Green_orb class
in it, I give the 'deplastifyer' (the instance I have created)
all of its functionality. I go more into depth for how each aspect of move works. 
'''
class Green_orb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("orb.png")
        self.rect = self.image.get_rect()   # grabs the rect based on the image
        self.rect.x = 500
        self.rect.y = 400
        self.change_y = 3
        self.change_x = 3
        self.lives = 3
        self.level = 0
        self.done = False

    def move(self):

        self.rect.x += self.change_x
        # collisions, (very timely !) adds score too
        # the collisions are kind of wonky
        # Mr. Lee helped me get started on the x collisions, but I edited the code to work for y too
        hit_list = pygame.sprite.spritecollide(self, deplastifyer.bottle_group, True)
        for hit in hit_list:
            plastic_sound.play()
            paddle.score += 1
            if self.change_x > 0:
                self.rect.right = hit.rect.left
                self.change_x *= -1.1
            else:
                self.rect.left = hit.rect.right
                self.change_x *= -1.1


        
        # important, moves the y
        self.rect.y += self.change_y
        hit_list = pygame.sprite.spritecollide(self, deplastifyer.bottle_group, True)
        for hit in hit_list:
            plastic_sound.play()
            paddle.score += 1
            if self.change_y > 0:
                self.rect.bottom = hit.rect.top
                self.change_y *= - 1.1
 
            else:
                self.rect.top = hit.rect.bottom
                self.change_y *= - 1.1            


        #  regulations on the ball, effect life
        if self.rect.y >= 590:
            if self.lives <= 0:
                lose_screen()
            elif self.lives > 0:
                self.lives -= 1


        #  to make sure the ball doesn't leave the screen
        if self.rect.right >= screen_width:
            self.change_x *= -1
        if self.rect.x < 0:
            self.change_x *= -1

        # regulation for y, top of screen
        if self.rect.top < 0:
            self.change_y *= -1


'''
This is my paddle. It keeps track of the score.
The bottom of the rect y position is always 570, 
but the x position is the mouses x position

'''
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # my actual image
        self.image = pygame.Surface([80, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect() # grabs the rect based on the image
        self.rect.bottom = 570  # sets the bottoms rect y to 570
        self.score = 0

    def move(self):
      # gets the position for the mouse x
        self.rect.x = pygame.mouse.get_pos()[0]
      # makes sure it doesn't leave the screen
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.left <= 0:
            self.rect.left = 0


'''
The water bottle class, 
gives the waterbottle the needed atrributes for later
'''
class Waterbottle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("waterbottle2.png")
        self.rect = self.image.get_rect()

# creation of my groups
fungame_group = pygame.sprite.Group()
bottle_group = pygame.sprite.Group()


# creation of my instances
deplastifyer = Green_orb()

paddle = Paddle()


paddle.ball = deplastifyer
deplastifyer.bottle_group = bottle_group


# adding what I need to be added to my all sprites groups
fungame_group.add(deplastifyer)
fungame_group.add(paddle)


# This is the first screen that the player will see.

'''
These are all of my cut_screens
I blitted images to most of them
I got the code from the cut_screen example in class
but then I edited them to fit my game more, 
and added more at the beginning and end
'''
def start_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                background_music.play(-1)
                done = True

        screen.fill(WHITE)
        screen.blit(entrancescreen_image, [10, 10])

        my_texta = my_font.render("It is no lie that our planet is in trouble.", False, BLACK)
        screen.blit(my_texta, [30, 50])
        my_textlob = my_font.render("We must do whatever we need to do to save it.", False, BLACK)
        screen.blit(my_textlob, [30, 150])
        ascore_text = my_font.render("Now, its your job to fix the planet by 'deplastfying' some water bottles!",  False, BLACK)
        screen.blit(ascore_text, [30, 250])
        a_text = my_font.render("Click 'a' to continue", False, BLACK)
        screen.blit(a_text, [30, 350])
        pygame.display.flip()
        clock.tick(60)

def deplastifyer_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(WHITE)
        screen.blit(greenorb_image, [150, 150])

        my_texta = my_font.render("This is your deplastifyer, a godly item.", False, BLACK)
        screen.blit(my_texta, [30, 50])
        my_textlob = my_font.render("With it, you shall 'deplastify' all of the plastic water bottles", False, BLACK)
        screen.blit(my_textlob, [30, 150])
        ascore_text = my_font.render("We myst save our earth, and 'deplastifying' all is our goal", False, BLACK)
        screen.blit(ascore_text, [30, 250])
        bscore_text = my_font.render("You get to control the 'deplastifyer' with your paddle", False, BLACK)
        screen.blit(bscore_text, [30, 350])
        a_text = my_font.render("Click 'a' to continue onto the paddle explanation", False, BLACK)
        screen.blit(a_text, [30, 450])
        pygame.display.flip()

        clock.tick(60)
        pygame.display.flip()

def paddle_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(WHITE)
        screen.blit(paddle_image, [750, 430])

        my_texta = my_font.render("This is your paddle, a very important tool.", False, BLACK)
        screen.blit(my_texta, [30, 50])
        my_textlob = my_font.render("It gives you the power of controlling your deplastifyer", False, BLACK)
        screen.blit(my_textlob, [30, 150])
        ascore_text = my_font.render("You control the paddle with your mouse.", False, BLACK)
        screen.blit(ascore_text, [30, 250])
        bscore_text = my_font.render("You get to control the 'deplastifyer' with your paddle", False, BLACK)
        screen.blit(bscore_text, [30, 350])
        cscore_text = my_font.render("Of course, it isn't this big in the game.", False, BLACK)
        screen.blit(cscore_text, [30, 450])
        a_text = my_font.render("Click 'a' to continue onto the paddle explanation", False, BLACK)
        screen.blit(a_text, [30, 550])
        pygame.display.flip()

        clock.tick(60)

def laststart_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(WHITE)
        screen.blit(people_image, [450, 150])

        my_texta = my_font.render("One final time, your objective is to 'deplastify' all of the water bottles", False, BLACK)
        screen.blit(my_texta, [30, 50])
        my_textlob = my_font.render("Use your mouse.", False, BLACK)
        screen.blit(my_textlob, [30, 150])
        ascore_text = my_font.render("Now, go do some good for humanity!", False, BLACK)
        screen.blit(ascore_text, [30, 250])
        a_text = my_font.render("Click a to continue", False, BLACK)
        screen.blit(a_text, [30, 350])
        pygame.display.flip()
        clock.tick(60)

def level_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(BLACK)
        my_text = my_font.render("You are on level: " + str(level + 1), False, WHITE)
        screen.blit(my_text, [30, 50])
        my_textlo = my_font.render("Press any key to continue", False, WHITE)
        screen.blit(my_textlo, [30, 250])
        score_text = my_font.render("Score: " + str(paddle.score), False, WHITE)
        screen.blit(score_text, [30, 150])
        pygame.display.flip()

        clock.tick(60)


# there is an error arising from the interaction of the three of these
# but the game still works.
# I just wanted to make note of that
def end_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                pygame.quit()
        screen.fill(DARKBLUE)

        final_text = my_font.render("Thanks for playing!", True, WHITE)
        screen.blit(final_text, [30, 50])

        finalhahno_text = my_font.render("Hope you enjoyed", True, WHITE)
        screen.blit(finalhahno_text, [30, 150])

        finalfinal_text = my_font.render("Have a nice day!", True, WHITE)
        screen.blit(finalfinal_text, [30, 250])

        finalreal_text = my_font.render("Final score: " + str(paddle.score), True, WHITE)
        screen.blit(finalreal_text, [30, 350])

        finalrealreal_text = my_font.render("Final level: " + str(level + 1), True, WHITE)
        screen.blit(finalrealreal_text, [30, 450])

        finalrealreal_text = my_font.render("Press the 'a' key to end", True, WHITE)
        screen.blit(finalrealreal_text, [30, 550])

        pygame.display.flip()

        clock.tick(60)

def lose_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                end_screen()
        screen.fill(BLUE)
        screen.blit(endbottle_image, [470, 200])

        final_text = my_font.render("You lost", True, WHITE)
        screen.blit(final_text, [30, 50])

        finalhahno_text = my_font.render(":(((", True, WHITE)
        screen.blit(finalhahno_text, [30, 150])

        finalfinal_text = my_font.render("Better luck next time!", True, WHITE)
        screen.blit(finalfinal_text, [30, 250])

        finalreal_text = my_font.render("Final score: " + str(paddle.score), True, WHITE)
        screen.blit(finalreal_text, [30, 350])

        isitrealreal_text = my_font.render("Final level" + str(level + 1), True, WHITE)
        screen.blit(isitrealreal_text, [30, 450])

        finalrealreal_text = my_font.render("Press the 'a' key to end", True, WHITE)
        screen.blit(finalrealreal_text, [30, 550])

        pygame.display.flip()

        clock.tick(60)

def win_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                end_screen()
        screen.fill(WHITE)
        screen.blit(happyearth_image, [300, 10])

        my_texta = my_font.render("WINNER WINNER CHIKCEN DINNER", False, BLACK)
        screen.blit(my_texta, [30, 50])
        my_textlob = my_font.render("You saved the earth", False, BLACK)
        screen.blit(my_textlob, [30, 250])
        real_text = my_font.render(":))))", True, WHITE)
        screen.blit(real_text, [30, 150])
        aascore_text = my_font.render("Your score was:" + str(paddle.score), False, BLACK)
        screen.blit(aascore_text, [30, 350])
        ascore_text = my_font.render("You're a hero", False, BLACK)
        screen.blit(ascore_text, [30, 450])
        a_text = my_font.render("Thanks for playing", False, BLACK)
        screen.blit(a_text, [30, 550])
        pygame.display.flip()
        clock.tick(60)

# Game loop

start_screen()

deplastifyer_screen()

paddle_screen()

laststart_screen()

waterbottle = Waterbottle()

# create initial bottles
# I used the code from the example in class
# but edited it to work better in my game
for x in range(5, 980, waterbottle.rect.width):
    for y in range(0, 400, waterbottle.rect.height):
        if random.randrange(50) == 0:
            waterbottle = Waterbottle()
            fungame_group.add(waterbottle)
            bottle_group.add(waterbottle)
            waterbottle.rect.x = x
            waterbottle.rect.y = y

while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
        if deplastifyer.lives == 0:
            lose_screen()


    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # updating one of my groups and then making sure two of my instances move
    fungame_group.update()
    deplastifyer.move()
    paddle.move()


    '''I
      did the first part, nut then to make it more interesting Mr lee helped me change 
      the change of the deplastifyer based on how it hits the paddle
    '''
    if pygame.sprite.collide_rect(paddle, deplastifyer):
        bounce_sound.play()
        deplastifyer.rect.bottom = paddle.rect.top
        deplastifyer.change_y *= -1
        deplastifyer.change_x += (deplastifyer.rect.centerx - paddle.rect.centerx)/6

    # makes sure player isn't playing after they have lost all lives
    if deplastifyer.lives <= 0:
        lose_screen()

    '''
    I wrote indivual Level code, Mr. Lee helped me condense
    Basically, this code makes sure all of the bottles are 'deplastified' before moving to the nect level
    after all have been deplastified, 
    one is added to the level
    and the level screen shows up
    the change x and change y are reset
    as well as x and y
    '''
    if len(bottle_group) == 0:

        level += 1
        level_screen()

        for x in range(5, 980, waterbottle.rect.width):
            for y in range(40, 400, waterbottle.rect.height):
                if random.randrange(int(40/level)) == 0:
                    waterbottle = Waterbottle()
                    fungame_group.add(waterbottle)
                    bottle_group.add(waterbottle)
                    waterbottle.rect.x = x
                    waterbottle.rect.y = y


        level_screen()

        deplastifyer.x = 500
        deplastifyer.y = 400
        deplastifyer.change_y = 3 + (level / 3)
        deplastifyer.change_x = 3 + (level / 3)


    #moves player over to the win screen if they have won
    if level == 7:
        win_screen()

  # another check for lives
    if deplastifyer.lives <= 0:
        lose_screen()

    # a check in case people quit before the game is over
    if done == True:
        end_screen()


    # Clear the screen and set the screen background
    screen.fill(BLACK)

    # Blitted background image here
    screen.blit(background_image, [0, 0])

    fungame_group.draw(screen)
    fungame_group.update()

    # updates on scores, lives, and levels here

    scoreupdate_text = my_font.render("Score: " + str(paddle.score), True, RED)
    screen.blit(scoreupdate_text, [30, 50])
    levelupdate_text = my_font.render("Level: " + str(level + 1), True, RED)
    screen.blit(levelupdate_text, [30, 15])
    lives_text = my_font.render("Lives: " + str(deplastifyer.lives), True, RED)
    screen.blit(lives_text, [30, 85])

    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)


if deplastifyer.lives <= 0:
    lose_screen()


if done == True:
    pygame.quit()

