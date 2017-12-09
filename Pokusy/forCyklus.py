#!/usr/bin/python

from sense_hat import SenseHat

from time import sleep

sense = SenseHat()

for x in range (8):
	print "Zapinam LED %d" %(x)
	sense.set_pixel(x,0,[0,0,128])
