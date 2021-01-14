import pygame
import sys
from pygame.locals import *
import random



def livello1():

    global walkCount
    pygame.init()

    # SETTING

    # finestra
    screen_width = 900
    screen_height = 570
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygliese - A Unical Story - Livello 1")

    clock = pygame.time.Clock()

    # personaggio
    personaggio_x = 70
    personaggio_y = 430
    ambiente_x = 0

    # movement
    spostamento = 2.5
    walkCount = 0
    isJump = False
    jumpCount = 10
    left = False
    right = False

    # sound
    deadsound = pygame.mixer.Sound("sprite/Sound/dead.wav")
    hurt = pygame.mixer.Sound("sprite/Sound/hurt.wav")
    playsound = pygame.mixer.Sound("sprite/Sound/theme.wav")
    playsound.play(-1)
    buttonsound = pygame.mixer.Sound("sprite/Sound/button.wav")
    winsound = pygame.mixer.Sound("sprite/Sound/win.wav")

    # Funzione redrawGameWindow che viene chiamata ogni volta che il loop termina un ciclo e con cui gestisco le animazioni di nuvole, movimento e ferita del personaggio
    def redrawGameWindow():
        global walkCount
        screen.blit(bg, (0, 0))
        screen.blit(ambiente, (ambiente_x, 0))

        screen.blit(nuvole, (nuvx, nuvy))
        screen.blit(nuvole, (nuvx2, nuvy2))

        if colpito:
            screen.blit(life[vite], (-130, 10))
        if walkCount + 1 >= 9:
            walkCount = 0
        if left:
            screen.blit(walkLeft[walkCount], (personaggio_x, personaggio_y))
            walkCount += 1
        elif right:
            screen.blit(walkRight[walkCount], (personaggio_x, personaggio_y))
            walkCount += 1
        else:
            screen.blit(personaggio, (personaggio_x, personaggio_y))
        pygame.display.update()

    # Funzione dead che viene richiamata ofni volta che il numero di vite arriva a 0
    def dead():
        deadsound.play()
        diescreen = pygame.image.load("sprite/asset/die_screen.png")
        play = pygame.image.load("sprite/button/play.png")
        quit = pygame.image.load("sprite/button/quit.png")
        screen.blit(diescreen, (185, 111))
        screen.blit(play, (259, 347))
        screen.blit(quit, (481, 347))
        pygame.display.update()
        scelta = False
        while not scelta:
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                # gestisco se viene premuto il tasto play o quit
                if 418 >= mouse_pos[0] >= 259 and 347 <= mouse_pos[1] <= 417:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        playsound.stop()
                        buttonsound.play()
                        livello1()
                if 640 >= mouse_pos[0] >= 481 and 347 <= mouse_pos[1] <= 417:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        buttonsound.play()
                        scelta = True

    # Funzione vittoria che viene chiamata quando il personaggio supera il bordo dello schermo
    def vittoria():
        playsound.stop()
        winsound.play()
        screen.blit(winscreen, (0, 0))
        pygame.display.update()
        scelta = False
        while not scelta:
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if 418 >= mouse_pos[0] >= 259 and 347 <= mouse_pos[1] <= 417:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        playsound.stop()
                        buttonsound.play()
                        scelta = True
                        livello2()
                if 640 >= mouse_pos[0] >= 481 and 347 <= mouse_pos[1] <= 417:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        buttonsound.play()
                        scelta = True

    # CARICO IMMAGINI
    bg = pygame.image.load("sprite/asset/sky_bg.png")
    personaggio = pygame.image.load("sprite/Character/standing.png")
    ambiente = pygame.image.load("sprite/asset/ambiente.png")
    nuvole = pygame.image.load("sprite/asset/nuvole.png")
    walkLeft = [pygame.image.load("sprite/Character/L1.png"),
                pygame.image.load("sprite/Character/L2.png"),
                pygame.image.load("sprite/Character/L3.png"),
                pygame.image.load("sprite/Character/L4.png"),
                pygame.image.load("sprite/Character/L5.png"),
                pygame.image.load("sprite/Character/L6.png"),
                pygame.image.load("sprite/Character/L7.png"),
                pygame.image.load("sprite/Character/L8.png"),
                pygame.image.load("sprite/Character/L9.png")]
    walkRight = [pygame.image.load("sprite/Character/R1.png"),
                 pygame.image.load("sprite/Character/R2.png"),
                 pygame.image.load("sprite/Character/R3.png"),
                 pygame.image.load("sprite/Character/R4.png"),
                 pygame.image.load("sprite/Character/R5.png"),
                 pygame.image.load("sprite/Character/R6.png"),
                 pygame.image.load("sprite/Character/R7.png"),
                 pygame.image.load("sprite/Character/R8.png"),
                 pygame.image.load("sprite/Character/R9.png")]
    winscreen = pygame.image.load("sprite/asset/winscreen.png")
    life = [pygame.image.load("sprite/asset/vite1.png"), pygame.image.load(
        "sprite/asset/vite2.png"), pygame.image.load("sprite/asset/vite3.png")]

    vite = 2
    screen.blit(life[vite], (-130, 10))
    pygame.display.update()
    colpito = True

    # setto il loop
    running = True
    # main loop

    nuvx = random.randint(0, 900)
    nuvy = random.randint(0, 40)
    nuvx2 = random.randint(0, 900)
    nuvy2 = random.randint(0, 40)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # se premo esc chiude la finestra
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

        keys = pygame.key.get_pressed()
        
        # se la x e la y del personaggio coincidono con la posizione delle spine allora tolgo una vita e faccio saltare il personaggio
        if (312 < personaggio_x < 350 or 525 <= personaggio_x <= 560) and 420 <= personaggio_y <= 490:
            if vite > 0:
                colpito = True
                isJump = True
                vite -= 1
                hurt.play()
            # se il personaggio non ha vite allora richiamo la funzione dead
            else:
                dead()
                sys.exit()

        if personaggio_x > 880:
            vittoria()

        if keys[K_LEFT] or keys[K_a] and personaggio_x > 0:
            personaggio_x -= spostamento
            left = True
            right = False

        elif keys[K_RIGHT] or keys[K_d]:
            personaggio_x += spostamento
            left = False
            right = True

        else:
            right = False
            left = False
            walkCount = 0

        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                right = False
                left = False
                walkCount = 0

        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                personaggio_y -= (jumpCount ** 2) * 0.3 * neg
                jumpCount -= 1

            else:
                isJump = False
                jumpCount = 10

        if personaggio_y <= 420 and not isJump:
            personaggio_y += 1



        # Creo due nuvole con posizione y casuale e ad ogni ciclo diminuisco la x di 1 finchè non escono dallo schermo
        nuvx -= 1
        nuvx2 -= 1
        if nuvx <= -210:
            nuvx = 900
            nuvy = random.randint(-100, 160)
        if nuvx2 <= -210:
            nuvx2 = 900 + random.randint(140, 400)
            nuvy2 = random.randint(-100, 120)

        redrawGameWindow()
        clock.tick(60)











