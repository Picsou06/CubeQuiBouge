### BIBLIOTHEQUES & MODULES
import pygame
import pytmx
import pyscroll
import random
import player
import mazescan
import time
import endgame

start=0

### CLASSE
class Game:
    def __init__(self, screen, matrix, pos = False):
        if not pos:
            self.previous_key_state = {}
            self.screen = screen
            self.mouvement = 21
            self.matrix = matrix

        # Charger la carte
        tmx_data = pytmx.util_pygame.load_pygame('Tiled\\map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        # Collision
        self.walls = []
        self.shop = []
        self.chest = []
        self.key = []
        self.end = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "shop":
                self.shop.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "chest":
                self.chest.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.name == "key":
                self.key.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.name == "end":
                self.end.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        # Création du joueur
        if not pos:
            player_position = tmx_data.get_object_by_name("Player")
            self.player = player.Player(player_position.x, player_position.y)
            self.player.set_life(40)
            self.player.set_money(10)
            self.player.set_chance(1)
        # else:
            # player_position = tmx_data.get_object_by_name("Player")
            # self.player = player.Player(pos[0]/32, pos[1]/32)
        #Ajout du jon oueur au group de sprite de la map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)
    def input_pressed(self):
        pressed = pygame.key.get_pressed()
        # Boucle sur toutes les touches surveillées
        for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_a]:
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
                    elif key == pygame.K_a:
                        self.__init__(self.screen, self.matrix, self.player.get_location())
                    self.mouvement -= 1
            # Met à jour l'état précédent de la touche
            self.previous_key_state[key] = pressed[key]
    def update(self):
        self.group.update()
        # Verification collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.key) == 0:
                position=self.player.get_location()
                self.matrix[int(position[1]/32)][int(position[0]/32)]=0
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[i])):
                        if self.matrix[i][j]==6:
                            self.matrix[i][j]=7
                mazescan.create_xml_file(self.matrix)
                self.__init__(self.screen, self.matrix, self.player.get_location())
            if sprite.feet.collidelist(self.chest) >= 0:
                position=self.player.get_location()
                self.matrix[int(position[1]/32)][int(position[0]/32)]=0
                x=random.randint(5,20)*self.player.get_chance()
                print(x)
                self.player.add_money(x)
                mazescan.create_xml_file(self.matrix)
                self.__init__(self.screen, self.matrix, self.player.get_location())
            if sprite.feet.collidelist(self.walls) > 0:
                sprite.move_back()
            elif sprite.feet.collidelist(self.end) == 0:
                endgame.win(self.screen)


    def run(self):
        screen_width, screen_height = self.screen.get_size()
        money_img = pygame.transform.scale(pygame.image.load("images/money.png"), (45, 45))
        font = pygame.font.SysFont('bold', 30)
        money = font.render(str(self.player.get_money()), True, (255, 255, 255))
        vie_img = pygame.transform.scale(pygame.image.load("images/vie.png"), (45, 45))
        vie = font.render(str(self.player.get_life()), True, (255,255,255))
        barillet = pygame.transform.scale(pygame.image.load("images/barillet/barillet0.png"),(110,110))
        plus = pygame.transform.scale(pygame.image.load("images/boutton_plus.png"), (40,26))
        plus_rect = plus.get_rect()
        plus_rect.topleft = (screen_width-150, screen_height-75)
        moins = pygame.transform.scale(pygame.image.load("images/boutton_moins.png"), (40,26))
        moins_rect = moins.get_rect()
        moins_rect.topleft = (screen_width -150, screen_height - 75 + 26)
        vie_img = pygame.transform.scale(pygame.image.load("images/vie.png"), (45, 45))
        vie = font.render(str(self.player.get_life()), True, (255,255,255))
        barillet = pygame.transform.scale(pygame.image.load("images/barillet/barillet0.png"),(110,110))
        plus = pygame.transform.scale(pygame.image.load("images/boutton_plus.png"), (40,26))
        plus_rect = plus.get_rect()
        plus_rect.topleft = (screen_width-150, screen_height-75)
        moins = pygame.transform.scale(pygame.image.load("images/boutton_moins.png"), (40,26))
        moins_rect = moins.get_rect()
        moins_rect.topleft = (screen_width -150, screen_height - 75 + 26)
        clock = pygame.time.Clock()
        running = True
        self.screen.fill((0, 0, 0))
        nb_balle = 0
        t_barillet = 6
        pygame.display.flip()
        while running:
            self.player.save_location()
            self.input_pressed()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            self.screen.blit(money_img, (screen_width - 75, 25))
            self.screen.blit(money, (screen_width - 60, 35))
            self.screen.blit(vie_img, (screen_width - 75, 70))
            self.screen.blit(vie, (screen_width - 60, 80))
            self.screen.blit(plus, plus_rect)
            self.screen.blit(moins, moins_rect)
            self.screen.blit(barillet, (screen_width -110,screen_height - 110))
            self.screen.blit(vie_img, (screen_width - 75, 70))
            self.screen.blit(vie, (screen_width - 60, 80))
            self.screen.blit(plus, plus_rect)
            self.screen.blit(moins, moins_rect)
            self.screen.blit(barillet, (screen_width -110,screen_height - 110))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if plus_rect.collidepoint(event.pos):
                        if nb_balle < t_barillet :
                            print("+1")
                            nb_balle += 1
                            barillet = pygame.transform.scale(pygame.image.load(f"images/barillet/barillet{nb_balle}.png"),(110,110))
                    elif moins_rect.collidepoint(event.pos):
                        if nb_balle > 0 :
                            print("-1")
                            nb_balle -= 1
                            barillet = pygame.transform.scale(pygame.image.load(f"images/barillet/barillet{nb_balle}.png"),(110,110)) 
                    else :
                        self.roulette(nb_balle,t_barillet)
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if plus_rect.collidepoint(event.pos):
                        if nb_balle < t_barillet :
                            print("+1")
                            nb_balle += 1
                            barillet = pygame.transform.scale(pygame.image.load(f"images/barillet/barillet{nb_balle}.png"),(110,110))
                    elif moins_rect.collidepoint(event.pos):
                        if nb_balle > 0 :
                            print("-1")
                            nb_balle -= 1
                            barillet = pygame.transform.scale(pygame.image.load(f"images/barillet/barillet{nb_balle}.png"),(110,110)) 
                    else :
                        self.roulette(nb_balle,t_barillet)

    def roulette(self, nb_balle,chance):
         if random.randint(1,chance)> nb_balle:
              self.mouvement += nb_balle
         else:
              self.player.set_life(self.player.get_life() - 10)


#Crée un objet Game et lance la partie
def start(screen, matrix):
        game = Game(screen, matrix)
        game.run()
        global start
        start = time.monotonic()
