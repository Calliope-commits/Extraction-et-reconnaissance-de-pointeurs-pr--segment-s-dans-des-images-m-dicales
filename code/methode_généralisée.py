import cv2
import numpy as np
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

def preprocessing(imagette):
    img = Image.open(imagette).convert("1")
    imagette_filtrer = img.filter(ImageFilter.MedianFilter(size=3))
    return imagette_filtrer



def determine_couleur_contour(imagette_filtrer):
    Column_x, line_y = imagette_filtrer.size
    # print(Column_x, line_y)

    pix_val = list(
        imagette_filtrer.getdata())  # Ca permet d'avoir les valeurs de chaque pixel de gauche vers la droite a partir du point(0,0)
    # print(pix_val)
    points_cadre = []
    pos_val = []
    somme = 0
    for i in range(line_y):
        for j in range(Column_x):
            pos_val.append([j, i, imagette_filtrer.getdata()[somme]])
            if j == 0:
                points_cadre.append(imagette_filtrer.getdata()[somme])
            if j == Column_x-1:
                points_cadre.append(imagette_filtrer.getdata()[somme])
            if i == 0:
                points_cadre.append(imagette_filtrer.getdata()[somme])
            if i == line_y-1:
                points_cadre.append(imagette_filtrer.getdata()[somme])

            somme += 1
    pos_val = np.array(pos_val)  # cette matrice va servir a conserver les valeurs de chaque pixel avec sa position

    # print(pos_val[h*38+7])
    # print(pos_val)

    som0 = 0
    som1 = 0
    for i in points_cadre:
        if i < 200:
            som0 += 1
        else:
            som1 += 1
    if som0 > som1:
        pixel_rechercher = 200
    else:
        pixel_rechercher = 10

    return pixel_rechercher, pos_val



def determine_liste_points_extremes(imagette_filtrer, pixel_rechercher, pos_val):
    liste_points_extremes_final = []
    liste_points_extremes = []
    Column_x, line_y = imagette_filtrer.size
    a, b = np.shape(pos_val)
    for i in range(a):
        if pixel_rechercher == 200:
            if pos_val[i][0] == 0 and pos_val[i][2] > 200:
                liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
            else:
                if pos_val[i][0] == 1 and pos_val[i][2] > 200:
                    liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
            if pos_val[i][1] == 0 and pos_val[i][2] > 200:
                liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
            else:
                if pos_val[i][1] == 1 and pos_val[i][2] > 200:
                    liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])

            if pos_val[i][0] == Column_x-1 and pos_val[i][2] > 200:
                liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
            else:
                if pos_val[i][0] == Column_x-2 and pos_val[i][2] > 200:
                    liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
            if pos_val[i][1] == line_y-1 and pos_val[i][2] > 200:
                liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
            else:
                if pos_val[i][1] == line_y-2 and pos_val[i][2] > 200:
                    liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
        else:

            if pos_val[i][0] == 0 and pos_val[i][2] < 10:
                liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
            else:
                if pos_val[i][0] == 1 and pos_val[i][2] < 10:
                    liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
            if pos_val[i][1] == 0 and pos_val[i][2] < 10:
                liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
            else:
                if pos_val[i][1] == 1 and pos_val[i][2] < 10:
                    liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])

            if pos_val[i][0] == Column_x - 1 and pos_val[i][2] < 10:
                liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
            else:
                if pos_val[i][0] == Column_x - 2 and pos_val[i][2] < 10:
                    liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
            if pos_val[i][1] == line_y - 1 and pos_val[i][2] < 10:
                liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])
            else:
                if pos_val[i][1] == line_y - 2 and pos_val[i][2] < 10:
                    liste_points_extremes.append([pos_val[i][0], pos_val[i][1]])


    for p in liste_points_extremes:
        if p not in liste_points_extremes_final:
            liste_points_extremes_final.append(p) #Pour eviter d'avoir des points répététifs

    liste_points_extremes_final = np.array(liste_points_extremes_final)
    return liste_points_extremes_final



