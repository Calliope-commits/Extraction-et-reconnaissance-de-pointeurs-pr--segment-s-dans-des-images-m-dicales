# Extraction-et-reconnaissance-de-pointeurs-pr--segment-s-dans-des-images-m-dicales
Université Paris Cité - Travaux d'étude et de recherche - Encadrant : Laurent WENDLING

## Description 

Notre projet consiste en l’extraction et la reconnaissance de pointeurs pré-segmentés dans des images médicales. L’année précédente, une méthode a été proposée afin de procéder à ces traitements. Dans le but de participer davantage dans l’aide à la décision des experts, nous avons décidé de procéder à la détection de région d’intérêt (ROI), et de réaliser des traitements locaux dans celles-ci. Ces ROI consistent en les zones pointées par ces flèches. Nous allons donc procéder à cette tâche en réalisant les étapes suivantes (liste non exhaustive) :

➔ Détecter l’orientation et la direction des flèches

➔ Sélectionner une zone grâce à la direction détectée.

➔ Procéder à des traitements dans cette ROI : histogramme, seuillage, normalisation de l’histogramme…


## Contexte

Un des outils mis à la disposition des professionnels est le marqueur.  Celui-ci permet d’indiquer une zone d'intérêt pouvant présenter une anomalie.
Des travaux ont été réalisé afin d’extraire ces marqueurs et de les classifier.
L’informatique a pour but d’apporter de l’assistance dans la prise de décision des experts.

![image](https://github.com/Calliope-commits/Extraction-et-reconnaissance-de-pointeurs-pr--segment-s-dans-des-images-m-dicales/assets/61286710/23e17d47-f64d-4144-9128-3aded401aa15)

## Présentation du sujet : 
_Objectif_ : Cibler les zones pointées et leur appliquer différents traitements d’image.

_Plusieurs étapes pour l’atteindre_ : 

-Déterminer l’orientation de la flèche : Direction et sens
    
-Délimiter la zone d’extraction de la région d'intérêt (ROI)

-Appliquer différents types de traitements sur la ROI 


## Vérité terrain : 

![image](https://github.com/Calliope-commits/Extraction-et-reconnaissance-de-pointeurs-pr--segment-s-dans-des-images-m-dicales/assets/61286710/4fd507ab-2646-487c-aa7e-b88c827c5cf9)
![image](https://github.com/Calliope-commits/Extraction-et-reconnaissance-de-pointeurs-pr--segment-s-dans-des-images-m-dicales/assets/61286710/00e46c0f-6a07-4185-a1c5-fdcfaf3a4d43)


## Résultats au niveau de direction  : 
Accuracy : 90.6% sur un total de 53 flèches

![image](https://github.com/Calliope-commits/Extraction-et-reconnaissance-de-pointeurs-pr--segment-s-dans-des-images-m-dicales/assets/61286710/64de5a1a-de35-4e9e-8825-46845b9bb63a)

![image](https://github.com/Calliope-commits/Extraction-et-reconnaissance-de-pointeurs-pr--segment-s-dans-des-images-m-dicales/assets/61286710/a1b0450d-2840-4ae2-b932-e18b11954976)

## Résultat au niveau de l'extraction 

_Affichage des ROI_ : 

![image](https://github.com/Calliope-commits/Extraction-et-reconnaissance-de-pointeurs-pr--segment-s-dans-des-images-m-dicales/assets/61286710/aa1e5d59-927c-457c-9485-9c7c52ccfcd9)

_Traitement des ROI_ :
Image originale : 

![image](https://github.com/Calliope-commits/Extraction-et-reconnaissance-de-pointeurs-pr--segment-s-dans-des-images-m-dicales/assets/61286710/f6fdaa01-2ee9-4319-927f-21392bbc4897)


Traitements proposés : 

![image](https://github.com/Calliope-commits/Extraction-et-reconnaissance-de-pointeurs-pr--segment-s-dans-des-images-m-dicales/assets/61286710/972a7e6e-def4-4617-9747-2442fe9e3686)


Exemple sur l'ensemble de l'image :

![image](https://github.com/Calliope-commits/Extraction-et-reconnaissance-de-pointeurs-pr--segment-s-dans-des-images-m-dicales/assets/61286710/ccab3c60-0583-44db-a1ac-65c39db9facb)


Traitements : 

![image](https://github.com/Calliope-commits/Extraction-et-reconnaissance-de-pointeurs-pr--segment-s-dans-des-images-m-dicales/assets/61286710/43a393f5-4bf1-4ead-b085-a755a0b8f3f0)




## Auteurs : 

Aïssatou Signate , Amine Benmehrez

