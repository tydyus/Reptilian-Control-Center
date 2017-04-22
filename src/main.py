import pygame
import time

from pygame.locals import *
from ville import *


pygame.init()
clock = pygame.time.Clock()
FPS = 60
time = 0

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image



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

#creation planete/ville
world = pygame.image.load("../img/world.png").convert_alpha()
fenetre.blit(world, (140,140)) #imgtaille: 100*100
city1 = pygame.image.load("../img/city/city_1.png").convert_alpha() #imgtaille: 390*390
city2 = pygame.image.load("../img/city/city_2.png").convert_alpha()
city3 = pygame.image.load("../img/city/city_3.png").convert_alpha()
city4 = pygame.image.load("../img/city/city_4.png").convert_alpha()

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
cycle = 1

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
        print()
        print("cycle", cycle)
        time = 0
        cycle += 1
        
        ville1.addPop(1)
        ville1.checkPop()
        ville1.addDev()
        
        ville2.addPop(2)
        ville2.checkPop()
        ville2.addDev()
        
        ville3.addPop(3)
        ville3.checkPop()
        ville3.addDev()
        
        ville4.addPop(4)
        ville4.checkPop()
        ville4.addDev()
        
        ville5.addPop(5)
        ville5.checkPop()
        ville5.addDev()
        
        ville6.addPop(6)
        ville6.checkPop()
        ville6.addDev()
        
    # resolution crise
    # add dvlp
    
    ## visuel départ
    # visu map
    fenetre.blit(fond, (0,0))
    fenetre.blit(world, (140,140)) #imgtaille: 100*100

    fenetre.blit(city1, (45,45))  #ville1
    city = rot_center(city1, 60)  #ville2
    fenetre.blit(city, (45,45))
    city = rot_center(city1, 120) #ville3
    fenetre.blit(city, (45,45))
    city = rot_center(city1, 180) #ville4
    fenetre.blit(city, (45,45))
    city = rot_center(city1, 240) #ville5
    fenetre.blit(city, (45,45))
    city = rot_center(city1, 300) #ville6
    fenetre.blit(city, (45,45))
       
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
