from random import randint

x = input("Nombre d'heure d'entrainement pour la journée: ")

fate = randint(0,24)
if fate <=x : 
    print("Tu t'es bléssé")
else:
    print(f"Tu a gagné {x} ...")