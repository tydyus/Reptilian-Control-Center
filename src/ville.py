import pygame

from pygame.locals import *

class villes:

    dvlpCycle = 12 # pre-prod/ de base 12
    dvlpPop = 3 # pre-prod/ de base 3
    
    dvlp = 0 #developement global
    pop = 0 #population global
    rad = 0 #radiation
    pol = 0 #polution
    resPol = 0 #resistance polution
    
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
        villes.pol += (self.dvlp/10)/((100-villes.resPol)/100)

        # changement etat de la cité
        if self.dvlp <= 10:
            self.city = pygame.image.load("../img/city/city_0.png").convert_alpha()
        if self.dvlp > 10:
            self.city = pygame.image.load("../img/city/city_1.png").convert_alpha()
        if self.dvlp > 30:
            self.city = pygame.image.load("../img/city/city_2.png").convert_alpha()
        if self.dvlp > 70:
            self.city = pygame.image.load("../img/city/city_3.png").convert_alpha()
        if self.dvlp > 150:
            self.city = pygame.image.load("../img/city/city_4.png").convert_alpha()
        if self.dvlp > 225:
            self.city = pygame.image.load("../img/city/city_5.png").convert_alpha()
        if self.dvlp > 350:
            self.city = pygame.image.load("../img/city/city_6.png").convert_alpha()
        if self.dvlp > 500:
            self.city = pygame.image.load("../img/city/city_7.png").convert_alpha()
        if self.dvlp > 700:
            self.city = pygame.image.load("../img/city/city_8.png").convert_alpha()
        if self.dvlp > 1000:
            self.city = pygame.image.load("../img/city/city_9.png").convert_alpha()
        if self.dvlp > 1400:
            self.city = pygame.image.load("../img/city/city_10.png").convert_alpha()
        # remise a zero pour le nouveau cycle
        self.valeurDvlp = 100


    def polution (self):
        lvlP = int(villes.pol//500)
        return lvlP
            
