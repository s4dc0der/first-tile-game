import pygame

class Map:
    def __init__(self, level, tile_size = (10, 10)):

        self.tiles = []

        for tile in level:
            if level[tile] == "wall":
                self.tiles.append(pygame.Rect(tile[0], tile[1], tile_size[0], tile_size[1]))

    def map_render(self, display):

        for tile in self.tiles:
            pygame.draw.rect(display, (255, 255, 255), tile)

