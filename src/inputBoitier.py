import pygame

from pygame.locals import *

class repartitionRichesse:

    def __init__(self):

        self.curseur = 1
        self.angle = 0

    def click(self):

        self.curseur += 1
        if self.curseur == 7:
            self.curseur = 1
        self.angle = -(self.curseur-1)*60

        rV1=1
        rV2=2
        rV3=3
        rV4=5
        rV5=10
        rV6=20
        return rV1, rV2, rV3, rV4, rV5, rV6

class switch:
    def __init__(self):

        self.etat = 0
        self.img = pygame.image.load("../img/switch1OFF.png").convert_alpha()
        self.etatON = pygame.image.load("../img/switch1ON.png").convert_alpha()
        self.etatOFF = pygame.image.load("../img/switch1OFF.png").convert_alpha()

    def click(self):

        if self.etat == 0:
            self.etat = 1
            self.img = self.etatON
            print("on")
        else:
            self.etat = 0
            self.img = self.etatOFF
            print("off")
