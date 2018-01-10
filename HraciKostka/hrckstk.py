from __future__ import division
from sense_hat import SenseHat
sense = SenseHat()
from time import sleep
import random
random.seed()

qtl = False
viewed = 0
F = [int(random.random()*255),int(random.random()*255),int(random.random()*255)]
stat = [0,0,0,0,0,0]
soucetCisel = 0
pocetHodu = 0

while True:
  tlhq = False
  sleep(0.1)
  
  for event in sense.stick.get_events():
    if(event.direction == "middle" and event.action == "released"):
      qtl = not qtl
      tlhq = True
    if((event.direction == "up" or event.direction == "down")and not qtl):
      F = [int(random.random()*255),int(random.random()*255),int(random.random()*255)]
    
#    if(qtl):
#      F = [int(random.random()*255),int(random.random()*255),int(random.random()*255)]
  
  E = [0,0,0]
  states = [
  [E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,F,F,E,E,E,
   E,E,E,F,F,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E], #1
  [F,F,E,E,E,E,E,E,
   F,F,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,F,F,
   E,E,E,E,E,E,F,F], #2
  [F,F,E,E,E,E,E,E,
   F,F,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,F,F,E,E,E,
   E,E,E,F,F,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,F,F,
   E,E,E,E,E,E,F,F], #3
  [F,F,E,E,E,E,F,F,
   F,F,E,E,E,E,F,F,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   F,F,E,E,E,E,F,F,
   F,F,E,E,E,E,F,F], #4
  [F,F,E,E,E,E,F,F,
   F,F,E,E,E,E,F,F,
   E,E,E,E,E,E,E,E,
   E,E,E,F,F,E,E,E,
   E,E,E,F,F,E,E,E,
   E,E,E,E,E,E,E,E,          
   F,F,E,E,E,E,F,F,
   F,F,E,E,E,E,F,F], #5
  [F,F,E,F,F,E,F,F,
   F,F,E,F,F,E,F,F,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   E,E,E,E,E,E,E,E,
   F,F,E,F,F,E,F,F,
   F,F,E,F,F,E,F,F] #6
  ]

  def dejNoveCislo():
    global viewed
    if(not qtl):
      prepinac = False
      while not prepinac:
        nw = random.randint(0,5)
        if(nw != viewed):
          viewed = nw
          prepinac = True
      return nw

  nw = dejNoveCislo()

  if(tlhq and qtl):
    stat[viewed]+=1
    print("1: "+str(stat[0])+ ", 	2: "+str(stat[1])+ ", 	3: "+str(stat[2])+ ", 	4: "+str(stat[3])+ ", 	5: "+str(stat[4])+ " 	6: "+str(stat[5]))
    soucetCisel = soucetCisel + viewed + 1
    pocetHodu = pocetHodu + 1
    prumer = soucetCisel / pocetHodu
    print (prumer)
    
  sense.set_pixels(states[viewed])