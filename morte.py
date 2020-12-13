import pygame
from pygame.locals import *

def morte():
    screen_width = 900
    screen_height = 570
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill((0,0,0))
    pygame.display.update()
    pygame.init()
    bg = pygame.image.load("sprite/skybg.png")
    diescreen = pygame.image.load("sprite/die_screen.png")
    screen.blit(bg,(0,0))
    running = True
    screen.blit(bg,(0,0))
    pygame.display.update()
    personaggio_x = 70
    personaggio_y = 100


    while running:
    
    
        screen.blit(bg,(0,0))
        personaggio = pygame.draw.rect(screen, (255,0,0),pygame.Rect(personaggio_x,personaggio_y,40,60))

        if personaggio_y >= (screen_height-60):
            print("morto")
            screen.blit(diescreen,(186,112))
            pygame.display.flip()
        else:
            personaggio_y += 1

        pygame.display.flip()
        pygame.display.update()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
    

    
    pygame.quit()