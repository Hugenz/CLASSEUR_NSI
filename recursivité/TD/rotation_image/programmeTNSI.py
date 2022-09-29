from boite_a_outils_2021 import *


def rotate(img, x, y, width):
    if width > 1:

        width = width // 2
        for i in range(y, y + width):
            for j in range(x, x + width):
                pixtemp = img[i][j]
                img[i][j] = img[i + width][j]
                img[i + width][j] = img[i + width][j + width]
                img[i + width][j + width] = img[i][j + width]
                img[i][j + width] = pixtemp

        rotate(img, x, y, width)
        rotate(img, x + width, y, width)
        rotate(img, x + width, y + width, width)
        rotate(img, x, y + width, width)

    return img

# ------------------Programme principal


image=lire_image_P3('images/imagetest.pnm')
hauteur=len(image)
image2 = rotate(image, 0, 0, hauteur)

creer_image_P3(image,'images/imagetest2.pnm')




