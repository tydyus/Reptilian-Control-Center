import pygame

from pygame.locals import *

class repartitionRichesse:

    def __init__(self):

        self.curseur = 1

    def click(self):

        self.curseur += 1
        if self.curseur == 7:
            self.curseur = 1

        rV1=1
        rV2=2
        rV3=3
        rV4=5
        rV5=10
        rV6=20
        return rV1, rV2, rV3, rV4, rV5, rV6
