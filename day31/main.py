from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT1=("Ariel",40,"italic")
FONT2=("Ariel",60,"bold")
def is_known():
    global df,pos
    df=df.drop(index=pos)
    print(df)
    df.to_csv(r"day31\data\french_words.csv",index=False)
    new_card()
def flip():
    randomwordenglish=df["English"][pos]
    canvas.itemconfig(oldcardc,image=newcard)
    canvas.itemconfig(wordtext,text=randomwordenglish,fill="white")
    canvas.itemconfig(titletext,text="English",fill="white")
# ---------------------------- new word generator ------------------------------- #
def new_card():
    global df,pos
    csvdata=pandas.read_csv(r"day31\data\french_words.csv")
    df=pandas.DataFrame(csvdata)
    pos=random.randint(0,len(df)-1)
    print(pos)
    randomword=df["French"][pos]
    canvas.itemconfig(oldcardc,image=oldcard)
    canvas.itemconfig(wordtext,text=randomword,fill="black")
    canvas.itemconfig(titletext,text="French",fill="black")
    window.after(3000,flip)
    #if tick_button.after
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
oldcard=PhotoImage(file=r"day31\images\card_front.png")
newcard=PhotoImage(file=r"day31\images\card_back.png")
oldcardc=canvas.create_image(400,263,image=oldcard)
canvas.grid(column=0,row=0,columnspan=2)

titletext=canvas.create_text(400,150,text="French",font=FONT1)
wordtext=canvas.create_text(400,263,text="word",font=FONT2)

new_card()
tick = PhotoImage(file=r"day31\images\\right.png")
tick_button = Button(image=tick, highlightthickness=0,command=is_known)
tick_button.grid(column=0,row=1)

cross = PhotoImage(file=r"day31\images\wrong.png")
cross_button = Button(image=cross, highlightthickness=0,command=new_card)
cross_button.grid(column=1,row=1)


window.mainloop()