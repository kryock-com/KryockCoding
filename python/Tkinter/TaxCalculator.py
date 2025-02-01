import tkinter as tk
from decimal import *

root = tk.Tk()

gradeFrame = tk.Frame(root, pady=10, bg="black")
gradeFrame.pack()

taxVar = tk.IntVar()
billVar = tk.IntVar()
fianlOutputVAR = tk.StringVar()


def calculate():
    taxNumber=taxVar.get()
    bill=billVar.get()
    
    tax=taxNumber/100

    saleTaxInDollar=bill*tax
    finalCost=bill+saleTaxInDollar
    finalCost=("$"+str(finalCost))

    fianlOutputVAR.set("Price After Tax: "+finalCost)
#clears the boxs and final label
def clear():
    taxVar.set("")
    billVar.set("")
    fianlOutputVAR.set("")
    



gradeFrame = tk.Frame(root, pady=10, bg="black")
gradeFrame.pack()

#the current grade box
billLBL = tk.Label(gradeFrame,
                  text="Bill before tax : ",
                  compound="center",
                  font=("Time New Roman",14),
                  bd=0,
                  relief=tk.FLAT,
                  fg="white",
                  bg="black").grid(row=0, column=0,padx = 1,pady = 1)
billInput = tk.Entry(gradeFrame, textvariable = billVar, font=('arial',18),).grid(row=0, column=1, padx = 1, pady = 1)

#the grade you want box
salesTaxLBL = tk.Label(gradeFrame,
                  text="Sales tax : ",
                  compound="center",
                  font=("Time New Roman",14),
                  bd=0,
                  relief=tk.FLAT,
                  fg="white",
                  bg="black").grid(row=2, column=0,padx = 1,pady = 1)
taxInput = tk.Entry(gradeFrame, textvariable = taxVar, font=('arial',18),).grid(row=2, column=1,padx = 1,pady = 1)

#final out put
fianlOutPut = tk.Label(gradeFrame,
                  textvariable = fianlOutputVAR,
                  compound="center",
                  font=("Time New Roman",14),
                  bd=0,
                  relief=tk.FLAT,
                  fg="white",
                  bg="black").grid(row=4, column=1,padx = 1,pady = 1)



clearBTN=tk.Button(gradeFrame,width=8,height=2,text="Clear",command=clear).grid(row=5, column=0,padx = 1,pady = 1)
calBTN=tk.Button(gradeFrame,width=8,height=2,text="Calculate",command=calculate).grid(row=5, column=1,padx = 1,pady = 1)
root.mainloop()