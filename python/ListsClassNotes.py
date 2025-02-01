import random
print("List Notes")

'''
    print()
    Num=input("How many times would you want this to run? ")
    while():


        Data types
            Booleans    Primitive Data
            Integers    Primitive Data
            Float       Higher level of complexity as in more 1's and 0's
            Strings     and even higher
            Arry        and even higher
                Typically arrays only 
                In Python
                    Lists can actually contain multiple data types
                    Lists is typically considered the Class
'''
'''
#to creat a lis
#Variable       =   index
VariableName    =   []  #the brack
String_list = ["W", "or", "l", "d!"]
#4 elements in our string_list
#length of string_list
scores_list = [ 5, 15, -67, 191, 88, -23]
float_list = [2.2, -101.9, 60.00000008]
boolean_list = [False, False, True, False, True]
mixed_list = ["Hello", 2, "the", String_list] 
empty = []

#len(list or string) prints out an integer
print(len(boolean_list))
print(len(mixed_list))
#   there are 4 objects inside of the mixed_list
print(mixed_list)
print(scores_list)
#String_list = ["W", "or", "l", "d!"]
print(String_list)

#able to access each item in a list just like string
print(String_list[1])   #print out or

#this is not Dry.... it repeats itself
#   do not do the SCOTT method
#   this is an example of hardcode and not dynamic
print(String_list[0]+String_list[1]+String_list[2]+String_list[3])


output=""
#while something is true
i=0
while(i<len(String_list)):
    output+=String_list[i]
    i+=1
print(output)


output=""
#for each elementsJ in a range of 0 to the length of out String_list
for j in range(len(String_list)):
    output+=String_list[j]
    #print(output)
print(output)

#foe each loop
output=""
#for each j n for j in String_list
for j in String_list:
    output+=j
print(output)

for j in String_list:
    print(j)            #your print out a vertical list
'''

namelist=['Nick','Justis','Tyler','Bryce','Gaege','Gracey','Dylan','Noah','Kevin','Mason','Braylynn','Eric','Joyce','Katelyn','Anthony','Scott','Logan','Kai','Joe','Trump','Bill','Billy','Bob','Alex','Kacey','Johnny','Luke','Zach','Nathan','Justin']
#print in list from     (vertical list)
'''for i in namelist:
    print (i)'''

user=input("Enter a name ").title()
while(user!="quit"):
    #if the name we enter is in the list of names:
    if user in namelist:
        #then tell the user we are on the list
        print(f"{user}! You'er on the list!\n ")
    else:
        print("\nYou'er not on the list")
        user=input("Do you want to get on the list? It's only a couple dollar...")
        if (user=="yes"):
            namelist.append(input("What is your name?..."))
            #append function takes in any data
            #   addes the object to the end of the list
    user=input("Enter a name ").title()