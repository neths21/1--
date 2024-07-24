from turtle import Turtle, Screen
from random import random
timmy_the_turtle = Turtle()
n=3
m=3
while n<11:
    t=tuple(random() for i in range(0,3))
    print(t)
    timmy_the_turtle.pencolor(t)
    angle=360/n
    for i in range(0,m):
        timmy_the_turtle.forward(100)
        print(angle)
        timmy_the_turtle.right(angle)
    m+=1
    n+=1
        
screen = Screen()
screen.exitonclick()
