from turtle import Turtle, Screen
from colorgram import extract
from random import choice
colours=extract("hirst-1.jpg",30)
tu=[]
t=Turtle()
t.speed(0)
for i in range(30):
    first_color = colours[i]
    rgb = first_color.rgb # e.g. (255, 151, 210)
    hsl = first_color.hsl # e.g. (230, 255, 203)
    tu.append((rgb.r,rgb.g,rgb.b))
for i in range(10):
    for j in range(10):
        ch=choice(tu)
        t.color(tuple(i/255 for i in ch))
        t.dot(20)
        t.up()
        t.forward(50)
        t.down()
    t.teleport(x=0,y=50*(i+1))  
    print(t.pos)
s=Screen()
s.exitonclick()
