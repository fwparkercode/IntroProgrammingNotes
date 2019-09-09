
import pygame
import random



# Define some colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 215, 0)
pygame.init()  # starts pygame (Vroom!)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SPIKE SHOT")
done = False  # condition for the game loop
clock = pygame.time.Clock()
# fonts
font = pygame.font.SysFont('ArcadeClassic', 25, True, False)
font2 = pygame.font.SysFont('ArcadeClassic', 70, True, False)

# variables
r = 0
level = 1
score = 0

# sounds
laser = pygame.mixer.Sound("laser4.Wav")
bg = pygame.mixer.Sound("Chance is music PSG2.wav")
coin_sound = pygame.mixer.Sound("hjm-coin_clicker_3.wav")
player_explode = pygame.mixer.Sound("SFX_Explosion_01.wav")




# back ground music
bg.play(-1)

# ENEMY CLASS
class Enemy(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.image.load("spikedball (1).png")
        self.rect = self.image.get_rect()
        self.rect.x = screen_width + self.rect.width * 3
        self.rect.y = screen_height//2 - self.rect.height
        self.change_x = random.randrange(3, 5 + level) * -1
        self.change_y = random.randrange(3, 8 + level) * -1
        self.gravity = .3
        self.active = False

# GRAVITY UPDATE AND BOUNCING UPDATE
    def update(self):
        if self.rect.right < screen_width:
            self.active = True
        self.rect.x += self.change_x
        self.change_y += self.gravity
        self.rect.y += self.change_y
        if self.rect.bottom >= screen_height:
            self.change_y *= -.9
            self.rect.bottom = screen_height
        if self.rect.left <= 0:
            self.change_x *= -.9
            self.rect.left = 0
        if self.rect.right >= screen_width:
            if self.active == True:
                self.change_x *= -1
                self.rect.right = screen_width

# PLAYER CLASS


class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.image.load("cannon.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = screen_height
        self.rect.x = screen_width//2 - self.rect.width//2
        self.change_x = 0
# UPDATE ALLOWS FOR THE CONTROL OF THE PLAYER

    def update(self):
        self.rect.x += self.change_x

# BULLET CLASS


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cannon ball.png")
        self.rect = self.image.get_rect()
# UPDATE WHEN BULLET HITS ENEMY

    def update(self):
        self.rect.y -= 8
        if self.rect.bottom < 0:
            self.kill()

# COIN CLASS


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("goldCoin1.png")
        self.rect = self.image.get_rect()
        self.change_y = -6
# UPDATE FOR WHEN COIN HITS PLAYER

    def update(self):
        self.rect.y += 9
        if self.rect.bottom >= screen_height:
            self.change_y *= -.9
            self.rect.bottom = screen_height


player = Player(BLUE)
change_x = 0
player_x = 0
player_y = screen_height

key_x = change_x





# groups
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(player)
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

# making enemies
for x in range(screen_width, 10 * screen_width, screen_width):
    new_enemy = Enemy(RED)
    new_enemy.rect.x = x + 10
    all_sprites_group.add(new_enemy)
    enemy_group.add(new_enemy)

# CODE FOR CUT SCREEN


def cut_screen():
    done = False
    text = font.render("Use LEFT and RIGHT to Move and SPACE to shoot, press SPACE to Start!!", True, BLUE)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True

        screen.fill(BLACK)

        screen.blit(text, [screen_width // 2 - text.get_rect().width // 2, screen_height // 2 - text.get_rect().height // 2])
        pygame.display.flip()
        clock.tick(60)
#  CODE FOR GAME OVER SCREEN


def game_over():
    done = False
    text = font.render("Game Over, press E to exit", True, RED)
    bg.set_volume(0)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    done = True
                    pygame.quit()


        screen.fill(BLACK)

        screen.blit(text, [screen_width // 2 - text.get_rect().width // 2, screen_height // 2 - text.get_rect().height // 2])
        screen.blit(score_text, [40, 40])

        if score < 10:
            bad_text = font2.render("You're T", True, RED)
            screen.blit(bad_text, [screen_width // 2 - 110, screen_height // 2 - 80])
            pygame.draw.line(screen, RED, (240, 170), (112, 56), 3)
            pygame.draw.line(screen, RED, (114, 58), (114, 88), 3)
            pygame.draw.line(screen, RED, (114, 58), (144, 58), 3)
        pygame.display.flip()
        clock.tick(60)

cut_screen() # SHOWS CUT SCREEN BEFORE THE MAIN LOOP STARTS

#PAUSE SCREEN


def pause_screen():
    done = False
    text = font.render("PAUSE, Press Space To Play", True, BLUE)
    bg.set_volume(0.2)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bg.set_volume(1.0)
                    done = True

        screen.fill(BLACK)

        screen.blit(text,
                    [screen_width // 2 - text.get_rect().width // 2, screen_height // 2 - text.get_rect().height // 2])
        pygame.display.flip()
        clock.tick(60)

# -------- Main Program Loop -----------


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
# when a key is pressed down
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.change_x += 5
            elif event.key == pygame.K_LEFT:
                player.change_x -= 5
            elif event.key == pygame.K_SPACE:
                laser.play()
                new_bullet = Bullet()
                new_bullet.rect.center = player.rect.center
                all_sprites_group.add(new_bullet)
                bullet_group.add(new_bullet)
            elif event.key == pygame.K_ESCAPE:
                pause_screen()

# when a key is lifted up after being pressed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.change_x -= 5
            if event.key == pygame.K_LEFT:
                player.change_x += 5

    # --- Game logic should go here
    player.rect.right += player.change_x


    if player.rect.left <  0:
        player.rect.left = 0
    if player.rect.right > screen_width:
        player.rect.right = screen_width
    all_sprites_group.update()
# when bullet hits the enemy
    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, False)

        for hit in hit_list:
            hit.kill()
            bullet.kill()
            new_coin = Coin()
            new_coin.rect.center = hit.rect.center
            all_sprites_group.add(new_coin)
            coin_group.add(new_coin)
            score += 1
            print(score, "point")
            break

# when enemy hit the player
    for enemy in enemy_group:
        hit_list = pygame.sprite.spritecollide(player, enemy_group, True)

        for hit in hit_list:
            player_explode.play()
            player.kill()
            enemy.kill()
            game_over()

    for coin in coin_group:
        hit_list = pygame.sprite.spritecollide(player, coin_group, True)

        for hit in hit_list:
            coin.kill()
            coin_sound.play()
            score += 1

            print(score, "points")

# CHANGES LEVEL
    if len(enemy_group) <= 0:
        level += 1

        print("level", level)
        for i in range(level):
            new_enemy = Enemy(RED)
            all_sprites_group.add(new_enemy)
            enemy_group.add(new_enemy)
            r += 5
            if r >= 210:
                r = 255

    # --- Drawing code should go here
    screen.fill(WHITE)
    all_sprites_group.draw(screen)
    score_text = font.render("Score: " + str(score), True, BLUE)
    screen.blit(score_text, [40, 40])
    level_text = font2.render("Level: " + str(level), True, (r, 0, 0))
    screen.blit(level_text, [screen_width // 2 - 110, screen_height // 2 - 20])
    pause = font.render("Esc II", True, BLUE)
    screen.blit(pause, [screen_width - 85, 40])

    pygame.display.flip()  # update the screen
    clock.tick(60)  # 60 frames per second

pygame.quit()  # Close the window and quit.
