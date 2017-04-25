try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass

import pygame
from pygame.locals import *

import time
from ville import *
from inputBoitier import *


pygame.init()
clock = pygame.time.Clock()
FPS = 60
vitCycle = 20 # base: 20
time = 0

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image



#Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode((854, 480))
#regle le son
volume = pygame.mixer.music.get_volume() 
pygame.mixer.music.set_volume(0.5)
#son de fond
pygame.mixer.music.load("sound/loop.wav")

#Chargement et collage du boitier/fond
fond = pygame.image.load("img/fond.png").convert_alpha()
fondE = pygame.image.load("img/fondE.png").convert_alpha()
fondW = pygame.image.load("img/fondW.png").convert_alpha()
boitier = pygame.image.load("img/controlCenter.png").convert_alpha()

#Chargement et collage des inputs du boitier
switch1 = switch()
switch1.etatON = pygame.image.load("img/switch1ON.png").convert_alpha()
switch1.etatOFF = pygame.image.load("img/switch1OFF.png").convert_alpha()
switch1.img = pygame.image.load("img/switch1OFF.png").convert_alpha()
switch2 = switch()
switch2.etatON = pygame.image.load("img/switch2ON.png").convert_alpha()
switch2.etatOFF = pygame.image.load("img/switch2OFF.png").convert_alpha()
switch2.img = pygame.image.load("img/switch2OFF.png").convert_alpha()
switch3 = switch()
switch3.etatON = pygame.image.load("img/switch3ON.png").convert_alpha()
switch3.etatOFF = pygame.image.load("img/switch3OFF.png").convert_alpha()
switch3.img = pygame.image.load("img/switch3OFF.png").convert_alpha()
switch4 = switch()
switch4.etatON = pygame.image.load("img/switch4ON.png").convert_alpha()
switch4.etatOFF = pygame.image.load("img/switch4OFF.png").convert_alpha()
switch4.img = pygame.image.load("img/switch4OFF.png").convert_alpha()
curseurM = pygame.image.load("img/curseurMoney.png").convert_alpha()
jaugeB = pygame.image.load("img/jaugeB.png").convert_alpha()
jaugeJ = pygame.image.load("img/jaugeJ.png").convert_alpha()
jaugeR = pygame.image.load("img/jaugeR.png").convert_alpha()
alimOn = pygame.image.load("img/alimon.png").convert_alpha()
sSoins = slides()
sRichesse = slides()
sTest = slides()
slides.slide = pygame.image.load("img/slide.png").convert_alpha()
slides.slider = pygame.image.load("img/slider.png").convert_alpha()
alimOff = pygame.image.load("img/alimoff.png").convert_alpha()
        


#creation planete/ville
world = pygame.image.load("img/world.png").convert_alpha()
city1 = pygame.image.load("img/city/city_1.png").convert_alpha() #imgtaille: 390*390
city2 = pygame.image.load("img/city/city_2.png").convert_alpha() 
city3 = pygame.image.load("img/city/city_3.png").convert_alpha()
city4 = pygame.image.load("img/city/city_4.png").convert_alpha()
testR = pygame.image.load("img/testRotate.png").convert_alpha()

#creation objets villes
ville1 = villes()
ville2 = villes()
ville3 = villes()
ville4 = villes()
ville5 = villes()
ville6 = villes()

#creation objets input boitier
rptRich = repartitionRichesse()
ville1.repartition, ville2.repartition, ville3.repartition, ville4.repartition, ville5.repartition, ville6.repartition, = rptRich.initEtat()

#Rafraichissement de l'ecran

pygame.display.flip()


#BOUCLE INFINIE

continuer = 1
boitierAlim = 0
cycle = 1
angle = 0
mousemove = 0
win = 0

