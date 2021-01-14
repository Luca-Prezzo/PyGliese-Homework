import pygame
from pygame.locals import *


def tutorial():


    # init che permette tutto
    pygame.init()

    # Setto la finestra con dimensioni e titolo
    screen_width = 900
    screen_height = 570
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("PyGliese -- A Unical Story -- TUTORIAL")

    # Carico le immagini da utilizzare
    bg_title = pygame.image.load("sprite/asset/unical_bg.png")
    tutorial = [pygame.image.load("sprite/asset/tutorial1.png"),
                pygame.image.load("sprite/asset/tutorial2.png"),
                pygame.image.load("sprite/asset/tutorial3.png"),
                pygame.image.load("sprite/asset/tutorial4.png"),
                pygame.image.load("sprite/asset/tutorial5.png"),
                pygame.image.load("sprite/asset/tutorial6.png"),
                pygame.image.load("sprite/asset/tutorial7.png"),
                pygame.image.load("sprite/asset/tutorial8.png")]

    # inizializzo la pagina
    pagina = 0

    # blit mi permette di visualizzare con la sintassi blit("nome img caricata" , (x,y))
    screen.fill((0, 0, 0))
    screen.blit(bg_title, (0, 0))
    screen.blit(tutorial[pagina], (0, 0))

    # rendo effettive le modifiche e aggiorno la schermata
    pygame.display.flip()

    # Carico i suoni da utilizzare
    buttonsound = pygame.mixer.Sound("sprite/Sound/button.wav")

    # setto la condizione del main loop
    running = True

    # avvio il main loop
    while running:

        # Gestisco gli eventi
        for event in pygame.event.get():

            # se premo la crocetta chiudi tutto
            if event.type == pygame.QUIT:
                runnig = False

            # se premo esc chiude la finestra
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                # Se premo la freccia destra e il numero di pagina è minore di 7 vado alla prossima
                if event.key == K_RIGHT:
                    if pagina < 7:
                        buttonsound.play()
                        pagina += 1
                        screen.blit(tutorial[pagina], (0, 0))
                        pygame.display.flip()

                # Se il numero pagina è maggiore di 7 torno al menù
                    else:
                        running = False

                # Se premo la freccia sinistra e la pagina è compresa tra 0 e 7 allora vado alla precedente
                if event.key == K_LEFT:
                    if 0 < pagina < 7:
                        buttonsound.play()
                        pagina -= 1
                        screen.blit(tutorial[pagina], (0, 0))
                        pygame.display.flip()

