import time
from grovepi import *

# Connect the Grove LED to digital port D4
led = 8
leed = 7
leeed = 4

pinMode(led,"OUTPUT")

#On allume les 3 LEDS
def allumer_led():
	digitalWrite(led,1)     # Send HIGH to switch on LED
	digitalWrite(leed,1)
	digitalWrite(leeed,1)
	return("LEDS ON!")

#On eteint les 3 LEDS
def eteindre_led():
	digitalWrite(led,0)     # Send LOW to switch off LED
	digitalWrite(leed,0)
	digitalWrite(leeed,0)
	return("LEDS OFF!")

