from tkinter import *
from tkinter import colorchooser
groot = Tk()
groot.title("The Color Picker")
groot.geometry("400x400")


def color():
    myColor = colorchooser.askcolor()[1]
    myLabel = Label(groot,text=myColor).pack(pady=10)
    myLabel2 = Label(groot,text="You picked a color", bg = myColor).pack()


colorButton = Button(groot,text="Pick a color",command=color).pack()

groot.mainloop()