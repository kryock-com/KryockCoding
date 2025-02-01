"""
        G−((1−w)×C)
   F= --------------
            w

F = Final exam grade
G = Grade you want for the class
w = Weight of the final exam, divided by 100 (put weight in decimal form vs. percentage form)
C = Your current grade
"""
import tkinter as tk


root = tk.Tk()

wantVar = tk.IntVar()
gradeVar = tk.IntVar()
weightVar = tk.IntVar()
fianlExamVAR = tk.StringVar()

def calculate():
    #C = Your current grade
    c = gradeVar.get()

    #G = Grade you want for the class
    g = wantVar.get()

    #w = Weight of the final exam, divided by 100
    w = weightVar.get()
    w = w/100

    """
            G−((1−w)×C)
        F= --------------
                 w
    """
    #the top of the fraction
    topOfFrac = (g-((1-w)*c))

    #dividing the toptopOfFrac with the weight of grade
    final = topOfFrac/w

    #rounds the final number
    finalNumber = str(round(final, 0))
    wantedGrade =str(g)
    fianlExamVAR.set("You'll need to get a "+finalNumber+"%"+"on the test to get a "+wantedGrade+" in the class")
    


#clears the boxs and final label
def clear():
    gradeVar.set("")
    wantVar.set("")
    weightVar.set("")
    fianlExamVAR.set("")
    

gradeFrame = tk.Frame(root, pady=10, bg="black")
gradeFrame.pack()

#the current grade box
currentGD = tk.Label(gradeFrame,
                  text="Current Grade : ",
                  compound="center",
                  font=("Time New Roman",14),
                  bd=0,
                  relief=tk.FLAT,
                  fg="white",
                  bg="black").grid(row=0, column=0,padx = 1,pady = 1)
gdInput = tk.Entry(gradeFrame, textvariable = gradeVar, font=('arial',18),).grid(row=0, column=1, padx = 1, pady = 1)

#the grade you want box
gradewant = tk.Label(gradeFrame,
                  text="Grade You Want : ",
                  compound="center",
                  font=("Time New Roman",14),
                  bd=0,
                  relief=tk.FLAT,
                  fg="white",
                  bg="black").grid(row=2, column=0,padx = 1,pady = 1)
wantInput = tk.Entry(gradeFrame, textvariable = wantVar, font=('arial',18),).grid(row=2, column=1,padx = 1,pady = 1)

#the weight of exam box
examWeight = tk.Label(gradeFrame,
                  text="Final Exam Weight : ",
                  compound="center",
                  font=("Time New Roman",14),
                  bd=0,
                  relief=tk.FLAT,
                  fg="white",
                  bg="black").grid(row=3, column=0,padx = 1,pady = 1)
weightInput = tk.Entry(gradeFrame, textvariable = weightVar, font=('arial',18),).grid(row=3, column=1,padx = 1,pady = 1)

#final out put
fianlExam = tk.Label(gradeFrame,
                  textvariable = fianlExamVAR,
                  compound="center",
                  font=("Time New Roman",14),
                  bd=0,
                  relief=tk.FLAT,
                  fg="white",
                  bg="black").grid(row=4, column=1,padx = 1,pady = 1)





clearBTN=tk.Button(gradeFrame,width=8,height=2,text="Clear",command=clear).grid(row=5, column=0,padx = 1,pady = 1)
calBTN=tk.Button(gradeFrame,width=8,height=2,text="Calculate",command=calculate).grid(row=5, column=1,padx = 1,pady = 1)




root.mainloop()