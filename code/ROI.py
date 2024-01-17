import cv2
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import numpy as np
import numpy
import cv2
import glob
from PIL import Image,ImageDraw,ImageFont
import cv2 as cv
import os
from os import listdir

import cv2




maliste = []
liste_rayon = []
liste_centre = []
liste_rect = []


def Affichage_ROI(imagette, Base_X, Base_Y, Pointe_X, Pointe_Y, image):

    b = imagette.split(", ")
    c = []
    for i in b:
        c.append(i.split("["))
    p = c[0]
    i = p[1]
    imagette_split1 = imagette.split(", ")
    imagette_split2 = []
    for X in imagette_split1:
        imagette_split2.append(X.split("["))
    p1 = imagette_split2[0]
    p2 = imagette_split2[1]
    X = float(p1[1])
    Y = float(p2[0])

    diff_carree_x = (Pointe_X - Base_X) ** 2
    diff_carree_y = (Pointe_X - Base_Y) ** 2
    Rayon = (diff_carree_x + diff_carree_y) ** 0.5
    img = cv2.imread(image, )
    img = cv2.medianBlur(img, 3)
    Coordonnee_Centre_X = 2*Pointe_X-Base_X+X
    Coordonnee_Centre_Y = 2*Pointe_Y-Base_Y+Y
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    alt = cv2.arrowedLine(img, (int(X+Base_X), int(Y+Base_Y)), (int(Coordonnee_Centre_X), int(Coordonnee_Centre_Y)), (255, 0, 0), 1)
    cercle = cv2.circle(img, (int(Coordonnee_Centre_X), int(Coordonnee_Centre_Y)), int(Rayon), (255, 255, 0), 5)
    #plt.imshow(alt)
    #plt.imshow(cercle)
    plt.show()

    maliste.append(Coordonnee_Centre_X)
    maliste.append(Coordonnee_Centre_Y)
    maliste.append(Rayon)

    liste_rayon.append(Rayon)

    liste_centre.append(Coordonnee_Centre_X)
    liste_centre.append(Coordonnee_Centre_Y)

    liste_rect.append(Coordonnee_Centre_X - int(Rayon) - 1)
    liste_rect.append(Coordonnee_Centre_X + int(Rayon) + 1)

    liste_rect.append(Coordonnee_Centre_Y - int(Rayon) - 1)
    liste_rect.append(Coordonnee_Centre_Y + int(Rayon) + 1)



#print(ROI())



def Extraction_ROI_originale(image):

    src = cv2.imread(image, )
    img = cv2.medianBlur(src, 3)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    i = 0
    p = 0
    max_rayon = liste_rayon[0]
    min_rayon = liste_rayon[0]
    for r in liste_rayon:
        if max_rayon < r:
            max_rayon = r
        if min_rayon > r:
            min_rayon = r

    for j in range(len(maliste)):
        X = maliste[i]
        Y = maliste[i + 1]
        R = maliste[i + 2]
        cercle = cv2.circle(img, (int(X), int(Y)), int(R), (255, 255, 0), 5)
        i += 3

        if i == len(maliste):
            plt.imshow(cercle)
        #   k = cv2.waitKey(0)
        #   if k == ord("s"):
            cv.imwrite("les_cercles.png", cercle)

            plt.show()
            break


    color = (55, 255, 255)
    image_height, image_width, number_of_color_channels = img.shape
    pixel_array = numpy.full((image_height, image_width, number_of_color_channels), color, dtype=numpy.uint8)
    for j in range(len(maliste)):
        Xr_debut = liste_rect[p]
        Xr_fin = liste_rect[p+1]
        Yr_debut = liste_rect[p+2]
        Yr_fin = liste_rect[p+3]
        p += 4
        img = cv.imread(image)
        #img = cv.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #img = highpass(img, 3)

        img_highpass = highpass(img,3)
        img_edges = detection_contours(img)
        img_egualisation = egalisation_hist(img)


        ROI = img[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)]


        #cv.imshow("roi", ROI)
        #cv.waitKey()

        #cv.destroyAllWindows()

        pixel_array[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)] = ROI

        cv.imwrite("derniere.png", pixel_array)

        if p == len(liste_rect):

            break

    image_ROIs = cv.imread("derniere.png")
    #imS = cv.resize(image_ROIs, (400,400))

    #cv.imshow("image_ROIs", imS)

    #cv.waitKey(0)
    return pixel_array



