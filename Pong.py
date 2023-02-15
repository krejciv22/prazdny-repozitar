import sys
import random
import pygame
import math
pygame.init()

ROZLISENI_Y = 1017
ROZLISENI_X = 1920
FPS = 60

velikost = 50
pozice_x = (ROZLISENI_X - velikost) / 2
pozice_y = (ROZLISENI_Y - velikost) / 2
rychlost = 3


okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))
pygame.display.set_caption('Pong')

obrazek = pygame.image.load('pozadí správné.png')

pygame.display.set_icon(obrazek)

pozadi = pygame.image.load('pozadí správné.png')
pozadi = pygame.transform.scale(pozadi,(1920,1017,))

micek = pygame.image.load('micek spravny.png')
micek = pygame.transform.scale(micek,(100,100,))


while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    okno.blit(pozadi,(0,0))
    okno.blit(micek,(902,510))

    pygame.display.update()
