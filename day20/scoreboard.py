from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()    
        self.score=0
        self.open_file()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-10,250)
    def open_file(self):
        with open(r"day20\data.txt") as f1:
            self.highscore=int(f1.read())
    def write_file(self):
        with open(r"day20\data.txt","w") as f1:
            f1.write(str(self.highscore))
    def displayscore(self):
        self.clear()
        self.write(f"Score: {self.score} High score:{self.highscore}",align="center",font=("Arial","24","normal"))
        
    def updatescore(self):
        self.score+=1
        
        self.displayscore()
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.write_file()
        self.displayscore()