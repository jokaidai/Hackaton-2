from numpy import character
import pygame
import os
from support import import_folder


class Player(pygame.sprite.Sprite):
    """
    handle the main character creation 
    """
    def __init__(self:object, pos:tuple) -> None:
        super().__init__()

        # player set up
        self.import_char_assets()
        self.frame_index = 0
        self.animation_speed = 0.08
        self.image = self.animations['Stand'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        #player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.4
        self.jump_trigger = -16

    
    def import_char_assets(self:object) -> None:
        """
        a method that make the process of importing an image easy and automated
        """
        character_path = 'Assets/Graphics/Oop/'
        self.animations = {'Stand':[], 'StandL':[], 'Run':[], 'RunL':[], 'Jump':[], 'JumpL':[], 'Attack':[], 'AttackL':[] }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)


    def animate(self:object) -> None:
        """
        handle the switching of surface for the character to animate him depending on the situation
        """
        animation = self.animations['Stand']
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]

    def check_keys(self:object) -> None:
        """
        check wich key is being pressed and execute the appropriate action for the player
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
           self.direction.x = 1
            

        elif keys[pygame.K_a]:
            self.direction.x = -1
        
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
        self.animate()
        
       