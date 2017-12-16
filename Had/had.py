from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
barvaHlavy = [250,0,0]
barvaOcasu = [100,100,100]
ToJeTma = [0,0,0]
smer = "up"
h = [randint(3,7),randint(3,7)]
o1 = [h[0],h[1] -1]
o2 = [h[0],h[1] -2]
t = [h[0],h[1] -3]

def rozsvitHada(hlava,ocas1,ocas2,tma):
    #print (hlava[0], hlava[1], tma[0], tma[1])
    sense.set_pixel(hlava[0],hlava[1],barvaHlavy)
    sense.set_pixel(ocas1[0],ocas1[1],barvaOcasu)
    sense.set_pixel(ocas2[0],ocas2[1],barvaOcasu)
    sense.set_pixel(tma[0],tma[1],ToJeTma)

def zjistiSmer(direction):
    for event in sense.stick.get_events():
        if(event.direction != "middle" and event.action == "pressed"):
            direction = event.direction
    return direction

def dejNovouPozici(direction,position):
    if direction == "left":
        position[0] = position[0] - 1
    elif direction == "right":
        position[0] = position[0] + 1
    elif direction == "down":
        position[1] = position[1] + 1
    elif direction == "up":
        position[1] = position[1] - 1
    
    if position[0] == 8:
        position[0] = 0
    elif position[1] == 8:
        position[1] = 0
    elif position[0] == -1:
        position[0] = 7
    elif position[1] == -1:
        position[1] = 7
    
    return position

sense.clear()
sleep(1)

while True:
    smer = zjistiSmer(smer)
    rozsvitHada(h,o1,o2,t)
    
    t[0] = o2[0]
    t[1] = o2[1]
    o2[0] = o1[0]
    o2[1] = o1[1]
    o1[0] = h[0]
    o1[1] = h[1]
    
    h = dejNovouPozici(smer,h)
    #print (h[0],h[1])
    sleep(0.5)