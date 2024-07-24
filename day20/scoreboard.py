from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()    
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-10,250)
        
    def displayscore(self):
        self.write(f"Score: {self.score}",align="center",font=("Arial","24","normal"))

    def updatescore(self):
        self.score+=1
        self.clear()
        self.displayscore()
    def game_over(self):
        self.goto(-10,0)
        self.write("GAME OVER",align="center",font=("Arial","24","normal"))