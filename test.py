import pygame
import pytmx
import pyscroll
import player
import random

class Game:
    def __init__(self, screen):
        # Initialisation du jeu
        self.previous_key_state = {}
        self.screen = screen
        self.mouvement = 5
        self.map_surface = pygame.Surface((800, 600))  # Crée une surface pour dessiner la carte
        pygame.display.set_caption("CubeQuiBouge")

        # Charger la carte inclinée
        tmx_data = pytmx.util_pygame.load_pygame('Tiled\\mapvierge.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.map_surface.get_size())
        self.map_layer.zoom = 4

        # Ajouter la couche de carte au groupe
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)

        # Initialiser le joueur
        self.player = player.Player(20, 20)
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

    def run(self):
        # Boucle principale du jeu
        screen_width, screen_heidth = self.screen.get_size()
        leave = pygame.transform.scale(pygame.image.load("images/quitter.png"), (45,45))
        clock = pygame.time.Clock()
        running = True
        while running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.roulette(100)

            # Mettre à jour le joueur et centrer la carte sur le joueur
            self.input_pressed()
            self.group.update()
            self.group.center(self.player.rect.center)

            # Effacer la surface de la carte
            self.map_surface.fill((0, 0, 0))

            # Dessiner la carte sur la surface
            self.group.draw(self.map_surface)

            # Blit la surface de la carte sur l'écran du jeu
            self.screen.blit(self.map_surface, (0, 0))
            self.screen.blit(leave, (screen_width-75, 25))

            # Mettre à jour l'écran
            pygame.display.flip()

            # Limiter le nombre de frames par seconde
            clock.tick(60)

    def roulette(self, chance):
         if random.randint(0,chance)!=1:
              self.mouvement+=1
         else:
              self.player.set_life(self.player.get_life()-10)

# Fonction principale pour démarrer le jeu
def start(screen):
    game = Game(screen)
    game.run()
