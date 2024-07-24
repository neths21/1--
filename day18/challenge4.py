from turtle import Turtle, Screen
from random import random,choice


def cl():
    l=tuple(random() for _ in range(3))
    t.pencolor(l)
def move():
    m=[1,2,3,4]
    if choice(m)==1:
        t.right(90)
    elif choice(m)==2: 
        t.left(90)
    elif choice(m)==3:
        t.forward(50)
    else:
        t.backward(50)


t=Turtle()
t.pensize(10)
t.speed(10)
while True:
    cl()
    move()
s=Screen()
s.exitonclick()