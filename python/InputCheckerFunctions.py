#program to check user input for yes, no, y, n
inPut=["yes","no","y","n","maybe"]
uI=input("type in yes, no, y, n, or maybe - ")

def inputchecker(uI,inPut):
    while(True):
        if uI in inPut:
            print("you're good")
            break
        else:
            uI=input("you must type in yes, no, y, n, or maybe - ")
inputchecker(uI,inPut)


#program to check user input for a number

def numbachecker(userInput):
    while(True):
        if userInput.isdigit():
            userInput=int(userInput)
            print("Is a number")
            break
        elif ("." in userInput):
            splitui = userInput.split(".")
            if (splitui[0][1:].isdigit() and splitui[0][0]=="-"and splitui[1].isdigit() and len(splitui)==2):
                print("it is a negative decimal")
                break
            elif(splitui[0].isdigit() and splitui[1].isdigit() and len(splitui)==2):
                print("it is a positive decimal")
                break
        elif(userInput[1:].isdigit() and userInput[0]=="-"):
            print("negative number")
            break

        else:
            userInput=input(f"type in an actual number please - ")

userInput=input("give me a numba - ")
numbachecker(userInput)























