import cv2
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import numpy as np
import numpy
import cv2
import glob
from PIL import Image,ImageDraw,ImageFont, ImageFilter
import cv2 as cv
import os
from os import listdir


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
            if j == Column_x - 1:
                points_cadre.append(imagette_filtrer.getdata()[somme])
            if i == 0:
                points_cadre.append(imagette_filtrer.getdata()[somme])
            if i == line_y - 1:
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

def determine_points_extremes(imagette_filtrer, pixel_rechercher, pos_val):
    Column_x, line_y = imagette_filtrer.size

    first_line = []

    for j in range(Column_x):
        if pixel_rechercher == 200:
            if pos_val[j][2] > pixel_rechercher:
                first_line.append(pos_val[j][0])
                first_line.append(pos_val[j][1])
                break
        else:
            if pos_val[j][2] < pixel_rechercher:
                first_line.append(pos_val[j][0])
                first_line.append(pos_val[j][1])
                break

    if not first_line:
        for j in range(Column_x):
            if pixel_rechercher == 200:
                if pos_val[j + Column_x][2] > pixel_rechercher:
                    first_line.append(pos_val[j + Column_x][0])
                    first_line.append(pos_val[j + Column_x][1])
                    break
            else:
                if pos_val[j + Column_x][2] < pixel_rechercher:
                    first_line.append(pos_val[j + Column_x][0])
                    first_line.append(pos_val[j + Column_x][1])
                    break
    if not first_line:
        for j in range(Column_x):
            if pixel_rechercher == 200:
                if pos_val[j + 2 * Column_x][2] > pixel_rechercher:
                    first_line.append(pos_val[j + 2 * Column_x][0])
                    first_line.append(pos_val[j + 2 * Column_x][1])
                    break
            else:
                if pos_val[j + 2 * Column_x][2] < pixel_rechercher:
                    first_line.append(pos_val[j + 2 * Column_x][0])
                    first_line.append(pos_val[j + 2 * Column_x][1])
                    break

    first_line_fin = []
    for j in range(Column_x):
        if pixel_rechercher == 200:
            if pos_val[Column_x - 1 - j][2] > pixel_rechercher:
                first_line_fin.append(pos_val[Column_x - 1 - j][0])
                first_line_fin.append(pos_val[Column_x - 1 - j][1])
                break
        else:
            if pos_val[Column_x - 1 - j][2] < pixel_rechercher:
                first_line_fin.append(pos_val[Column_x - 1 - j][0])
                first_line_fin.append(pos_val[Column_x - 1 - j][1])
                break
    if not first_line_fin:
        for j in range(Column_x):
            if pixel_rechercher == 200:
                if pos_val[2 * Column_x - 1 - j][2] > pixel_rechercher:
                    first_line_fin.append(pos_val[2 * Column_x - 1 - j][0])
                    first_line_fin.append(pos_val[2 * Column_x - 1 - j][1])
                    break
            else:
                if pos_val[2 * Column_x - 1 - j][2] < pixel_rechercher:
                    first_line_fin.append(pos_val[2 * Column_x - 1 - j][0])
                    first_line_fin.append(pos_val[2 * Column_x - 1 - j][1])
                    break
    if not first_line_fin:
        for j in range(Column_x):
            if pixel_rechercher == 200:
                if pos_val[3 * Column_x - 1 - j][2] > pixel_rechercher:
                    first_line_fin.append(pos_val[3 * Column_x - 1 - j][0])
                    first_line_fin.append(pos_val[3 * Column_x - 1 - j][1])
                    break
            else:
                if pos_val[3 * Column_x - 1 - j][2] < pixel_rechercher:
                    first_line_fin.append(pos_val[3 * Column_x - 1 - j][0])
                    first_line_fin.append(pos_val[3 * Column_x - 1 - j][1])
                    break

    last_line = []

    z = 0
    for j in range(Column_x):
        z = Column_x * line_y - Column_x + j
        if pixel_rechercher == 200:
            if pos_val[z][2] > pixel_rechercher:
                last_line.append(pos_val[z][0])
                last_line.append(pos_val[z][1])
                break
        else:
            if pos_val[z][2] < pixel_rechercher:
                last_line.append(pos_val[z][0])
                last_line.append(pos_val[z][1])
                break
    if not last_line:
        for j in range(Column_x):
            z = Column_x * line_y - 2 * Column_x + j
            if pixel_rechercher == 200:
                if pos_val[z][2] > pixel_rechercher:
                    last_line.append(pos_val[z][0])
                    last_line.append(pos_val[z][1])
                    break
            else:
                if pos_val[z][2] < pixel_rechercher:
                    last_line.append(pos_val[z][0])
                    last_line.append(pos_val[z][1])
                    break
    if not last_line:
        for j in range(Column_x):
            z = Column_x * line_y - 3 * Column_x + j
            if pixel_rechercher == 200:
                if pos_val[z][2] > pixel_rechercher:
                    last_line.append(pos_val[z][0])
                    last_line.append(pos_val[z][1])
                    break
            else:
                if pos_val[z][2] < pixel_rechercher:
                    last_line.append(pos_val[z][0])
                    last_line.append(pos_val[z][1])
                    break

    z = 0
    last_line_fin = []
    for j in range(1, Column_x + 1):
        z = Column_x * line_y - 1 * j
        if pixel_rechercher == 200:
            if pos_val[z][2] > pixel_rechercher:
                last_line_fin.append(pos_val[z][0])
                last_line_fin.append(pos_val[z][1])
                break
        else:
            if pos_val[z][2] < pixel_rechercher:
                last_line_fin.append(pos_val[z][0])
                last_line_fin.append(pos_val[z][1])
                break
    if not last_line_fin:
        for j in range(1, Column_x + 1):
            z = Column_x * line_y - 1 * j - Column_x
            if pixel_rechercher == 200:
                if pos_val[z][2] > pixel_rechercher:
                    last_line_fin.append(pos_val[z][0])
                    last_line_fin.append(pos_val[z][1])
                    break
            else:
                if pos_val[z][2] < pixel_rechercher:
                    last_line_fin.append(pos_val[z][0])
                    last_line_fin.append(pos_val[z][1])
                    break
    if not last_line_fin:
        for j in range(1, Column_x + 1):
            z = Column_x * line_y - 1 * j - 2 * Column_x
            if pixel_rechercher == 200:
                if pos_val[z][2] > pixel_rechercher:
                    last_line_fin.append(pos_val[z][0])
                    last_line_fin.append(pos_val[z][1])
                    break
            else:
                if pos_val[z][2] < pixel_rechercher:
                    last_line_fin.append(pos_val[z][0])
                    last_line_fin.append(pos_val[z][1])
                    break

    # print("first_line", first_line)
    # print("last_line", last_line)
    # print("first_line_fin", first_line_fin)
    # print("last_line_fin", last_line_fin)

    first_column = []
    z = 0
    for i in range(line_y):
        z = i * Column_x
        if pixel_rechercher == 200:
            if pos_val[z][2] > pixel_rechercher:
                first_column.append(pos_val[z][0])
                first_column.append(pos_val[z][1])
                break
        else:
            if pos_val[z][2] < pixel_rechercher:
                first_column.append(pos_val[z][0])
                first_column.append(pos_val[z][1])
                break
    if not first_column:
        for i in range(line_y):
            z = i * Column_x + 1
            if pixel_rechercher == 200:
                if pos_val[z][2] > pixel_rechercher:
                    first_column.append(pos_val[z][0])
                    first_column.append(pos_val[z][1])
                    break
            else:
                if pos_val[z][2] < pixel_rechercher:
                    first_column.append(pos_val[z][0])
                    first_column.append(pos_val[z][1])
                    break
    if not first_column:
        for i in range(line_y):
            z = i * Column_x + 2
            if pixel_rechercher == 200:
                if pos_val[z][2] > pixel_rechercher:
                    first_column.append(pos_val[z][0])
                    first_column.append(pos_val[z][1])
                    break
            else:
                if pos_val[z][2] < pixel_rechercher:
                    first_column.append(pos_val[z][0])
                    first_column.append(pos_val[z][1])
                    break

    first_column_fin = []
    z = 0
    for i in range(1, line_y + 1):
        z = Column_x * line_y - i * Column_x
        if pixel_rechercher == 200:
            if pos_val[z][2] > pixel_rechercher:
                first_column_fin.append(pos_val[z][0])
                first_column_fin.append(pos_val[z][1])
                break
        else:
            if pos_val[z][2] < pixel_rechercher:
                first_column_fin.append(pos_val[z][0])
                first_column_fin.append(pos_val[z][1])
                break
    if not first_column_fin:
        for i in range(1, line_y + 1):
            z = Column_x * line_y - i * Column_x + 1
            if pixel_rechercher == 200:
                if pos_val[z][2] > pixel_rechercher:
                    first_column_fin.append(pos_val[z][0])
                    first_column_fin.append(pos_val[z][1])
                    break
            else:
                if pos_val[z][2] < pixel_rechercher:
                    first_column_fin.append(pos_val[z][0])
                    first_column_fin.append(pos_val[z][1])
                    break
    if not first_column_fin:
        for i in range(1, line_y + 1):
            z = Column_x * line_y - i * Column_x + 2
            if pixel_rechercher == 200:
                if pos_val[z][2] > pixel_rechercher:
                    first_column_fin.append(pos_val[z][0])
                    first_column_fin.append(pos_val[z][1])
                    break
            else:
                if pos_val[z][2] < pixel_rechercher:
                    first_column_fin.append(pos_val[z][0])
                    first_column_fin.append(pos_val[z][1])
                    break

    z = 0
    last_column = []
    for i in range(1, line_y + 1):
        z = i * Column_x - 1
        if pixel_rechercher == 200:
            if pos_val[z][2] > pixel_rechercher:
                last_column.append(pos_val[z][0])
                last_column.append(pos_val[z][1])
                break
        else:
            if pos_val[z][2] < pixel_rechercher:
                last_column.append(pos_val[z][0])
                last_column.append(pos_val[z][1])
                break
    if not last_column:
        for i in range(1, line_y + 1):
            z = i * Column_x - 2
            if pixel_rechercher == 200:
                if pos_val[z][2] > pixel_rechercher:
                    last_column.append(pos_val[z][0])
                    last_column.append(pos_val[z][1])
                    break
            else:
                if pos_val[z][2] < pixel_rechercher:
                    last_column.append(pos_val[z][0])
                    last_column.append(pos_val[z][1])
                    break
    if not last_column:
        for i in range(1, line_y + 1):
            z = i * Column_x - 3
            if pixel_rechercher == 200:
                if pos_val[z][2] > pixel_rechercher:
                    last_column.append(pos_val[z][0])
                    last_column.append(pos_val[z][1])
                    break
            else:
                if pos_val[z][2] < pixel_rechercher:
                    last_column.append(pos_val[z][0])
                    last_column.append(pos_val[z][1])
                    break

    z = 0
    last_column_fin = []
    for i in range(line_y):
        z = Column_x * line_y - 1 - Column_x * i
        if pixel_rechercher == 200:
            if pos_val[z][2] > pixel_rechercher:
                last_column_fin.append(pos_val[z][0])
                last_column_fin.append(pos_val[z][1])
                break
        else:
            if pos_val[z][2] < pixel_rechercher:
                last_column_fin.append(pos_val[z][0])
                last_column_fin.append(pos_val[z][1])
                break
    if not last_column_fin:
        for i in range(line_y):
            z = Column_x * line_y - 2 - Column_x * i
            if pixel_rechercher == 200:
                if pos_val[z][2] > pixel_rechercher:
                    last_column_fin.append(pos_val[z][0])
                    last_column_fin.append(pos_val[z][1])
                    break
            else:
                if pos_val[z][2] < pixel_rechercher:
                    last_column_fin.append(pos_val[z][0])
                    last_column_fin.append(pos_val[z][1])
                    break
    if not last_column_fin:
        for i in range(line_y):
            z = Column_x * line_y - 3 - Column_x * i
            if pixel_rechercher == 200:
                if pos_val[z][2] > pixel_rechercher:
                    last_column_fin.append(pos_val[z][0])
                    last_column_fin.append(pos_val[z][1])
                    break
            else:
                if pos_val[z][2] < pixel_rechercher:
                    last_column_fin.append(pos_val[z][0])
                    last_column_fin.append(pos_val[z][1])
                    break
    point_haut = []
    if first_line == first_line_fin:
        point_haut = first_line
    else:
        point_haut.append((first_line[0] + first_line_fin[0]) / 2)
        point_haut.append((first_line[1] + first_line_fin[1]) / 2)

    point_bas = []
    if last_line == last_line_fin:
        point_bas = last_line
    else:
        point_bas.append((last_line[0] + last_line_fin[0]) / 2)
        point_bas.append((last_line[1] + last_line_fin[1]) / 2)

    point_gauche = []
    if first_column == first_column_fin:
        point_gauche = first_column
    else:
        point_gauche.append((first_column[0] + first_column_fin[0]) / 2)
        point_gauche.append((first_column[1] + first_column_fin[1]) / 2)

    point_droit = []
    if last_column == last_column_fin:
        point_droit = last_column
    else:
        point_droit.append((last_column[0] + last_column_fin[0]) / 2)
        point_droit.append((last_column[1] + last_column_fin[1]) / 2)

    point_coin_bd = []
    point_coin_hd = []
    point_coin_bg = []
    point_coin_hg = []

    if (
            last_line_fin == last_column_fin):  # or ((last_line_fin[0]+1 == last_column_fin[0]) and (last_line_fin[1] == last_column_fin[1]+1)):
        point_coin_bd = last_column_fin
    if (
            first_line_fin == last_column):  # or ((first_line_fin[0] == last_column[0]-1) and (first_line_fin[1]+1 == last_column[1])):
        point_coin_hd = first_line_fin

    if (
            last_line == first_column_fin):  # or ((first_column_fin[0]+1 == last_line[0]) and (first_column_fin[1] == last_line[1]-1)):
        point_coin_bg = first_column_fin
    if (
            first_line == first_column):  # or ((first_column[0] == first_line[0]-1) and (first_column[1]-1 == first_line[1])):
        point_coin_hg = first_column

    liste_points_extremes_final = []
    s = 0
    if point_coin_bg:
        s += 1
    if point_coin_bd:
        s += 1
    if point_coin_hg:
        s += 1
    if point_coin_hd:
        s += 1

    if s > 1:

        if (point_coin_hd and point_coin_bg):
            liste_points_extremes_final.append(point_coin_hd)
            liste_points_extremes_final.append(point_coin_bg)
            return liste_points_extremes_final
        else:
            liste_points_extremes_final.append(point_coin_bd)
            liste_points_extremes_final.append(point_coin_hg)
            return liste_points_extremes_final

    elif s == 1:
        if point_coin_bg:
            liste_points_extremes_final.append(point_coin_bg)
            liste_points_extremes_final.append(point_haut)
            liste_points_extremes_final.append(point_droit)
            return liste_points_extremes_final
        elif point_coin_bd:
            liste_points_extremes_final.append(point_coin_bd)
            liste_points_extremes_final.append(point_haut)
            liste_points_extremes_final.append(point_gauche)
            return liste_points_extremes_final
        elif point_coin_hg:
            liste_points_extremes_final.append(point_coin_hg)
            liste_points_extremes_final.append(point_bas)
            liste_points_extremes_final.append(point_droit)
            return liste_points_extremes_final
        else:
            liste_points_extremes_final.append(point_coin_hd)
            liste_points_extremes_final.append(point_bas)
            liste_points_extremes_final.append(point_gauche)
            return liste_points_extremes_final

    else:
        liste_points_extremes_final.append(point_haut)
        liste_points_extremes_final.append(point_bas)
        liste_points_extremes_final.append(point_gauche)
        liste_points_extremes_final.append(point_droit)
        return liste_points_extremes_final


