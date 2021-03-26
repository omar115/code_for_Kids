import random
import turtle
p1=turtle.Turtle()
p1.color("green")
p1.shape("turtle")
p1.penup()
p1.goto(-200,100)
p1.goto(300,60)
p1.pendown()
p1.circle(40)
p1.penup()
p1.goto(-200,100)
p2=p1.clone()
p2.color('blue')
p2.penup()
p2.goto(-200,-100)
p2.goto(300,-140)
p2.pendown()
p2.circle(40)
p2.penup()
p2.goto(-200,-100)

i = 1

while(i <= 20):
    if(p1.pos()>=(300,60)):
        print("p1 winner")
        break
    elif(p2.pos()>=(300,-140)):
        print('p2 winner')
        break
    else:
        print('press any button')
        computer=random.randint(1,6)
        p1.forward(computer*10)
        print('press any button')
        computer=random.randint(1,6)
        p2.forward(computer*10)