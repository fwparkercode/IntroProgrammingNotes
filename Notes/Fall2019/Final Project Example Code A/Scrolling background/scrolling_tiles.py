"""
Example of repeating scrolled background image
This uses a tiles.  Maybe for a skiing game??
"""

# FIX ME
# 10 seconds in it multiplies images
 
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
 

background_image = pygame.image.load("snow_tile.jpg") #389 × 373 image
bg_width = 389
bg_height = 373
bg_y = 0

 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
 
    bg_y -= 3 # scroll to the left
    if bg_y > bg_height:
        # 1600 is the image width
        bg_y = 0 # reset both images back on the screen
    
    
    for x in range(4):
        for y in range(5):
            screen.blit(background_image, [bg_width * x, bg_y + y * bg_height])
    
 
   
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()