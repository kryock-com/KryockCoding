import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def doCommand(command):
    global commandTextBox, urlENT
    #subprocess.call("ping localhost")
    
    commandTextBox.delete(1.0,tk.END)
    commandTextBox.insert(tk.END,command + " working...\n")
    commandTextBox.update()

    #run the Powershell command
    urlVal = urlENT.get()
    if (len(urlVal)==0):
        urlVal="::1"    #also know as 127.0.0.1 also know as localhost
    powershellCommmand = command + " " + urlVal     #string value
    p = subprocess.Popen(powershellCommmand,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    results,errors = p.communicate()    #returns the results and errors of the process
    commandTextBox.insert(tk.END,results)
    commandTextBox.insert(tk.END,errors)



def mSave():
    filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
    if filename is None:
        return
    file = open (filename, mode = 'w')
    text_to_save = commandTextBox.get("1.0", tk.END)
  
    file.write(text_to_save)
    commandTextBox.delete(1.0,tk.END)
    commandTextBox.insert(tk.END,"Saved file")
    commandTextBox.insert(tk.END,filename)
    file.close()
    





groot = tk.Tk()
frameBTN = tk.Frame(groot)
frameBTN.pack()

#ping button and properties of the button
pingBTN = tk.Button(frameBTN,text="Check to see if a URL is up and active", command=lambda:doCommand("ping"))
pingBTN.pack()

#nslookup button and properties of the button
nslookup = tk.Button(frameBTN,text="Check the IP address of a website", command=lambda:doCommand("nslookup"))
nslookup.pack()

#tracert button and properties of the button
tracert = tk.Button(frameBTN,text="Trace route to website", command=lambda:doCommand("tracert"))
tracert.pack()

#save button and properties of the button
saveBTN = tk.Button(frameBTN,text="Save text", command=mSave)
saveBTN.pack()

#Frame for the URL window - frameURL
frameURL = tk.Frame(groot, pady=10, bg="black")
frameURL.pack()


#url lable
urlLBL = tk.Label(frameURL,
                  text="Enter a URL of interest: ",
                  compound="center",
                  font=("Time New Roman",14),
                  bd=0,
                  relief=tk.FLAT,
                  cursor="heart",
                  fg="mediumpurple3",
                  bg="black")
urlLBL.pack(side=tk.LEFT)

#url entry
urlENT = tk.Entry(frameURL,font=('arial',18),)
urlENT.pack(side=tk.LEFT)

#scrolledText widget for the command output
commandTextBox = tksc.ScrolledText(frameURL,height=10,width=100)
commandTextBox.pack(padx=10)

groot.mainloop()