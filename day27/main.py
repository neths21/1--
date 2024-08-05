from tkinter import *

#conversion
def convert():
    mi=int(entry.get())
    km=mi*1.6
    label4.config(text=km)

window=Tk()
window.title("Mile to Km Converter")


#label 1
label1=Label(text="is equal to",font=("Arial", 15))
label1.grid(column=0,row=1)

#label 2
label1=Label(text="Miles",font=("Arial", 15))
label1.grid(column=2,row=0)
#label 3
label1=Label(text="Km",font=("Arial", 15))
label1.grid(column=2,row=1)
#label 4
label4=Label(text=0,font=("Arial", 15))
label4.grid(column=1,row=1)
#entry
entry=Entry(width=10)
entry.insert(END,string="0")
#button
button=Button(text="Calculate",command=convert)
button.grid(column=1,row=3)
entry.grid(column=1,row=0)

window.mainloop()