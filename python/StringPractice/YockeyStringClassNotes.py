
Name = input("Put Your Name In CamelCase Style?\t ")        #\t inserts a tab in the output
City = input("What City do you Live in? ")
State = input("What State? ")
Food = input("What is Your Favorite Breakfast Food? ")

print(f"Hello! {Name}")
#print(f"You are from {City}, {State}")    #there are 3 parameters in the print f(x)
#print(string,string,string, etc...) inputs spaces btwn str
#print(f"AND, your favorite food for breakfast is {Food}")

#print("My name is %s " % (Name))  #another string formatting (% is a placeholder)


print("""
Multi Line Out
Hello! {}
You are from {}, {}
AND, your favorate food for breakfast is {}
    """.format(Name,City,State,Food))

#print(iD + Name + City + State)  #using the + operand needs to have same data types
iD=14253647586970890

print(f"""
ID:      {iD}
NAME:    {Name}
CITY:    {City}
STATE:   {State}
    """)

'''
    Common Escape Character (\):
        \t      Tab
        \n      New line
        \\      Adds a backslash
        \'      Adds an '
'''


print("upper method",Name.upper())
print("lower method",Name.lower())
print("title method",Name.title())
print("swapcase method",Name.swapcase())
print("capitalize method",Name.capitalize())

#slice and dice our strings
fullName = input("What is your full name? ")
first,last = fullName.split(" ")                #split(Delimiter,#ofTimes)
print(last.capitalize(),first.capitalize())
print(last,first)
print("{0}, {1}".format(first,last))
print("{1}, {0}".format(first.capitalize(),last.capitalize()))  #0 is first, 1 is last

#printing individual letters
#srings and lists are very similar
print(fullName[0])      #[] are indexs  0 index is first item
#the first number in a computer is 0
print(fullName[1])
print(fullName[2])
firstLetter = fullName[0]
print("everything but the first letter",fullName[1:])
                                               #[start:end]
print(fullName[0:3])
print(fullName.index("y"))  #index returns the first occurence of the value
#pulling a substring
print(fullName[0:fullName.index("y")])    #fullname[start: index of the letter]
#lenght how many characters total
#index is which character are you talking about
print(len(fullName))
print(fullName[0:len(fullName)])    #make it dynamic so we dont get an index out of bounds

#reverses
#str[start:end:step]
print(fullName[::-1])


print(2==2)
print(2.0==2)
print("2"=="2")
print("1"<"2")
print("a"<"b")
print("steak">"salad")
print("A">"a")
print("ant" in "anthony")
print("ant " in "anthony")

email="joyce.tsiga@evsck12.com"
#print(".com" in email)
#print("@" in email)
if((".com" in email) and ("@" in email)):
    print("email is valid")