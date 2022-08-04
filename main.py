import pygame
import os
from sys import exit
from setting import *
from tiles import Tile

# ----- INIT -----
pygame.init()
pygame.display.set_caption('Python Tamer')
CLOCK = pygame.time.Clock()
# ----- INIT(END) -----

# ----- GEN VAR -----
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# ----- GEN VAR(END)-----


# for row_index, row in enumerate(WORLD_MAP):
#     for col_index, cell in enumerate(row):
#         x = col_index * tile_size
#         y = row_index * tile_size

#         if cell == 'X':
#             tile = Tile((x, y), tile_size)
#             self.tiles.add(tile)


test_tile = pygame.sprite.Group(Tile((100,100), 200))        
while True:
        
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
             pygame.quit()
             exit()

    SCREEN.fill('black')
    test_tile.draw(SCREEN)
    pygame.display.update()
    CLOCK.tick(FPS)