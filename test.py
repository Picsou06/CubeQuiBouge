import pytmx
from pytmx.util_pygame import load_pygame
import pyscroll
import pygame

# Taille d'une tuile en pixels
TILE_SIZE = 32

def generate_tmx_map(data):
    # Créer un fichier TMX vide
    tmx_map = pytmx.TiledMap()

    # Définir les propriétés de la carte
    tmx_map.width = len(data[0])
    tmx_map.height = len(data)
    tmx_map.tilewidth = TILE_SIZE
    tmx_map.tileheight = TILE_SIZE
    
    # Créer un nouveau calque de tuiles
    tile_layer = pytmx.TiledTileLayer(tmx_map.width, tmx_map.height)
    tile_layer.name = "Ground"
    
    # Parcourir la liste et remplir le calque de tuiles
    for y, row in enumerate(data):
        for x, tile in enumerate(row):
            # Ajouter la tuile en fonction de sa valeur dans la liste
            if tile == 0:  # Sol
                tile_layer.data[y][x] = pytmx.Tile(None, None, None, None)
            elif tile == 1:  # Mur
                tile_layer.data[y][x] = pytmx.Tile(None, None, None, None, True)
            elif tile == 2:  # Coffre
                tile_layer.data[y][x] = pytmx.Tile(None, None, None, None)
            elif tile == 3:  # Boutique
                tile_layer.data[y][x] = pytmx.Tile(None, None, None, None, True)
            elif tile == 4:  # Départ
                tile_layer.data[y][x] = pytmx.Tile(None, None, None, None)
            elif tile == 5:  # Coffre clé
                tile_layer.data[y][x] = pytmx.Tile(None, None, None, None)
            elif tile == 6:  # Arrivée
                tile_layer.data[y][x] = pytmx.Tile(None, None, None, None)
                
    # Ajouter le calque de tuiles à la carte
    tmx_map.layers.append(tile_layer)
    
    return tmx_map

# Exemple d'utilisation
data = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 1], [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 2, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Générer la carte TMX
tmx_map = generate_tmx_map(data)

# Enregistrer la carte TMX dans un fichier
with open("generated_map.tmx", "w") as f:
    tmx_map.save(f)

print("Fichier TMX généré avec succès !")
