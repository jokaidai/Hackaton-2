import pygame

class Tile(pygame.sprite.Sprite):
    """
    Class used for the creation and management of the tiles 
    """

    def __init__(self:object, pos:tuple, size:int) -> None:
        super().__init__()
        
        self.image = pygame.Surface((size, size))
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft = pos)



    def update(self:object, x_move) -> None: 
        """
        'main' method of the class to execute redondant task of the class
        """
        self.rect.x += x_move

class StaticTile(Tile):
    """
    class used for the creatin and managment of designed tiles
    """
    def __init__(self:object, size:int, pos:tuple, surface:object):
        super().__init__(size, pos)
        self.image = surface