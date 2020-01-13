#!/usr/bin/env python

from picamera import *

from time import *

#Créer un fichier "photo.jpg" correspondant à la photo capturée par la caméra
def Prendre_Photo():
	camera = PiCamera()
	camera.start_preview(alpha=192)
	sleep(0.8)
	camera.capture("/projet/photo.jpg")
	camera.stop_preview()
	camera.close()
	print("Photo Prise")
	
