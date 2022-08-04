from tkinter import S
import pygame
from player import Player
from tiles import Tile
from setting import SCREEN_WIDTH, TILE_SIZE

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
        self.player = pygame.sprite.GroupSingle()

        for row_idx, row in enumerate(level_data):
            for col_idx, col in enumerate(row):
                
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE
                
                if col == 'X':
                    
                    tile_sprite = Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile_sprite)

                if col == 'P':
    
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self:object) -> None:
        """
        method that scroll the screen horizontaly when the player have reach the border
        """ 
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < SCREEN_WIDTH // 4  and direction_x < 0:
            self.camera = 8
            player.speed = 0

        elif player_x > SCREEN_WIDTH - (SCREEN_WIDTH // 4) and direction_x > 0:
            self.camera = -8
            player.speed = 0
          

        else:
            self.camera = 0
            player.speed = 8
           

    def run(self:object) -> None:
        """
        method that will be called from the main to draw information from this class
        """
        # level tile
        self.tiles.update(self.camera)
        self.tiles.draw(self.display_surface)

        # player tile
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()


