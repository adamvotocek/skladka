from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
barvaHlavy = [250,0,0]
barvaOcasu = [100,100,100]
toJeTma = [0,0,0]
barvaPotravy = [randint(0,250),randint(0,250),randint(0,250)]
smer = "up"
p = []
skore = 0
h = [4,4]
o1 = [h[0],h[1] +1]
o2 = [h[0],h[1] +2]
t = [h[0],h[1] +3]
had = [h,o1,o2,t]

def rozsvitHada(had):
    for i in range(len(had)):
        barva = barvaOcasu
        if i == 0:
            barva = barvaHlavy
        if i == len(had) - 1:
            barva = toJeTma
        pozice = had[i]
        sense.set_pixel(pozice[0],pozice[1],barva)


def muzuZmenitSmer(novy, stary):
    return (novy == "left" and stary != "right") or (novy == "right" and stary != "left") or (novy == "down" and stary != "up") or (novy == "up" and stary != "down")

def zjistiSmer(direction):
    for event in sense.stick.get_events():
        if(event.direction != "middle" and event.action == "pressed"):
            #if event.direction == "left" and direction != "right":
            #    direction = event.direction
            #elif event.direction == "right" and direction != "left":
            #    direction = event.direction
            #elif event.direction == "down" and direction != "up":
            #    direction = event.direction
            #elif event.direction == "up" and direction != "down":
            #    direction = event.direction
            if (muzuZmenitSmer(event.direction, direction)):
                    direction = event.direction      
    return direction

def vytvorPotravu(hlava,ocas1,ocas2,tma,potrava):
    while True:
        potrava = [randint(0,7),randint(0,7)]
        if potrava != hlava or potrava != ocas1 or potrava != ocas2 or potrava != t:
            barvaPotravy = [randint(0,250),randint(0,250),randint(0,250)]
            sense.set_pixel(potrava[0],potrava[1],barvaPotravy)
            return potrava

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
    rozsvitHada(had)
    
   
    #if (not p) or (h == p):
    #    if h == p:
    #        skore = skore + 1
    #    print ("POTRAVA")
    #    p = vytvorPotravu(h,o1,o2,t,p)
    
    # Posun body hada
    for i in reversed(range(len(had))):        
        if i != 0:
            had[i][0] = had[i - 1][0]
            had[i][1] = had[i - 1][1]
        else:
           had[i] = dejNovouPozici(smer,had[i])
           
                
    # pridat do pole https://docs.python.org/2/tutorial/datastructures.html
    # odstranit comm.
    
    #print (skore, p[0],p[1])
    #print (h[0],h[1])
    sleep(0.5)