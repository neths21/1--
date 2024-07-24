from turtle import Turtle
WIDTH=5
HEIGHT=1
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(WIDTH,HEIGHT)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor()<250:
            self.goto(self.xcor(),self.ycor()+20)
    def down(self):
        if self.ycor()>-240:
            self.goto(self.xcor(),self.ycor()-20)
