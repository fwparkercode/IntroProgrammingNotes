"""
Final project
Ready, Set, Flip! - a pancake cooking game
Sofia Brown

Description: in this game, you must cook pancakes on the stove, making sure not to burn or undercook any of them.
the end goal is to make as many good pancakes as possible, and keep playing to beat your high score.
"""

import pygame

pygame.init()

# Global Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (170, 230, 250)
RED = (190, 6, 6)
TAN = (250, 220, 150)

SCREEN_WIDTH = 1066
SCREEN_HEIGHT = 788
done = False

size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ready, Set, Flip!")
clock = pygame.time.Clock()  # Used to manage how fast the screen updates
pygame.mouse.set_visible(False)

# Images
background_image = pygame.image.load("stove.png")
spatula_image = pygame.image.load("spatula.png")
pancake_image = pygame.image.load("pancake.png")
ladle_image = pygame.image.load("ladle.png")
plate_image = pygame.image.load("plate.png")
batter_pancake_image = pygame.image.load("batter_pancake.png")
burnt_pancake_image = pygame.image.load("burnt_pancake.png")
intro_image = pygame.image.load("intro_page.png")

# Sounds
bg_music = pygame.mixer.Sound("background_music.wav")
bg_music.set_volume(0.05)
bg_music.play(-1)
sizzle_sound = pygame.mixer.Sound("sizzle.wav")
sizzle_sound.set_volume(0.05)
tool_switch_sound = pygame.mixer.Sound("spatula_sound.wav")
batter_sound = pygame.mixer.Sound("batter_drop.wav")
intro_jingle = pygame.mixer.Sound("shop_bell.wav")
bad_sound = pygame.mixer.Sound("bad.wav")
bad_sound.set_volume(50.0)
good_sound = pygame.mixer.Sound("plusscore.wav")
good_sound.set_volume(50.0)

# control variables
score = 0
instruction_x = 760
instruction_y = 100

# timer variables
frame_count = 0
frame_rate = 20
start_time = 30

# text fonts
title_font = pygame.font.SysFont("Arial", 80, True, False)
instructions_title_font = pygame.font.SysFont("Arial", 30, True, False)
score_font = pygame.font.SysFont("Arial", 50, True, False)
instructions_font = pygame.font.SysFont("Arial", 24, False, False)
end_font = pygame.font.SysFont("Calibri", 150, True, False)
end_font_2 = pygame.font.SysFont("Calibri", 70, False, False)
sign_font = pygame.font.SysFont("Arial", 35, True, False)
timer_font = pygame.font.Font(None, 50)


# classes
class Tools(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spatula = pygame.image.load("spatula.png")
        self.ladle = pygame.image.load("ladle.png")
        self.image = self.ladle
        self.rect = self.image.get_rect()
        self.has_batter = False

    def update(self):
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]

        self.rect.x = x
        self.rect.y = y

        if self.rect.x > SCREEN_WIDTH - 288:  # make it so spatula can go off to the left a little
            self.rect.x = SCREEN_WIDTH - 288
        if self.rect.y > SCREEN_HEIGHT - 288:
            self.rect.y = SCREEN_HEIGHT - 288

    def draw_batter(self):
        if self.has_batter:
            pygame.draw.ellipse(screen, TAN, [tool.rect.x + 56, tool.rect.y + 196, 125, 40])


class Batter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.burnt_img = pygame.image.load("burnt_pancake.png")
        self.pancake_img = pygame.image.load("pancake.png")
        self.batter_img = pygame.image.load("batter_pancake.png")
        self.image = self.batter_img
        self.rect = self.image.get_rect()
        self.health = 12
        self.change_health = 0.1
        self.move = False

    def update(self):
        if self.move:
            self.rect.center = pygame.mouse.get_pos()
            self.rect.x += 250
            self.rect.y += 20
        else:
            self.health -= self.change_health

        if self.health <= 5:
            self.image = self.pancake_img
        if self.health <= 0:
            self.image = self.burnt_img


tool_list = pygame.sprite.Group()
tool = Tools()
tool_list.add(tool)

pancake_list = pygame.sprite.Group()


