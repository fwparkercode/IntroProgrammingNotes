import pygame

pygame.init()
screen = pygame.display.set_mode((700, 500))
clock  = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

surf = pygame.Surface((100, 100), pygame.SRCALPHA)
surf.fill(WHITE)
rotated_surf = surf

rect = surf.get_rect()  # grab pygame rect object
angle = 45  # degrees

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    angle += 1  # make it spin

    screen.fill(BLACK)
    pygame.draw.rect(surf, RED, [20,20,30,30])
    pygame.draw.rect(surf, RED, [50,50,30,30])


    rotated_surf = pygame.transform.rotate(surf, angle)

    # you have to grab a new rectangle to represent the rotated object because it distorts the size.  A rotated box is a bigger rectangle than one at the 90 deg cardinal headings
    rect = rotated_surf.get_rect(center = (100, 100))  # lock the position of the rectangle so you don't have to switch back and forth.
    screen.blit(rotated_surf, (rect.x, rect.y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()