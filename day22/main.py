from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)


r_paddle=Paddle((350,0)) 
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

game_is_on=True
tim=0.1

screen.listen()
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.down,"s")
screen.onkey(r_paddle.up,"Up")
screen.onkey(l_paddle.up,"w")
while game_is_on:
    time.sleep(tim)
    screen.update()
    ball.move()
    if ball.ycor()==300 or ball.ycor()==-300:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
        tim/=10
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
        tim/=10
    print(tim)
screen.exitonclick()