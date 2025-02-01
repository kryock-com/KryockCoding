'''
    easyPass="123456"
    medPass="passw0rd"
    hardPass="P@$$w0rd"
    goodLuckPass="$jDjmp)&4kIZ3oib"
'''
specialCharacters=[33,35,36,37,38,40,41,64,94]
#            [length,lower,upper,numbers,specials]
reqCheckList=[False ,False,False, False , False  ]
#       abandon this idea because the for loop would reset the values everytime
passwordToCheck=input("input a password ")
passwordToCheckLIST=[]
passwordList=[]
strengthList=[]


#.append() adds items to the list
for i in range(len(passwordToCheck)):
    passwordToCheckLIST.append(False)
print(passwordToCheckLIST)

if(len(passwordToCheck)>=6 and len(passwordToCheck)<=16):
    reqCheckList[0]=True
    #iterating through passwordToCheck
    for i in range(len(passwordToCheck)):
        #print(passwordToCheck[i])   
        #a-z on ASCII is ....   range(97,123) remember range(start,stopANDnotInclude)
        if(ord(passwordToCheck[i]) in range(97,123)):
            passwordToCheckLIST[i]=True
            reqCheckList[1]=True
        #A-Z on ASCII is ....   range(65,91)     
        elif(ord(passwordToCheck[i]) in range(65,91)):
            passwordToCheckLIST[i]=True
            reqCheckList[2]=True
        #0-9 on ASCII is ....   range(48,58)    
        elif(ord(passwordToCheck[i]) in range(48,58)):
            passwordToCheckLIST[i]=True
            reqCheckList[3]=True
        elif(ord(passwordToCheck[i]) in specialCharacters):
            passwordToCheckLIST[i]=True
            reqCheckList[4]=True

print(passwordToCheckLIST)
print(reqCheckList)
outPutscore=(sum(reqCheckList))
scorelist=[
    "1 out of 5 points = |##--------|",
    "2 out of 5 points = |####------|",
    "3 out of 5 points = |######----|",
    "4 out of 5 points = |########--|",
    "5 out of 5 points = |##########|"
    ]

if any((str(outPutscore) + "out of") in str(item) for item in scorelist):
    print(scorelist)

if(False in passwordToCheckLIST or False in reqCheckList):
    print("Your password did not meet all requirements")
else:
    print("Your password met all requirements")
