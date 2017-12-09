from sense_hat import SenseHat
sense = SenseHat()
from time import sleep
import random
random.seed()

E = [0,0,0]
qtl = False;
viewed = 0;
F = [int(random.random()*255),int(random.random()*255),int(random.random()*255)]
arr=[0,0,0,0,0,0]

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


while True:
	tlhq=0
	sleep(0.25);
	for event in sense.stick.get_events():
		#print(event.direction, event.action)
		if(event.direction == "middle" and event.action == "released"):
			qtl = not qtl;
			tlhq=1
		if((event.direction == "up" or event.direction == "down")and not qtl):
			F = [int(random.random()*255),int(random.random()*255),int(random.random()*255)]
		if(qtl):
			F = [int(random.random()*255),int(random.random()*255),int(random.random()*255)]
	if(not qtl):
		btl = False;
		while not btl:
			nw = random.randint(0,5)                                                                                                                                                     
			if(nw != viewed):
				viewed = nw
				btl = True
	if(tlhq and qtl):
		arr[viewed]+=1
		print("1: "+str(arr[0])+ ", 2: "+str(arr[1])+ ", 3: "+str(arr[2])+ ", 4: "+str(arr[3])+ ", 5: "+str(arr[4])+ " 6: "+str(arr[5]))
	sense.set_pixels(states[viewed])