def traitement_ROI_egalisation(image):
    img = Extraction_ROI_originale(image)
    img_out = egalisation_hist(img)
    #img_out = img - cv2.GaussianBlur(img, (0, 0), sigma) + 127
    for j in range(len(maliste)):

        cv.imshow("Egalisation", img_out)  # affiche les ROI une à une


        cv.destroyAllWindows()


        cv.imwrite("derniere.png", img_out)



    image_ROIs = cv.imread("derniere.png")
    imS = cv.resize(image_ROIs, (400, 400))

    cv.imshow("ROI-Egalisation Histogramme", imS)

    cv.waitKey(0)

"""
    cpt = 0
    src = cv2.imread(image, )
    img = cv2.medianBlur(src, 3)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    i = 0
    p = 0
    max_rayon = liste_rayon[0]
    min_rayon = liste_rayon[0]
    for r in liste_rayon:
        if max_rayon < r:
            max_rayon = r
        if min_rayon > r:
            min_rayon = r

    for j in range(len(maliste)):
        X = maliste[i]
        Y = maliste[i + 1]
        R = maliste[i + 2]
        cercle = cv2.circle(img, (int(X), int(Y)), int(R), (255, 255, 0), 5)
        i += 3

        if i == len(maliste):
            plt.imshow(cercle)
        #   k = cv2.waitKey(0)
        #   if k == ord("s"):
            cv.imwrite("les_cercles.png", cercle)

            plt.show()
            break


    color = (55, 255, 255)
    image_height, image_width, number_of_color_channels = img.shape
    pixel_array = numpy.full((image_height, image_width, number_of_color_channels), color, dtype=numpy.uint8)
    for j in range(len(maliste)):
        Xr_debut = liste_rect[p]
        Xr_fin = liste_rect[p+1]
        Yr_debut = liste_rect[p+2]
        Yr_fin = liste_rect[p+3]
        p += 4
        img = cv.imread(image)
        #img = cv.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #img = highpass(img, 3)

        #img_seuillage = seuillage(img)
        #ROI = img[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)]

        ROI_equi = equalize_ROI(img[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)])


        #cv.imshow("roi", ROI)
        #cv.waitKey()
        cv.imshow("Egalisation Histogramme", ROI_equi) #affiche les ROI une à une

        #cv.destroyAllWindows()

        pixel_array[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)] = ROI_equi
        cv.imwrite("derniere.png", pixel_array)

        if p == len(liste_rect):

            break

    image_ROIs = cv.imread("derniere.png")
    imS = cv.resize(image_ROIs, (400,400))

    cv.imshow("ROI-Egalisation Histogramme", imS)

    cv.waitKey(0)

"""

def traitement_ROI_highpass(image):
    img = Extraction_ROI_originale(image)
    img_out = highpass(img,3)
    #img_out = img - cv2.GaussianBlur(img, (0, 0), sigma) + 127
    for j in range(len(maliste)):

        cv.imshow("High pass", img_out)  # affiche les ROI une à une


        cv.destroyAllWindows()


        cv.imwrite("derniere.png", img_out)



    image_ROIs = cv.imread("derniere.png")
    imS = cv.resize(image_ROIs, (400, 400))

    cv.imshow("ROI-Highpass", imS)

    cv.waitKey(0)


"""

    cpt = 0
    src = cv2.imread(image, )
    img = cv2.medianBlur(src, 3)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    i = 0
    p = 0
    max_rayon = liste_rayon[0]
    min_rayon = liste_rayon[0]
    for r in liste_rayon:
        if max_rayon < r:
            max_rayon = r
        if min_rayon > r:
            min_rayon = r

    for j in range(len(maliste)):
        X = maliste[i]
        Y = maliste[i + 1]
        R = maliste[i + 2]
        cercle = cv2.circle(img, (int(X), int(Y)), int(R), (255, 255, 0), 5)
        i += 3

        if i == len(maliste):
            plt.imshow(cercle)
        #   k = cv2.waitKey(0)
        #   if k == ord("s"):
            cv.imwrite("les_cercles.png", cercle)

            plt.show()
            break


    color = (55, 255, 255)
    image_height, image_width, number_of_color_channels = img.shape
    pixel_array = numpy.full((image_height, image_width, number_of_color_channels), color, dtype=numpy.uint8)
    for j in range(len(maliste)):
        Xr_debut = liste_rect[p]
        Xr_fin = liste_rect[p+1]
        Yr_debut = liste_rect[p+2]
        Yr_fin = liste_rect[p+3]
        p += 4
        img = cv.imread(image)
        #img = cv.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #img = highpass(img, 3)

        #img_seuillage = seuillage(img)
        #ROI = img[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)]

        ROI_highpass = highpass(img[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)],3)


        #cv.imshow("roi", ROI)
        #cv.waitKey()
        cv.imshow("High pass", ROI_highpass) #affiche les ROI une à une
        cv.waitKey()

        #cv.destroyAllWindows()

        pixel_array[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)] = ROI_highpass
        cv.imwrite("derniere.png", pixel_array)

        if p == len(liste_rect):

            break

    image_ROIs = cv.imread("derniere.png")
    imS = cv.resize(image_ROIs, (400,400))

    cv.imshow("ROI-Highpass", imS)

    cv.waitKey(0)
"""




