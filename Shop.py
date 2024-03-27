import pygame
from math import *

def s_inv(inv, phase_shop):

  pressed = pygame.key.get_pressed()

  #Afficher décor 
  quitter = False
  while quitter == False:
    if phase_shop == 0:
      statut_barillet = "sold"
      while quitter == False:
        if inv[0] == 0: 
          #Afficher l'article [barillet]
          statut_barillet = "dispo"
          #Afficher l'article [barillet]
        #Afficher bouton quitter
        for key in [pygame.K_ENTER, pygame.K_ONE, pygame.K_a]:
            if key == pygame.K_ONE:
              if statut_barillet == "dispo":
                if inv[3] >= 40:
                  inv[0] = 1
                  inv[3] = inv[3]-40
                  statut_barillet = "sold"
                  print("vendu")
            if key == pygame.K_ENTER:
              quitter = True  


  #Enlever le decor
  return inv

