import pygame

def win(screen,time):
    screen_width, screen_height = screen.get_size()
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
        #Affichages
    

        screen.blit(fin, fin_rect)
        screen.blit(time_txt, time_rect)
        pygame.display.flip()

def lose(screen,time):
    screen_width, screen_height = screen.get_size()
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
        #Affichages
        
        
        screen.blit(perdu, perdu_rect)
        screen.blit(time_txt, time_rect)
        pygame.display.flip()