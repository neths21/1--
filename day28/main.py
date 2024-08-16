from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer1)
    canvas.itemconfig(timer_text,text="00:00")
    tick_label.config(text="")
    label.config(text="Timer",fg=RED)
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps%8==0:
        countdown(long_break_sec)
        label.config(text="Break",fg=RED)
    elif reps%2==0:
        countdown(short_break_sec)
        label.config(text="Break",fg=PINK)
    else:
        countdown(work_sec)
        label.config(text="Work",fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    countmin=count//60
    countsec=count%60
    if len(str(countsec))==1:
        countsec="0"+str(countsec)
    canvas.itemconfig(timer_text,text=f"{countmin}:{countsec}")
    if count>0:
        global timer1
        timer1=window.after(1000,countdown,count-1)
    else:
        start_timer()
        t=""
        for i in range(reps//2):
            t+="✔"
        tick_label.config(text=t)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="day28\\tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=2)


tick_label = Label(bg=YELLOW,fg=GREEN)
tick_label.grid(column=1, row=3) 

#label 1
label=Label(text="Timer",font=(FONT_NAME,30),bg=YELLOW,fg=GREEN)
label.grid(column=1,row=0)

#BUTTOM START
button1=Button(text="Start",font=(FONT_NAME,10),command=start_timer)
button1.grid(column=0,row=3)

#BUTTOM RESET
button1=Button(text="Restart",font=(FONT_NAME,10),command=reset)
button1.grid(column=2,row=3)
window.mainloop()