# intro page
def intro_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro_jingle.play()
                    done = True
        screen.fill(BLUE)
        screen.blit(intro_image, [0, 80])

        # instructions
        pygame.draw.rect(screen, WHITE, [750, 0, 500, SCREEN_HEIGHT])
        pygame.draw.line(screen, BLACK, [750, 59], [750, SCREEN_HEIGHT], 4)
        instructions_title = instructions_title_font.render("Instructions:", True, BLACK)
        screen.blit(instructions_title, [760, 70])

        line_1 = instructions_font.render("In this game, you have to flip as many", True, BLACK)
        screen.blit(line_1, [instruction_x, instruction_y])
        line_2 = instructions_font.render("pancakes as you can in a given", True, BLACK)
        screen.blit(line_2, [instruction_x, instruction_y + 20])
        line_3 = instructions_font.render("amount of time without burning or", True, BLACK)
        screen.blit(line_3, [instruction_x, instruction_y + 40])
        line_4 = instructions_font.render("undercooking any. You can play many", True, BLACK)
        screen.blit(line_4, [instruction_x, instruction_y + 60])
        line_5 = instructions_font.render("rounds to try and beat your high score", True, BLACK)
        screen.blit(line_5, [instruction_x, instruction_y + 80])
        line_6 = instructions_font.render("Press the SPACE key to switch between", True, BLACK)
        screen.blit(line_6, [instruction_x, instruction_y + 120])
        line_7 = instructions_font.render("the spatula and the ladle. Use the", True, BLACK)
        screen.blit(line_7, [instruction_x, instruction_y + 140])
        line_8 = instructions_font.render("ladle to DRAG batter onto the stove.", True, BLACK)
        screen.blit(line_8, [instruction_x, instruction_y + 160])
        line_9 = instructions_font.render("Use the spatula to DRAG cooked", True, BLACK)  # flip pancakes?
        screen.blit(line_9, [instruction_x, instruction_y + 180])
        line_10 = instructions_font.render("pancakes onto any plate up top.", True, BLACK)
        screen.blit(line_10, [instruction_x, instruction_y + 200])
        line_11 = instructions_font.render("Each pancake has their own timer", True, BLACK)
        screen.blit(line_11, [instruction_x, instruction_y + 240])
        line_12 = instructions_font.render("indicating when they're done cooking.", True, BLACK)
        screen.blit(line_12, [instruction_x, instruction_y + 260])
        line_13 = instructions_font.render("Burning or undercooking a pancake", True, BLACK)
        screen.blit(line_13, [instruction_x, instruction_y + 280])
        line_14 = instructions_font.render("will result in a loss of points. Try", True, BLACK)
        screen.blit(line_14, [instruction_x, instruction_y + 300])
        line_15 = instructions_font.render("to get as many points as possible in", True, BLACK)
        screen.blit(line_15, [instruction_x, instruction_y + 320])
        line_16 = instructions_font.render("the time given.", True, BLACK)
        screen.blit(line_16, [instruction_x, instruction_y + 340])
        line_17 = instructions_font.render("DON'T USE THE 2 LEFT STOVES", True, BLACK)
        screen.blit(line_17, [instruction_x, instruction_y + 380])
        line_18 = instructions_font.render("THEY'RE OUT OF ORDER", True, BLACK)
        screen.blit(line_18, [instruction_x, instruction_y + 400])
        line_19 = instructions_font.render("YOUR PANCAKES WILL BURN THERE", True, BLACK)
        screen.blit(line_19, [instruction_x, instruction_y + 420])
        line_20 = instructions_font.render("Good luck chef!", True, BLACK)
        screen.blit(line_20, [instruction_x, instruction_y + 460])
        line_21 = instructions_title_font.render("Press the RETURN key to", True, BLACK)
        screen.blit(line_21, [instruction_x, instruction_y + 500])
        line_22 = instructions_title_font.render("enter the kitchen and", True, BLACK)
        screen.blit(line_22, [instruction_x, instruction_y + 520])
        line_23 = instructions_title_font.render("begin right away.", True, BLACK)
        screen.blit(line_23, [instruction_x, instruction_y + 540])

        # title
        pygame.draw.rect(screen, WHITE, [0, 0, 906, 58])
        pygame.draw.line(screen, BLACK, [0, 59], [SCREEN_WIDTH, 59], 4)
        title = title_font.render("Welcome to Ready, Set, Flip!", True, BLACK)
        screen.blit(title, [100, 0])

        pygame.display.flip()
        clock.tick(60)


