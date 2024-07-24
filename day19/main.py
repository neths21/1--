from turtle import Turtle, Screen
from random import randint
is_race_on=False
s=Screen()

s.setup(width=500,height=400)
user_bet=s.textinput(title="Make your bet",prompt="Which turtle will win the race")
col=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,70]
all_turtles=[]
for i in range(6):
    t=Turtle()
    t.speed("slow")
    t.shape("turtle")
    t.color(col[i])
    t.penup()
    t.goto(x=-230,y=y_positions[i])
    all_turtles.append(t)
if user_bet:
    is_race_on=True
while is_race_on:
    for i in all_turtles:
        if i.xcor()>230:
            is_race_on=False
            winningcolour=i.pencolor()
            if winningcolour==user_bet:
                print("You won")
            else:
                print("You lost")
            break
        m=randint(0,10)
        i.forward(m)
s.exitonclick()