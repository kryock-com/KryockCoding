"""
print("Loop Practice")

butt=input("Hey guess what? ").lower    #this brings in everything as lower case
'''
#if this is true
if(butt=="what" or butt=="wut" or butt=="wat" or butt=="Watt"):
    #do this
    print("Chichen butt.........")
'''
#iteration is a loop structure that repeats until something is false
#while this is true
while((butt!="what") and (butt!="wut") and (butt!="wat") and (butt!="watt")):
    #do this
    butt=input("Hey guess what? ").lower()

print("Chichen butt.........")

print()
i=1
while(i!=101):
#while i is not equal to x
    print(i)
    i+=1

print()
i=20            #i is an iterator variable
while(i!=1):    #remeber to read your program when it donest comelete the last step
#while i is not equal to x
    print(i)
    i-=1
while(i!=21):   #i is a global variable
    print(i)
    i+=1

i=0             #i is a global varible acting as an iterator
while(i<=10):    #since i < 50 it will stop if i is 50
    print(i)
    i+=1
print("\nFor loop below")
for j in range(6):          #i is a local variable acting as an iterator
    print(j)
print("\n"+str(j))

#WATCH what you call your global variable to make sure they are not
#   the same as your local variable

#printing each number btwn 1 and 10
for j in range(11):     #range(start,end,step)  like    [s,e,step]
    print(j)

#print each number btwn 1 and 50 that are odd
for j in range(0,5000000,100000):
    print(j)

#to print each number use a for loop
#to check the user input use a while loop

#for every "j" in a sequence of "5"
for j in range(5):
    #do something
    print(j)

#print out name vertically (list form)
name="gerald"
for i in range(len(name)):
        #range need integers
        # len(name) returns the length or an integer value
        # DO NOT put strings or floats or anything else besides integers in here
    print(name[i])
"""
total=0
for x in range(0,6,2):
    y=-(x**2)+4*(x)+4
    base=x
    height=y     #literally y or your function
    areaOfLittleRectangel=base*height
    total+=areaOfLittleRectangel
    print(areaOfLittleRectangel)
print(total)