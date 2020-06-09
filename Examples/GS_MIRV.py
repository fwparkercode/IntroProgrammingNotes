"""
MISSILE DEFENSE GAME
first attempt at Missile Command Clone
by Aaron Lee
"""
import pygame
import random


# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
BLUE     = (   100,   100, 255)
YELLOW   = ( 255, 255,   0)
GREEN    = (   0, 140,   0)       #Dark green for plane

class Reticule(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([3, 3])
        self.rect = self.image.get_rect()
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.size = 10
        self.rect.x = x
        self.rect.y = y

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
        self.rect.x += self.change_x
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.y += self.change_y
        if self.rect.bottom > screen_height - 25:
            self.rect.bottom = screen_height - 25
        if self.rect.top < 0:
            self.rect.top = 0


    def draw_me(self):
        pygame.draw.line(screen, BLACK, [self.rect.x - self.size, self.rect.y], [self.rect.x + self.size, self.rect.y], 2)
        pygame.draw.line(screen, BLACK, [self.rect.x, self.rect.y - self.size], [self.rect.x, self.rect.y + self.size], 2)
        pygame.draw.circle(screen, BLACK, self.rect.center, int(self.size * 2 / 3), 1)
        pygame.draw.circle(screen, BLACK, self.rect.center, int(self.size / 2), 1)




class Base(pygame.sprite.Sprite):
    """ This class represents the Player's bases and player too. """
    def __init__(self):
        """ They are Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([20, 10])
        self.image.set_colorkey(BLACK)
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.y = screen_height - 10
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, [self.rect.x - 1, self.rect.y-1, self.rect.width+2, self.rect.height+2])
        pygame.draw.rect(screen, BLUE, [self.rect.x, self.rect.y, self.rect.width, self.rect.height])
        

class Button(pygame.sprite.Sprite):
    '''Menu buttons for the start screen'''
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([150, 40])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width//2 - 75
        self.rect.y = screen_height//2 -20
        

class Controller():
    '''holds the global type variables and controls the levels, lives, etc.'''
    def __init__(self):
        self.frame = 0 # frame to track time and other 
        self.high_score = 0 # experimental, not used yet in code
        self.restarter = False # boolean to track restart trigger
        self.level = 1 
        self.score = 0
        self.missile_count = 50 # DIFFICULTY SETTING
        self.missile_dead = 0
        self.framerate = 60
        self.num_base = 5
        self.font = pygame.font.SysFont('Calibri', 15, True, False)
        self.font_med = pygame.font.SysFont('Calibri', 20, True, False)
        self.font_game_over = pygame.font.SysFont('Calibri', 50, True, False)
        self.reticule = None
        self.paused = False

    def start(self):        
        ready = False
        
        intro_text1 = self.font.render("Move reticule with pad, shoot with A Button" ,True,BLACK)
        intro_text2 = self.font.render("Protect your bases from MIRV hits." ,True,BLACK)
        intro_text3 = self.font.render("Bonuses for bases and ammo after each wave!" ,True,BLACK)
        intro_text4 = self.font.render("Any key to start......." ,True,BLACK)
        intro_text5 = self.font.render("by Aaron Lee, 2015", True, GREEN)
        for i in range(20):
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        break            
            screen.fill(WHITE)
            pygame.display.flip()
            clock.tick(self.framerate)
        title = "M.I.R.V!"
        for letters in range(1, len(title)+1):
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        break            
            screen.fill(WHITE)   
            intro_text0 = self.font_game_over.render(title[:letters] ,True,RED)
            center_text(screen, intro_text0, -80)
            pygame.display.flip() 
            clock.tick(20)

        not_yet = False
        while not ready:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        ready = True
                    if event.type == pygame.KEYDOWN:
                        if event.key  in (pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP):
                            not_yet = True
                        elif not_yet == False:
                            ready = True
                    if event.type == pygame.KEYUP:
                        if event.key  in (pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP):
                            not_yet = False
            screen.fill(WHITE)
            center_text(screen, intro_text0, -80)
            center_text(screen, intro_text1, 0)
            center_text(screen, intro_text2, 10)
            center_text(screen, intro_text3, 20)
            center_text(screen, intro_text4, 40)
            center_text(screen, intro_text5, 60)


            pygame.display.flip() 
            #clock.tick(-1)
        for i in range(self.num_base):
            base = Base()
            base.rect.bottom = screen_height - 10
            base.rect.centerx = (i+1) * screen_width//(self.num_base+ 1)
            base_list.add(base)
            all_sprites_list.add(base)      


    def next_level(self):
        self.level+=1
        self.missile_dead = 0
        all_sprites_list.empty()
        missile_list.empty()
        explosion_list.empty()
        planes_list.empty()
        self.score += (self.level-1)*10 * len(base_list)
        self.score += self.missile_count
        for frame in range(self.framerate*5):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        ret.changespeed(-3, 0)
                    elif event.key == pygame.K_RIGHT:
                        ret.changespeed(3, 0)
                    elif event.key == pygame.K_UP:
                        ret.changespeed(0, -3)
                    elif event.key == pygame.K_DOWN:
                        ret.changespeed(0, 3)
                    else:
                        break

                    # Reset speed when key goes up
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        ret.changespeed(3, 0)
                    elif event.key == pygame.K_RIGHT:
                        ret.changespeed(-3, 0)
                    elif event.key == pygame.K_UP:
                        ret.changespeed(0, 3)
                    elif event.key == pygame.K_DOWN:
                        ret.changespeed(0, -3)
            screen.fill(WHITE)
            next_level_text = font.render("Wave " + str(self.level-1) + " Complete" ,True,BLACK)
            next_level_text2 = font.render("City bonus: " + str((self.level-1) * 10) + " x " + str(len(base_list)) + " cities = " + str((self.level-1)*10*len(base_list)) + "pts",True, BLACK)
            next_level_text3 = font.render("Remaining Missile bonus: " + str(self.missile_count) + " pts", True, BLACK)

            center_text(screen, next_level_text, -10)
            center_text(screen, next_level_text2, +10)
            center_text(screen, next_level_text3, +30)



            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip() 
            # --- Limit to 20 frames per second
            clock.tick(self.framerate)
        self.missile_count = 50
        plane = Plane()
        planes_list.add(plane)
        all_sprites_list.add(plane)        
        
    def restart(self):
        ready = False
        #screen.fill(WHITE)
        #pygame.display.flip()
        restart_text = font.render("Press Start to play again", True, RED)
        while not ready:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ready = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ready = True
                        return True
                    if event.key == pygame.K_RETURN:
                        ready = True

            screen.fill(WHITE)
            center_text(screen, restart_text, 0)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip() 
            # --- Limit to 20 frames per second
            clock.tick(self.framerate)

        self.level=1
        self.missile_dead = 0
        all_sprites_list.empty()
        missile_list.empty()
        explosion_list.empty()
        planes_list.empty()
        base_list.empty()
        self.missile_count = 50
        self.framerate = 60
        self.score = 0
        controller.start()
        return False
        
 
class Missile(pygame.sprite.Sprite):
    """ This class represents the incoming missiles. """
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.duplicate_yes = random.randrange(2)
        self.duplicate_yes = 0
        self.duplicate = random.randrange(1,controller.level+1)
        self.duplicate_spacing = random.randrange(10,100)
        self.image = pygame.Surface([3, 3])
        
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.startx = x
        self.starty = y
        self.x = x
        self.y = y
        self.rect.centerx = x
        self.rect.centery = y
        self.xspeed = random.random() * 3 - 1.5
        self.yspeed = random.random() * controller.level / 4 + 0.25

        #self.xspeed = random.randrange(-2, 3)
        #self.yspeed = random.randrange(1, 1 + controller.level)

    def draw_line(self):
        pygame.draw.line(screen, BLACK, [self.startx, self.starty], [self.x,self.y],3)
        pygame.draw.line(screen, RED, [self.startx, self.starty], [self.x, self.y],1)

    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.draw_line()
        if self.rect.right < 0 or self.rect.left > screen_width:
            self.kill()
        if self.rect.top > screen_height:
            self.kill()

        if random.randrange(2000//controller.level +100) == 0:
            self.split()

        self.rect.x = self.x
        self.rect.y = self.y


    def split(self):
        for i in range(random.randrange(1,controller.level//3 + 2)):
            split_missile = Missile(self.rect.centerx, self.rect.centery)
            split_missile.xspeed = self.xspeed + random.random() - 0.5
            split_missile.yspeed = self.yspeed
            missile_list.add(split_missile)
            all_sprites_list.add(split_missile)
    def draw(self):
        pygame.draw.circle(screen, BLACK, [self.rect.centerx, self.rect.centery], 3)
        pygame.draw.circle(screen, BLUE, [self.rect.centerx, self.rect.centery], 1)
        
        
class Plane(pygame.sprite.Sprite):
    """ This class represents the Player. """
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.height = 7
        self.width = 20
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(20, (screen_height*2)//3)
        
        if random.randrange(2) == 0:
            self.rect.x = -30
            self.startx = -30
            self.speedx = random.random() * 3 + 1
        else:
            self.rect.x = screen_width +30
            self.startx = screen_width +30
            self.speedx = -random.random() * 3 - 1
    def update(self):
        self.rect.x += self.speedx
        if (random.randrange(50 - controller.level * 2) == 0) and controller.missile_dead < controller.level*10:
            missile = Missile(self.rect.centerx, self.rect.centery)
            missile_list.add(missile)
            all_sprites_list.add(missile)
        if (self.startx < 0 and self.rect.x > screen_width + self.width):
            self.kill()
        if (self.startx > screen_width and self.rect.right < 0):
            self.kill()
        
    def draw_plane(self):
        if self.startx < 0:
            pygame.draw.polygon(screen, BLACK, [[self.rect.x + self.width, self.rect.y], [self.rect.x + self.width,self.rect.y + self.height], [self.rect.x+self.width+10,self.rect.y+self.height//2]], 4) #cone moving right
            pygame.draw.polygon(screen, BLACK, [[self.rect.x,self.rect.y], [self.rect.x,self.rect.y-8], [self.rect.x+4,self.rect.y]], 4) #tail moving right
            pygame.draw.rect(screen, BLACK, [self.rect.x,self.rect.y, self.width, self.height], 4)            
            
            pygame.draw.polygon(screen, GREEN, [[self.rect.x + self.width, self.rect.y], [self.rect.x + self.width,self.rect.y + self.height], [self.rect.x+self.width+10,self.rect.y+self.height//2]]) #cone moving right
            pygame.draw.polygon(screen, GREEN, [[self.rect.x,self.rect.y], [self.rect.x,self.rect.y-8], [self.rect.x+4,self.rect.y]]) #tail moving right
            pygame.draw.rect(screen, GREEN, [self.rect.x,self.rect.y, self.width, self.height])
        else:
            pygame.draw.polygon(screen, BLACK, [[self.rect.x,self.rect.y], [self.rect.x-10,self.rect.y+self.height//2], [self.rect.x,self.rect.y+self.height]], 4) #cone moving left
            pygame.draw.polygon(screen, BLACK, [[self.rect.x + self.width,self.rect.y], [self.rect.x+self.width,self.rect.y-8], [self.rect.x+self.width-4,self.rect.y]], 4)   #tail  moving left  
            pygame.draw.rect(screen, BLACK, [self.rect.x,self.rect.y, self.width, self.height], 4) 
            
            pygame.draw.polygon(screen, GREEN, [[self.rect.x,self.rect.y], [self.rect.x-10,self.rect.y+self.height//2], [self.rect.x,self.rect.y+self.height]]) #cone moving left
            pygame.draw.polygon(screen, GREEN, [[self.rect.x + self.width,self.rect.y], [self.rect.x+self.width,self.rect.y-8], [self.rect.x+self.width-4,self.rect.y]])   #tail  moving left  
            pygame.draw.rect(screen, GREEN, [self.rect.x,self.rect.y, self.width, self.height])



class Patriot(Missile):
    '''Missiles fired at incoming'''
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__(x, y)
        
        self.image = pygame.Surface([2, 2])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.startx = screen_width//2
        self.starty = screen_height-20
        self.rect.x = self.startx
        self.rect.y = self.starty
        self.pos = [x, y]
        self.xspeed = (-self.rect.x + self.pos[0])//10
        self.yspeed = (-self.rect.y + self.pos[1])//10
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.y <= self.pos[1]:
            explosion = Explosion(self.pos[0],self.pos[1])
            all_sprites_list.add(explosion)
            explosion_list.add(explosion) 
            all_sprites_list.remove(self)
            patriot_list.remove(self)        
    def pat_draw(self):
        pygame.draw.circle(screen, BLACK, [self.rect.centerx, self.rect.centery], self.rect.width)


class Explosion(pygame.sprite.Sprite):

    """ This class represents the bullet . """
    xbig = 0
    ybig = 0
    
    def __init__(self,x,y):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([1, 1])
        #self.image.fill(BLACK)
        #self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.expanding = True
        self.second_expand = False        
    def update(self):
        if self.expanding:
            self.xbig+=1.3
            self.ybig+=1.3
        else:
            self.xbig-=0.5
            self.ybig-=0.5
        if self.ybig > 40 and self.expanding == True:
            self.expanding = False
        if self.ybig <10 and  self.expanding == False :
            explosion_list.remove(self)
            all_sprites_list.remove(self) 
        self.image = pygame.Surface([self.xbig, self.xbig])
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x - self.xbig//2
        self.rect.y = self.y -self.ybig//2
        """ Move the bullet. """
        
    def draw(self):
        """ draw ellipse"""
        pygame.draw.ellipse(screen,BLACK,[self.rect.x - 2, self.rect.y -2 , self.xbig + 4,self.ybig +4])   
        pygame.draw.ellipse(screen,RED,[self.rect.x, self.rect.y, self.xbig,self.ybig])         



#  FUNCTIONS

def center_text(screen, rendered_text, y_offset):
    w, h = screen.get_size()
    x = w // 2 - rendered_text.get_width() // 2
    y = h // 2 - rendered_text.get_height() // 2 + y_offset
    screen.blit(rendered_text, [x, y])

def game_over(screen, controller):
    for frame in range(controller.framerate * 5):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                break
        screen.fill(WHITE)
        game_over_text = controller.font_game_over.render("GAME OVER", True, BLACK)
        score_text = controller.font_med.render("You scored: " + str(controller.score) + " pts!",True, RED)
        center_text(screen, game_over_text, -60)
        center_text(screen, score_text, 10)
        pygame.display.flip()
        clock.tick(controller.framerate)
    controller.restarter = True
    controller.frame = 0





pygame.init()
 

screen_width = 320
screen_height = 240
screen = pygame.display.set_mode([screen_width, screen_height])

# Sprite groups
all_sprites_list = pygame.sprite.Group()
explosion_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
missile_list = pygame.sprite.Group()
base_list = pygame.sprite.Group()
patriot_list = pygame.sprite.Group()
buttons_list = pygame.sprite.Group()
planes_list = pygame.sprite.Group()
# Create sprites 
controller = Controller()

#Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates

clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 20, True, False)    
font_game_over = pygame.font.SysFont('Calibri', 50, True, False) 

#high_score()
controller.start()
ret = Reticule(screen_width // 2, screen_height // 2)
all_sprites_list.add(ret)
controller.reticule = ret



# -------- Main Program Loop -----------

while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                if controller.paused:
                    controller.paused = False
                else:
                    controller.paused = True

            elif event.key == pygame.K_j and not controller.paused:
                if controller.missile_count > 0:
                    newpatriot = Patriot(ret.rect.x, ret.rect.y)
                    patriot_list.add(newpatriot)
                    all_sprites_list.add(newpatriot)
                    controller.missile_count-=1
            elif event.key == pygame.K_LEFT:
                ret.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                ret.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                ret.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                ret.changespeed(0, 3)

            # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ret.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                ret.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                ret.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                ret.changespeed(0, -3)
            
                
 
    # --- Game logic

    if random.randrange(max(5, (50-(controller.level*3)))) == 0 and controller.missile_dead < controller.level*10 and not controller.paused:
        missile = Missile(random.randrange(screen_width), -10)
        if missile.duplicate_yes == 1:
            for i in range(1, missile.duplicate + 1):
                duplicate = Missile(missile.rect.centerx + missile.duplicate_spacing * i, missile.rect.centery)
                duplicate.xspeed = missile.xspeed
                duplicate.yspeed = missile.yspeed
                missile_list.add(duplicate)
                all_sprites_list.add(duplicate)
        if random.randrange(20)== 0:
            plane = Plane()
            planes_list.add(plane)
            all_sprites_list.add(plane)
            
        missile_list.add(missile)
        all_sprites_list.add(missile)
    
    
    
        
    if controller.missile_dead >= controller.level*10 and (len(missile_list) == 0):
        controller.next_level()        

    # Call the update() method on all the sprites
    if not controller.paused: missile_list.update()
    
    
    screen.fill(WHITE)
    
    # Calculate mechanics for each bullet
    explosion_list.draw(screen)
    for explosion in explosion_list:
        if not controller.paused: explosion.update()
        explosion.draw()
    
    patriot_list.draw(screen)    
    for patriot in patriot_list:
        if not controller.paused: patriot.update()
        patriot.pat_draw()
        
    if not controller.paused: ret.update()
    ret.draw_me()

    #explosion_list.draw(screen)
    #all_sprites_list.draw(screen)
    for planes in planes_list:
        if not controller.paused: planes.update()
        planes.draw_plane()
    for missiles in missile_list:
        missiles.draw_line()
               
    for bases in base_list:
        bases.draw(screen)


    missile_hit_list = pygame.sprite.groupcollide(missile_list, explosion_list, True, False)
    base_hit_list = pygame.sprite.groupcollide(base_list, missile_list, True, True)
    plane_hit_list = pygame.sprite.groupcollide(planes_list, explosion_list, True, False)
    base2_hit_list = pygame.sprite.groupcollide(base_list, explosion_list, False, True)
    for bases in base_hit_list:
        explosion = Explosion(bases.rect.x+20, bases.rect.y+10)
        all_sprites_list.add(explosion)
        explosion_list.add(explosion)        
           
    for missiles in missile_hit_list:
        controller.score += controller.level
        explosion = Explosion(missiles.rect.x, missiles.rect.y)
        all_sprites_list.add(explosion)
        explosion_list.add(explosion)
        controller.missile_dead+=1
    for planes in plane_hit_list:
        controller.score += 10 * controller.level
        explosion = Explosion(planes.rect.x + planes.width//2, planes.rect.y + planes.height//2)
        all_sprites_list.add(explosion)
        explosion_list.add(explosion)
        planes.kill()        
    if len(base_list) == 0:
        screen.fill(WHITE)
        game_over(screen, controller)
        #high_score()
        
    if controller.restarter == True:
        controller.restarter = False
        done = controller.restart()
    
    base_list.draw(screen)
    for missiles in missile_list:
        missiles.draw()
    missile_text = controller.font.render("Missiles: " + str(controller.missile_count),True,BLACK)
    score_text = controller.font.render("Score: " + str(controller.score), True, BLACK)
    level_text = controller.font.render("Level: " + str(controller.level), True, BLACK)
    screen.blit(score_text, [5,5])
    center_text(screen, missile_text, screen_height // 2 - 5)
    screen.blit(level_text, [5, 15])
    if controller.missile_count == 0 and (controller.frame//10)%2 == 0:
        empty_text = controller.font_med.render("OUT OF MISSILES!!!", True,RED)
        center_text(screen, empty_text, 0)

    if controller.paused:
        pause_text = controller.font_med.render("PAUSED", True, RED)
        center_text(screen, pause_text, -30)

    controller.frame += 1
    #explosion_list.draw(screen)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    clock.tick(controller.framerate)
 
pygame.quit()