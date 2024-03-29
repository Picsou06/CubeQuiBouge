import pygame
from math import *
import time


def s_inv(screen, player): #inv = [phase_barillet, armure, shield, champi_r, champi_v, Fer a cheval, Trèfle, Popo de Vie]
  inv = player.get_inventory()
  running = True
  
  font = pygame.font.SysFont('bold', 30)
  vie_img = pygame.transform.scale(pygame.image.load("images/vie.png"), (45, 45))
  screen_width, screen_height = screen.get_size()
  base = pygame.transform.scale(pygame.image.load("images/Shop/sprite_01.png"), (550, 500))
  rect_base = base.get_rect()
  rect_base.center = (screen_width/2,screen_height/2)
  champi_r = pygame.transform.scale(pygame.image.load("images/Shop/sprite_02.png"), (550, 500))
  rect_champ_r = pygame.Rect(rect_base.left+324,rect_base.top+98,24,20)
  champi_v = pygame.transform.scale(pygame.image.load("images/Shop/sprite_03.png"), (550, 500))
  rect_champ_v = pygame.Rect(rect_base.left+354,rect_base.top+98,24,20)
  portal_gun = pygame.transform.scale(pygame.image.load("images/Shop/sprite_04.png"), (550, 500))
  barillet = pygame.transform.scale(pygame.image.load("images/Shop/sprite_05.png"), (550, 500))
  rect_barillet = pygame.Rect(rect_base.left+262,rect_base.top+88,54,30)
  trefle = pygame.transform.scale(pygame.image.load("images/Shop/sprite_06.png"), (550, 500))
  rect_trefle = pygame.Rect(rect_base.left+246,rect_base.top+98,16,20)
  popo_de_vie = pygame.transform.scale(pygame.image.load("images/Shop/sprite_07.png"), (550, 500))
  rect_popo_vie = pygame.Rect(rect_base.left+218,rect_base.top+74,22,44)
  sabre_laser = pygame.transform.scale(pygame.image.load("images/Shop/sprite_08.png"), (550, 500))
  triforce = pygame.transform.scale(pygame.image.load("images/Shop/sprite_09.png"), (550, 500))
  Rick = pygame.transform.scale(pygame.image.load("images/Shop/sprite_10.png"), (550, 500))
  Nyan = pygame.transform.scale(pygame.image.load("images/Shop/sprite_11.png"), (550, 500))
  Armure = pygame.transform.scale(pygame.image.load("images/Shop/sprite_12.png"), (550, 500))
  rect_armure = pygame.Rect(rect_base.left+120,rect_base.top+180,24,54) 
  bocal = pygame.transform.scale(pygame.image.load("images/Shop/sprite_13.png"), (550, 500))
  shield = pygame.transform.scale(pygame.image.load("images/Shop/sprite_14.png"), (550, 500))
  rect_shield = pygame.Rect(rect_base.left+366,rect_base.top+174,60,60)
  fer_cheval = pygame.transform.scale(pygame.image.load("images/Shop/sprite_15.png"), (550, 500))
  rect_fer_cheval = pygame.Rect(rect_base.left+434,rect_base.top+212,34,22)
  leave = pygame.transform.scale(pygame.image.load("images/quitter.png"), (45,45))
  rect_leave = pygame.Rect(rect_base.left,rect_base.top,45,45)
  money_img = pygame.transform.scale(pygame.image.load("images/money.png"), (45, 45))
  notmoney_img = pygame.transform.scale(pygame.image.load("images/notmoney.png"), (45, 45))
  lst_prix = [40,60,20,15,130,60,40,30]
  statut_armure="sold"
  statut_barillet="sold"
  statut_champi_r="sold"
  statut_champi_v="sold"
  statut_shield="sold"
  statut_fer_a_cheval="sold"
  statut_trefle="sold"
  statut_popo_de_vie="sold"  
  
  while running:
      money = font.render(str(player.get_money()), True, (255, 255, 255))
      vie = font.render(str(player.get_life()), True, (255,255,255))
      screen.fill((48,46,55))
      screen.blit(base, rect_base)
      screen.blit(portal_gun, rect_base)
      screen.blit(bocal, rect_base)
      screen.blit(Rick, rect_base)
      screen.blit(Nyan, rect_base)
      screen.blit(triforce, rect_base)
      screen.blit(sabre_laser, rect_base)
      screen.blit(leave, rect_base)
      screen.blit(money_img, (screen_width - 75, 25))
      screen.blit(money, (screen_width - 65, 35))
      screen.blit(vie_img, (screen_width - 75, 70))
      screen.blit(vie, (screen_width - 70, 80))
      if inv[0] == 0:
        #Barillet 9 places
        statut_barillet = "dispo"
        screen.blit(barillet, rect_base)
      if inv[1] == 0: 
        #Armure
        statut_armure = "dispo"
        screen.blit(Armure, rect_base)
      if inv[2] == 0: 
        #Shield
        statut_shield = "dispo"
        screen.blit(shield, rect_base)
      if inv[3] == 0: 
        #Champi_r
        statut_champi_r = "dispo"
        screen.blit(champi_r, rect_base)
      if inv[4] == 0: 
        #Champi_v
        statut_champi_v = "dispo"
        screen.blit(champi_v, rect_base)
      if inv[5] == 0: 
        #Fer à cheval
        statut_fer_a_cheval = "dispo"
        screen.blit(fer_cheval, rect_base)
      if inv[6] == 0: 
        #Trèfle
        statut_trefle = "dispo"
        screen.blit(trefle,rect_base)
      if inv[7] == 0: 
        #Trèfle
        statut_popo_de_vie = "dispo"
        screen.blit(popo_de_vie,rect_base)
      
      for event in pygame.event.get():
              if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_barillet.collidepoint(event.pos):
                  if statut_barillet == "dispo":
                    if player.get_money() >= 40:
                      inv[0] = 1
                      player.set_money(player.get_money() - 40) 
                      statut_barillet = "sold"
                    else:
                       screen.blit(notmoney_img, pygame.mouse.get_pos())
                       screen.blit(font.render(str(40), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
                       pygame.display.flip()
                       time.sleep(0.2)
                if rect_armure.collidepoint(event.pos):
                  if statut_armure == "dispo":
                    if player.get_money() >= 60:
                      inv[1] = 1
                      player.set_money(player.get_money() - 60)
                      statut_armure = "sold"
                    else:
                       screen.blit(notmoney_img, pygame.mouse.get_pos())
                       screen.blit(font.render(str(60), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
                       pygame.display.flip()
                       time.sleep(0.2)

              
                if rect_shield.collidepoint(event.pos):
                    if statut_shield == "dispo":
                      if player.get_money() >= 20:
                        inv[2] = 1
                        player.set_money(player.get_money() - 20)
                        statut_shield = "sold"
                      else:
                       screen.blit(notmoney_img, pygame.mouse.get_pos())
                       screen.blit(font.render(str(20), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
                       pygame.display.flip()
                       time.sleep(0.2)

                if rect_champ_r.collidepoint(event.pos):
                    if statut_champi_r == "dispo":
                      if player.get_money() >= 15:
                        player.set_money(player.get_money() - 15)
                        player.set_life(player.get_life()+5)
                      else:
                       screen.blit(notmoney_img, pygame.mouse.get_pos())
                       screen.blit(font.render(str(15), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
                       pygame.display.flip()
                       time.sleep(0.2)

                if rect_champ_v.collidepoint(event.pos):
                  if statut_champi_v == "dispo":
                    if player.get_money() >= 130:
                      inv[4] = 1
                      player.set_money(player.get_money()-130)
                      statut_champi_v = "sold"
                    else:
                       screen.blit(notmoney_img, pygame.mouse.get_pos())
                       screen.blit(font.render(str(130), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
                       pygame.display.flip()
                       time.sleep(0.2)

                if rect_fer_cheval.collidepoint(event.pos):
                  if statut_fer_a_cheval == "dispo":
                    if player.get_money() >= 60:
                      inv[5] = 1
                      player.set_money(player.get_money()-60)
                      statut_fer_a_cheval = "sold"
                      player.add_chance(2)
                    else:
                       screen.blit(notmoney_img, pygame.mouse.get_pos())
                       screen.blit(font.render(str(60), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
                       pygame.display.flip()
                       time.sleep(0.2)

                if rect_trefle.collidepoint(event.pos):
                  if statut_trefle == "dispo":
                    if player.get_money() >= 40:
                      inv[6] = 1
                      player.set_money(player.get_money()-40)
                      statut_trefle = "sold"
                      player.add_chance(1)
                    else:
                       screen.blit(notmoney_img, pygame.mouse.get_pos())
                       screen.blit(font.render(str(40), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
                       pygame.display.flip()
                       time.sleep(0.2)

                if rect_popo_vie.collidepoint(event.pos):
                  if statut_popo_de_vie == "dispo":
                    if player.get_money() >= 30:
                      player.set_money(player.get_money()-30)
                      player.set_life(player.get_life()+10)
                    else:
                       screen.blit(notmoney_img, pygame.mouse.get_pos())
                       screen.blit(font.render(str(30), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
                       pygame.display.flip()
                       time.sleep(0.2)

                if event.type == pygame.QUIT:
                  running = False
                  pygame.quit()
                  exit()

                if rect_leave.collidepoint(event.pos):
                  return inv
      if rect_barillet.collidepoint(pygame.mouse.get_pos()):
            if statut_barillet == "dispo":
                  screen.blit(money_img, pygame.mouse.get_pos())
                  screen.blit(font.render(str(lst_prix[0]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
      if rect_armure.collidepoint(pygame.mouse.get_pos()):
            if statut_armure == "dispo":
                screen.blit(money_img, pygame.mouse.get_pos())
                screen.blit(font.render(str(lst_prix[1]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
      if rect_shield.collidepoint(pygame.mouse.get_pos()):
            if statut_shield == "dispo":
                screen.blit(money_img, pygame.mouse.get_pos())
                screen.blit(font.render(str(lst_prix[2]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
      if rect_champ_r.collidepoint(pygame.mouse.get_pos()):
            if statut_champi_r == "dispo":
                screen.blit(money_img, pygame.mouse.get_pos())
                screen.blit(font.render(str(lst_prix[3]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
      if rect_champ_v.collidepoint(pygame.mouse.get_pos()):
            if statut_champi_v == "dispo":
                screen.blit(money_img, pygame.mouse.get_pos())
                screen.blit(font.render(str(lst_prix[4]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
      if rect_fer_cheval.collidepoint(pygame.mouse.get_pos()):
            if statut_fer_a_cheval == "dispo":
                screen.blit(money_img, pygame.mouse.get_pos())
                screen.blit(font.render(str(lst_prix[5]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
      if rect_trefle.collidepoint(pygame.mouse.get_pos()):
            if statut_trefle == "dispo":
                screen.blit(money_img, pygame.mouse.get_pos())
                screen.blit(font.render(str(lst_prix[6]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
      if rect_popo_vie.collidepoint(pygame.mouse.get_pos()):
            if statut_popo_de_vie == "dispo":
                screen.blit(money_img, pygame.mouse.get_pos())
                screen.blit(font.render(str(lst_prix[7]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
      pygame.display.flip()              

