import pygame
import os
import mazescan
import game
import random

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
maze = {}

maze_files = [f for f in os.listdir('images/MAZE') if f.endswith('.png')]

for i, f in enumerate(maze_files):
    maze_path = os.path.join('images/MAZE', f)
    maze[i] = mazescan.scan(maze_path)

screen_width, screen_heidth = screen.get_size()
pygame.display.set_caption("Cubequibouge")
leave = pygame.transform.scale(pygame.image.load("images/quitter.png"), (45,45))
background = pygame.transform.scale(pygame.image.load("images/lobby (Dall-E).png"), (screen_width,screen_heidth))
play = pygame.transform.scale(pygame.image.load("images/play.png"), (200,150))
mouse=pygame.mouse.get_pos()

running=True
while running:
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if screen_width-75 <= mouse[0] <= screen_width-30 and 25 <= mouse[1] <= 60:
                    pygame.quit()
                    exit()
                elif screen_width/2-100 <= mouse[0] <= screen_width/2+100 and (screen_heidth/3)*2 <= mouse[1] <= (screen_heidth/3)*2+150:
                     print(maze[random.randint(0,len(maze)-1)])
                     game.start(screen, maze[random.randint(0,len(maze)-1)])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen_width-75 <= mouse[0] <= screen_width-30 and 25 <= mouse[1] <= 60:
                    leave = pygame.transform.scale(pygame.image.load("images/quitter.png"), (45,45))
                elif screen_width/2-100 <= mouse[0] <= screen_width/2+100 and (screen_heidth/3)*2 <= mouse[1] <= (screen_heidth/3)*2+150:
                     play = pygame.transform.scale(pygame.image.load("images/play_off.png"), (200,150))
    screen.blit(background, (0, 0))
    screen.blit(leave, (screen_width-75, 25))
    screen.blit(play, (screen_width/2-100, (screen_heidth/3)*2))
    mouse=pygame.mouse.get_pos()
    pygame.display.flip()