def livello2():

    global walkCount
    pygame.init()

    # SETTING
    # finestra
    screen_width = 900
    screen_height = 570
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygliese - A Unical Story - Livello 1")

    clock = pygame.time.Clock()

    # personaggio
    personaggio_x = 70
    personaggio_y = 430
    ambiente_x = 0

    # movement
    spostamento = 2.5
    walkCount = 0
    isJump = False
    jumpCount = 10
    left = False
    right = False

    # sound
    deadsound = pygame.mixer.Sound("sprite/Sound/dead.wav")
    hurt = pygame.mixer.Sound("sprite/Sound/hurt.wav")
    playsound = pygame.mixer.Sound("sprite/Sound/theme.wav")
    playsound.play(-1)
    buttonsound = pygame.mixer.Sound("sprite/Sound/button.wav")
    winsound = pygame.mixer.Sound("sprite/Sound/win.wav")

    def redrawGameWindow():
        global walkCount
        screen.blit(bg, (0, 0))
        screen.blit(ambiente, (ambiente_x, 0))

        screen.blit(nuvole, (nuvx, nuvy))
        screen.blit(nuvole, (nuvx2, nuvy2))

        if colpito:
            screen.blit(life[vite], (-130, 10))
        if walkCount + 1 >= 9:
            walkCount = 0
        if left:
            screen.blit(walkLeft[walkCount], (personaggio_x, personaggio_y))
            walkCount += 1
        elif right:
            screen.blit(walkRight[walkCount], (personaggio_x, personaggio_y))
            walkCount += 1
        else:
            screen.blit(personaggio, (personaggio_x, personaggio_y))
        pygame.display.update()

    def dead():
        deadsound.play()
        diescreen = pygame.image.load("sprite/asset/die_screen.png")
        play = pygame.image.load("sprite/button/play.png")
        quit = pygame.image.load("sprite/button/quit.png")
        screen.blit(diescreen, (185, 111))
        screen.blit(play, (259, 347))
        screen.blit(quit, (481, 347))
        pygame.display.update()
        scelta = False
        while not scelta:
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if 418 >= mouse_pos[0] >= 259 and 347 <= mouse_pos[1] <= 417:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        playsound.stop()
                        buttonsound.play()
                        livello1()
                if 640 >= mouse_pos[0] >= 481 and 347 <= mouse_pos[1] <= 417:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        buttonsound.play()
                        scelta = True
                        sys.exit()

    def vittoria():
        playsound.stop()
        winsound.play()
        screen.blit(winscreen, (0, 0))
        pygame.display.update()
        scelta = False
        while not scelta:
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if 418 >= mouse_pos[0] >= 259 and 347 <= mouse_pos[1] <= 417:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        playsound.stop()
                        buttonsound.play()
                        scelta = True
                        livello3()
                if 640 >= mouse_pos[0] >= 481 and 347 <= mouse_pos[1] <= 417:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        buttonsound.play()
                        scelta = True

    # CARICO IMMAGINI
    bg = pygame.image.load("sprite/asset/sky_bg.png")
    personaggio = pygame.image.load("sprite/Character/standing.png")
    ambiente = pygame.image.load("sprite/asset/ambiente2.png")
    nuvole = pygame.image.load("sprite/asset/nuvole.png")
    walkLeft = [pygame.image.load("sprite/Character/L1.png"),
                pygame.image.load("sprite/Character/L2.png"),
                pygame.image.load("sprite/Character/L3.png"),
                pygame.image.load("sprite/Character/L4.png"),
                pygame.image.load("sprite/Character/L5.png"),
                pygame.image.load("sprite/Character/L6.png"),
                pygame.image.load("sprite/Character/L7.png"),
                pygame.image.load("sprite/Character/L8.png"),
                pygame.image.load("sprite/Character/L9.png")]
    walkRight = [pygame.image.load("sprite/Character/R1.png"),
                 pygame.image.load("sprite/Character/R2.png"),
                 pygame.image.load("sprite/Character/R3.png"),
                 pygame.image.load("sprite/Character/R4.png"),
                 pygame.image.load("sprite/Character/R5.png"),
                 pygame.image.load("sprite/Character/R6.png"),
                 pygame.image.load("sprite/Character/R7.png"),
                 pygame.image.load("sprite/Character/R8.png"),
                 pygame.image.load("sprite/Character/R9.png")]
    winscreen = pygame.image.load("sprite/asset/winscreen2.png")
    life = [pygame.image.load("sprite/asset/vite1.png"), pygame.image.load(
        "sprite/asset/vite2.png"), pygame.image.load("sprite/asset/vite3.png")]

    vite = 2
    screen.blit(life[vite], (-130, 10))
    pygame.display.update()
    colpito = True

    # setto il loop
    running = True
    # main loop

    nuvx = random.randint(0, 900)
    nuvy = random.randint(0, 40)
    nuvx2 = random.randint(0, 900)
    nuvy2 = random.randint(0, 40)

    while running:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # se premo esc chiude la finestra
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        if (320 <= personaggio_x <= 336 or 370 <= personaggio_x <= 386 or 417 <= personaggio_x <= 433 or 657 <= personaggio_x <= 673) and 420 <= personaggio_y <= 490:
            if vite > 0:
                colpito = True
                isJump = True
                vite -= 1
                hurt.play()
            else:
                dead()
                sys.exit()

        if personaggio_x > 880:
            vittoria()

        if keys[K_LEFT] or keys[K_a] and personaggio_x > 0:
            personaggio_x -= spostamento
            left = True
            right = False

        elif keys[K_RIGHT] or keys[K_d]:
            personaggio_x += spostamento
            left = False
            right = True

        else:
            right = False
            left = False
            walkCount = 0

        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                right = False
                left = False
                walkCount = 0

        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                personaggio_y -= (jumpCount ** 2) * 0.3 * neg
                jumpCount -= 1

            else:
                isJump = False
                jumpCount = 10

        if personaggio_y <= 420 and not isJump:
            personaggio_y += 1

        nuvx -= 1
        nuvx2 -= 1
        if nuvx <= -210:
            nuvx = 900
            nuvy = random.randint(-100, 160)
        if nuvx2 <= -210:
            nuvx2 = 900 + random.randint(140, 400)
            nuvy2 = random.randint(-100, 120)

        redrawGameWindow()








