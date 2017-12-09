#!/usr/bin/python

from sense_hat import SenseHat

import time

sense = SenseHat()

mistoX = 0
mistoY = 0

while mistoY <= 7:
    while mistoX <= 7:
        sense.set_pixel(mistoX,mistoY,[0,0,0])
        mistoX = mistoX +1
    mistoX = 0
    mistoY = mistoY + 1

mistoY = 0

time.sleep(0.5)

while mistoY <= 7:
    while mistoX <= 7:
        sense.set_pixel(mistoX,mistoY,[0,0,125])
        time.sleep(0.05)
        mistoX = mistoX +1
    mistoX = 0
    time.sleep(0.05)
    mistoY = mistoY + 1
