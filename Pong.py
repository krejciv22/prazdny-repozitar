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
pohyb = False

okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))
pygame.display.set_caption('Pong')

obrazek = pygame.image.load('pozadí správné.png')

pygame.display.set_icon(obrazek)

pozadi = pygame.image.load('pozadí správné.png')
pozadi = pygame.transform.scale(pozadi,(1920,1017,))

micek = pygame.image.load('micek spravny.png')
micek = pygame.transform.scale(micek,(100,100,))

platforma = pygame.image.load('platforma.png')
platforma = pygame.transform.scale(platforma,(20,200,))

platforma2 = pygame.image.load('platforma2.png')
platforma2 = pygame.transform.scale(platforma,(500,20,))

vyskamice = 520
sirkamice = 902
platforma1vyska = 408
platforma1sirka = 0
platforma2vyska = 408
platforma2sirka = 1900
platforma3vyska = 3
platforma3sirka = 709
platforma4vyska = 985
platforma4sirka = 709


micek_rychlost_x = 7
micek_rychlost_y = 7



while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        pohyb = True                
        platforma3sirka-=1
    if keys[pygame.K_d]:
        pohyb = True
        platforma3sirka+=1
    
    
    
    
    
    
    if keys[pygame.K_b]:
        pohyb = True
        platforma4sirka-=1
    if keys[pygame.K_m]:
        pohyb = True
        platforma4sirka+=1
    if keys[pygame.K_UP]:
        pohyb = True
        platforma1vyska-=1
    if keys[pygame.K_DOWN]:
        pohyb = True
        platforma1vyska+=1
    if keys[pygame.K_KP6]:
        pohyb = True
        platforma2vyska+=1
    if keys[pygame.K_KP9]:
        pohyb = True
        platforma2vyska-=1





    okno.blit(pozadi,(0,0))
    okno.blit(micek,(sirkamice,vyskamice))
    
    okno.blit(platforma,(platforma1sirka,platforma1vyska))  
    okno.blit(platforma,(platforma2sirka,platforma2vyska))
    okno.blit(platforma2,(platforma3sirka,platforma3vyska))
    okno.blit(platforma2,(platforma4sirka,platforma4vyska))
       

    
   
   
   
    pygame.display.update()
