print("Conditional Practice")
#PLTW's activity 3.1.2

#print((4*5)-4) #print looks for the ( and it will print anything inside of the other )

#What are the following data types?
'''
    print(type(10))     #int
    print(type("10"))   #string
    print(type(10.0))   #float
    print(type(-10))    #int
    #print(type(true))   #error because true is not defined
    print(type(False))  #boolean
    print(type(10+1.0)) #float
    print(type(10+"10"))    #error

    print(type("10"*3))
    print("10"*3)       #two differnt types BUT * means concatenating the item 2getHer
    #print("10"+3)       #this should be 103 but you cant cuz data types
    #print("10"/2)       #Unsupported operand type

    print(bool(int(.0000000000000000000000000000000000000000000000000000004)))
    print(int(.9))
    print(int(3.4))
    print(int(3.99999999999999999999999999999999999999999999999999))
    print(int(3.9))
    print(int(3.9999999999999999999999999999))
    print(int(3.99))
    print(int(3.9999999999999999))  #16 decimal places then it will round up


#boolean return true or false amd are the basis of conditional statement

x=int(input("pick a number bewtween 1 and 10"))  #1 = means setting
if(x == 7):                             #is is for string and == is for int
    print("You guessed it right")
    print("somthing else")                  #to check your indents
elif(x<7):                                  #else if or elif need a condition
    print("Oh, to low")
else:                                       #if all else fails, just do this
    print("Oh, to high")


converting data types
    int()
    float()
    str()
    bool()

numside=int(input("How Many starchy sides do you have on your food"))
if numside== 1:
    print("Yo, you be eating Toast")
elif numside== 2:
    print("Yo, you be eating a Sandwich")
elif numside == 3:
    print("Yo, you be eating a Taco")
elif numside == 4:
    print("Yo, you be eating a Sushi")
elif numside == 5:
    print("yo you be eating a Quiche")
elif numside == 6:
    print("yo you be eating a Calzone")
elif numside == 7:
    print("yo you be eating a Cake")
elif numside == 0:
    print("yo you be eating a Salad")
else:
    print("It is not in the range of 0-7")

Boolean symblos
        equal to                    == or is(for list and objectss)
        less than                  <
        less than or equal to      <=
        greater than               >
        greater than or equal to   >=
        not equal to               != or not
        and                        and             both has to be correct
        or                          or              either has to be correct

        False + True == False       0 + 1 == 0      1!=0

hours = input("how many hours of sleep did you have")
food = input("did you eat breakfest")

if hours>=8:
    if food=="yes":                     #this is an example of nesting conditional
        print("you can exercise")       #nesting is used for massive conditional

if hours>=8 and food=="yes":            #this is more proper that nesting
    print("you can ecercise")

food=input("did you have a cake or muffins ")
if food=="cake" or food=="muffins":             #only one has to be correct
    print("Im Happy")

duck = input("Do you like Rubber Duckies")
duckR = input("Do you like Real Duckies")
if duck=="y" and duckR=="y":        #4 different boolean expressions
    print("squeak quack")
elif duck=="y" and duckR=="n":      #4 different boolean expressions
    print("squeck")
elif duck=="n" and duckR=="y":      #4 different boolean expressions
    print("quack")
else:
    print("do you like cats")
'''
x=int(input("What is your x "))
y=int(input("What is your y "))
'''
#adding the not keyword before the paraenthese i am looking for the opposite
if (x>= 0 and x<= 50 and y>= 0 and y<= 50): #9 totl boolean expressions
    print("You're Out")
else:
    print("You're In")
'''
if (x>= 0 and y>= 0 and y<=x and y<=50 and x<=50):
    print("You're in")
else:
    print("You're out") 