from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
barvaHlavy = [250,0,250]
barvaOcasu = [125,0,125]
zacatecniX = randint(3,7)
zacatecniY = randint(3,7)
smer = "up"

def zjistiSmer(direction):
    for event in sense.stick.get_events():
        if(event.direction != "middle" and event.action == "pressed"):
            direction = event.direction
    return direction


while True:
    smer = zjistiSmer(smer)
    print (smer)
    sleep(1)