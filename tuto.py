import pygame
def tuto(screen):
        SCREEN_HEIGHT,SCREEN_WIDTH = screen.get_size()
        #Chargement des images de boutons & fond de la page d'accueil
        play = pygame.transform.scale(pygame.image.load("images/play.png"), (200,150))
        shop = pygame.transform.scale(pygame.image.load("images/shop.png"), (150,100))

        #Créations de zones cliquables sous forme de Rect pour simplifier la gestion des collisions avec les images des boutons et régler leur position (en prenant le centre du rectangle)
        play_rect = play.get_rect()
        play_rect.topleft =(SCREEN_HEIGHT/2-100, (SCREEN_WIDTH/3)*2-70)
        play_rect.height=play_rect.height-50
        shop_rect = shop.get_rect()
        shop_rect.height=shop_rect.height
        shop_rect.center=(SCREEN_HEIGHT-100, (SCREEN_WIDTH/3)*2+80)
        font = pygame.font.SysFont('bold', 30)
        ZQSD=pygame.transform.scale(pygame.image.load("images/ZQSD.png"), (150,100))
        fleche=pygame.transform.scale(pygame.image.load("images/fleche.png"), (150,100))
        A=pygame.transform.scale(pygame.image.load("images/A.png"), (50,50))
        click=pygame.transform.scale(pygame.image.load("images/click_souris.png"), (50,50))
        ajouter=pygame.transform.scale(pygame.image.load("images/boutton_plus.png"), (40,26))
        enlever=pygame.transform.scale(pygame.image.load("images/boutton_moins.png"), (40,26))

        ###Boucle principale
        running = True
        while running:
                leave = pygame.transform.scale(pygame.image.load("images/quitter.png"), (45,45))
                rect_leave = pygame.Rect(screen.get_rect().left,screen.get_rect().top,45,45)
                #Récupération des évènements
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                running = False
                                pygame.quit()
                                exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if rect_leave.collidepoint(event.pos):
                                                        return None
                                        if shop_rect.collidepoint(event.pos):
                                                shop_tuto(screen)

                #Affichages
                screen.fill((48,46,55))
                screen.blit(leave, rect_leave)
                screen.blit(shop, shop_rect)
                screen.blit(font.render(str("Mouvements:"), True, (255, 255, 255)), (50,70))
                screen.blit(ZQSD, (50,100))
                screen.blit(fleche, (250,100))
                screen.blit(font.render(str("Ouvrir le shop:"), True, (255, 255, 255)), (50,210))
                screen.blit(A, (50,250))
                screen.blit(font.render(str("Fusil:"), True, (255, 255, 255)), (50,310))
                screen.blit(click, (50,340))
                screen.blit(font.render(str("Tirer"), True, (255, 255, 255)), (150,355))
                screen.blit(ajouter, (50,440))
                screen.blit(font.render(str("Ajouter une balle au barillet"), True, (255, 255, 255)), (150,440))
                screen.blit(enlever, (50,490))
                screen.blit(font.render(str("Enlever une balle du barillet"), True, (255, 255, 255)), (150,490))
                pygame.display.flip()

def shop_tuto(screen):
    running = True
    
    font = pygame.font.SysFont('bold', 30)

    lst_prix = [40,60,20,15,130,60,40,30]
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
    
    while running:
        screen.fill((48,46,55))
        screen.blit(base, rect_base)
        screen.blit(portal_gun, rect_base)
        screen.blit(bocal, rect_base)
        screen.blit(Rick, rect_base)
        screen.blit(Nyan, rect_base)
        screen.blit(triforce, rect_base)
        screen.blit(sabre_laser, rect_base)
        screen.blit(leave, rect_base)
        screen.blit(barillet, rect_base)
        screen.blit(Armure, rect_base)
        screen.blit(shield, rect_base)
        screen.blit(champi_r, rect_base)
        screen.blit(champi_v, rect_base)
        screen.blit(fer_cheval, rect_base)
        screen.blit(trefle,rect_base)
        screen.blit(popo_de_vie,rect_base)
        
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect_leave.collidepoint(event.pos):
                                        return None
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

                    
        if rect_barillet.collidepoint(pygame.mouse.get_pos()):
            screen.blit(font.render(str("Barillet 9 places"), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
            screen.blit(money_img, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] + 30))
            screen.blit(font.render(str(lst_prix[0]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 40))
        if rect_armure.collidepoint(pygame.mouse.get_pos()):
                screen.blit(money_img, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] + 30))
                screen.blit(font.render(str(lst_prix[1]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 40))
                screen.blit(font.render(str("Divise les dégats par deux"), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
        if rect_shield.collidepoint(pygame.mouse.get_pos()):
                screen.blit(money_img, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] + 30))
                screen.blit(font.render(str(lst_prix[2]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 40))
                screen.blit(font.render(str("Protège d'une balle"), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
        if rect_champ_r.collidepoint(pygame.mouse.get_pos()):
                screen.blit(money_img, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] + 30))
                screen.blit(font.render(str(lst_prix[3]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 40))
                screen.blit(font.render(str("Redonne 5 pv"), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
        if rect_champ_v.collidepoint(pygame.mouse.get_pos()):
                screen.blit(money_img, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] + 30))
                screen.blit(font.render(str(lst_prix[4]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 40))
                screen.blit(font.render(str("Permet de revenir a la vie"), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
        if rect_fer_cheval.collidepoint(pygame.mouse.get_pos()):
                screen.blit(money_img, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] + 30))
                screen.blit(font.render(str(lst_prix[5]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 40))
                screen.blit(font.render(str("Donne +2 en chance"), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
        if rect_trefle.collidepoint(pygame.mouse.get_pos()):
                screen.blit(money_img, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] + 30))
                screen.blit(font.render(str(lst_prix[6]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 40))
                screen.blit(font.render(str("Donne +1 en chance"), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
        if rect_popo_vie.collidepoint(pygame.mouse.get_pos()):
                screen.blit(money_img, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] + 30))
                screen.blit(font.render(str(lst_prix[7]), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 40))
                screen.blit(font.render(str("Redonne 10 pv"), True, (255, 255, 255)), (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10))
        pygame.display.flip()              