def livello3():

    global walkCount
    pygame.init()

    # SETTING
    # finestra
    screen_width = 900
    screen_height = 570
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygliese - A Unical Story - Livello 3")

    clock = pygame.time.Clock()

    # personaggio
    personaggio_x = 70
    personaggio_y = 430
    ambiente_x = 0

    # movement
    spostamento = 2.5
    walkCount = 0
    isJump = False
    jumpCount = 10
    left = False
    right = False

    # sound
    deadsound = pygame.mixer.Sound("sprite/Sound/dead.wav")
    hurt = pygame.mixer.Sound("sprite/Sound/hurt.wav")
    playsound = pygame.mixer.Sound("sprite/Sound/theme.wav")
    playsound.play(-1)
    buttonsound = pygame.mixer.Sound("sprite/Sound/button.wav")
    winsound = pygame.mixer.Sound("sprite/Sound/win.wav")

    def redrawGameWindow():
        global walkCount
        screen.blit(bg, (0, 0))
        screen.blit(ambiente, (ambiente_x, 0))

        screen.blit(nuvole, (nuvx, nuvy))
        screen.blit(nuvole, (nuvx2, nuvy2))

        if colpito:
            screen.blit(life[vite], (-130, 10))
        if walkCount + 1 >= 9:
            walkCount = 0
        if left:
            screen.blit(walkLeft[walkCount], (personaggio_x, personaggio_y))
            walkCount += 1
        elif right:
            screen.blit(walkRight[walkCount], (personaggio_x, personaggio_y))
            walkCount += 1
        else:
            screen.blit(personaggio, (personaggio_x, personaggio_y))
        pygame.display.update()

    def dead():
        deadsound.play()
        diescreen = pygame.image.load("sprite/asset/die_screen.png")
        play = pygame.image.load("sprite/button/play.png")
        quit = pygame.image.load("sprite/button/quit.png")
        screen.blit(diescreen, (185, 111))
        screen.blit(play, (259, 347))
        screen.blit(quit, (481, 347))
        pygame.display.update()
        scelta = False
        while not scelta:
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if 418 >= mouse_pos[0] >= 259 and 347 <= mouse_pos[1] <= 417:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        playsound.stop()
                        buttonsound.play()
                        livello1()
                if 640 >= mouse_pos[0] >= 481 and 347 <= mouse_pos[1] <= 417:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        buttonsound.play()
                        scelta = True
                        sys.exit()

    def vittoria():
        playsound.stop()
        winsound.play()
        screen.blit(winscreen, (0, 0))
        pygame.display.update()
        scelta = False
        while not scelta:
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if 418 >= mouse_pos[0] >= 259 and 347 <= mouse_pos[1] <= 417:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        playsound.stop()
                        buttonsound.play()
                        scelta = True
                        livello1()
                if 640 >= mouse_pos[0] >= 481 and 347 <= mouse_pos[1] <= 417:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        buttonsound.play()
                        scelta = True

    # CARICO IMMAGINI
    bg = pygame.image.load("sprite/asset/sky_bg.png")
    personaggio = pygame.image.load("sprite/Character/standing.png")
    ambiente = pygame.image.load("sprite/asset/ambiente3.png")
    nuvole = pygame.image.load("sprite/asset/nuvole.png")
    walkLeft = [pygame.image.load("sprite/Character/L1.png"),
                pygame.image.load("sprite/Character/L2.png"),
                pygame.image.load("sprite/Character/L3.png"),
                pygame.image.load("sprite/Character/L4.png"),
                pygame.image.load("sprite/Character/L5.png"),
                pygame.image.load("sprite/Character/L6.png"),
                pygame.image.load("sprite/Character/L7.png"),
                pygame.image.load("sprite/Character/L8.png"),
                pygame.image.load("sprite/Character/L9.png")]
    walkRight = [pygame.image.load("sprite/Character/R1.png"),
                 pygame.image.load("sprite/Character/R2.png"),
                 pygame.image.load("sprite/Character/R3.png"),
                 pygame.image.load("sprite/Character/R4.png"),
                 pygame.image.load("sprite/Character/R5.png"),
                 pygame.image.load("sprite/Character/R6.png"),
                 pygame.image.load("sprite/Character/R7.png"),
                 pygame.image.load("sprite/Character/R8.png"),
                 pygame.image.load("sprite/Character/R9.png")]
    winscreen = pygame.image.load("sprite/asset/winscreen3.png")
    life = [pygame.image.load("sprite/asset/vite1.png"), pygame.image.load(
        "sprite/asset/vite2.png"), pygame.image.load("sprite/asset/vite3.png")]

    vite = 2
    screen.blit(life[vite], (-130, 10))
    pygame.display.update()
    colpito = True

    # setto il loop
    running = True
    # main loop

    nuvx = random.randint(0, 900)
    nuvy = random.randint(0, 40)
    nuvx2 = random.randint(0, 900)
    nuvy2 = random.randint(0, 40)

    while running:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # se premo esc chiude la finestra
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        if (267 < personaggio_x < 283 or 320 <= personaggio_x <= 336 or 370 < personaggio_x < 386 or 417 <= personaggio_x <= 433) and 420 <= personaggio_y <= 490:
            if vite > 0:
                colpito = True
                isJump = True
                vite -= 1
                hurt.play()
            else:
                dead()
                sys.exit()

        if personaggio_x > 880:
            vittoria()
            sys.exit()

        if keys[K_LEFT] or keys[K_a] and personaggio_x > 0:
            personaggio_x -= spostamento
            left = True
            right = False

        elif keys[K_RIGHT] or keys[K_d]:
            personaggio_x += spostamento
            left = False
            right = True

        else:
            right = False
            left = False
            walkCount = 0

        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                right = False
                left = False
                walkCount = 0

        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                personaggio_y -= (jumpCount ** 2) * 0.3 * neg
                jumpCount -= 1

            else:
                isJump = False
                jumpCount = 10

        if personaggio_y <= 420 and not isJump:
            personaggio_y += 1

        nuvx -= 1
        nuvx2 -= 1
        if nuvx <= -210:
            nuvx = 900
            nuvy = random.randint(-100, 160)
        if nuvx2 <= -210:
            nuvx2 = 900 + random.randint(140, 400)
            nuvy2 = random.randint(-100, 120)

        redrawGameWindow()
