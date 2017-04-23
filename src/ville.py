import pygame

from pygame.locals import *
from inputBoitier import *

class villes:

    dvlpT = 0
    dvlpCycle = 12 # pre-prod/ de base 12
    dvlpPop = 3 # pre-prod/ de base 3
    
    dvlp = 0 #developement global
    pop = 0 #population global
    rad = 0 #radiation
    pol = 0 #polution
    resPol = 0 #resistance polution
    mort = 0 #mort total
    
    def __init__(self):

        self.dvlp = 0
        self.valeurDvlp = 100
        self.repartition = 4 # sur 24, valeur de base: 4/24
        self.pop = 0
        self.city = pygame.image.load("../img/city/city_0.png").convert_alpha()

    def info(self):
        print("__info-ville__")
        print("dvlp ",self.dvlp)
        print("valeur dvlp: ",self.valeurDvlp)
        print("gain de richesse: ",self.repartition)
        print("pop: ",self.pop)
    def infoW(self):
        print("__info-World__")
        print("Dvlp total: ",villes.dvlpT)
        print("Developement global: ",villes.dvlp)
        print("Ropulation: ",villes.pop)
        print("Radiation: ",villes.rad)
        print("Polution: ",int(villes.pol),"/11000")
        print("Resistance polution: ",villes.resPol)
        print("Mort total: ",villes.mort,"/2200")
        
    def reset(self):

        villes.dvlpT = 0
        villes.dvlpCycle = 12 
        villes.dvlpPop = 3 
    
        villes.dvlp = 0 
        villes.pop = 0 
        villes.rad = 0 
        villes.pol = 0 
        villes.resPol = 0 
        villes.mort = 0
        
    def addPop(self,nameville):
        
        villes.pop += villes.dvlpPop
        self.pop += villes.dvlpPop

    def checkPop(self):
        
        if self.pop < (self.dvlp - 5):
            self.valeurDvlp -= 50
            print("surpopulation")
            
        if self.pop > (self.dvlp + 5):
            villes.mort += int((self.pop - (self.dvlp + 5))//2)
            self.pop -= (self.pop - (self.dvlp + 5))//2
            print("famine")

        #rad
        self.pop -= (villes.rad//100)
        villes.mort += int((villes.rad//100))

    def addDev(self):

        villes.dvlpT = villes.dvlpCycle+switch.dvlpNuke+switch.recyDev
        self.dvlp += (villes.dvlpT/24*(self.repartition))*(self.valeurDvlp/100)
        villes.resPol = switch.resPol
        villes.pol += (self.dvlp/10)/((100-(villes.resPol))/100)
        villes.dvlp += self.dvlp

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
        lvlP = int(villes.pol//1000)
        return lvlP
    def morts (self):
        lvlP = int(villes.mort//200)
        return lvlP
            
