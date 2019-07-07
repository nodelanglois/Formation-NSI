# Christophe Nodé-Langlois
import PIL
from PIL import Image # Pour lire et écrire des images dans un fichier


def noircissement(image) :
    #recuperation des dimensions
    (xmax,ymax) = image.size
    #parcours de l’image
    for x in range(xmax):
        for y in range(ymax):
            #recuperation du pixel
            px = image.getpixel((x,y))
            (r,g,b) = px
            #noircissement du pixel
            px2 = (r//2, g//2, b//2)
            image.putpixel((x,y), px2)



def eclaircir(image) :
    #recuperation des dimensions
    (xmax,ymax) = image.size
    #parcours de l’image
    for x in range(xmax):
        for y in range(ymax):
            #recuperation du pixel
            px = image.getpixel((x,y))
            (r,g,b) = px
            #noircissement du pixel
            px2 = (r*2, g*2, b*2)
            image.putpixel((x,y), px2)


def negatif(image) :
    #recuperation des dimensions
    (xmax,ymax) = image.size
    #parcours de l’image
    for x in range(xmax):
        for y in range(ymax):
            #recuperation du pixel
            px = image.getpixel((x,y))
            (r,g,b) = px
            #noircissement du pixel
            px2 = (256-r, 256-g, 256-b)
            image.putpixel((x,y), px2)


def flip_h(image) :
    #recuperation des dimensions
    (xmax,ymax) = image.size
    # image vide temporaire
    temps = [["" for x in range(xmax)] for y in range(ymax)]
    #parcours de l’image
    for x in range(xmax):
        for y in range(ymax):
            #recuperation du pixel
            px = image.getpixel((x, y))
            temps[x][y]=px
    for x in range(xmax):
        for y in range(ymax):
            image.putpixel((x, y), temps[x][ymax-y-1])

def flip_v(image) :
    #recuperation des dimensions
    (xmax, ymax) = image.size
    # image vide temporaire
    temps = [["" for x in range(xmax)] for y in range(ymax)]
    #parcours de l’image
    for x in range(xmax):
        for y in range(ymax):
            #recuperation du pixel
            px = image.getpixel((x, y))
            temps[x][y]=px
    for x in range(xmax):
        for y in range(ymax):
            image.putpixel((x, y), temps[xmax-x-1][y])


def rot90(image) :
    #recuperation des dimensions
    (xmax, ymax) = image.size
    # image vide temporaire
    temps = [["" for x in range(xmax)] for y in range(ymax)]
    #parcours de l’image
    for x in range(xmax):
        for y in range(ymax):
            #recuperation du pixel
            px = image.getpixel((x, y))
            temps[x][y] = px
    # rrotation de l'image
    for x in range(xmax):
        for y in range(ymax):
            image.putpixel((ymax-y-1, x), temps[x][y])


def supperposition(Image1, Image2) :
    image1 = Image.open("TP_images/"+Image1)
    image2 = Image.open("TP_images/"+Image2)
    #recuperation des dimensions
    (xmax,ymax) = image.size
    #parcours de l’image
    for x in range(xmax):
        for y in range(ymax):
            #moyenne des pixels
            px = (image1.getpixel((x, y))[0] + image2.getpixel((x, y))[0])//2, 
                 (image1.getpixel((x, y))[1] + image2.getpixel((x, y))[1])//2,
                 (image1.getpixel((x, y))[2] + image2.getpixel((x, y))[2])//2
            (r,g,b) = px
            image.putpixel((x, y), px)


image = Image.open("TP_images/peppers.jpg")
#noircissement(image)
#eclaircir(image)
#flip_h(image)
#flip_v(image)
rot90(image)
#supperposition("peppers.jpg", "flare.jpg")

image.show()
