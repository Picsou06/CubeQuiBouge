import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__()
        self.sprite_sheet = pygame.image.load("images/player.png")
    
    def get_image(self):
        return self.sprite_sheet