import sys
import random
import pygame

pygame.init()

ROZLISENI_X = 1920
ROZLISENI_Y = 1017
FPS = 60
CERNA_BARVA = (0, 0, 0)
BILA_BARVA = (255, 255, 255)

velikost = 50
pozice_x = (ROZLISENI_X - velikost) / 2
pozice_y = (ROZLISENI_Y - velikost) / 2
rychlost = 3

okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))
pygame.display.set_caption('Pong')

obrazek = pygame.image.load('pozadí správné.png')
obrazek = pygame.transform.scale(obrazek, (velikost, velikost))
pygame.display.set_icon(obrazek)

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()

from tkiner import *
from PIL import  ImageTk, image
master=Tk()
master.title(obrazek)
image_0=Image.open('pozadí správné.png')
bck_end=ImageTk.PhotoImage(image_0)
master.geometry('1920x1017')
