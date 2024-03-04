from PIL import Image
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