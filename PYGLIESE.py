import pygame
import sys
from pygame.locals import *
import LIVELLI
import TUTORIAL


def menu():


    # init che permette tutto
    pygame.init()
    
    # Setto la finestra con dimensioni e titolo
    screen_width = 900
    screen_height = 570
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("PyGliese -- A Unical Story")

    # Carico le immagini da utilizzare
    title = pygame.image.load("sprite/asset/title.png")
    bg_title = pygame.image.load("sprite/asset/unical_bg.png")
    play = pygame.image.load("sprite/button/play.png")
    tutorial = pygame.image.load("sprite/button/tutorial.png")
    esci = pygame.image.load("sprite/button/quit.png")

    # blit mi permette di visualizzare con la sintassi blit("nome img caricata" , (x,y))
    screen.fill((0, 0, 0))
    screen.blit(bg_title, (0, 0))
    screen.blit(play, (371, 277))
    screen.blit(tutorial, (371, 364))
    screen.blit(esci, (371, 450))
    screen.blit(title, (202, 45))
    
    # Carico i suoni
    menusound = pygame.mixer.Sound("sprite/Sound/menu.wav")
    buttonsound = pygame.mixer.Sound("sprite/Sound/button.wav")

    # il -1 mi permette di mandare in loop il suono
    menusound.play(-1)

    # rendo effettive le modifiche e aggiorno lo schermo
    pygame.display.flip()

    # setto la condizione del main loop
    running = True

    # avvio il main loop
    while running:

        # gestisco gli eventi
        for event in pygame.event.get():

            # ottengo la posizione del mouse
            mouse_pos = pygame.mouse.get_pos()

            # se la posizione del mause combacia con quella del primo bottone e premo, allora fai partire i livelli
            if 529 >= mouse_pos[0] >= 373 and 346 >= mouse_pos[1] >= 278:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttonsound.play()
                    menusound.stop()
                    LIVELLI.livello1()
                    sys.exit()

            # se la posizione del mause combacia con quella del primo bottone e premo, allora fai partire il tutorial
            if 529 >= mouse_pos[0] >= 373 and mouse_pos[1] <= 426 and mouse_pos[1] >= 369:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttonsound.play()
                    TUTORIAL.tutorial()
                    menusound.stop()
                    menu()

            # se la posizione del mause combacia con quella del primo bottone e premo, allora esci
            if 373 <= mouse_pos[0] <= 529 >= mouse_pos[1] >= 452:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttonsound.play()
                    sys.exit()

            # se premo la crocetta chiudi tutto
            if event.type == pygame.QUIT:
                sys.exit()

            # se premo esc chiude la finestra
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()


menu()
