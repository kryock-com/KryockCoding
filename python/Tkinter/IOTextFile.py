from tkinter import *
from tkinter import filedialog
import os

groot=Tk()
groot.geometry("500x400")

'''
    read only r
    read and write r+ (beginning of file)
    write only w (over-written)
    write and read w+ (over written)
    append only a (end of file)
    append and read a+ (end of file)
    create and write x (cannot already exist)
'''
def openText():
    #fileName="iosample.txt"

    fileName=filedialog.askopenfilename(initialdir=os.getcwd(),filetype=(("Text Files","*.txt"),))
    #fileName=filedialog.askopenfilename(initialdir=os.path.adspath(__file__),filetype=(("Text Files","*.txt"),))
    
    textFile=open(fileName,'r')
    stuff=textFile.read() #read will take the entire file and store it in stuff
    print(type(stuff))

    myText.insert(END,stuff)
    textFile.close()

def saveText():
    textFile=open("iosample.txt","w")
    textFile.write(myText.get(1.0,END))
    textFile.close()



myText=Text(groot,width=40,height=10,font=("Times New Roman",20))
myText.pack(pady=10)

openButton=Button(groot,text="open text file",command=openText)
openButton.pack(pady=10)

saveButton=Button(groot,text="save text file",command=saveText)
saveButton.pack(pady=10)
#

groot.mainloop()