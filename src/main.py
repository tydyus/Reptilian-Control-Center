import pygame

from pygame.locals import *


pygame.init()


#Ouverture de la fenêtre Pygame

fenetre = pygame.display.set_mode((854, 480))


#Chargement et collage du boitier
fond = pygame.image.load("../img/controlCenter.png").convert_alpha()
fenetre.blit(fond, (0,0))

#Chargement et collage des inputs du boitier
switch1 = pygame.image.load("../img/switch1OFF.png").convert_alpha()
fenetre.blit(switch1, (0,0))
switch2 = pygame.image.load("../img/switch2OFF.png").convert_alpha()
fenetre.blit(switch2, (0,0))
switch3 = pygame.image.load("../img/switch3OFF.png").convert_alpha()
fenetre.blit(switch3, (0,0))
switch4 = pygame.image.load("../img/switch4OFF.png").convert_alpha()
fenetre.blit(switch4, (0,0))

#Rafraîchissement de l'écran

pygame.display.flip()


#BOUCLE INFINIE

continuer = 1

while continuer:

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
