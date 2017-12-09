from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

V = [0,0,0]
Z = [0,125,0]


while True:
	cislo = random.randint(1,6)
	
	if cislo==1:
		zobrazeni=[V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,Z,Z,V,V,V,V,V,V,Z,Z,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V]
		
	if cislo==2:
		zobrazeni=[V,V,V,V,V,V,V,V,
		V,V,V,V,V,V,V,V,
		V,V,V,V,V,V,V,V,
		V,V,V,V,V,V,V,V,
		V,V,V,V,V,V,V,V,
		V,V,V,V,V,V,V,V,
		V,V,V,V,V,V,V,V,
		V,V,V,V,V,V,V,V]
		
	if cislo==3:
		zobrazeni=[V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,Z,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V]
		
	if cislo==4:
		zobrazeni=[V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,Z,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V]
		
	if cislo==5:
		zobrazeni=[V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,Z,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V]
		
	if cislo==6:
		zobrazeni=[V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,Z,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V]
	
	sense.set_pixels(zobrazeni)	
	sleep(0.025)