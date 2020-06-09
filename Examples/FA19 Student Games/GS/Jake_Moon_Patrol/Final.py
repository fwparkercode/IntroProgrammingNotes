###
### Moon Pytrol, a Pygame remake of the 80s arcade game "Moon Patrol"
### Created by J. Boxerman Jan. 2020
### for Computer Programming I Final Project
###

import pygame
import random
from rover import Rover, UpBullet, SideBullet, Explosion
from worldgen import WorldGen, GenHole, Rock
from ufo import UFO
pygame.init()

#################
## VARS
GROUND_POS = 285

rover_speed = 0.5
rover_starting_x = 130
ROVER_GRAVITY = 0.16

UFO_SPEED = 1

WORLD_SPEED = 0.8 # Scroll speed
## END VARS
#################

#################
## FUNCTIONS

def intro_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(BLACK)
        screen.blit(pygame.image.load("assets/title.jpg"), [190, 30])
        start_inst = font.render("Any key to begin", True, WHITE)
        inst = font.render("Arrow keys to move,", True, WHITE)
        inst2 = font.render("spacebar to shoot", True, WHITE)
        inst3 = font_small.render("Go for time - difficulty will increase!", True, WHITE)
        screen.blit(start_inst, [160, 210])
        screen.blit(inst, [140, 250])
        screen.blit(inst2, [155, 275])
        screen.blit(inst3, [15, 315])
        to_blit = pygame.transform.scale(screen, (320, 240))
        real_screen.blit(to_blit, (0, 0))
        pygame.display.flip()
        clock.tick(60)

def outro_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
                pygame.quit()

        screen.fill(BLACK)
        end_txt = font.render("Sorry, you lost!", True, WHITE)
        end_score_txt = font.render("Score: " + str(ufos_killed), True, WHITE)
        screen.blit(end_score_txt, [20, SCREEN_HEIGHT - 35])
        screen.blit(end_txt, [160, 170])
        to_blit = pygame.transform.scale(screen, (320, 240))
        real_screen.blit(to_blit, (0, 0))

        pygame.display.flip()

def shoot():
    if len(side_bullet_sprites_list) == 0:
        new_bullet = UpBullet(rover) # make new bullet sprite
        new_side_bullet = SideBullet(rover)
        all_sprites_list.add(new_bullet) # adding it to the container to be drawn
        all_sprites_list.add(new_side_bullet)
        bullet_sprites_list.add(new_bullet)
        bullet_sprites_list.add(new_side_bullet)
        side_bullet_sprites_list.add(new_side_bullet)
    elif len(side_bullet_sprites_list) >= 1:
        new_bullet = UpBullet(rover)
        all_sprites_list.add(new_bullet)
        bullet_sprites_list.add(new_bullet)

def genHole(x, holetype):
    hole = GenHole(WORLD_SPEED, -10, GROUND_POS, x, holetype)
    #all_sprites_list.add(hole)
    hole_list.add(hole)

def genRock(x, rocktype):
    rock = Rock(WORLD_SPEED, 1, GROUND_POS, x, rocktype)
    rock_list.add(rock)

def genUFO(speed, x):
    ufo = UFO(speed, GROUND_POS, all_sprites_list, bomb_list)
    ufo.rect.x = x
    ufo.rect.y = random.randrange(30, 59)
    all_sprites_list.add(ufo)
    ufo_sprites_list.add(ufo)

def oneInThree():
    if random.randrange(0, 3) == 1:
        return(1)
    else:
        return(0)

## END FUNCTIONS
#################

#################
## SETUP
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 340
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.Surface(size)
real_screen = pygame.display.set_mode([320, 240])

pygame.display.set_caption("Moon Pytrol")
done = False
clock = pygame.time.Clock()

## SFX
bg_music = pygame.mixer.Sound("assets/sounds/theme.wav")
start_music = pygame.mixer.Sound("assets/sounds/start-course.wav")
crash_sfx = pygame.mixer.Sound("assets/sounds/crash.wav")
game_over_music = pygame.mixer.Sound("assets/sounds/game_over.wav")
ufo_died_sfx = pygame.mixer.Sound("assets/sounds/shoot.wav")
shoot_sfx = pygame.mixer.Sound("assets/sounds/shoot.wav")

## Fonts
font_small = pygame.font.Font("assets/pixel_font.ttf", 16)
font = pygame.font.Font("assets/pixel_font.ttf", 20)
font_big = pygame.font.Font("assets/pixel_font.ttf", 50)
## END SETUP STUFF
#################

