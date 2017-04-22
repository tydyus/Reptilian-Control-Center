import pygame
import time

from pygame.locals import *
from ville import *


pygame.init()
clock = pygame.time.Clock()
FPS = 60
time = 0

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((854, 480))
#rêgle le son
volume = pygame.mixer.music.get_volume() 
pygame.mixer.music.set_volume(0.5)
#son de fond
pygame.mixer.music.load("../sound/loop.wav")
pygame.mixer.music.play(-1)

#Chargement et collage du boitier/fond
fond = pygame.image.load("../img/fond.png").convert_alpha()
fenetre.blit(fond, (0,0))
boitier = pygame.image.load("../img/controlCenter.png").convert_alpha()
fenetre.blit(boitier, (0,0))

#Chargement et collage des inputs du boitier
switch1 = pygame.image.load("../img/switch1OFF.png").convert_alpha()
fenetre.blit(switch1, (0,0))
switch2 = pygame.image.load("../img/switch2OFF.png").convert_alpha()
fenetre.blit(switch2, (0,0))
switch3 = pygame.image.load("../img/switch3OFF.png").convert_alpha()
fenetre.blit(switch3, (0,0))
switch4 = pygame.image.load("../img/switch4OFF.png").convert_alpha()
fenetre.blit(switch4, (0,0))

#creation villes
ville1 = villes()
ville2 = villes()
ville3 = villes()
ville4 = villes()
ville5 = villes()
ville6 = villes()

#Rafraîchissement de l'écran

pygame.display.flip()


#BOUCLE INFINIE

continuer = 1

while continuer:

    #fps
    clock.tick(FPS)

    # event de kill
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

    ## cycle
    # add habitants
    if time == 180:
        time = 0
        ville1.addPop(1)
        ville2.addPop(2)
        ville3.addPop(3)
        ville4.addPop(4)
        ville5.addPop(5)
        ville6.addPop(6)
        
    # resolution crise
    # add dvlp
    
    ## visuel départ
    # visu map
    fenetre.blit(fond, (0,0))
    
    # visu boitier
    fenetre.blit(boitier, (0,0))
    
    # visu input boitier
    fenetre.blit(switch1, (0,0))
    fenetre.blit(switch2, (0,0))
    fenetre.blit(switch3, (0,0))
    fenetre.blit(switch4, (0,0))
    
    # Rafraîchissement de l'écran
    pygame.display.flip()
    # maj time
    time += 1
