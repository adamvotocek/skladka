#!/usr/bin/python

from sense_hat import SenseHat

import time

def printme( textik ):
   "This prints a passed string into this function"
   print(textik)
   print("*")
  
   return;

def nakresliBod(x, y):
    sense.set_pixel(x,y,[250,0,0])
    time.sleep (0.15)
    sense.set_pixel(x,y,[0,0,0])
    return

sense = SenseHat()
sense.clear()

#for x=0..7
#    mojeMe(x, 0)
    
    
#for x=0..7
#    mojeMe(x, 7)

for mojeY in range(0, 8):
    for mojeX in range(0, 8):
        if mojeX == 0 or mojeX == 7 or mojeY == 0 or mojeY == 7:
            nakresliBod(mojeX, mojeY)


for x in range(0, 7):
    print ("We're on " + str(x))
    
  

    
#mojeME()    