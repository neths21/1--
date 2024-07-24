import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
score=Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")
i=0
l=[]
game_is_on = True
while game_is_on:
    screen.tracer(0)
    time.sleep(0.1)
    screen.update()
    if i%6==0:
        l.append(CarManager())
        l[-1].start()
    screen.tracer(1)
    for m in l:
        m.move()
        if m.distance(player)<25:
            score.game_over()
            game_is_on=False

    if player.ycor()>250:
        player.restart()
        score.update_score()
    i+=1
    

screen.exitonclick()