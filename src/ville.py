import pygame

from pygame.locals import *

class villes:

    dvlp = 0
    pop = 0
    
    def __init__(self):

        self.dvlp = 0
        self.pop = 0

    def addPop(self,nameville):
        villes.pop += 3
        self.pop += 3
        print("ville ", nameville," a ", self.pop," habitants, pour ", villes.pop, " habitants global")
        print("testF")
