from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
s=Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("My snake game")
s.tracer(0)

sn=Snake()
food=Food()
sc=Scoreboard()

s.listen()
s.onkey(sn.up,"Up")
s.onkey(sn.down,"Down")
s.onkey(sn.right,"Right")
s.onkey(sn.left,"Left")
game_is_on=True
while game_is_on:
    s.update()
    time.sleep(0.1)
    sn.move()
    sc.displayscore()
    #detect collision with food
    if sn.head.distance(food)<15:
        food.refresh()
        sc.updatescore()
        sn.extend()
    #detect collision with wall
    if sn.head.xcor()>280 or sn.head.xcor()<-280 or sn.head.ycor()>280 or sn.head.ycor()<-280:
        sc.game_over()
        game_is_on=False
    #detect collision with tail
    for segment in sn.segments:
        if segment!=sn.head:
            if segment.distance(sn.head)<10:
                sc.game_over()
                game_is_on=False
        



s.exitonclick()

