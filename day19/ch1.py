from turtle import Turtle,Screen
def forw():
    t.forward(10)
def ba():
    t.back(10)
def l():
    t.left(45)
def r():
    t.right(45)
def h():
    t.reset()
t=Turtle()
s=Screen()
s.onkey(forw,"w")
s.onkey(ba,"s")
s.onkey(l,"a")
s.onkey(r,"d")
s.onkey(h,"c")
s.listen()

s.exitonclick()