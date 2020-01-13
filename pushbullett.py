from pushbullet import Pushbullet
import time

# On récupère la clé API
with open("/var/www/html/cle.txt", "r") as fichier:	
	cle = fichier.readline()
	cle = cle.rstrip()

pb = Pushbullet(cle)

#Envoie grâce à la clé API un message à l'utilisateur concerné 
def messagePushbullet(msg):
#	h = time.localtime().tm_hour
#	m = time.localtime().tm_min+1
#	a = msg + " " + str(h) + "h" + str(m) 
	a = msg
	push = pb.push_note("Alerte",a)

#Envoie grâce à la clé API le fichier "photo.jpg" 
def envoyerPhoto():
	with open("photo.jpg", "rb") as pic:
   		file_data = pb.upload_file(pic, "photo.jpg")

	push = pb.push_file(**file_data)
