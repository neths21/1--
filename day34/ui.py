from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT=("Arial",20,"italic")
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.score_label=Label(text="Score: 0",font=FONT,bg=THEME_COLOR,fg="white")
        self.score_label.grid(column=1,row=0)
        
        self.canvas=Canvas(width=300,height=250)
        self.canvas.grid(column=0,row=1)
        self.statement=self.canvas.create_text(150,125,width=280,text="text",font=FONT,fill=THEME_COLOR)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        self.tickpath=PhotoImage(file=r"day34\\images\\true.png")
        self.tickbutton=Button(image=self.tickpath,highlightthickness=0,command=self.checkTrue)
        self.tickbutton.grid(column=0,row=2)

        self.crosspath=PhotoImage(file=r"day34\\images\\false.png")
        self.crossbutton=Button(image=self.crosspath,highlightthickness=0,command=self.checkFalse)
        self.crossbutton.grid(column=1,row=2)
        
        self.get_next_question()

        self.window.mainloop()
    def checkTrue(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def checkFalse(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right==True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.statement,text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.statement,"End of quiz")
            self.tickbutton.config(state="disabled")
            self.crossbutton.config(state="disabled")

