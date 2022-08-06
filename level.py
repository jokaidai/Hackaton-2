import pygame
from player import Player
from tiles import Tile
from setting import SCREEN_WIDTH, TILE_SIZE
from particles import ParticleEffect

class Level:
    """
    class that rely on the Tile class to draw the level
    """
    def __init__(self:object, level_data:list, screen) -> None:
        
        self.display_surface = screen
        self.setup_level(level_data)
        self.camera = 0

        #jump dust
        self.dust_sprite = pygame.sprite.GroupSingle()


    def create_jump_particles(self:object, pos:tuple) -> None:
        """
        create the jump particle sprites ... need to be in level to access the require variable
        """
        if self.player.sprite.facing_right:
            pos -= pygame.math.Vector2(10, 5)
        else:
            pos += pygame.math.Vector2(10, -5)

        jump_particle_spite = ParticleEffect(pos, 'jump')
        self.dust_sprite.add(jump_particle_spite)


    def setup_level(self:object, level_data):
        """
        method that will draw the tiles accordinf to the level data
        """
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_idx, row in enumerate(level_data):
            for col_idx, col in enumerate(row):
                
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE
                
                if col == 'X':
                    
                    tile_sprite = Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile_sprite)

                if col == 'P':
    
                    player_sprite = Player((x, y), self.display_surface, self.create_jump_particles)
                    self.player.add(player_sprite)


    def scroll_x(self:object) -> None:
        """
        method that scroll the screen horizontaly when the player have reach the border
        """ 
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < SCREEN_WIDTH // 4  and direction_x < 0:
            self.camera = 8
            player.speed = 0

        elif player_x > SCREEN_WIDTH - (SCREEN_WIDTH // 4) and direction_x > 0:
            self.camera = -8
            player.speed = 0
          

        else:
            self.camera = 0
            player.speed = 8
           

    def horizontal_collision(self:object) -> None:
        """
        a method that will check all type of horizontal collisions but only horizontal
        """
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left


    def vertical_collision(self:object) -> None:
        """
        a method that will check all type of vertical collisions but only vertical
        """
        player = self.player.sprite
        player.create_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0


    def create_level(self:object) -> None:
        """
        method that will be called from the main to draw information from this class
        """

        # dust particle
        self.dust_sprite.update(self.camera)
        self.dust_sprite.draw(self.display_surface)

        # level tile
        self.tiles.update(self.camera)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # player tile
        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.player.draw(self.display_surface)