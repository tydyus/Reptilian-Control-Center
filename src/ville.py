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
        self.répartition = 4 # sur 24, valeur de base: 4/24
        self.pop = 0

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
        
        self.dvlp += (villes.dvlpCycle/24*(self.répartition))*(self.valeurDvlp/100)
        print("gagne",(villes.dvlpCycle/24*(self.répartition))*(self.valeurDvlp/100), " a ",self.dvlp, " de dvlp.")
        # remise a zero pour le nouveau cycle
        self.valeurDvlp = 100
