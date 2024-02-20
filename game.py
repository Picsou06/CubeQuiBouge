import pygame
import pytmx
import pyscroll
import os
import random


class Game:
    def __init__(self, screen):
        self.screen = screen
        pygame.display.set_caption("CubeQuiBouge")

        # Charger la carte
        tmx_data = pytmx.util_pygame.load_pygame('Tiled\\mapvierge.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

    def run(self):
        running = True
        self.screen.fill((0,0,0))
        pygame.display.flip()
        while running:
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("coucou")

def start(screen):
    if __name__ == '__main__':
        pygame.init()
        game = Game(screen)
        game.run()
