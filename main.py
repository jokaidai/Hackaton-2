import pygame, sys
from setting import *
from level import Level

# ----- INIT -----
pygame.init()
pygame.display.set_caption('Python Tamer')
CLOCK = pygame.time.Clock()
# ----- INIT(END) -----

# ----- GEN VAR -----
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
LEVEL = Level(LEVEL_0, SCREEN)
# ----- GEN VAR(END)-----

while True:
        
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
             pygame.quit()
             exit()

    SCREEN.fill('black')
    LEVEL.create_level()

    pygame.display.update()
    CLOCK.tick(FPS)