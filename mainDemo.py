#!/usr/bin/env python

#On Importe les fonctions de tous nos modules
from rgb_lcd import *
from camera import *
from pushbullett import *
from led import *

import time
import os

#import subprocess
#subprocess.call("start python /projet/dweet.py")


#Fonction qui permet de regarder la nature de l'objet introduit et renvoie une distance stable et la nature de l'objet
natureObjet="Lettre ou Colis"
tailleColis = 2  #Taille en cm qui separe lettre de colis
def Nature_Objet():
        nouvelleValeurStable = 10
        if nouvelleValeurStable-valeurStable < -tailleColis or nouvelleValeurStable-valeurStable > tailleColis :
                nature="Colis"
        else :
                nature="Lettre"
        return([nouvelleValeurStable,nature])



#Main :

setText("Bonjour,\nDemarrage")
setRGB(0,128,64)

time.sleep(4)
valeurStable = 0

while True:
        setRGB(10,120,0)
        setText("En attente de\ncourrier")
        time.sleep(15)

        # On detecte du mouvement
        setText("TRAITEMENT\n EN COURS")
        setRGB(120,0,0)
        time.sleep(1)

        #On regarde si on a ajoute ou enleve du courrier :
        natureObjet = Nature_Objet()
        nouvelleValeur=natureObjet[0]   #Distance actuelle apres avoir introduit un objet
        natureObjet=natureObjet[1]      #Lettre ou colis.
                                                                                                                                                                                                                                                      #Si on rentre du courrier et pas qu'on le recupere
        allumer_led() #On allume la lampe, prend la photo, puis on eteint la lampe et on envoie la photo.
        time.sleep(0.5)
        Prendre_Photo()
        time.sleep(0.2)
        eteindre_led()

        #ENVOIE NOTIF
        envoyerPhoto()
        messagePushbullet(natureObjet)
        time.sleep(0.1)

