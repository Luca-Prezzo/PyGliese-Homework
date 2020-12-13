import pygame
from pygame.locals import *
from pygame.time import Clock

def lv1():
    
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
    
    isJump = False
    jumpCount = 10

    while running:
        #clock = pygame.time.Clock()
        #clock.tick(30)
    
        screen.blit(bg,(0,0))
        personaggio = pygame.draw.rect(screen, (255,0,0),pygame.Rect(personaggio_x,personaggio_y,40,60))

        if personaggio_y >= (screen_height-60):
            screen.blit(diescreen,(186,112))

        elif personaggio_y <= (screen_height-180):
            personaggio_y += 2


        pygame.display.flip()
        pygame.display.update()


        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            if keys[K_a]:
                if personaggio_x >= 0:
                    personaggio_x -= 4
            if keys[K_d]:
                if personaggio_x <= screen_width-40:
                    personaggio_x += 4

            if not isJump:
                if keys[K_SPACE]:
                    isJump = True
            else:
                if jumpCount >= -10:
                    personaggio_y -= (jumpCount * abs(jumpCount)) * 0.3
                    jumpCount -= 1
                else:
                    jumpCount = 10
                    isJump = False

    
    pygame.quit()