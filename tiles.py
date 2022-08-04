import pygame

class Tile(pygame.sprite.Sprite):
    """
    Class used for the creation and management of the tiles on the screen
    """

    def __init__(self, pos:tuple, size:int) -> None:
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('cyan')
        self.rect = self.image.get_rect(topleft = pos)