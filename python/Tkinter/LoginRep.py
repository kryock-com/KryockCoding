import tkinter as tk

userName="CSAM"
passWord=987654



def testMyButton():
    #print("testMyButton")

    #get the info from the text box
    username = entUsername.get()    #accessor
    password = entPassword.get()
    globalUserName = username
    print(username,password)
    if userName == username and passWord == passWord:
        frameAuth.tkraise()
    else:
        btnLogin.config(text = "wrong inputs")
"""
def checkUserPass():
    if """



#main window
root = tk.Tk()      #root is the window
root.wm_geometry("200x200")

root.title('Authorization')

#frame for successful log in
frameAuth = tk.Frame(root)
frameAuth.grid(row=0,column=0,sticky='news')

# create empty frame
frameLogin=tk.Frame(root)
frameLogin.grid(row=0,column=0,sticky='news')



#                     (positiomnalArgument, keyWord Argument)
lblUsername = tk.Label(frameLogin         ,text='Username: ')
lblUsername.pack(pady=5)


entUsername = tk.Entry(frameLogin,bd=3)
entUsername.pack(pady=5)

enteredUsername = entUsername.get()


lblPassword = tk.Label(frameLogin         ,text='Password: ')
lblPassword.pack(pady=5)

entPassword = tk.Entry(frameLogin,bd=3,show="*")
entPassword.pack(pady=5)

btnLogin = tk.Button(frameLogin,text="Log in", command=testMyButton)
btnLogin.pack(pady=20,padx=175)


lblDisplay=tk.Label(frameAuth,text="Welcome "+userName)
lblDisplay.pack(padx=5)


root.mainloop()     #you need this at the bottom of your file to run everything