from math import *
from random import *


def tour(nb_balle, t_barillet):
  print(t_barillet)
  if nb_balle > t_barillet:
    nb_balle = t_barillet - 1
  
  fate = randint(1,t_barillet)
  if fate <= nb_balle:
    return False
  else:
    return True