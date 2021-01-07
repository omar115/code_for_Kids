import turtle
import random

p1=turtle.Turtle()
p1.color("green")
p1.shape("turtle")
p1.penup()
p1.goto(-200,100)

p2=p1.clone()
p2.color("blue")
p2.penup()
p2.goto(-200,-100)

p1.goto(300,60)
p1.pendown()
p1.circle(40)
p1.penup()
p1.goto(-200,100)

p2.goto(300,-140)
p2.pendown()
p2.circle(40)
p2.penup()
p2.goto(-200,-100)


die=[1,2,3,4,5,6]

i=1
while(i <= 20):
    if p1.pos() >= (300,100):
        print("p1 wins")
        break
    
    elif p2.pos() >= (300,-100):
        print("p2 wins")
        break
    
    else:
        p1_turn=input("press enter to start")
        die_out=random.choice(die)
        print("you get", die_out)
        print("the number of steps:", 20*die_out)
        p1.forward(20*die_out)
        
        p2_turn=input("press enter to challenge")
        d=random.choice(die)
        print("you get",d)
        print("the number os steps:",20*d)
        p2.forward(20*d)