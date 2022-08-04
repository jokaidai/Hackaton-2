import pygame
from tiles import Tile
from setting import TILE_SIZE

class Level:
    """
    class that rely on the Tile class to draw the level
    """
    def __init__(self:object, level_data:list, screen) -> None:
        self.display_surface = screen
        self.setup_level(level_data)
        self.camera = 0


    def setup_level(self:object, level_data):
        """
        method that will draw the tiles accordinf to the level data
        """
        self.tiles = pygame.sprite.Group() 
        for row_idx, row in enumerate(level_data):
            for col_idx, col in enumerate(row):
                if col == 'X':
                    x = col_idx * TILE_SIZE
                    y = row_idx * TILE_SIZE
                    tile = Tile ((x, y), TILE_SIZE)
                    self.tiles.add(tile)


    def run(self:object) -> None:
        """
        method that will be called from the main to draw information from this class
        """
        self.tiles.update(self.camera)
        self.tiles.draw(self.display_surface)