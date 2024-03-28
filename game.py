### BIBLIOTHEQUES & MODULES
import pygame
import pytmx
import pyscroll
import random
import player
import mazescan
import time
import endgame
import threading
import time
import Shop

start=0

### CLASSE
class Game:
    def __init__(self, screen, matrix, pos = False):
        if not pos:
            self.previous_key_state = {}
            self.screen = screen
            self.mouvement = 24
            self.matrix = matrix

        # Charger la carte
        self.timer_in_live=True
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
            self.player.set_life(80)
            self.player.set_money(0)
            self.player.set_chance(1) 
            self.player.set_inventory([0, 0, 0, 0, 0, 0, 0, 0])
        #Ajout du joueur au group de sprite de la map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)
    def input_pressed(self):
        pressed = pygame.key.get_pressed()
        # Boucle sur toutes les touches surveillées
        for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_ESCAPE, pygame.K_s]:
            # Vérifie si la touche est enfoncée et si elle était relâchée précédemment
            if pressed[key] and not self.previous_key_state.get(key, False):
                if key == pygame.K_ESCAPE:
                        if self.timer_in_live:
                            self.timer_in_live=False
                            GRAY_TRANSPARENT = (100, 100, 100, 128)
                            timer.pause()
                            pause_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
                            pause_surface.fill(GRAY_TRANSPARENT)
                            self.screen.blit(pause_surface, (0, 0))
                            font = pygame.font.SysFont('bold', 64)
                            text_surface = font.render("PAUSE", True, (255, 255, 255))
                            self.screen.blit(text_surface, ((screen_width - text_surface.get_width()) // 2, (screen_height - text_surface.get_height()) // 2))
                            pygame.display.flip()
                            while not self.timer_in_live:
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        self.timer_in_live=True
                                    if event.type == pygame.QUIT:
                                        running = False
                                        pygame.quit()
                                        exit()
                            timer.start()
                if key == pygame.K_s:
                    timer.pause()
                    Shop.s_inv(self.screen, self.player)
                    timer.resume()
                    if self.player.get_inventory()[0]==1:
                        global t_barillet, barillet, nb_balle
                        t_barillet=9
                        barillet = pygame.transform.scale(pygame.image.load("images/barillet/big_barillet0.png"), (110, 110))
                if self.mouvement > 0:
                    # Effectue le mouvement correspondant à la touche pressée
                    if key == pygame.K_UP:
                        self.player.move_up()
                        self.mouvement -= 1
                    elif key == pygame.K_DOWN:
                        self.player.move_down()
                        self.mouvement -= 1
                    elif key == pygame.K_RIGHT:
                        self.player.move_right()
                        self.mouvement -= 1
                    elif key == pygame.K_LEFT:
                        self.player.move_left()
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
                self.player.add_money(x)
                mazescan.create_xml_file(self.matrix)
                self.__init__(self.screen, self.matrix, self.player.get_location())
            if sprite.feet.collidelist(self.walls) > 0:
                sprite.move_back()
            elif sprite.feet.collidelist(self.end) == 0:
                endgame.win(self.screen, format_time(timer.get_elapsed_time()))


    def run(self):
        global screen_width, screen_height, barillet, t_barillet, nb_balle
        screen_width, screen_height = self.screen.get_size()
        money_img = pygame.transform.scale(pygame.image.load("images/money.png"), (45, 45))
        font = pygame.font.SysFont('bold', 30)
        shield_img = pygame.transform.scale(pygame.image.load("images/shild_on.png"), (45, 45))
        vie_img = pygame.transform.scale(pygame.image.load("images/vie.png"), (45, 45))
        barillet = pygame.transform.scale(pygame.image.load("images/barillet/barillet0.png"),(110,110))
        plus = pygame.transform.scale(pygame.image.load("images/boutton_plus.png"), (40,26))
        plus_rect = plus.get_rect()
        plus_rect.topleft = (screen_width-150, screen_height-75)
        moins = pygame.transform.scale(pygame.image.load("images/boutton_moins.png"), (40,26))
        moins_rect = moins.get_rect()
        moins_rect.topleft = (screen_width -150, screen_height - 75 + 26)
        running = True
        nb_balle = 0
        t_barillet = 6
        timer.start()
        pygame.display.flip()
        while running:
            money = font.render(str(self.player.get_money()), True, (255, 255, 255))
            vie = font.render(str(self.player.get_life()), True, (255,255,255))
            elapsed_time = format_time(timer.get_elapsed_time())  # Obtenez le temps écoulé
            if self.player.get_life() <= 0:
                if self.player.get_inventory()[3]==1:
                    self.player.set_life(40)
                    temp=self.player.get_inventory()
                    temp[3]==0
                    self.player.set_inventory
                else:
                    endgame.lose(self.screen, elapsed_time)
            self.player.save_location()
            self.input_pressed()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            self.screen.blit(money_img, (screen_width - 75, 25))
            if self.player.get_inventory()[2]==1:
                self.screen.blit(shield_img, (screen_width - 130, 25))
            self.screen.blit(money, (screen_width - 65, 35))
            self.screen.blit(vie_img, (screen_width - 75, 70))
            self.screen.blit(vie, (screen_width - 70, 80))
            self.screen.blit(plus, plus_rect)
            self.screen.blit(moins, moins_rect)
            self.screen.blit(barillet, (screen_width - 110, screen_height - 110))
            # Afficher le temps écoulé
            time_surface = font.render(elapsed_time, True, (255, 255, 255))
            self.screen.blit(time_surface, (10, 10))  # Positionnez le texte du temps écoulé
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.player.get_inventory()[0] == 0 :
                        if plus_rect.collidepoint(event.pos):
                            if nb_balle < 6:
                                nb_balle += 1
                                barillet = pygame.transform.scale(pygame.image.load(f"images/barillet/barillet{nb_balle}.png"), (110, 110))
                        elif moins_rect.collidepoint(event.pos):
                            if nb_balle > 0:
                                nb_balle -= 1
                                barillet = pygame.transform.scale(pygame.image.load(f"images/barillet/barillet{nb_balle}.png"), (110, 110))
                        else:
                            self.roulette(nb_balle, t_barillet)
                    else :
                        if plus_rect.collidepoint(event.pos):
                            if nb_balle < 9:
                                nb_balle += 1
                                barillet = pygame.transform.scale(pygame.image.load(f"images/barillet/big_barillet{nb_balle}.png"), (110, 110))
                        elif moins_rect.collidepoint(event.pos):
                            if nb_balle > 0:
                                nb_balle -= 1
                                barillet = pygame.transform.scale(pygame.image.load(f"images/barillet/big_barillet{nb_balle}.png"), (110, 110))
                        else:
                            self.roulette(nb_balle, t_barillet)


    def roulette(self, nb_balle,chance):
        if nb_balle!=0:
            if nb_balle - self.player.get_chance() > 0:
                if random.randint(1,chance) > nb_balle - self.player.get_chance():
                    self.mouvement += nb_balle
                    self.player.add_life(int((random.randint(1,nb_balle)*self.player.get_chance())/2))
                else:
                    self.player.set_damaged(random.randint(5,11-self.player.get_chance()))
                    RED_TRANSPARENT = (255, 0, 0, 150)
                    pause_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
                    pause_surface.fill(RED_TRANSPARENT)
                    self.screen.blit(pause_surface, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.2)

            else:
                if random.randint(1,chance) > 1:
                    self.mouvement += nb_balle
                    self.player.add_life(int((random.randint(1,nb_balle)*self.player.get_chance())/2))
                else: 
                    self.player.set_damaged(random.randint(5,11-self.player.get_chance()))
                    RED_TRANSPARENT = (255, 0, 0, 150)
                    pause_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
                    pause_surface.fill(RED_TRANSPARENT)
                    self.screen.blit(pause_surface, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.2)


class Timer:
    def __init__(self):
        self._start_time = False
        self._elapsed_time = 0
        self._timer_thread = None
        self._timer_is_running = False

    def _run_timer(self):
        while self._timer_is_running:
            if self._start_time is not None:
                self._elapsed_time = time.time() - self._start_time
            time.sleep(1)

    def start(self):
        if not self._timer_is_running:
            self._start_time = time.time() - self._elapsed_time
            self._timer_is_running = True
            self._timer_thread = threading.Thread(target=self._run_timer)
            self._timer_thread.start()

    def pause(self):
        if self._timer_is_running:
            self._timer_is_running = False

    def resume(self):
        if not self._timer_is_running:
            self._start_time = time.time() - self._elapsed_time
            self._timer_is_running = True

    def stop(self):
        self._timer_is_running = False
        self._start_time = None
        self._elapsed_time = 0

    def get_elapsed_time(self):
        return self._elapsed_time

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))



#Crée un objet Game et lance la partie
def start(screen, matrix):
        game = Game(screen, matrix)
        global timer
        timer = Timer()
        timer.start()
        game.run()