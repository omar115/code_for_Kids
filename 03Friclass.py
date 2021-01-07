'''
import turtle
wn = turtle.Screen()
color=["orange","blue","red"]
t = turtle.Turtle()
t.goto(100,100)
t.forward(100)
t.fd(100)
t.shapesize(1,5,10)
'''

import turtle

t=turtle.Turtle()

turtle.bgcolor("#CD853F")

#t.shapesize(1,5,5)

t.fillcolor("red")

#t.shape("triangle")

t.pen(pencolor="purple", fillcolor="red", pensize=50, speed=9)

c=t.clone()

c.goto(100,100)

t.circle(10)

c.circle(10)