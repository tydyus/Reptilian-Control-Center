import pygame

from pygame.locals import *
from ville import *

class repartitionRichesse:

    def __init__(self):

        self.curseur = 1
        self.angle = 0
        self.rV1=1
        self.rV2=1
        self.rV3=1
        self.rV4=5
        self.rV5=7
        self.rV6=9

    def click(self):

        self.curseur += 1
        if self.curseur == 7:
            self.curseur = 1
        self.angle = -(self.curseur-1)*60
        if self.curseur == 1:
            self.rV1=1
            self.rV2=1
            self.rV3=1
            self.rV4=5
            self.rV5=7
            self.rV6=9
        if self.curseur == 2:
            self.rV1=1
            self.rV2=1
            self.rV3=3
            self.rV4=5
            self.rV5=6
            self.rV6=8
        if self.curseur == 3:
            self.rV1=1
            self.rV2=2
            self.rV3=4
            self.rV4=5
            self.rV5=5
            self.rV6=7
        if self.curseur == 4:
            self.rV1=2
            self.rV2=3
            self.rV3=4
            self.rV4=4
            self.rV5=5
            self.rV6=6
        if self.curseur == 5:
            self.rV1=3
            self.rV2=3
            self.rV3=4
            self.rV4=4
            self.rV5=5
            self.rV6=5
        if self.curseur == 6:
            self.rV1=4
            self.rV2=4
            self.rV3=4
            self.rV4=4
            self.rV5=4
            self.rV6=4
        
        return self.rV1, self.rV2, self.rV3, self.rV4, self.rV5, self.rV6

    def initEtat(self):
        return self.rV1, self.rV2, self.rV3, self.rV4, self.rV5, self.rV6
    

class switch:

    resPol = 0
    recyDev = 0
    dvlpNuke = 0
    
    def __init__(self):

        self.etat = 0
        self.img = pygame.image.load("../img/switch1OFF.png").convert_alpha()
        self.etatON = pygame.image.load("../img/switch1ON.png").convert_alpha()
        self.etatOFF = pygame.image.load("../img/switch1OFF.png").convert_alpha()
        self.son = pygame.mixer.Sound("../sound/switch.wav")
        
    def click(self):

        self.son.play()
        if self.etat == 0:
            self.etat = 1
            self.img = self.etatON
            print("on")
        else:
            self.etat = 0
            self.img = self.etatOFF
            print("off")

    def nuke(self):
        rad = 0 
        switch.dvlpNuke = 0 
        if self.etat == 1:
            rad = 1 #radiation
        switch.dvlpNuke = 12 #bonus de dev
        return rad
    
    def recycle(self):
        switch.resPol = 0
        switch.recyDev = 0
        if self.etat == 1:
            switch.resPol = 50
            switch.recyDev = -6
            
    
class slides():

    slide = 0
    slider = 0

    def __init__(self):

        self.xCurseur = 0
