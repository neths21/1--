from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LENGTH=1
BREADTH=3


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(LENGTH,BREADTH)
        self.penup()
    def start(self):
        self.goto(305,random.randint(-250,250))
    def move(self):
        self.goto(self.xcor()-STARTING_MOVE_DISTANCE,self.ycor())
    def increase_speed(self):
        STARTING_MOVE_DISTANCE+=MOVE_INCREMENT