while continuer:

    #fps
    clock.tick(FPS)

    # event de kill
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    if event.type == MOUSEBUTTONDOWN:
        mousemove = 0

    
        ## input

    
    if mousemove == 0 :
        
        #curseur richesse
        if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 497 and event.pos[1] > 202 and event.pos[0] < 590 and event.pos[1] < 275:
            mousemove = 1
            #print("repartition de la richesse")
            ville1.repartition, ville2.repartition, ville3.repartition, ville4.repartition, ville5.repartition, ville6.repartition, = rptRich.click()
        #switch1 nuke
        if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 598 and event.pos[1] > 200 and event.pos[0] < 638 and event.pos[1] < 280:
            mousemove = 1
            #print("switch1")
            switch1.click()
        #switch2
        if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 650 and event.pos[1] > 200 and event.pos[0] < 692 and event.pos[1] < 280:
            mousemove = 1
            #print("switch2")
            switch2.click()
        #switch3
        if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 704 and event.pos[1] > 200 and event.pos[0] < 744 and event.pos[1] < 280:
            mousemove = 1
            #print("switch3")
            switch3.click()
        #switch4
        if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 757 and event.pos[1] > 200 and event.pos[0] < 797 and event.pos[1] < 280:
            mousemove = 1
            #print("switch4")
            switch4.click()
        #slide soins
        if event.type == MOUSEBUTTONDOWN and event.pos[0] > 602 and event.pos[1] > 103 and event.pos[0] < 797 and event.pos[1] < 114:
            sSoins.xCurseur = (event.pos[0] - 612)
        #slide richesse
        if event.type == MOUSEBUTTONDOWN and event.pos[0] > 602 and event.pos[1] > 133 and event.pos[0] < 797 and event.pos[1] < 144:
            sRichesse.xCurseur = (event.pos[0] - 612)
        #slide test
        if event.type == MOUSEBUTTONDOWN and event.pos[0] > 602 and event.pos[1] > 163 and event.pos[0] < 797 and event.pos[1] < 174:
            sTest.xCurseur = (event.pos[0] - 612)
    
    #Alimentation du boitier
    if mousemove == 0 and boitierAlim == 0 and event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 497 and event.pos[1] > 400 and event.pos[0] < 585 and event.pos[1] < 460:
        switch1.son.play()
        mousemove = 1
        boitierAlim = 1
        win = 0
        pygame.mixer.music.play(-1)
    if boitierAlim == 1:
        
        # maj time
        time += 1
        ## cycle
        villes.dvlp = 0
        # add habitants
        if time == vitCycle:
            print()
            #print("cycle", cycle)
            time = 0
            cycle += 1
        
            ville1.addPop(1)
            ville1.checkPop()
            ville1.addDev()
            #ville1.info()
        
            ville2.addPop(2)
            ville2.checkPop()
            ville2.addDev()
            #ville2.info()
        
            ville3.addPop(3)
            ville3.checkPop()
            ville3.addDev()
            #ville3.info()
            
            ville4.addPop(4)
            ville4.checkPop()
            ville4.addDev()
            #ville4.info()
                
            ville5.addPop(5)
            ville5.checkPop()
            ville5.addDev()
            #ville5.info()
                
            ville6.addPop(6)
            ville6.checkPop()
            ville6.addDev()
            #ville6.info()

            #ville1.infoW()
        
            # resolution crise
            villes.rad += switch1.nuke() #effets switch 1, rad+dev
            switch2.recycle() #effets switch 2, resP + -dev
            
            # add dvlp
    
        ## visuel depart
        # visu map
        fenetre.blit(fond, (0,0))
        fenetre.blit(world, (140,140)) #imgtaille: 100*100

        city = rot_center(ville1.city, 60)  #ville1
        fenetre.blit(city, (45,45))
        city = rot_center(ville2.city, 0)   #ville2
        fenetre.blit(city, (45,45))
        city = rot_center(ville3.city, 180) #ville3
        fenetre.blit(city, (45,45))
        city = rot_center(ville4.city, 120) #ville4
        fenetre.blit(city, (45,45))
        city = rot_center(ville5.city, 300) #ville5
        fenetre.blit(city, (45,45))
        city = rot_center(ville6.city, 240) #ville6
        fenetre.blit(city, (45,45))

        cloud = rot_center(testR, angle) #test
        fenetre.blit(cloud, (45,45))
        angle += 0.4

        if villes.dvlp > 2000:
            win = 1
            
        
            
        

    if boitierAlim == 0:
        fenetre.blit(fondE, (0,0))
    if win == 2 and boitierAlim == 0:
            fenetre.blit(fondW, (0,0))
    # visu boitier
    fenetre.blit(boitier, (0,0))
    
    # visu input boitier
    if boitierAlim == 0:
        fenetre.blit(alimOff, (0,0))
    if boitierAlim == 1:
        fenetre.blit(alimOn, (0,0))
    fenetre.blit(switch1.img, (0,0))
    fenetre.blit(switch2.img, (0,0))
    fenetre.blit(switch3.img, (0,0))
    fenetre.blit(switch4.img, (0,0))

    fenetre.blit(slides.slide, (600,103))
    fenetre.blit(slides.slider, ((602 + sSoins.xCurseur),103))
    fenetre.blit(slides.slide, (600,133))
    fenetre.blit(slides.slider, ((602 + sRichesse.xCurseur),133))
    fenetre.blit(slides.slide, (600,163))
    fenetre.blit(slides.slider, ((602 + sTest.xCurseur),163))

    curseur = rot_center(curseurM, rptRich.angle)
    fenetre.blit(curseur, (497,202))

    # visu graph boitier

    for i in range(ville1.polution()):
        if i < 3:
            fenetre.blit(jaugeB, (516,(169-(8*(i-1)))))
        if i > 2 and i < 6:
            fenetre.blit(jaugeJ, (516,(169-(8*(i-1)))))
        if i > 5:
            fenetre.blit(jaugeR, (516,(169-(8*(i-1)))))
    for i in range(ville1.morts()):
        if i < 3:
            fenetre.blit(jaugeB, (546,(169-(8*(i-1)))))
        if i > 2 and i < 6:
            fenetre.blit(jaugeJ, (546,(169-(8*(i-1)))))
        if i > 5:
            fenetre.blit(jaugeR, (546,(169-(8*(i-1)))))
        
    #endGame+reset
    if ville1.polution() > 10 or ville1.morts() > 10 or win == 1 or mousemove == 0 and boitierAlim == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 497 and event.pos[1] > 400 and event.pos[0] < 585 and event.pos[1] < 460:
        pygame.mixer.music.stop()
        mousemove = 1
        boitierAlim = 0
        switch1.son.play()
        ville1.reset()
        ville1 = villes()
        ville2 = villes()
        ville3 = villes()
        ville4 = villes()
        ville5 = villes()
        ville6 = villes()
        cycle = 1
        if win == 1:
            win = 2
        
        

    

        

    
    # Rafraichissement de l'ecran
    pygame.display.flip()
    
