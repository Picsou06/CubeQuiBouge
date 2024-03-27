from random import *

class File:
    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        return len(self.valeurs) == 0 

    def enfile(self, x):
        self.valeurs.insert(0, x)

    def defile(self):
        if self.est_vide():
            print('Vous avez essayé de défiler une file vide !')
            return None
        else :
            return self.valeurs.pop() 
        
    def affiche(self):       # Hors-Programme : pour afficher 
        chaine = '|'              # convenablement la file avec print(p)
        for v in self.valeurs:
            chaine = chaine + str(v) + '|'
        print(chaine)

    def __str__(self):       # Hors-Programme : pour afficher 
        chaine = '|'              # convenablement la file avec print(p)
        for v in self.valeurs:
            chaine = chaine + str(v) + '|'
        return chaine
        
    def minimum(self):
        tmp= File()
        mini = self.defile()
        tmp.enfile(mini)
        while not self.est_vide():
            element = self.defile()
            if element < mini :
                mini = element
            tmp.enfile(element)
        while not tmp.est_vide():
            self.enfile(tmp.defile())
        return mini 
    def __len__(self):
        return len(self.valeurs)
    

def pompe(nb_reelle, nb_blanc):
    
    assert nb_blanc + nb_reelle <= 8, "Il n'y que 8 balle au total maximum"
    
    chambre = File()
    while nb_blanc > 0 or nb_reelle > 0:
        inserer = randint (1,2)
        if inserer == 1:
            if nb_blanc > 0:
                chambre.enfile("Blanc")
                nb_blanc -= 1
            else:
                while nb_reelle > 0:
                    chambre.enfile("Reelle")
                    nb_reelle -= 1
        else:
            if nb_reelle > 0:
                chambre.enfile("Reelle")
                nb_reelle -= 1
            else:
                while nb_blanc > 0:
                    chambre.enfile("Blanc")
                    nb_blanc -= 1
    return chambre

def Duel(Rouge, Blanc):
    print ("Il y a ",Rouge," balles réelles et ",Blanc," balles à Blanc")
    print ("On les insères dans un ordre aléatoire dans le fusils à pompe")
    Chargeur = pompe(Rouge, Blanc)
    #print(Chargeur)
