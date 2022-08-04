import pygame

class Player(pygame.sprite.Sprite):
    """
    handle the main character creation 
    """
    def __init__(self:object, pos:tuple) -> None:
        super().__init__()

        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8

    def check_keys(self:object) -> None:
        """
        check wich key is being pressed and execute the appropriate action for the player
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
           self.direction.x = 1

        elif keys[pygame.K_a]:
            self.direction.x =  - 1
        
        # elif keys[pygame.K_SPACE]:
        #     self.direction.y = -20
        
        else:
            self.direction.x = 0
            # self.direction.y = 0
        
    def update(self:object) -> None:
        """
        'main' method of the class to execute redondant task of the class
        """
        self.rect.x += self.direction.x * self.speed
        self.check_keys()