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
        
def vlocka(sloupec, y):
    kresliVlocku(sloupec,y)
    
    if y==10:
        sloupec = random.randint(0,7)
        y = random.randint(0,3)
        
    y= y+1
    return [sloupec, y]
	
sense.clear()
sleep(1)

start1 = random.randint(0,3)
start2 = random.randint(0,3)
start3 = random.randint(0,3)
sloupec1 = random.randint(0,7)
sloupec2 = random.randint(0,7)
sloupec3 = random.randint(0,7)

while True:
    v1 = vlocka(sloupec1, start1)
    sloupec1 = v1[0]
    start1 = v1[1]
    
    
    sleep(0.5)
#while True:
    #sloupec = random.randint(0,7)
#    sleep (0.6)
#    kresliVlocku(0, vyska)