# end screen
def end_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BLUE)
        screen.blit(pancake_image, [60, 300])
        screen.blit(pancake_image, [260, 300])
        screen.blit(pancake_image, [460, 300])
        screen.blit(pancake_image, [660, 300])
        screen.blit(pancake_image, [860, 300])

        end_screen1 = end_font.render("TIME'S UP!", True, BLACK)
        screen.blit(end_screen1, [230, 100])
        end_screen2 = end_font_2.render("you made " + str(score) + " perfectly cooked pancakes", True, BLACK)
        screen.blit(end_screen2, [100, 500])
        end_screen3 = end_font_2.render("play again to beat your score", True, BLACK)
        screen.blit(end_screen3, [200, 600])

        pygame.display.flip()
        clock.tick(60)


intro_screen()

# ----------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # spatula and ladle controls
        if tool.image == tool.spatula:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for pancake in pancake_list:
                    if pancake.rect.collidepoint(event.pos[0] + 250, event.pos[1] + 20):
                        pancake.move = True

            if event.type == pygame.MOUSEBUTTONUP:
                for p in pancake_list:
                    if p.move:
                        pancake = p
                    p.move = False

                if tool.rect.y < 230:
                    if pancake.image == pancake.pancake_img:
                        pancake.change_health = 0
                        good_sound.play()
                        score += 1
                    else:
                        pancake.change_health = 0
                        bad_sound.play()
                        score -= 1
                        pancake.kill()

        elif tool.image == tool.ladle:
            if event.type == pygame.MOUSEBUTTONDOWN:
                batter_sound.play()
                if 350 < tool.rect.x < 550 and 400 < tool.rect.y < 787:
                    tool.has_batter = True
            if event.type == pygame.MOUSEBUTTONUP:
                if 230 < tool.rect.y + 160 < 525:
                    tool.has_batter = False
                    sizzle_sound.play()
                    new_pancake = Batter()
                    new_pancake.rect.x = tool.rect.x + 30
                    new_pancake.rect.y = tool.rect.y + 160
                    pancake_list.add(new_pancake)
                else:
                    tool.has_batter = False

        # changing the tool with space bar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if tool.image == tool.spatula:
                    tool.image = tool.ladle
                    tool_switch_sound.play()
                elif tool.image == tool.ladle:
                    tool.image = tool.spatula
                    tool_switch_sound.play()

    # ----------- Game Logic - updates -----------
    tool_list.update()
    pancake_list.update()

    # ----------- Drawing Code -----------
    screen.blit(background_image, [0, 0])

    # draw plates
    screen.blit(plate_image, [250, 5])
    screen.blit(plate_image, [550, 5])
    screen.blit(plate_image, [790, 5])

    # draw score ellipse
    pygame.draw.ellipse(screen, BLACK, [16, SCREEN_HEIGHT - 155, 230, 150])
    pygame.draw.ellipse(screen, RED, [20, SCREEN_HEIGHT - 152, 223, 143])

    # timer code

    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    if total_seconds <= 0:
        total_seconds = 0
        done = True
        end_screen()

    # Use python string formatting to format in leading zeros
    output_string = "time: {0:02}:{1:02}".format(minutes, seconds)

    # Blit to the screen
    text = timer_font.render(output_string, True, WHITE)

    screen.blit(text, [40, SCREEN_HEIGHT - 80])

    frame_count += 1

    # draw score text
    score_text = score_font.render("score: " + str(score), True, WHITE)
    screen.blit(score_text, [40, SCREEN_HEIGHT - 120])

    # draw out of order sign
    out_of_order = sign_font.render("OUT OF ORDER", True, RED)
    screen.blit(out_of_order, [30, 295])
    out_of_order = sign_font.render("OUT OF ORDER", True, RED)
    screen.blit(out_of_order, [30, 485])

    # draw lists to screen
    pancake_list.draw(screen)
    tool_list.draw(screen)
    tool.draw_batter()

    pygame.display.flip()
    clock.tick(frame_rate)

pygame.quit()