## Sprite containers
all_sprites_list = pygame.sprite.Group()
hole_list = pygame.sprite.Group()
rock_list = pygame.sprite.Group()
ufo_sprites_list = pygame.sprite.Group()
bomb_list = pygame.sprite.Group()
bullet_sprites_list = pygame.sprite.Group()
side_bullet_sprites_list = pygame.sprite.Group()
explo_list = pygame.sprite.Group()

## Making rover + world
rover = Rover(ROVER_GRAVITY, GROUND_POS)
rover.rect.x = rover_starting_x
rover.rect.y = 50
all_sprites_list.add(rover)

world = WorldGen(WORLD_SPEED, 30, GROUND_POS - 30)

## Misc tracking variables
ufos_killed = 0
level = 0
time_since_hole_gen = 0
time_since_rock_gen = 0
time_since_ufo_gen = 0
time_since_level_change = 0
ufos_killed_previous = 0

## Game flow tracking
in_outro = False
dead_sequence_played_yet = False
intro_music_played = False

intro_screen()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rover.jump()
                if event.key == pygame.K_j:
                    if rover.status == "alive" and level != 0:
                        shoot()
                        shoot_sfx.play(0)


    # Rover lateral control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and rover.rect.x <= 230:
        rover_speed = 1.8
        if rover.rect.x >= 228:
            rover.rect.x = 228
    elif keys[pygame.K_LEFT]:
        rover_speed = -0.4
        if rover.rect.x <= 70:
            rover.rect.x = 70
    elif pygame.K_LEFT not in keys or pygame.K_RIGHT not in keys:
        rover_speed = 0.5
        if rover.rect.x > rover_starting_x: rover.rect.x -= 1.3
        if rover.rect.x < rover_starting_x and rover.rect.y <= 286: rover.rect.x += 1.3

    # --- GAME LOGIC --- #
    dt = clock.tick()

    print(dt)

    # --- Collision Detections

    ## Player death by UFO
    player_bombed_hitlist = pygame.sprite.spritecollide(rover, bomb_list, False) # single object on group collision
    for bomb in player_bombed_hitlist:
        if rover.rect.bottom + 7 >= GROUND_POS:
            rover.kill()
            rover.status = "dead"

    ## Player death by hole
    player_holed_hitlist = pygame.sprite.spritecollide(rover, hole_list, False)
    for hole in player_holed_hitlist:
        rover.kill()
        rover.status = "dead"

    ## Player death by rock
    player_rocked_hitlist = pygame.sprite.spritecollide(rover, rock_list, False)
    for rock in player_rocked_hitlist:
        rover.kill()
        rover.status = "dead"

    ## UFO death by bullet
    for bullet in bullet_sprites_list:
        bullet_ufo_hit_list = pygame.sprite.spritecollide(bullet, ufo_sprites_list, False)
        for ufo_killed in bullet_ufo_hit_list:
            bullet.kill()
            ufo_killed.death()
            ufo_killed.kill() # Kill UFO
            ufo_died_sfx.play(0)
            ufos_killed += 1

    ## Bomb death by bullets
    for bullet in bullet_sprites_list:
        bullet_bomb_hit_list = pygame.sprite.spritecollide(bullet, bomb_list, False)
        for bomb_killed in bullet_bomb_hit_list:
            bomb_killed.kill()
            bullet.kill()

    for sidebullet in side_bullet_sprites_list:
        sidebullet_bomb_hit_list = pygame.sprite.spritecollide(sidebullet, bomb_list, False)
        for bomb_killed in sidebullet_bomb_hit_list:
            bomb_killed.kill()

    ## Rock death by bullet
    for sidebullet in side_bullet_sprites_list:
        side_bullet_hit_list = pygame.sprite.spritecollide(sidebullet, rock_list, False)
        for rock_killed in side_bullet_hit_list:
            sidebullet.kill()
            rock_killed.death()

    ## Making sure rock isn't touching hole
    for rock in rock_list:
        rock_dont_touch_hole = pygame.sprite.spritecollide(rock, hole_list, True)

    # --- Level System / World Generation Logic

    time_since_level_change += dt
    if level <= 4:
        if time_since_level_change > 210:
            level += 1
            time_since_level_change = 0
    elif level == 5:
        if time_since_level_change > 270:
            level += 1
            time_since_level_change = 0
    elif level == 6:
        if time_since_level_change > 310:
            level += 1
            time_since_hole_gen = 0

    if level == 1:
        time_since_hole_gen += dt
        if time_since_hole_gen > random.randrange(60, 80):
            genHole(random.randrange(700, 730), 0) # Gen small hole
            time_since_hole_gen = 0

    elif level == 2:
        time_since_hole_gen += dt
        if time_since_hole_gen > random.randrange(40, 60):
            genHole(random.randrange(700, 730), 0) # Gen small hole
            time_since_hole_gen = 0

        time_since_ufo_gen += dt
        if time_since_ufo_gen > random.randrange(70, 120) and len(ufo_sprites_list) == 0:
            ufo_gen_spot = random.randrange(-60, -20)
            genUFO(random.random() * 1.8 + 1.3, ufo_gen_spot)
            genUFO(random.random() * 1.8 + 1, ufo_gen_spot - random.randrange(60, 90))
            time_since_ufo_gen = 0

        for ufo in ufo_sprites_list:
            if ufo.last_dropped_bomb > random.randrange(60, 120):
                ufo.dropBomb(all_sprites_list, bomb_list)
                ufo.last_dropped_bomb = 0

    elif level == 3:
        time_since_hole_gen += dt
        if time_since_hole_gen > random.randrange(35, 55):
            if oneInThree() == 1:
                genHole(random.randrange(700, 730), 1) # 1/3 chance of gen medium hole
            else:
                genHole(random.randrange(700, 730), 0)
            time_since_hole_gen = 0

        time_since_ufo_gen += dt
        if time_since_ufo_gen > random.randrange(65, 100) and len(ufo_sprites_list) == 0:
            ufo_gen_spot = random.randrange(-60, -20)
            genUFO(random.random() * 1.8 + 1.5, ufo_gen_spot)
            genUFO(random.random() * 1.8 + 1.2, ufo_gen_spot - random.randrange(60, 90))
            time_since_ufo_gen = 0

        for ufo in ufo_sprites_list:
            if ufo.last_dropped_bomb > random.randrange(60, 120):
                ufo.dropBomb(all_sprites_list, bomb_list)
                ufo.last_dropped_bomb = 0

    elif level == 4:
        time_since_hole_gen += dt
        if time_since_hole_gen > random.randrange(40, 70):
            if oneInThree() == 1:
                genHole(random.randrange(700, 730), 1) # 1/3 chance of gen medium hole
            else:
                genHole(random.randrange(700, 730), 0)
            time_since_hole_gen = 0

        time_since_ufo_gen += dt
        if time_since_ufo_gen > random.randrange(70, 110) and len(ufo_sprites_list) == 0:
            ufo_gen_spot = random.randrange(-60, -20)
            genUFO(random.random() * 1.8 + 1.5, ufo_gen_spot)
            genUFO(random.random() * 1.8 + 1.2, ufo_gen_spot - random.randrange(60, 90))
            time_since_ufo_gen = 0

        for ufo in ufo_sprites_list:
            if ufo.last_dropped_bomb > random.randrange(60, 120):
                ufo.dropBomb(all_sprites_list, bomb_list)
                ufo.last_dropped_bomb = 0

        time_since_rock_gen += dt
        if time_since_rock_gen > random.randrange(40, 50):
            genRock(random.randrange(650, 690), random.randrange(0, 2))
            time_since_rock_gen = 0

    elif level == 5:
        time_since_hole_gen += dt
        if time_since_hole_gen > random.randrange(40, 70):
            if oneInThree() == 1:
                genHole(random.randrange(700, 730), 1) # 1/3 chance of gen medium hole
            else:
                genHole(random.randrange(700, 730), 0)
            time_since_hole_gen = 0

        time_since_ufo_gen += dt
        if time_since_ufo_gen > random.randrange(50, 120) and len(ufo_sprites_list) == 0:
            ufo_gen_spot = random.randrange(-100, -20)
            genUFO(random.random() * 1.8 + 1.5, ufo_gen_spot)
            genUFO(random.random() * 1.8 + 1.2, ufo_gen_spot - random.randrange(70, 130))
            genUFO(random.random() * 1.8 + 1, ufo_gen_spot - random.randrange(160, 180))
            time_since_ufo_gen = 0

        for ufo in ufo_sprites_list:
            if ufo.last_dropped_bomb > random.randrange(60, 120):
                ufo.dropBomb(all_sprites_list, bomb_list)
                ufo.last_dropped_bomb = 0

        time_since_rock_gen += dt
        if time_since_rock_gen > random.randrange(50, 70):
            genRock(random.randrange(650, 690), random.randrange(0, 2))
            time_since_rock_gen = 0

    elif level == 6:
        time_since_hole_gen += dt
        if time_since_hole_gen > random.randrange(47, 70):
            genHole(random.randrange(700, 730), random.randrange(0, 3))
            time_since_hole_gen = 0

        time_since_ufo_gen += dt
        if time_since_ufo_gen > random.randrange(50, 120) and len(ufo_sprites_list) == 0:
            ufo_gen_spot = random.randrange(-100, -20)
            genUFO(random.random() * 1.8 + 1.5, ufo_gen_spot)
            genUFO(random.random() * 1.8 + 1.2, ufo_gen_spot - random.randrange(70, 130))
            genUFO(random.random() * 1.8 + 1, ufo_gen_spot - random.randrange(160, 180))
            time_since_ufo_gen = 0

        for ufo in ufo_sprites_list:
            if ufo.last_dropped_bomb > random.randrange(60, 120):
                ufo.dropBomb(all_sprites_list, bomb_list)
                ufo.last_dropped_bomb = 0

        time_since_rock_gen += dt
        if time_since_rock_gen > random.randrange(34, 42):
            genRock(random.randrange(650, 690), random.randrange(1, 4))
            time_since_rock_gen = 0

    elif level == 7:
        time_since_hole_gen += dt
        if time_since_hole_gen > random.randrange(40, 70):
            genHole(random.randrange(700, 730), random.randrange(0, 3))
            time_since_hole_gen = 0

        time_since_ufo_gen += dt
        if time_since_ufo_gen > random.randrange(50, 120) and len(ufo_sprites_list) == 0:
            ufo_gen_spot = random.randrange(-100, -20)
            genUFO(random.random() * 1.8 + 1.5, ufo_gen_spot)
            genUFO(random.random() * 1.8 + 1.2, ufo_gen_spot - random.randrange(70, 130))
            genUFO(random.random() * 1.8 + 1, ufo_gen_spot - random.randrange(160, 180))
            if oneInThree() == 1:
                genUFO(random.random() * 1.8 + 1.8, ufo_gen_spot - random.randrange(190, 200))
            time_since_ufo_gen = 0

        for ufo in ufo_sprites_list:
            if ufo.last_dropped_bomb > random.randrange(60, 120):
                ufo.dropBomb(all_sprites_list, bomb_list)
                ufo.last_dropped_bomb = 0

        time_since_rock_gen += dt
        if time_since_rock_gen > random.randrange(24, 37):
            genRock(random.randrange(650, 690), random.randrange(1, 4))
            time_since_rock_gen = 0

    # --- GAME FLOW LOGIC --- #
    if rover.status != "dead" and level == 0:
        start_music.set_volume(0.8)
        pygame.mixer.Channel(7).play(start_music)
    while pygame.mixer.Channel(7).get_busy() == True and intro_music_played == False:
       pass

    intro_music_played = True

    if pygame.mixer.Channel(7).get_busy() == False and level == 0:
        level = 1
    elif rover.status != "dead" and level > 0:
        bg_music.set_volume(0.8)
        bg_music.play(0)
    elif rover.status == "dead" and dead_sequence_played_yet == False:
        bg_music.stop()
        for bullet in bullet_sprites_list:
            bullet.kill()
        crash_sfx.set_volume(0.6)
        crash_sfx.play(0)
        explosion = Explosion(rover.rect.x, rover.rect.y)
        explo_list.add(explosion)
        you_died = font_big.render("You Died!", True, BLACK)
        while pygame.mixer.get_busy():
            screen.fill(BLACK)
            world.drawBackground(screen)
            world.drawForeground(screen)
            world.drawGround(screen)
            hole_list.draw(screen)
            all_sprites_list.draw(screen)
            screen.blit(you_died, [110, SCREEN_HEIGHT / 2])
            explo_list.draw(screen)
            explo_list.update()
            pygame.display.flip()
            clock.tick(5)

        game_over_music.set_volume(0.4)
        game_over_music.play(0)
        dead_sequence_played_yet = True


    # --- DRAWING CODE --- #
    screen.fill(BLACK)

    # --- World Generation
    world.drawBackground(screen)
    world.drawForeground(screen)
    world.drawGround(screen)

    hole_list.draw(screen)
    hole_list.update()

    rock_list.draw(screen)
    rock_list.update()

    # --- Drawing all sprites (few exceptions)
    all_sprites_list.draw(screen)

    # Rendering score counter
    score_txt = font.render("Score: " + str(ufos_killed), True, BLACK)
    screen.blit(score_txt, [20, SCREEN_HEIGHT - 35])

    # Doing outro screen if need be
    if rover.status == "dead" and pygame.mixer.get_busy() == False:
        outro_screen()
        done = True



    # --- Rover Control
    rover.blitWheels(screen)
    rover.calc_grav()
    rover.update(rover_speed)

    bullet_sprites_list.update()

    # --- UFO Control
    ufo_sprites_list.update(dt)
    bomb_list.update()

    to_blit = pygame.transform.scale(screen, (320, 240))
    real_screen.blit(to_blit, (0, 0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()  # Close the window and quit.
