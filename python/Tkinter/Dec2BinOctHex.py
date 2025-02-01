from tkinter import *

root = Tk()  
root.wm_geometry('312x324')
root.title("Dec2BinOctHex")

inputText=StringVar()

inputFrame = Frame(root, width=312,height=50)
inputFrame.pack(side=TOP)

binNum=''
octNum=''
hexNum=''


def binary():
    decimal = float(decimalInput.get())
    # 1 byte = 8 bits = 256 unique integers = highest value is 255
    checkList=[]
    
    #this while loop generates the list to calculate the bin string
    i=0
    while decimal>=2**i:
        #insert will allow you to put where you want (location,value)
        checkList.insert(0,2**i)
        i+=1
    
    #this loop calculates the bin string or converts int to binary
    for i in range(len(checkList)):
        #if the 2**checkList[i] is less than or equal to our integer
        if decimal >= checkList[i]:
            decimal-=checkList[i]
            checkList[i]="1"
        else:
            checkList[i]="0"
    
    #out put string
    out="0b"
    for b in checkList:
        out+=b
    binNum=("Binary number - "+out[2:])
    bin = Label(root,text=binNum,font=('arial',18,)).pack()
    #print(binNum)

def octal():
    # 1 byte = 8 bits = 256 unique integers = highest value is 255
    decimal = float(decimalInput.get())
    
    checkList=[]

    #this while loop generates the list to calculate the bin string
    i=0
    while decimal>=2**i:
        #insert will allow you to put where you want (location,value)
        checkList.insert(0,2**i)
        i+=1

    #this loop calculates the bin string or converts int to binary
    for i in range(len(checkList)):
        #if the 2**checkList[i] is less than or equal to our integer
        if decimal >= checkList[i]:
            decimal-=checkList[i]
            checkList[i]="1"
        else:
            checkList[i]="0"


    #out put string
    out="0b"
    for b in checkList:
        out+=b
    octal=(out[2:]) #get the first three char

    for i in range(2):
        if(len(octal)%3==0):
            print(" ")
        else:
            octal = octal[:0] + "0" + octal[0:]

    n=3
    numlist=[]
    for i in range(0,len(octal),n):
        numlist.append(octal[i:i+n])

    """
    OCTAL          BINARY
    0             000
    1             001
    2             010
    3             011
    4             100
    5             101
    6             110
    7             111
    """
    octallist =  [ "0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" ]
    binarylist = ["000","001","010","011","100","101","110","111"]
    for i in range(len(numlist)):
        numlist[i]=octallist[binarylist.index(numlist[i])]

    def concatenate_list_data(list):
        result= ''
        for element in list:
            result += str(element)
        return result

    octNum=("Oct number - "+concatenate_list_data(numlist))
    oct = Label(root,text=octNum,font=('arial',18,)).pack()
    #print(octNum)
    
def hexadecimal():
    # 1 byte = 8 bits = 256 unique integers = highest value is 255
    decimal = float(decimalInput.get())
    
    checkList=[]

    #this while loop generates the list to calculate the bin string
    i=0
    while decimal>=2**i:
        #insert will allow you to put where you want (location,value)
        checkList.insert(0,2**i)
        i+=1

    #this loop calculates the bin string or converts int to binary
    for i in range(len(checkList)):
        #if the 2**checkList[i] is less than or equal to our integer
        if decimal >= checkList[i]:
            decimal-=checkList[i]
            checkList[i]="1"
        else:
            checkList[i]="0"

    #out put string
    out="0b"
    for b in checkList:
        out+=b
    hex=(out[2:]) #get the first three char

    for i in range(3):
        if(len(hex)%4==0):
            print(" ")
        else:
            hex = hex[:0] + "0" + hex[0:]

    n=4
    numlist=[]
    for i in range(0,len(hex),n):
        numlist.append(hex[i:i+n])
    #print(numlist)
    """
    HEXADEC        BINARY
    0             0000
    1             0001
    2             0010
    3             0011
    4             0100
    5             0101
    6             0110
    7             0111
    8             1000
    9             1001
    A             1010
    B             1011
    C             1100
    D             1101
    E             1110
    F             1111
    """
    hexlist    = [ "0"  , "1"  , "2"  , "3"  , "4"  , "5"  , "6"  , "7"  , "8"  , "9"  , "A"  , "B"  , "C"  , "D"  , "E"  , "F"  ]
    binarylist = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
    for i in range(len(numlist)):
        numlist[i]=hexlist[binarylist.index(numlist[i])]

    def concatenate_list_data(list):
        result= ''
        for element in list:
            result += str(element)
        return result

    hexNum=("Hex number - "+concatenate_list_data(numlist))
    hex = Label(root,text=hexNum,font=('arial',18,)).pack()
    #print(hexNum)

def enterClick():
    
    binary()
    octal()
    hexadecimal()

    
    
    

btnFrame = Frame(root, width=300, height=300)
btnFrame.pack()

decimalInput = Entry(inputFrame,font=('arial',18,'bold'),width=50,justify=RIGHT,textvariable=inputText)
decimalInput.grid(row=0,column=0)
decimalInput.pack()


enterBTN=Button(btnFrame,width=8,height=2,text="Enter",command=enterClick).grid(row=1, column=2,padx = 1,pady = 1)




root.mainloop()