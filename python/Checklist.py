checkList= [False   ,False  ,False  ,False  ,False]

while(False in checkList):
    userInput = input("Did you make your bed? (y/n)")
    if userInput=="y":
        checkList[0]=True
    userInput = input("Did you brush your teeth? (y/n)")
    if userInput=="y":
        checkList[1]=True
    userInput = input("Did you eat breakfast? (y/n)")
    if userInput=="y":
        checkList[2]=True
    userInput = input("Did you take a shower? (y/n)")
    if userInput=="y":
        checkList[3]=True
    userInput = input("do you have clean school appropriate clothes? (y/n)")
    if userInput=="y":
        checkList[4]=True
    print(checkList)
print("Have a good day Boy")