from os import walk
import pygame

def import_folder(path) -> list:
    """
    this funct get the path from the player and import the required images
    """
    anim_list = []
    for _, __,img_files in walk (path):
       for img in img_files:
            full_path = path + '/' + img
            img_surf = pygame.image.load(full_path).convert_alpha()
            anim_list.append(img_surf)
    
    return anim_list