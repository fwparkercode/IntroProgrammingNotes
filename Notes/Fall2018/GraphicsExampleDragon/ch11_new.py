'''
IMAGE TYPES
let's do an advanced google search
scale and sizing in preview
opengameart
kenney.nl

FOLDERS
If we use external images, sound, or files, we must use folders.

BLITTING TEXT (REVIEW):
Recall the 3 step process to add text...
Set font, render text, blit text (let's try this out)

my_font = pygame.font.SysFont('font', font_size, bold, italic) #creates usable object named my_font
my_text = my_font.render(string_to_display, anti_alias, color) #creates a rendered graphical object my_text
screen.blit(my_text,[x, y]) #places rendered image on screen

BACKGROUND IMAGES:
# This line loads the image (location of your image must be in same folder)
pygame.image.load("specific_name_of_file.jpg")

# This loads the image 
# AND creates a usable object called background_image (or whatever you want to call it)
background_image = pygame.image.load("specific_name_of_file.jpg")
^^^THIS^^^ line needs to be OUTSIDE THE LOOP

# THis line blits the image to the screen.
screen.blit(background_image, [0, 0])
^^^THIS^^^ line needs to be INSIDE THE LOOP

For backgrounds, jpegs are fine.
Let's add the file

MOVING IMAGES:
Now lets use the same process to load a dragon
Now let's move him with the mouse

ADDING SOUND:
my_sound = pygame.mixer.Sound("file_name")
^^^THIS^^^ must come after pygame.init()
my_sound.play() # plays the sound object
'''
 
# Import a library of functions called 'pygame'
import pygame
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

# Set the height and width of the screen
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Graphics and Sound Demo")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Global Variables
score = 0

# Text resources
my_font = pygame.font.SysFont('Calibri', 30, True, False) # creates usable object named my_font

# Image resources
background_image = pygame.image.load("bgCave.bmp")
dragon_image = pygame.image.load("dragon2.png")

# Sound resources
background_music = pygame.mixer.Sound("bgMusic.wav")
background_music.set_volume(0.5)  # set to 50% volume
background_music.play()
fireball_sound = pygame.mixer.Sound("fireball.wav")

# Game loop
while not done:
 
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            fireball_sound.play(0)  # play one time
            #background_music.stop()
        
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
    x, y = pygame.mouse.get_pos()
    
    # Clear the screen and set the screen background
    screen.fill(BLACK)
    screen.blit(background_image, [0, 0])

    # Blit images here (blit background first!)
    screen.blit(dragon_image, [x, y])

    # Render the score text
    my_text = my_font.render("Score: " + str(score), True, WHITE)


    # Increasing score up to 1000... let's add this
    screen.blit(my_text, [50, 50])  # places rendered image on screen

 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
     
 
# Be IDLE friendly
pygame.quit()
