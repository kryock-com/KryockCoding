easyPass="13456"
medPass="p@ssword"
hardPass="P@$$w0rd"
goodLuckPass="Ch@0t1cTw!n"
specialCharacters=[33,35,36,37,38,40,41,64,94]
reqCheckList=[False,False,False,False,False]

passwordToCheck=input("input a password ")
passwordToCheckLIST=[]
for i in range(len(passwordToCheck)):
    passwordToCheckLIST.append(False)
if(len(passwordToCheck)>=6 and len(passwordToCheck)<=16):
    for i in range(len(passwordToCheck)):
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
if(False in passwordToCheckLIST):
    print("Your password did not meet the requirements")
else:
    print("Your password met the requirements")





'''
    import re 
    flag = 0
    passwordToCheak=medPass
    while True:   
        if (len(passwordToCheak)>=6 and len(passwordToCheak)<=16):
            print("Length Requirements Satisfied")
            flag = -1
            break
        elif not re.search("[a-z]", passwordToCheak):
            print("Has some lower case letters")
            flag = -1
            break
        elif not re.search("[A-Z]", passwordToCheak):
            print("Has some Upper cased letter")
            flag = -1
            break
        elif not re.search("[0-9]", passwordToCheak):
            print("Has numbers")
            flag = -1
            break
        elif not re.search("[!,@,#,$,%,^,&,(,)]", passwordToCheak):
            print("has some spe")
            flag = -1
            break
        elif re.search("\s ", passwordToCheak):
            flag = -1
            break
        else: 
            flag = 0
            print("Valid Password") 
            break
    
    if flag ==-1: 
        print("Not a Valid Password") 
'''
