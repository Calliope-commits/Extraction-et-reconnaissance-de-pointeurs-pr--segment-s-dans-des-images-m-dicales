import methode_généralisée
import Flèche
import ROI
import os


def get_imagette():
    return imagette


mypath = "stock2/ImgE128859.jpg.pgmCC"
names = os.listdir(path=mypath)
image = "ref_data_set/E128859.jpg.pgm.png"
for imagette in names:
   """" if imagette == "infos.txt":
        names.remove(imagette)
        continue"""

    imagette_filtrer = methode_généralisée.preprocessing(imagette)
    imagette = get_imagette()
    pixel_rechercher, pos_val = methode_généralisée.determine_couleur_contour(imagette_filtrer)

    liste_points_extremes_final = Flèche.determine_points_extremes(imagette_filtrer, pixel_rechercher, pos_val)

    if len(liste_points_extremes_final) == 2:
        base_fleche = methode_généralisée.recherche_base(liste_points_extremes_final)
        pointe = methode_généralisée.recherche_pointe(liste_points_extremes_final, base_fleche)
    else:
        base_fleche = Flèche.recherche_base(liste_points_extremes_final)
        pointe = Flèche.recherche_pointe(liste_points_extremes_final, base_fleche)

    methode_généralisée.affichage_direction(imagette, base_fleche, pointe)
    Base_X = base_fleche[0]
    Base_Y = base_fleche[1]
    Pointe_X = pointe[0]
    Pointe_Y = pointe[1]
    ROI.Affichage_ROI(imagette, Base_X, Base_Y, Pointe_X, Pointe_Y, image)
    ROI.Extraction_ROI_originale(image)
    ROI.traitement_ROI_egalisation(image)
    ROI.traitement_ROI_filtre_median(image)
    ROI.traitement_ROI_highpass(image)
    ROI.traitement_ROI_contours(image)
