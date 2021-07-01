import turtle
screen = turtle.Screen()
t = turtle.Turtle()
# ~ #turtle.tracer(0, 0)

dist = 2
i = 0 
for i in range(20):
    onclick(turn); 
    t.fd(dist)
    t.pencolor('#37F9F9')
    t.width(3)
    t.circle(200,200)
    t.rt(1)
    dist += 5
    print(dist)
d = 0
for d in range(4):
    t.fd(dist)
    t.pencolor('#3775F9')
    t.width(2)
    t.circle(200,200)
    t.rt(1)
    dist += 3
    print(dist)
# ~ #turtle.update()
screen.exitonclick()    