def traitement_ROI_filtre_median(image):
    img = Extraction_ROI_originale(image)

    img_out = cv2.medianBlur(img,3)
    for j in range(len(maliste)):
        cv.imshow("Filtre Median", img_out)  # affiche les ROI une à une

        cv.destroyAllWindows()

        cv.imwrite("derniere.png", img_out)

    image_ROIs = cv.imread("derniere.png")
    imS = cv.resize(image_ROIs, (400, 400))

    cv.imshow("ROI-Filtre Median", imS)

    cv.waitKey(0)
"""

    cpt = 0
    src = cv2.imread(image, )
    img = cv2.medianBlur(src, 3)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    i = 0
    p = 0
    max_rayon = liste_rayon[0]
    min_rayon = liste_rayon[0]
    for r in liste_rayon:
        if max_rayon < r:
            max_rayon = r
        if min_rayon > r:
            min_rayon = r

    for j in range(len(maliste)):
        X = maliste[i]
        Y = maliste[i + 1]
        R = maliste[i + 2]
        cercle = cv2.circle(img, (int(X), int(Y)), int(R), (255, 255, 0), 5)
        i += 3

        if i == len(maliste):
            plt.imshow(cercle)
        #   k = cv2.waitKey(0)
        #   if k == ord("s"):
            cv.imwrite("les_cercles.png", cercle)

            plt.show()
            break


    color = (55, 255, 255)
    image_height, image_width, number_of_color_channels = img.shape
    pixel_array = numpy.full((image_height, image_width, number_of_color_channels), color, dtype=numpy.uint8)
    for j in range(len(maliste)):
        Xr_debut = liste_rect[p]
        Xr_fin = liste_rect[p+1]
        Yr_debut = liste_rect[p+2]
        Yr_fin = liste_rect[p+3]
        p += 4
        img = cv.imread(image)
        #img = cv.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #img = highpass(img, 3)

        #img_seuillage = seuillage(img)
        #ROI = img[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)]

        ROI_median = cv.medianBlur(img[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)],3)


        #cv.imshow("roi", ROI)
        #cv.waitKey()
        cv.imshow("Filtre Median", ROI_median) #affiche les ROI une à une

        cv.destroyAllWindows()

        pixel_array[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)] = ROI_median
        cv.imwrite("derniere.png", pixel_array)

        if p == len(liste_rect):

            break

    image_ROIs = cv.imread("derniere.png")
    imS = cv.resize(image_ROIs, (400,400))

    cv.imshow("ROI-filtre median", imS)

    cv.waitKey(0)
"""

def traitement_ROI_contours(image):
    img = Extraction_ROI_originale(image)

    img_out = detection_contours(img)
    for j in range(len(maliste)):
        cv.imshow("Filtre contours", img_out)  # affiche les ROI une à une

        cv.destroyAllWindows()

        cv.imwrite("derniere.png", img_out)

    image_ROIs = cv.imread("derniere.png")
    imS = cv.resize(image_ROIs, (400, 400))

    cv.imshow("ROI-Filtre contours", imS)

    cv.waitKey(0)

