import pygame
import pytmx
import pyscroll
import os
import random


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("CubeQuiBouge")

        # Charger la carte
        tmx_data = pytmx.util_pygame.load_pygame('Tiled\\mapvierge.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

    def run(self):
        running = True
        while running:
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("coucou")


if __name__ == '__main__':
    pygame.init()
    game = Game()
