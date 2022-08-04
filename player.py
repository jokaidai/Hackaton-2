from tkinter import N
import pygame

class Player(pygame.sprite.Sprite):
    """
    handle the main character creation 
    """
    def __init__(self:object, pos:tuple) -> None:
        super().__init__()

        # player set up
        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft = pos)

        #player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_trigger = -16


    def check_keys(self:object) -> None:
        """
        check wich key is being pressed and execute the appropriate action for the player
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
           self.direction.x = 1

        elif keys[pygame.K_a]:
            self.direction.x =  - 1
        
        elif keys[pygame.K_SPACE]:
             self.jump()
        
        else:
            self.direction.x = 0


    def create_gravity(self:object) -> None:
        """
        method that will activate gravity using on the player rect
        """
        self.direction.y += self.gravity
        self.rect.y += self.direction.y


    def jump(self:object) -> None:
        """
        method that will emulate a jump
        """
        self.direction.y = self.jump_trigger


    def update(self:object) -> None:
        """
        'main' method of the class to execute redondant task of the class
        """
        self.check_keys()
        
       