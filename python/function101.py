'''
    Procedures - purple blocks from MIT where it does something
        to DO block in MIT
    Function - Again like the purple blocks, but similar to the result block
    Methods - Methods are used with object and Classes
        Example:  s.isdigit()    s is an object od the String class
                  In MIT, we had the button.click() where button is an obj of Button

    There are two main types of functions:
        void - it doesn't return anything, so kind of like print statments
             similar to the to DO block in MIT
        return - after the function is ran, it gives the computer back data
            result block in MIT


#printHowdy
#print("Howdy")
#define the function howdy ():
def howdy():
    #this starts the block of code
    #And this is where you tell PY what howdy() will do
    print("Howdy")

#call the function howdy()


#print("supercalifragilisticexpialidocious")
def printsuper():
    print("supercalifragilisticexpialidocious")

#adding
def adding():
    a=int(input("give the 1st number"))
    b=int(input("give the 2nd number"))
    print(a+b)

#returns
#adding
def adding():
    a=int(input("give the 1st number"))
    b=int(input("give the 2nd number"))
    return(a+b)
a=adding()
print(a)
'''
def slopeIntercept():
    slope=2
    x=2
    b=2
    y=slope*x+b
    return y
slope=slopeIntercept()
#printing (str + int + str)
print("y intercept is: "+str(slope)+" ")

#define the slopeIntercept that passes in slope,x, and b
#                   the tuple has variable
def slopeintercept(slope,x,b):
    y=slope*x+b
    return y

#the tuple lenght needs to match
slope=-.02
x=10
b=41
print(slopeintercept(slope,x,b))
print(slopeintercept(slope,3,b))
#you redefined slopeInercept to have 3 parameters rather than no parameters...
#print(slopeintercept())

def dude():
    name=input("what is your name? ")
    age=input("whats your age? ")
    soda=input("what is your favorite soda? ")
    print(f"Hi {name}, you are {age}, and you drink {soda}")
dude()