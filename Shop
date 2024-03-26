from math import *
from kandinsky import *
from ion import *

def s_inv(inv, phase_shop):
  fill_rect(60,65,210,100,"white")
  quitter = False
  while quitter == False:
    if phase_shop == 0:
      statut_barillet = "sold"
      while quitter == False:
        if inv[0] == 0: 
          draw_string("1 : Barillet 9 places",60,65)
          statut_barillet = "dispo"
          draw_string("40 gold",60,83)
        draw_string("OK : Quitter",60,145)
        if keydown(KEY_ONE):
          if statut_barillet == "dispo":
            if inv[3] >= 40:
              inv[0] = 1
              inv[3] = inv[3]-40
              statut_barillet = "sold"
              print("vendu")
        if keydown(KEY_OK):
          quitter = True  
  fill_rect(60,65,210,100,color(0,200,0))
  return inv