def recherche_base(liste_points_extremes_final):
    ligne, colonne = np.shape(liste_points_extremes_final)
    # print(ligne, colonne)
    distance = []
    distance_filtrer = []

    # Dans cette partie, on va enlever les coordonnées ayant une distance inferieur a 7 pour eviter de confondre avec la base
    for point in liste_points_extremes_final:
        for i in range(ligne):
            diff_carree_x = (point[0] - liste_points_extremes_final[i][0]) ** 2
            diff_carree_y = (point[1] - liste_points_extremes_final[i][1]) ** 2
            dist = (diff_carree_x + diff_carree_y) ** 0.5
            if dist < 7:
                liste_points_extremes_final[i][0] = point[0]
                liste_points_extremes_final[i][1] = point[1]
            else:
                if liste_points_extremes_final[i][0] - 1 == liste_points_extremes_final[i - 1][0]:
                    liste_points_extremes_final[i][0] = point[0]
                    liste_points_extremes_final[i][1] = point[1]

                if liste_points_extremes_final[i][1] - 1 == liste_points_extremes_final[i - 1][1]:
                    liste_points_extremes_final[i][0] = point[0]
                    liste_points_extremes_final[i][1] = point[1]

    points_ex = np.array(liste_points_extremes_final)
    # print(points_ex)

    for point in points_ex:
        for i in range(ligne):
            diff_carree_x = (point[0] - points_ex[i][0]) ** 2
            diff_carree_y = (point[1] - points_ex[i][1]) ** 2
            dist = (diff_carree_x + diff_carree_y) ** 0.5
            distance.append(dist)
    # print(distance)

    for element in distance:
        if element not in distance_filtrer:
            distance_filtrer.append(element)

    distance_filtrer.remove(0)
    # print(distance_filtrer)
    distance_minimum = min(distance_filtrer)
    Base = []
    B = []
    A = []
    # On va garder seulement les coordonnées qui ont réaliser une distance minimum
    for point in points_ex:
        for i in range(ligne):
            diff_carree_x = (point[0] - points_ex[i][0]) ** 2
            diff_carree_y = (point[1] - points_ex[i][1]) ** 2
            dist = (diff_carree_x + diff_carree_y) ** 0.5

            if distance_minimum == dist:
                B.append(points_ex[i][0])
                B.append(points_ex[i][1])
                A.append(point[0])
                A.append(point[1])
                break
    Base.append(B[0])
    Base.append(B[1])
    Base.append(A[0])
    Base.append(A[1])

    # print(Base)
    # premier point
    X1 = Base[0]
    Y1 = Base[1]
    # 2eme point
    X2 = Base[2]
    Y2 = Base[3]

    # Calcul des coordonnées du nouveau point

    X3 = (X1 + X2) / 2
    Y3 = (Y1 + Y2) / 2
    # print(X3, Y3)
    base_fleche = []
    base_fleche.append(X3)
    base_fleche.append(Y3)
    # on rajoute X3 et Y3 dans la liste des points_ex
    return base_fleche


def recherche_pointe(liste_points_extremes_final, base_fleche):
    ligne, colonne = np.shape(liste_points_extremes_final)
    new_distance = []
    for i in range(ligne):
        diff_carree_x = (base_fleche[0] - liste_points_extremes_final[i][0]) ** 2
        diff_carree_y = (base_fleche[1] - liste_points_extremes_final[i][1]) ** 2
        dist = (diff_carree_x + diff_carree_y) ** 0.5
        new_distance.append(dist)

    distance_maximum = max(new_distance)

    pointe = []

    for i in range(ligne):#on cherche maintenant la distance max afin de trouver la pointe
        diff_carree_x = (base_fleche[0] - liste_points_extremes_final[i][0]) ** 2
        diff_carree_y = (base_fleche[1] - liste_points_extremes_final[i][1]) ** 2
        dist = (diff_carree_x + diff_carree_y) ** 0.5

        if distance_maximum == dist:
            pointe.append(liste_points_extremes_final[i][0])
            pointe.append(liste_points_extremes_final[i][1])

            break
    return pointe

def affichage_direction(imagette, base_fleche, pointe):
    img = cv2.imread(imagette, )
    img = cv2.medianBlur(img, 3)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    img = cv2.arrowedLine(img, (int(base_fleche[0]), int(base_fleche[1])), (int(pointe[0]), int(pointe[1])), (255, 0, 0), 1)
    plt.imshow(img)
    plt.show()


