import pygame
from math import *



def s_inv(screen, player): #inv = [phase_barillet, armure, shield, champi_r, champi_v, Fer a cheval, Trèfle]
  inv = player.get_inventory()
  running = True

  screen_width, screen_height = screen.get_size()
  base = pygame.transform.scale(pygame.image.load("images/Shop/sprite_01.png"), (550, 500))
  rect_base = base.get_rect()
  rect_base.center = (screen_width/2,screen_height/2)
  champi_r = pygame.transform.scale(pygame.image.load("images/Shop/sprite_02.png"), (550, 500))
  rect_champ_r = pygame.Rect(rect_base.left+324,rect_base.top+98,24,20)
  money_img = pygame.transform.scale(pygame.image.load("images/money.png"), (45, 45))
  lst_prix = [40,60,20,15,130,60,40,30]
  font = pygame.font.SysFont('bold', 30)

  while running:
        if inv[3] == 0:
            #Champi_r
            statut_champi_r = "dispo"
            screen.blit(base, rect_base)
            screen.blit(champi_r, rect_base)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_champ_r.collidepoint(event.pos):
                    if statut_champi_r == "dispo":
                        if player.get_money() >= 5:
                            inv[3] = 1
                            player.set_money(player.get_money() - 5)
                            statut_champi_r = "sold"
                            print("champi rouge vendu")
        if rect_champ_r.collidepoint(pygame.mouse.get_pos()):
            if statut_champi_r == "dispo":
                screen.blit(money_img, pygame.mouse.get_pos())
                screen.blit(font.render(str(lst_prix[3]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))

        pygame.draw.rect(screen, (100,100,100), rect_champ_r)
        pygame.display.flip()
                

