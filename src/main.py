import pygame

from pygame.locals import *


pygame.init()


#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((854, 480))
#rêgle le son
volume = pygame.mixer.music.get_volume() 
pygame.mixer.music.set_volume(0.5)
#son de fond
pygame.mixer.music.load("../sound/loop.wav")
pygame.mixer.music.play(-1)

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

    # event de kill
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

    # cycle


    # Rafraîchissement de l'écran
    pygame.display.flip()
