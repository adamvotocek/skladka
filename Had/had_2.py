from sense_hat import SenseHat
import time
from random import randint
import datetime

sense = SenseHat()
O = [0,0,0]
N = [0,128,0]
E = [0,0,128]
M = [128,0,0]
barvaHlavy = [250,0,0]
barvaOcasu = [100,100,100]
barvaPotravy = [randint(0,250),randint(0,250),randint(0,250)]
hadHaduje = True
smer = "up"
snedenaPotrava = 0
p = []
skore = 0
had = [[4,4],[4,5],[4,6],[4,7]]

def rozsvitHada(had):
    for i in range(len(had)):
        barva = barvaOcasu
        if i == 0:
            barva = barvaHlavy
        if i == len(had) - 1:
            barva = O
        pozice = had[i]                                                                 
        
        sense.set_pixel(pozice[0],pozice[1],barva)

def zapisSkore():
    date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    skoretxt = open("skore.txt","a")
    skoretxt.write(str(date) + "  Skore: " + str(skore) + "\n")
    skoretxt.close()

def muzuZmenitSmer(novy, stary):
    return (novy == "left" and stary != "right") or (novy == "right" and stary != "left") or (novy == "down" and stary != "up") or (novy == "up" and stary != "down")

def zjistiSmer(direction):
    for event in sense.stick.get_events():
        if(event.direction != "middle" and event.action == "pressed"):
            if (muzuZmenitSmer(event.direction, direction)):
                    direction = event.direction      
    return direction

def vytvorPotravu(had,potrava):
    while True:
        prepinac = True
        barvaPotravy = [randint(0,250),randint(0,250),randint(0,250)]
        potrava = [randint(0,7),randint(0,7)]
        for i in reversed(range(len(had))):
            if potrava == had[i]:
                prepinac = False  
        if prepinac:
            sense.set_pixel(potrava[0],potrava[1],barvaPotravy)
            return potrava

def rozsvitSmailika():
    sense.set_pixels([O,E,E,O,O,E,E,O,O,E,E,O,O,E,E,O,O,O,O,O,O,O,O,O,O,O,O,N,N,O,O,O,O,O,O,N,N,O,O,O,M,M,O,O,O,O,M,M,O,M,M,M,M,M,M,O,O,O,M,M,M,M,O,O])

def dejNovouPozici(direction,position):
    if direction == "left":
        position[0] = position[0] - 1
    elif direction == "right":
        position[0] = position[0] + 1
    elif direction == "down":
        position[1] = position[1] + 1
    elif direction == "up":
        position[1] = position[1] - 1
    skore =+ 1
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
time.sleep(1)

while True:
    smer = zjistiSmer(smer)
    
    if hadHaduje == False:
        sense.show_message(str(skore))
        rozsvitSmailika()
        zapisSkore()
        
        while hadHaduje == False:
            for event in sense.stick.get_events():
                if(event.direction == "middle" and event.action == "pressed"):
                    hadHaduje = True
                    sense.clear()
                    snedenaPotrava = 0
                    smer = "up"
                    p = []
                    skore = 0
                    had = [[4,4],[4,5],[4,6],[4,7]]
                    break
                    
    if hadHaduje == True:
        print (had)
        rozsvitHada(had)
        
        # Zere se had?
        for i in range(1, len(had) - 1):
            if had[0] == had[i]:
                hadHaduje = False
                break
        
        # Zere had potravu?
        if (not p) or (had[0] == p):
            if had[0] == p:
                if (skore % 1) == 0 and skore != 0:
                    had.insert(len(had) -2, [had[len(had) -2][0],had[len(had) -2][1]])
                skore = skore + 1
            p = vytvorPotravu(had,p)
        
        # Posun body hada
        for i in reversed(range(len(had))):        
          if i != 0:
              had[i][0] = had[i - 1][0]
              had[i][1] = had[i - 1][1]
          else:
              had[i] = dejNovouPozici(smer,had[i])
             
    #print (had[0][0],had[0][1])
    time.sleep(0.4)