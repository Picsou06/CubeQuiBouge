### BIBLIOTHEQUES & MODULES
import pygame
import os
import mazescan
import game


### Initialisation de la fenêtre pygame
pygame.init()
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH),pygame.NOFRAME)
pygame.display.set_caption("Cubequibouge")

###Chargement des ressources

#Chargement des images de labyrinthes
maze_files = [f for f in os.listdir('images/MAZE') if f.endswith('.png')]

#Range les chemins d'accès dans une liste maze
maze = {}
for i, f in enumerate(maze_files):
    maze_path = os.path.join('images/MAZE', f)
    maze[i] = mazescan.scan(maze_path)

mazescan.create_xml_file(maze[1])

#Chargement des images de boutons & fond de la page d'accueil
leave = pygame.transform.scale(pygame.image.load("images/quitter.png"), (45,45))
background = pygame.transform.scale(pygame.image.load("images/lobby (Dall-E).png"), screen.get_size())
play = pygame.transform.scale(pygame.image.load("images/play.png"), (200,150))


#Créations de zones cliquables sous forme de Rect pour simplifier la gestion des collisions avec les images des boutons et régler leur position (en prenant le centre du rectangle)
leave_rect = leave.get_rect()
leave_rect.topleft = (SCREEN_HEIGHT-75, 25)
play_rect = play.get_rect()
play_rect.topleft =(SCREEN_HEIGHT/2-100, (SCREEN_WIDTH/3)*2)

###Boucle principale
running = True
while running:
    #Récupération des évènements
    for event in pygame.event.get():
        #on récupère les clics de la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            #collisions avec les rectangles
            if leave_rect.collidepoint(event.pos):
                leave = pygame.transform.scale(pygame.image.load("images/quitter.png"), (45,45))
                #sortie de la boucle
                running = False

            elif play_rect.collidepoint(event.pos):
                play = pygame.transform.scale(pygame.image.load("images/play_off.png"), (200,150))
                running = False
                #lancement du jeu
                game.start(screen, maze[1])

    #Affichages
    screen.blit(background, (0, 0))
    screen.blit(leave, leave_rect)
    screen.blit(play, play_rect)
    pygame.display.flip()

#fermeture de pygame
pygame.quit()