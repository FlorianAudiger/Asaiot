#!/usr/bin/env python

#CAPTEUR ULTRASON


from grovepi import *

ultrasonic_ranger = 4

#Fonction qui renvoie la distance entre le capteur a ultrasons et le premier obstacle en cm
def Capter_Distance(): # -> Int
        try:
		d = (ultrasonicRead(ultrasonic_ranger))
		print(d)
		d = float(d)
                return(d)

        except TypeError:
                return "TypeError"
        except IOError:
                return "IOError"

#Fonction similaire a Capter_Distance mais qui renvoie une valeur stable pendant temps_stabilisation
def Valeur_Stable(temps_stabilisation): # -> Int
        interruptionAutomatique=0
	temp=Capter_Distance()
	Continuer=True
        time.sleep(temps_stabilisation/2)
        while Continuer and interruptionAutomatique<10:			#Interruption du programme si trop d'attente.
                nouv1=Capter_Distance()
                if nouv1==temp :
                        time.sleep(temps_stabilisation/2)
			nouv2=Capter_Distance()
			if nouv2==temp:
				Continuer=False
			temp=nouv2
			interruptionAutomatique+=1   
                else :
			temp=nouv1
		interruptionAutomatique+=1
		time.sleep(temps_stabilisation/2)
	if Continuer:
		print("echec de la stabilisation")
	return(temp)
