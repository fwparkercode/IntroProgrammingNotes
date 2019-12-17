"""
Example of repeating scrolled background image
"""
 
import pygame
 
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# This sets the name of the window
pygame.display.set_caption('Scrolling background')
 
clock = pygame.time.Clock()
 
background_image = pygame.image.load("background_image.png")
bg_x = 0
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
 
    bg_x -= 2 # scroll to the left
    if bg_x < -1600:
        # 1600 is the image width
        bg_x = 0 # reset both images back on the screen
    
    
    for i in range(2):
        # the image is 1600 wide in this case
        # image is repeated twice so there are no gaps
        screen.blit(background_image, [bg_x + 1600 * i, 0])
    
 
   
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()