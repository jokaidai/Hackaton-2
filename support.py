from os import walk
import pygame
from csv import reader
from setting import TILE_SIZE

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


def import_csv_files(path) -> list:
    """
    this funct get the path from of the csv files and import the required data
    """
    platform_map = []
    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:
            platform_map.append(list(row))

    return platform_map


def import_cut_graphics(path) -> list:
    """
    slice the tile assets into surface so it can be used independately
    """
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / TILE_SIZE)
    tile_num_y = int(surface.get_size()[1] / TILE_SIZE)
    
    sliced_assets = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            new_surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
            new_surface.blit(surface,(0, 0), pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
    
    return sliced_assets

