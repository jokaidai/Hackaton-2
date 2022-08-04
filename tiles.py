import pygame

class Tile(pygame.sprite.Sprite):
    """
    Class used for the creation and management of the tiles 
    """

    def __init__(self, pos:tuple, size:int) -> None:
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('cyan')
        self.rect = self.image.get_rect(topleft = pos)


    def update(self:object, x_move) -> None:
        """
        'main' method of the class to execute redondant task of the class
        """
        self.rect.x += x_move