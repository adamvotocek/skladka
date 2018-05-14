from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

yellow = (100, 100, 0)

while True:
  acceleration = sense.get_accelerometer_raw()
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']

  x = abs(x)
  y = abs(y)
  z = abs(z)

  if x + y + z > 0:
    yellow = (randint(20,255), randint(20,255), randint(20,255))
    sense.show_message(str(int(x + y + z)), 0.01, yellow)
    print(x + y + z)
    #sleep(0.2)
  else:
    sense.clear()