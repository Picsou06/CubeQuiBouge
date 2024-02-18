import pygame
import math
def summonbarrillet(screen,nb_balles):
    ball_image = pygame.transform.scale(pygame.image.load("images\Barillet Plein.png"), (100, 100))
    ball_radius = 25
    angle_step = 2 * math.pi / nb_balles
    center = (screen.get_width() // 2, screen.get_height() // 2)

    for i in range(nb_balles):
        angle = i * angle_step
        x = center[0] + ball_radius * math.cos(angle)
        y = center[1] + ball_radius * math.sin(angle)
        rotated_ball_image = pygame.transform.rotate(ball_image, i * 360 / nb_balles)
        screen.blit(rotated_ball_image, (x, y))

def start(screen,maze):
    screen_width, screen_heidth = screen.get_size()
    leave = pygame.transform.scale(pygame.image.load("images/quitter.png"), (45,45))
    background = pygame.transform.scale(pygame.image.load("images/lobby (Dall-E).png"), (screen_width,screen_heidth))
    play = pygame.transform.scale(pygame.image.load("images/play.png"), (200,150))
    
    mouse=pygame.mouse.get_pos()

    running=True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if screen_width-75 <= mouse[0] <= screen_width-30 and 25 <= mouse[1] <= 60:
                            pygame.quit()
                            exit()
        screen.blit(background, (0, 0))
        screen.blit(leave, (screen_width-75, 25))
        summonbarrillet(screen, 6)

        mouse=pygame.mouse.get_pos()
        pygame.display.flip()