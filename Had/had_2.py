from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
barvaHlavy = [250,0,0]
barvaOcasu = [100,100,100]
toJeTma = [0,0,0]
barvaPotravy = [randint(0,250),randint(0,250),randint(0,250)]
hadHaduje = True
smer = "up"
snedenaPotrava = 0
p = []
skore = 0
had = [[3,1],[0,0],[0,0],[0,0]]
had[1][0] = had[0][0]
had[1][1] = had[0][1] +1
had[2][0] = had[1][0]
had[2][1] = had[1][1] +2
had[3][0] = had[2][0]
had[3][1] = had[2][1] +3

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
    if hadHaduje == False:
        for event in sense.stick.get_events():
            if(event.direction == "middle" and event.action == "pressed"):
                hadHaduje = True
                snedenaPotrava = 0
                skore = 0
                had = [[3,1],[0,0],[0,0],[0,0]]
                had[1][0] = had[0][0]
                had[1][1] = had[0][1] +1
                had[2][0] = had[1][0]
                had[2][1] = had[1][1] +2
                had[3][0] = had[2][0]
                had[3][1] = had[2][1] +3
    
    if hadHaduje == True:
        rozsvitHada(had)
        for i in reversed(range(len(had))):
            for n in reversed(range(len(had))):
                if had[i] == had [n]:
                    hadHaduje = False
        
        if (not p) or (had[0] == p):
            if had[0] == p:
                had.insert(len(had) -2, [had[len(had) -2][0],had[len(had) -2][1]])
                skore = skore + 1
                print (skore)
            p = vytvorPotravu(had,p)
        # Posun body hada
        for i in reversed(range(len(had))):        
          if i != 0:
              had[i][0] = had[i - 1][0]
              had[i][1] = had[i - 1][1]
          else:
              had[i] = dejNovouPozici(smer,had[i])
             
    #print (had[0][0],had[0][1])
    sleep(0.4)