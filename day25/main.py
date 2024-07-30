import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S States Game")
img=r"day25\blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

'''*def get_mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()'''
data=pandas.read_csv(r"day25\50_states.csv")
df=pandas.DataFrame(data)
l=[]
m=[]
score=0
while len(l)<50:
    answer_State=screen.textinput(title=f"{len(l)}/50 states correct",prompt="Whats another state's name?")
    answer_State=answer_State.title()
    print(answer_State)
    print(df["state"].values)
    if answer_State=="Exit":
        m= [i for i in df["state"].values if i not in l]
        datalearn=pandas.DataFrame(m)
        datalearn.to_csv(r"D:\code\python\100 days of python\day25\states_to_learn.csv",index=False)
        break
    if answer_State in df["state"].values:
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        l.append(answer_State)
        score+=1
        location = df[df['state'] == answer_State][['x', 'y']]
        location=location.values.tolist()
        print(location[0])
        t.goto(location[0])
        t.write(answer_State)