"""
    cpt = 0
    src = cv2.imread(image, )
    img = cv2.medianBlur(src, 3)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    i = 0
    p = 0
    max_rayon = liste_rayon[0]
    min_rayon = liste_rayon[0]
    for r in liste_rayon:
        if max_rayon < r:
            max_rayon = r
        if min_rayon > r:
            min_rayon = r

    for j in range(len(maliste)):
        X = maliste[i]
        Y = maliste[i + 1]
        R = maliste[i + 2]
        cercle = cv2.circle(img, (int(X), int(Y)), int(R), (255, 255, 0), 5)
        i += 3

        if i == len(maliste):
            plt.imshow(cercle)
        #   k = cv2.waitKey(0)
        #   if k == ord("s"):
            cv.imwrite("les_cercles.png", cercle)

            plt.show()
            break


    color = (55, 255, 255)
    image_height, image_width, number_of_color_channels = img.shape
    pixel_array = numpy.full((image_height, image_width, number_of_color_channels), color, dtype=numpy.uint8)
    for j in range(len(maliste)):
        Xr_debut = liste_rect[p]
        Xr_fin = liste_rect[p+1]
        Yr_debut = liste_rect[p+2]
        Yr_fin = liste_rect[p+3]
        p += 4
        img = cv.imread(image)
        #img = cv.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #img = highpass(img, 3)

        #img_seuillage = seuillage(img)
        #ROI = img[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)]

        ROI_contours = detection_contours(img[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)])


        #cv.imshow("roi", ROI)
        #
        cv.imshow("Contours", ROI_contours) #affiche les ROI une à une
        cv.waitKey()
        cv.destroyAllWindows()

        pixel_array[int(Yr_debut):int(Yr_fin), int(Xr_debut):int(Xr_fin)] = ROI_contours
        cv.imwrite("derniere.png", pixel_array)

        if p == len(liste_rect):

            break

    image_ROIs = cv.imread("derniere.png")
    imS = cv.resize(image_ROIs, (400,400))

    cv.imshow("ROI-Contours", imS)

    cv.waitKey(0)"""


def highpass(img, sigma):
    return img - cv2.GaussianBlur(img, (0, 0), sigma) + 127


def egalisation_hist(img_in):
    #source : https://towardsdatascience.com/histogram-equalization-a-simple-way-to-improve-the-contrast-of-your-image-bcd66596d815
    # segregate color streams
    b, g, r = cv2.split(img_in)
    h_b, bin_b = np.histogram(b.flatten(), 256, [0, 256])
    h_g, bin_g = np.histogram(g.flatten(), 256, [0, 256])
    h_r, bin_r = np.histogram(r.flatten(), 256, [0, 256])
    # calculate cdf
    cdf_b = np.cumsum(h_b)
    cdf_g = np.cumsum(h_g)
    cdf_r = np.cumsum(h_r)

    # mask all pixels with value=0 and replace it with mean of the pixel values
    cdf_m_b = np.ma.masked_equal(cdf_b, 0)
    cdf_m_b = (cdf_m_b - cdf_m_b.min()) * 255 / (cdf_m_b.max() - cdf_m_b.min())
    cdf_final_b = np.ma.filled(cdf_m_b, 0).astype('uint8')

    cdf_m_g = np.ma.masked_equal(cdf_g, 0)
    cdf_m_g = (cdf_m_g - cdf_m_g.min()) * 255 / (cdf_m_g.max() - cdf_m_g.min())
    cdf_final_g = np.ma.filled(cdf_m_g, 0).astype('uint8')


    cdf_m_r = np.ma.masked_equal(cdf_r, 0)
    cdf_m_r = (cdf_m_r - cdf_m_r.min()) * 255 / (cdf_m_r.max() - cdf_m_r.min())
    cdf_final_r = np.ma.filled(cdf_m_r, 0).astype('uint8')
    # merge the images in the three channels
    img_b = cdf_final_b[b]
    img_g = cdf_final_g[g]
    img_r = cdf_final_r[r]

    img_out = cv2.merge((img_b, img_g, img_r))
    # validation
    equ_b = cv2.equalizeHist(b)
    equ_g = cv2.equalizeHist(g)
    equ_r = cv2.equalizeHist(r)
    equ = cv2.merge((equ_b, equ_g, equ_r))
    # print(equ)
    # cv2.imwrite('output_name.png', equ)
    return img_out

#on utilise un filtre de sobel
def detection_contours(img):
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = img
    x = cv2.Sobel(gray,  cv.CV_64F,1, 0, ksize=3, scale=1)
    y = cv2.Sobel(gray, cv.CV_64F, 0, 1, ksize=3, scale=1)
    absx = cv2.convertScaleAbs(x)
    absy = cv2.convertScaleAbs(y)
    edge = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)

    return edge

