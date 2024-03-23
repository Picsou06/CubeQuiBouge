from typing import Any
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.life=40
        super().__init__()
        self.sprite_sheet = pygame.image.load("images/player.png")
        self.image=self.get_image(0,0)
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.images = {"stay":self.get_image(0,0),"up":self.get_image(32,32),"down":self.get_image(0,64),"right":self.get_image(0,32),"left":self.get_image(32,0)}
        self.position = [x*32,y*32]
        self.feet= pygame.Rect(0,0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()


    def save_location(self):
        self.old_position = self.position.copy()


    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_up(self):
        clock = pygame.time.Clock()
        self.image=self.images["up"]
        self.position[1]-=32
        clock.tick(64)
    
    def move_down(self):
        clock = pygame.time.Clock()
        self.image=self.images["down"]
        self.position[1]+=32
        clock.tick(64)

    def move_right(self):
        clock = pygame.time.Clock()
        self.image=self.images["right"]
        self.position[0]+=32
        clock.tick(64)

    def move_left(self):
        clock = pygame.time.Clock()
        self.image=self.images["left"]
        self.position[0]-=32
        clock.tick(64)
    
    def get_image(self, x, y):
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet, (0,0), (x, y, 32, 32))
        return image
    
    def get_life(self):
        return self.life
    
    def set_life(self,life):
        self.life=life