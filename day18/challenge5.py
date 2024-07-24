from turtle import Turtle,Screen
from random import random
t=Turtle()
n=1
t.speed(0)
while n<75:
    l=tuple(random() for i in range(3))
    t.pencolor(l)
    t.circle(100)
    t.left(5)
    n+=1
s=Screen()
s.exitonclick()
