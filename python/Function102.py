import random

#defined the f(x) giveMeSomeNumbers that takes in theAmountOfNumberIWant
#this is a void function because it doesnt return \

def giveMeSomeNumbers(theAmountOfNumberIWant,theHightestValueIWant,theLowestValueIWant):
    #stores the number in this numList
    numList=[]
    #for loop to do something theAmountOfNumberIWant times
    for i in range(theAmountOfNumberIWant):
        #what i wanted to do, add a random number to my list
        numList.append(random.randint(theLowestValueIWant,theHightestValueIWant))
    #prints my list
    print(numList)

#742 is a positonal argumemnt
#giveMeSomeNumbers(999999999999999) hard coding the amount of nums i want
#giveMeSomeNumbers(9,99,1)

#unstead of creating another variable, just put the input into the f(x)
#giveMeSomeNumbers(int(input("How many number do you want? ")),int(input("What is the highest number do you want? ")),int(input("What is the lowest number do you want? ")))

#new version that willreturn the list of numbers
def giveMeSomeNumbers(theAmountOfNumberIWant,theHightestValueIWant,theLowestValueIWant):
    #stores the number in this numList
    numList=[]
    #for loop to do something theAmountOfNumberIWant times
    for i in range(theAmountOfNumberIWant):
        #what i wanted to do, add a random number to my list
        numList.append(random.randint(theLowestValueIWant,theHightestValueIWant))
    #prints my list
    return numList





def ave(listToFindTheAverageOf):
    return sum(listToFindTheAverageOf)/len(listToFindTheAverageOf)

def ran(listToFindTheRangeOf):
    return max(listToFindTheRangeOf)-min(listToFindTheRangeOf)


def basicStats(listToBeAnalyzed):
    print(f'''Here is the basic stats
            Min: {min(listToBeAnalyzed)}
            Max: {max(listToBeAnalyzed)}
            Sum: {sum(listToBeAnalyzed)}
            Avg: {ave(listToBeAnalyzed)}
            Ran: {ran(listToBeAnalyzed)}''')
"""
randoNumbos=giveMeSomeNumbers(10,50,0)
print(randoNumbos)
basicStats(randoNumbos)
"""

'''
def isPrime(n):
    #use a for loop to iterate through all of the numbers to check
    for i in range(2,n):
        #check is n is divisible by the value
        if(n%i==0):
            #if it is not divisible by that value,break the loop and return false
            #print(n, "is not a prime number")
            #print(i,"times",n//i,"is",n)
            return False
    #True or False is simple: or it is either 1 or 0
    return True

def PrimeCheacker(someListofIntegers):
    counter=0
    #look at every item in the list
    for i in range(len(someListofIntegers)):
        #check to see if it is a prime
        if(isPrime(someListofIntegers[i])):
            #if it is prime number, iterate a accumulator varuable
            counter+=1
            print(someListofIntegers[i]," is Prime")
        else:
            print(someListofIntegers[i])
    print(counter,"Prime numbers")


PrimeCheacker(giveMeSomeNumbers(10,50,0))

'''


#create a function that tell you
"""
wordAsker = input("yo boy i need a word-")
def Vowels(wordAsker, vowels): 
    final = [each for each in wordAsker if each in vowels] 
    print("Their are",len(final),"vowles") 
    print(final) 
    
vowelsList=["a","e","i","o","u","y"]
Vowels(wordAsker, vowelsList);
"""
def fiftychance():
    c=random.randint(0,100)
    if (c<50):
        return True
    else:
        return False

def countvowels(word):
    counter=0
    vowelsList=["a","e","i","o","u","y"]
    yChecker=fiftychance()
    #iterate through the word and pull each letter
    for i in range(len(word)):
        #print(word[i])
        #iterate through the vowelslist and pull each vowel
        for j in range(len(vowelsList)):
            #print(vowelsList[j,end="")
            #if the letter is a vowel
            if (j==(len(vowelsList)-1)):
                if (yChecker==False):
                    break
            if (word[i]==vowelsList[j]):
                #iterate the counter
                counter+=1
            #if the letter is not a vowel
            #else:
                #print(word[i],'is not a vowel')
    print(counter,"of em is a vowel")
countvowels("polyhappytyrany")

