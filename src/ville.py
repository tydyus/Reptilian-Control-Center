import pygame

from pygame.locals import *

class villes:

    dvlpCycle = 12 # pre-prod/ de base 12
    dvlpPop = 3 # pre-prod/ de base 3
    
    dvlp = 0
    pop = 0
    
    def __init__(self):

        self.dvlp = 0
        self.valeurDvlp = 100
        self.repartition = 4 # sur 24, valeur de base: 4/24
        self.pop = 0
        self.city = pygame.image.load("../img/city/city_0.png").convert_alpha()

    def addPop(self,nameville):
        
        villes.pop += villes.dvlpPop
        self.pop += villes.dvlpPop
        print("ville ", nameville," a ", self.pop," habitants, pour ", villes.pop, " habitants global")

    def checkPop(self):
        
        if self.pop < (self.dvlp - 5):
            self.valeurDvlp -= 50
            print("surpopulation")
            
        if self.pop > (self.dvlp + 5):
            self.pop -= (self.pop - (self.dvlp + 5))//2
            print("famine")

    def addDev(self):
        
        self.dvlp += (villes.dvlpCycle/24*(self.repartition))*(self.valeurDvlp/100)
        print("gagne",(villes.dvlpCycle/24*(self.repartition))*(self.valeurDvlp/100), " a ",self.dvlp, " de dvlp.")

        # changement etat de la cité
        if self.dvlp <= 15:
            self.city = pygame.image.load("../img/city/city_0.png").convert_alpha()
        if self.dvlp > 15:
            self.city = pygame.image.load("../img/city/city_1.png").convert_alpha()
        if self.dvlp > 50:
            self.city = pygame.image.load("../img/city/city_2.png").convert_alpha()
        if self.dvlp > 200:
            self.city = pygame.image.load("../img/city/city_3.png").convert_alpha()
        if self.dvlp > 500:
            self.city = pygame.image.load("../img/city/city_4.png").convert_alpha()
        # remise a zero pour le nouveau cycle
        self.valeurDvlp = 100
