from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
r = 180
g = 0
b = 0

def pitch_calculate(p):
  if p > 67.5 and p < 90:
    return 7
  if p > 45 and p < 67.5:
    return 6
  if p > 22.5 and p < 45:
    return 5
  if p > 0 and p < 22.5:
    return 4
  if p > 337.5 and p < 360:
    return 3
  if p > 315 and p < 337.5:
    return 2
  if p > 292.5 and p < 315:
    return 1
  if p > 270 and p < 292.5:
    return 0

def roll_calculate(r):
  if r > 67.5 and r < 180:
    return 0
  if r > 45 and r < 67.5:
    return 1
  if r > 22.5 and r < 45:
    return 2
  if r > 0 and r < 22.5:
    return 3
  if r > 337.5 and r < 360:
    return 4
  if r > 315 and r < 337.5:
    return 5
  if r > 292.5 and r < 315:        
    return 6
  if r > 180 and r < 292.5:
    return 7
    
while True:
  orientation = sense.get_orientation_degrees()
  #print("p: {pitch}, r: {roll}".format(**orientation))
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  p = pitch_calculate(orientation["pitch"])
  r = roll_calculate(orientation["roll"])
  sense.clear()
  sense.set_pixel(p,r,[r,g,b])
  #sleep(0.2)


