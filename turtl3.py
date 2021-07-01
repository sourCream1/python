import turtle

w = turtle.Screen()
w.clear()
w.bgcolor("#26297C")
t = turtle.Turtle()
turtle.tracer(0, 0)
t.speed(10)   
t.color('yellow')
y = 0 
while y < 9:   
    t.forward(100)
    t.right(200)
    t.dot(5)
    y = y+1
t.penup()
t.setx(+400)
t.sety(+40)
t.pencolor('yellow')
m = 0 
while m < 9: 
    t.pendown()
    t.forward(100)
    t.right(200)
    t.dot(5)
    m = m+1

t.penup()
t.setx(0)
t.sety(-300)   
t.pencolor('yellow')
k = 0 
while k < 9:
    t.pendown()    
    t.forward(100)
    t.right(200)
    t.dot(5)
    k = k+1    

t.penup()
t.setx(+400)
t.sety(-270)   
t.pencolor('yellow')
b = 0 
while b < 9:
    t.pendown()    
    t.forward(100)
    t.right(200)
    t.dot(5)
    b = b+1    


t.penup()
t.setx(-300)
t.sety(+200)   
t.pencolor('yellow')
a = 0 
while a < 9:
    t.pendown()    
    t.forward(100)
    t.right(200)
    t.dot(5)
    a = a+1    


t.penup()
t.setx(-600)
t.sety(+400)   
t.pencolor('yellow')
c = 0 
while c < 10:
    t.pendown()    
    t.forward(100)
    t.right(200)
    t.dot(5)
    c = c+1    

t.penup()
t.setx(-700)
t.sety(+200)   
t.pencolor('yellow')
d = 0 
while d < 10:
    t.pendown()    
    t.forward(100)
    t.right(200)
    t.dot(5)
    d = d+1 
t.penup()
t.setx(+500)
t.sety(+300) 
t.color("white")
t.pendown
t.begin_fill()
t.circle(100)
t.end_fill()
  
t.penup()
t.setx(-60)
t.sety(+200)   
t.color("#F1F1C2")
dist = 2
for q in range(20):
   t.pendown()
   t.fd(dist)
   t.rt(90)
   dist += 2

 
w.exitonclick()
