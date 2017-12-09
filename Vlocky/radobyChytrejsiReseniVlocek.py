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

def zkontrolujY():
    global l
    global u
    global p
    global k
    global o
    global n
    if l==10:
        l = random.randint(0,3)
        k = random.randint(0,7)
    if u==10:
        u = random.randint(0,3)
        o = random.randint(0,7)
    if p==10:
        p = random.randint(0,3)
        n = random.randint(0,7)

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

l = random.randint(0,3)
u = random.randint(0,3)
p = random.randint(0,3)
k = random.randint(0,7)
o = random.randint(0,7)
n = random.randint(0,7)

while True:
    kresliVlocku(k,l)
    kresliVlocku(o,u)
    kresliVlocku(n,p)
    zkontrolujY()
    l= l+1
    u= u+1
    p= p+1 
    sleep(0.5)
#while True:
    #sloupec = random.randint(0,7)
#    sleep (0.6)
#    kresliVlocku(0, vyska)