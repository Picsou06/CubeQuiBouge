from PIL import Image
import random
# open the image file
def scan(nom):
    img = Image.open(nom)

    # create an empty matrix
    matrix = [[0 for x in range(img.height)] for y in range(img.width)]

    # scan the image (in pixels)
    for i in range(img.width):
        for j in range(img.height):
            # get the pixel color
            r, g, b, a = img.getpixel((i, j))

            # determine the value to add to the matrix
            if r == 0 and g == 0 and b == 0 and a == 0: #Sol
                matrix[i][j] = 0
            elif r == 0 and g == 0 and b == 0 and a == 255: #Mur
                matrix[i][j] = 1
            elif r == 254 and g == 235 and b == 0 and a == 255: #Coffre
                matrix[i][j] = 2
            elif r == 94 and g == 255 and b == 0 and a == 255: #Shop
                matrix[i][j] = 3
            elif r == 236 and g == 0 and b == 0 and a == 255: #start
                matrix[i][j] = 4
            elif r == 0 and g == 27 and b == 165 and a == 255: #clé
                matrix[i][j] = 5
            elif r == 246 and g == 246 and b == 246 and a == 255: #arrivé
                matrix[i][j] = 6
            else:
                matrix[i][j] = "ERROR"
    return matrix

def player_interaction(matrix):
    count=9
    result=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==1:
                result.append(f"""<object id="{count}" type="collision" x="{i*32}" y="{j*32}" width="32" height="32"/>""")
                count+=1
            if matrix[i][j]==2:
                result.append(f"""<object id="{count}" type="chest" x="{i*32}" y="{j*32}" width="32" height="32"/>""")
                count+=1
            if matrix[i][j]==3:
                result.append(f"""<object id="{count}" type="shop" x="{i*32}" y="{j*32}" width="32" height="32"/>""")
                count+=1
            if matrix[i][j]==5:
                result.append(f"""<object id="{count}" type="key" x="{i*32}" y="{j*32}" width="32" height="32"/>""")
                count+=1
            if matrix[i][j]==6:
                result.append(f"""<object id="{count}" type="end" x="{i*32}" y="{j*32}" width="32" height="32"/>""")
                count+=1
    return result

def create_xml_file(matrix):
    with open("Tiled\map.tmx", "w") as f:
        f.write("""<?xml version="1.0" encoding="UTF-8"?>
<map version="1.10" tiledversion="1.10.2" orientation="orthogonal" renderorder="right-down" width="50" height="50" tilewidth="32" tileheight="32" infinite="0" nextlayerid="3" nextobjectid="13">
 <tileset firstgid="1" source="Mur_et_shop.tsx"/>
 <layer id="1" name="map" width="50" height="50">
  <data encoding="csv">\n""")
        futurspawn=[0,0]

        for row_index, row in enumerate(matrix):
            futurspawn[0] += 1
            for val in row:
                futurspawn[1] += 1
                if val == 0:
                    new_val = random.choice([4, 5, 6])
                elif val == 1:
                    new_val = random.choice([1, 2, 3])
                elif val == 2:
                    new_val = 8
                elif val == 3:
                    new_val = 7
                elif val == 4:
                    new_val = random.choice([4, 5, 6])
                    spawn = futurspawn
                elif val == 5:
                    new_val = random.choice([4, 5, 6])
                elif val == 6:
                    new_val = random.choice([4, 5, 6])
                else:
                    new_val = val
                f.write(f"{new_val},")
            if row_index < len(matrix) - 1:
                f.write("\n")
            else:
                f.seek(f.tell() - 1, 0)
                f.truncate()

        f.write("\n")
        f.write("""</data>
 </layer>\n""")
        f.write(f""" <objectgroup id="2" name="Objects">
  <object id="3" name="Player" x="{spawn[0]}" y="{int(spawn[1]/spawn[0])}">
   <point/>
  </object>\n""")
        for i in player_interaction(matrix):
            f.write("  "+i+"\n")
        #f.write(""" <object id="1087" type="collision" x="1600" y="0" width="40" height="1600"/>\n <object id="1088" type="collision" x="-40" y="0" width="40" height="1600"/>\n <object id="1089" type="collision" x="1600" y="-40" width="40" height="1600" rotation="90"/>\n <object id="1090" type="collision" x="1600" y="1600" width="40" height="1600" rotation="90"/>\n""")
        f.write(""" </objectgroup>
</map>""")