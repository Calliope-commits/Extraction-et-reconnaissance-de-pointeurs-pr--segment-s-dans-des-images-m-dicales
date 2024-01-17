# Extraction-et-reconnaissance-de-pointeurs-pr--segment-s-dans-des-images-m-dicales
Université Paris Cité - Travaux d'étude et de recherche - 2022 - Encadrant : Laurent WENDLING

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

-Déterminer l’orientation de la flèche 
    Direction et sens
-Délimiter la zone d’extraction de la région d'intérêt (ROI)
-Appliquer différents types de traitements sur la ROI 

