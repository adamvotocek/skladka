from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
vyska = 3
bila = [255,255,255]
cerna = [0, 0, 0]
bilaOcasu1 = [128,128,128]
bilaOcasu2 = [68,68,68]
pocetVlocek = 0

def kresliVlocku(x,y):
    if y > -1 and y < 8:
        sense.set_pixel(x, y, bila)
    if y > 0 and y < 9:
        sense.set_pixel(x, y - 1, bilaOcasu1)
    if y > 1 and y < 10:
        sense.set_pixel(x, y - 2, bilaOcasu2)
    if y > 2 and y < 11:
        sense.set_pixel(x, y - 3, cerna)
	
sense.clear()
sleep(1)

l = 0

while True:
    kresliVlocku(0,l)
    l= l+1
    sleep(1)
#while True:
    #sloupec = random.randint(0,7)
#    sleep (0.6)
#    kresliVlocku(0, vyska)