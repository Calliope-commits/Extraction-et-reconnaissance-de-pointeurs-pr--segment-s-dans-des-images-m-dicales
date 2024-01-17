import methode_généralisée

names = ["arrow11.png","arrow22.png","arrow33.png","arrow44.png","arrow55.png","arrow66.png","arrow1.png","arrow2.png","arrow3.png","arrow4.png","arrow5.png","arrow6.png", "[803, 999, 119, 51, 1996]CC1.png", "[799, 995, 127, 58, 1134]CC11.png",
         "[1077, 196, 61, 45, 1378]CC2.png","[1049, 1328, 99, 95, 1915]CC13.png", "[1026, 954, 26, 44, 568]CC27.png","[1008, 1259, 24, 111, 1135]CC13.png",
         "[1256, 940, 30, 44, 570]CC26.png", "[1246, 591, 52, 48, 1404]CC6.png","[1276, 1189, 164, 194, 9335]CC38.png", "[1240, 887, 71, 98, 2960]CC10.png",
         "[1006, 1258, 30, 119, 521]CC10.png", "[822, 925, 89, 85, 2399]CC7.png",
         "[732, 1128, 119, 52, 2017]CC2.png", "[728, 1124, 127, 59, 1142]CC12.png", "[675, 154, 19, 67, 374]CC1.png","[749, 999, 88, 91, 2372]CC8.png",
         "[646, 634, 29, 75, 341]CC19.png", "[622, 760, 63, 195, 1155]CC11.png", "[530, 960, 54, 197, 1104]CC13.png",
         "[488, 933, 35, 45, 633]CC24.png", "[413, 302, 80, 186, 1110]CC7.png", "[384, 1108, 30, 51, 462]CC14.png",
         "[383, 163, 94, 101, 1905]CC3.png", "[377, 1177, 35, 104, 1029]CC12.png", "[375, 1169, 39, 115, 566]CC9.png", "[366, 253, 50, 37, 433]CC6.png",
         "[360, 913, 78, 97, 554]CC7.png", "[347, 456, 96, 181, 1166]CC8.png", "[293, 661, 31, 119, 573]CC3.png",
         "[275, 752, 51, 34, 433]CC10.png", "[264, 571, 51, 31, 386]CC9.png", "[263, 489, 29, 15, 195]CC15.png",
         "[228, 379, 115, 75, 1908]CC4.png", "[201, 158, 57, 59, 1120]CC2.png",
         "[183, 288, 98, 164, 5468]CC9.png", "[170, 688, 132, 39, 1883]CC6.png",
         "[153, 674, 89, 63, 2936]CC8.png", "[94, 680, 102, 46, 1059]CC11.png","[91, 678, 112, 51, 551]CC4.png","[31, 433, 67, 44, 1127]CC4.png", "[8, 864, 44, 39, 619]CC20.png"]


for imagette in names:
    if imagette == "infos.txt":
        names.remove(imagette)
        continue

    imagette_filtrer = methode_généralisée.preprocessing(imagette)

    pixel_rechercher, pos_val = methode_généralisée.determine_couleur_contour(imagette_filtrer)

    liste_points_extremes_final = methode_généralisée.determine_liste_points_extremes(imagette_filtrer, pixel_rechercher, pos_val)

    base_fleche = methode_généralisée.recherche_base(liste_points_extremes_final)

    pointe = methode_généralisée.recherche_pointe(liste_points_extremes_final, base_fleche)

    methode_généralisée.affichage_direction(imagette, base_fleche, pointe)










