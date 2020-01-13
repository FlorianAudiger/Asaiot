#!/usr/bin/env python

#On Importe les fonctions de tous nos modules
from rgb_lcd import *
from capteurUltrason import *
from camera import *
from pushbullett import *
from led import *

import time
import os

#Fonction qui permet de regarder la nature de l'objet introduit et renvoie une distance stable et la nature de l'objet
natureObjet="Lettre ou Colis"
tailleColis = 2  #Taille en cm qui separe lettre de colis
def Nature_Objet():
	nouvelleValeurStable = Valeur_Stable(1.5)
        if nouvelleValeurStable-valeurStable < -tailleColis or nouvelleValeurStable-valeurStable > tailleColis :
               	nature="Colis"
        else :
               	nature="Lettre"
	return([nouvelleValeurStable,nature])

#Main :

#Initialisation
setText("Bonjour,\nDemarrage")
setRGB(0,128,64)
time.sleep(0.5)
valeurStable = Valeur_Stable(1.5)

#Début de la boucle
while True:
	setRGB(10,120,0)
	setText("En attente de\ncourrier")
	time.sleep(1)
	Mouvement = False
	
	while not Mouvement:	#On boucle tant qu'un objet n'est pas insere
		time.sleep(0.1)

		distanceInstantanee=Capter_Distance()
		if ((distanceInstantanee > valeurStable + 2) or (distanceInstantanee < valeurStable - 2)):
			Mouvement = True
	
	# On detecte du mouvement
	setText("TRAITEMENT\n EN COURS")
        setRGB(120,0,0)
	time.sleep(1)
	
	#On regarde si on a ajoute ou enleve du courrier :
	natureObjet = Nature_Objet()
	nouvelleValeur=natureObjet[0]	#Distance actuelle apres avoir introduit un objet
	natureObjet=natureObjet[1]	#Lettre ou colis.

	if nouvelleValeur >= valeurStable : #On vérifie que c'est du nouveau courrier et non une récupération de courrier/colis
		allumer_led() #On allume la led
		time.sleep(0.5)
		Prendre_Photo() #On prends la photo
		time.sleep(0.01)
		eteindre_led() #On éteint la led

		#ENVOIE NOTIF
		envoyerPhoto() #Envoie photo
		messagePushbullet(natureObjet) #Envoie message
		time.sleep(0.2)

	valeurStable = Valeur_Stable(1.5) #On recalibre le capteur à ultrason


