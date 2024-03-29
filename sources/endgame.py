import pygame
import random
import mazescan
import game
import os


def win(screen,time):
    screen_width, screen_height = screen.get_size()
    ###Chargement des ressources

    #Chargement des images de labyrinthes
    maze_files = [f for f in os.listdir('images/MAZE') if f.endswith('.png')]

    #Range les chemins d'accès dans une liste maze
    maze = {}
    for i, f in enumerate(maze_files):
        maze_path = os.path.join('images/MAZE', f)
        maze[i] = mazescan.scan(maze_path)

    mazemap=maze[random.randint(0,len(maze)-1)]
    mazescan.create_xml_file(mazemap)
    newgame = pygame.transform.scale(pygame.image.load("images/newgame.png"), (200,150))
    new_rect = newgame.get_rect()
    new_rect.center =((screen_height/3)*2, (screen_width/2))
    font = pygame.font.SysFont('bold', 60)
    fin = font.render('WIN', True, (255, 255, 255))
    fin_rect = fin.get_rect()
    fin_rect.center = ((screen_width/2) -10,screen_width/4)
    font = pygame.font.SysFont('bold', 40)
    time_txt = font.render("Tu as fini en : "+str(time), True, (255,255,255))
    time_rect = time_txt.get_rect()
    time_rect.center = (screen_width/2,screen_height/2)
    ###Boucle principale
    running = True
    while running:
        #Récupération des évènements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_rect.collidepoint(event.pos):
                    running = False
                    #lancement du jeu
                    game.start(screen, mazemap)
    

        screen.blit(fin, fin_rect)
        screen.blit(newgame, new_rect)
        screen.blit(time_txt, time_rect)
        pygame.display.flip()

def lose(screen,time):
    screen_width, screen_height = screen.get_size()
    ###Chargement des ressources

    #Chargement des images de labyrinthes
    maze_files = [f for f in os.listdir('images/MAZE') if f.endswith('.png')]

    #Range les chemins d'accès dans une liste maze
    maze = {}
    for i, f in enumerate(maze_files):
        maze_path = os.path.join('images/MAZE', f)
        maze[i] = mazescan.scan(maze_path)

    mazemap=maze[random.randint(0,len(maze)-1)]
    mazescan.create_xml_file(mazemap)
    newgame = pygame.transform.scale(pygame.image.load("images/newgame.png"), (200,150))
    new_rect = newgame.get_rect()
    new_rect.center =((screen_height/3)*2, (screen_width/2))
    font = pygame.font.SysFont('bold', 60)
    perdu = font.render('PERDU', True, (255, 255, 255))
    perdu_rect = perdu.get_rect()
    perdu_rect.center = ((screen_width/2)-10,screen_width/4)
    font = pygame.font.SysFont('bold', 40)
    time_txt = font.render("Tu as perdu en : "+str(time), True, (255,255,255))
    time_rect = time_txt.get_rect()
    time_rect.center = (screen_width/2,screen_height/2)
    
    ###Boucle principale
    running = True
    while running:
        #Récupération des évènements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_rect.collidepoint(event.pos):
                    running = False
                    #lancement du jeu
                    game.start(screen, mazemap)
        #Affichages
        
        
        screen.blit(perdu, perdu_rect)
        screen.blit(newgame, new_rect)
        screen.blit(time_txt, time_rect)
        pygame.display.flip()