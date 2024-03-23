### BIBLIOTHEQUES & MODULES
import pygame
import pytmx
import pyscroll
import os
import random
import player

### CLASSE
class Game:
    def __init__(self, screen):
        self.previous_key_state = {}
        self.screen = screen
        self.mouvement = 5

        # Charger la carte
        tmx_data = pytmx.util_pygame.load_pygame('Tiled\\map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        # Collision
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
         # Création du joueur
        player_position = tmx_data.get_object_by_name("Player")
        print(int(player_position.x), int(player_position.y))
        self.player = player.Player(player_position.x/50, player_position.y/50)
        #Ajout du joueur au group de sprite de la map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def input_pressed(self):
        pressed = pygame.key.get_pressed()

        # Boucle sur toutes les touches surveillées
        for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]:
            # Vérifie si la touche est enfoncée et si elle était relâchée précédemment
            if pressed[key] and not self.previous_key_state.get(key, False):
                if self.mouvement > 0:
                    # Effectue le mouvement correspondant à la touche pressée
                    if key == pygame.K_UP:
                        self.player.move_up()
                    elif key == pygame.K_DOWN:
                        self.player.move_down()
                    elif key == pygame.K_RIGHT:
                        self.player.move_right()
                    elif key == pygame.K_LEFT:
                        self.player.move_left()
                    self.mouvement -= 1

            # Met à jour l'état précédent de la touche
            self.previous_key_state[key] = pressed[key]

    def update(self):
        self.group.update()
        # Verification collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > 0:
                sprite.move_back()

    def run(self):
        screen_width, screen_heidth = self.screen.get_size()
        leave = pygame.transform.scale(pygame.image.load("images/quitter.png"), (45, 45))
        clock = pygame.time.Clock()
        running = True
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
        while running:
            self.player.save_location()
            self.input_pressed()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            self.group.draw(leave)
            self.screen.blit(leave, (screen_width - 75, 25))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.roulette(100)
            clock.tick(8)

    def roulette(self, chance):
         if random.randint(0,chance)!=1:
              self.mouvement+=1
         else:
              self.player.set_life(self.player.get_life()-10)


#Crée un objet Game et lance la partie
def start(screen):
        game = Game(screen)
        game.run()
