from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
t=Turtle()
class Snake:
    def __init__(self) -> None:
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]
    def createsnake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
        
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
        
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
        


  
        