def recherche_base(liste_points_extremes_final):
    distance = []
    distance_filtrer = []
    for point1 in liste_points_extremes_final:
        for point2 in liste_points_extremes_final:
            if point1 == point2:
                continue
            else:
                diff_carree_x = (point1[0] - point2[0]) ** 2
                diff_carree_y = (point1[1] - point2[1]) ** 2
                dist = (diff_carree_x + diff_carree_y) ** 0.5
                distance.append(dist)
    for d in distance:
        if d not in distance_filtrer:
            distance_filtrer.append(d)

    distance_min = min(distance_filtrer)
    distance_filtrer.sort()
    verif = 0
    base_fleche = []
    for point1 in liste_points_extremes_final:
        if verif != 0:
            break
        else:
            for point2 in liste_points_extremes_final:
                if verif != 0:
                    break
                else:
                    diff_carree_x = (point1[0] - point2[0]) ** 2
                    diff_carree_y = (point1[1] - point2[1]) ** 2
                    dist = (diff_carree_x + diff_carree_y) ** 0.5
                    if dist == distance_min:
                        base_fleche.append((point1[0] + point2[0]) / 2)
                        base_fleche.append((point1[1] + point2[1]) / 2)
                        verif += 1

    return base_fleche


def recherche_pointe(liste_points_extremes_final, base_fleche):
    distance0 = []
    distance = []
    distance_filtrer = []
    new_distance = []
    pointe = []

    if len(liste_points_extremes_final) == 4:
        for point1 in liste_points_extremes_final:
            for point2 in liste_points_extremes_final:
                if point1 == point2:
                    continue
                else:
                    diff_carree_x = (point1[0] - point2[0]) ** 2
                    diff_carree_y = (point1[1] - point2[1]) ** 2
                    dist = (diff_carree_x + diff_carree_y) ** 0.5
                    distance0.append(dist)
        for d in distance0:
            if d not in distance_filtrer:
                distance_filtrer.append(d)
        distance_minimum = min(distance_filtrer)

        for point1 in liste_points_extremes_final:
            for point2 in liste_points_extremes_final:
                if point1 == point2:
                    continue
                else:
                    diff_carree_x = (point1[0] - point2[0]) ** 2
                    diff_carree_y = (point1[1] - point2[1]) ** 2
                    dist = (diff_carree_x + diff_carree_y) ** 0.5
                    if dist == distance_minimum:
                        if (point1 == liste_points_extremes_final[0] and point2 == liste_points_extremes_final[1])or(point1 == liste_points_extremes_final[1] and point2 == liste_points_extremes_final[0]):

                            diff_carree_x = (base_fleche[0] - liste_points_extremes_final[2][0]) ** 2
                            diff_carree_y = (base_fleche[1] - liste_points_extremes_final[2][1]) ** 2
                            dist1 = (diff_carree_x + diff_carree_y) ** 0.5
                            diff_carree_x = (base_fleche[0] - liste_points_extremes_final[3][0]) ** 2
                            diff_carree_y = (base_fleche[1] - liste_points_extremes_final[3][1]) ** 2
                            dist2 = (diff_carree_x + diff_carree_y) ** 0.5
                            new_distance.append(dist1)
                            if dist1 > dist2:
                                pointe = liste_points_extremes_final[3]
                                return pointe
                            else:
                                pointe = liste_points_extremes_final[2]
                                return pointe
                        elif (point1 == liste_points_extremes_final[2] and point2 == liste_points_extremes_final[3])or(point1 == liste_points_extremes_final[3] and point2 == liste_points_extremes_final[2]):

                            diff_carree_x = (base_fleche[0] - liste_points_extremes_final[0][0]) ** 2
                            diff_carree_y = (base_fleche[1] - liste_points_extremes_final[0][1]) ** 2
                            dist1 = (diff_carree_x + diff_carree_y) ** 0.5
                            diff_carree_x = (base_fleche[0] - liste_points_extremes_final[1][0]) ** 2
                            diff_carree_y = (base_fleche[1] - liste_points_extremes_final[1][1]) ** 2
                            dist2 = (diff_carree_x + diff_carree_y) ** 0.5
                            new_distance.append(dist1)
                            if dist1 > dist2:
                                pointe = liste_points_extremes_final[1]
                                return pointe
                            else:
                                pointe = liste_points_extremes_final[0]
                                return pointe
    if len(pointe) == 0:
        for point1 in liste_points_extremes_final:
            if point1 != base_fleche:
                diff_carree_x = (point1[0] - base_fleche[0]) ** 2
                diff_carree_y = (point1[1] - base_fleche[1]) ** 2
                dist = (diff_carree_x + diff_carree_y) ** 0.5
                distance.append(dist)
        distance_miximum = max(distance)
        for point1 in liste_points_extremes_final:
            if point1 != base_fleche:
                diff_carree_x = (point1[0] - base_fleche[0]) ** 2
                diff_carree_y = (point1[1] - base_fleche[1]) ** 2
                dist = (diff_carree_x + diff_carree_y) ** 0.5
                if dist == distance_miximum:
                    pointe.append(point1[0])
                    pointe.append(point1[1])
                    return pointe



