import pygame
import os
from sys import exit

# ----- INIT -----
pygame.init()
pygame.display.set_caption('Python Tamer')
CLOCK = pygame.time.Clock()
# ----- INIT(END) -----

# ----- GEN VAR -----
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60
# ----- GEN VAR(END)-----


while True:
        
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    CLOCK.tick(FPS)