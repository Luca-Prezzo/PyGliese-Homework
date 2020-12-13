import pygame
from pygame.locals import *
import pygame.freetype
import livello1




# init
pygame.init()




# salvo per comodità larghezza e lunghezza della finestra
screen_width = 900
screen_height = 570




# creo finestra
screen = pygame.display.set_mode((screen_width,screen_height))#, pygame.FULLSCREEN)




#nomino la finestra
pygame.display.set_caption("PyGliese - A Unical Story")




# gestisco loop
running = True




# carico l'immagine del titolo
title = pygame.image.load("sprite/title2.png")
title_width = 494
title_height = 178




#carico bg
bg = pygame.image.load("sprite/unical_bg.png")




# carico il menu
play = pygame.image.load("sprite/play.png")
options = pygame.image.load("sprite/opzioni.png")
quit = pygame.image.load("sprite/quit.png")




# riempio di nero il bg
screen.fill((0,0,0))




# visualizzo la foto in posizione e aggiorno con flip
screen.blit(bg,(0,0))




# visualizzo il menu
screen.blit(play,(378,277))
screen.blit(options,(378,364))
screen.blit(quit,(378,450))




# visualizzo il titolo
screen.blit(title,(202,45))
pygame.display.flip()





# creo il main loop
while running:

    # gestisco gli eventi
    for event in pygame.event.get():
        

        # ottengo la posizione del cursore
        mouse_pos = pygame.mouse.get_pos()

        # se la x e la y sono comprese nella x e y del bottone:
        if mouse_pos[0] >= 383 and mouse_pos[0] <= 518 and mouse_pos[1] <= 342 and mouse_pos[1] >= 280:
            if event.type == pygame.MOUSEBUTTONDOWN:
                livello1.lv1()
   

        if mouse_pos[0] >= 383 and mouse_pos[0] <= 518 and mouse_pos[1] <= 426 and mouse_pos[1] >= 369:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("OPZIONI")

        if mouse_pos[0] >= 383 and mouse_pos[0] <= 518 and mouse_pos[1] <= 518 and mouse_pos[1] >= 452:
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False



        # OBBLIGATORIO >>> gestire un'escape
        if event.type == pygame.QUIT:
            running = False
        
        # Se premo esc chiudi 
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False





# Chiudo tutto            
pygame.quit()