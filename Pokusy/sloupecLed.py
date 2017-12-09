#!/usr/bin/python

from sense_hat import SenseHat

sense = SenseHat()

misto1 = 0

while misto1 <= 7:
    sense.set_pixel(misto1,0,[0,0,250])
    misto1 = misto1 +1