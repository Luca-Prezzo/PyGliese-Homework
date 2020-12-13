import pygame
from pygame.locals import *

def menu():
    title = pygame.image.load("sprite/title2.png")
    title_width = 494
    title_height = 178

    #carico bg
    bg = pygame.image.load("sprite/unical_bg.png")

    # carico il menu
    play = pygame.image.load("sprite/play.png")
    options = pygame.image.load("sprite/opzioni.png")
    quit = pygame.image.load("sprite/quit.png")