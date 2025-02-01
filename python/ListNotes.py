'''
def printTheList():
    for i in groceryl:
        print (i)


user=("Welcome to your Non-Google Grocery List")
groceryl = [] 
while(user!="f"):
    #this struucture forces the user to insert a,r,f, or p
    #   and if not, the question is asked again
    user=input("Do you want to add(a), remove(r), clear(c), finished, or print(p) item ")
    if user=="a":
        #add item to our list
        groceryl.append(user)
        item=input("what item do you want to add")
        groceryl.append(item)
    elif user=="r":
        #remove item to our list
        groceryl.append(user)
        item=input("what item do you want to remove")
        groceryl.remove(item)
    elif user=="p":
        printTheList()
    elif user=="c":
        groceryl.clear

    
printTheList()
#defind printTheList():
#   the paraenthese allows py to know it is a f(x)

import random
numlist=[]
for i in range(100):
    numlist.append(random.randint(0,100))

print(numlist)
print("Min: ",min(numlist))
print("Max: ",max(numlist))
print("Range: ",max(numlist)-min(numlist))
'''

morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
alphabet=[]
for i in range(97,123):
    alphabet.append(chr(i))
print(alphabet)

message=input("word ").lower()
output=""
for i in message:
    output+=morse[alphabet.index(i)]
print(output)





