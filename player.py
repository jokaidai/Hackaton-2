import pygame
from support import import_folder


class Player(pygame.sprite.Sprite):
    """
    handle the main character creation and actions
    """
    def __init__(self:object, pos:tuple) -> None:
        super().__init__()

        # player set up
        self.import_char_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['Stand'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.4
        self.jump_trigger = -10

        # player status
        self.status = 'Stand'
        self.facing_right = True

    
    def import_char_assets(self:object) -> None:
        """
        a method that make the process of importing an image easy and automated
        """
        character_path = 'Assets/Graphics/Oop/'
        self.animations = {'Stand':[], 'Run':[], 'Jump':[], 'Fall':[], 'Attack':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)


    def animate(self:object) -> None:
        """
        handle the switching of surface for the character to animate him depending on the situation
        """
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        
        if self.frame_index >= len(animation):
            self.frame_index = 0
           
        image = animation[int(self.frame_index)]    
        if self.facing_right:
            self.image = image
        else:
            reverse_image = pygame.transform.flip(image, True, False)
            self.image = reverse_image
    

    def check_keys(self:object) -> None:
        """
        check wich key is being pressed and execute the appropriate action for the player
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
           self.direction.x = 1
           self.facing_right = True
            
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_right = False

        elif keys[pygame.K_SPACE] and self.direction.y == 0:
             self.jump()
        
        else:
            self.direction.x = 0


    def check_status(self:object) -> None:
        """
        method that will check the status of the char ( running, jumping ect ect).
        """
        if self.direction.y < 0:  
            self.status = 'Jump'
            self.animation_speed = 0.02
            
        elif self.direction.y > 1: # can not be 0 because gravity is = to 0.8 it will always fall
            self.status = 'Fall'
            self.animation_speed = 0.02
            
        elif self.direction.x != 0:
            self.status = 'Run'
            self.animation_speed = 0.08
        else:
            self.status = 'Stand'
            self.animation_speed = 0.05
            

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
        self.check_status()
        self.animate()   