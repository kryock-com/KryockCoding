import tkinter as tk

root = tk.Tk()
root.geometry('300x300')

frameBlue = tk.Frame(root,width=200,height=150,background="Blue")
#grid(where do you want it in the grid)
frameBlue.grid(row=0,column=0)

framered = tk.Frame(root,width=200,height=150,background="red")
framered.grid(row=1,column=0)

framered = tk.Frame(root,width=100,height=150,background="lime")
framered.grid(row=0,column=2)

framered = tk.Frame(root,width=100,height=150,background="yellow")
framered.grid(row=1,column=1)

root.mainloop()