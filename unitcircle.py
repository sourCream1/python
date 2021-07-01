#MODULE 7 - Pythin Turtle graphics
#https://docs.python.org/3/library/turtle.html (Links to an external site.)
#Before using turtle install turtle graphics.
#sudp apt install python3-tk python-tk
#
#Try this code:

import turtle
import random
import math 

w = turtle.Screen()
w.bgcolor("#000000")
t = turtle.Turtle()
t.speed("fastest")
for d in range (0, 360*13): 
	rads = (3.141592/180)*d
	x = math.cos(rads)*100
	y = math.sin(rads)*100
	#print(d,x,y)
	t.goto(x,y)
	hx = hex(random.randint(0,255))
	hx = hx.replace("0x","")
	thecolor = "#" +hx+hx+hx
	print(hx)
	t.width(10)
	t.pencolor(thecolor)
	if(d % 360 == 0): 
		amp = amp + 20
	


w.exitonclick()  
