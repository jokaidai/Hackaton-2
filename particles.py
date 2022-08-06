import pygame
from support import import_folder

class ParticleEffect(pygame.sprite.Sprite):
    """
    class that will hold the logic for the jump dust particles animation
    """

    def __init__(self:object, pos:tuple, type:str) -> None:
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.5
        
        if type == 'jump':
            self.frames = import_folder('Assets/Graphics/Oop/DustParticles/jump')

        if type == 'land':
            self.frames = import_folder('Assets/Graphics/Oop/DustParticles/land')

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
    

    def animate(self:object) -> None:
        """
        handle the jump dust animation
        """
        self.frame_index += self.animation_speed
       
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]


    def update(self:object, camera) -> None:
        """
        run the nesscesary classes method when called 
        """
        self.animate()
        self.rect.x += camera