total=0
sandwichSelected=False
beverageSelected=False
friesSelected=False
print("Welcome To Good Burger")
sandwich = input("Do you want a Chicken(c) $5.25, Beef(b) $6.25, or Tofu(t) $5.75? ")
if (sandwich=="c"or sandwich=="b"or sandwich=="t"):
    sandwichSelected=True
print (sandwich)

if sandwich=="c":
    total += 5.25
elif sandwich=="b":
    total += 6.25
elif sandwich=="t":
    total += 5.75

beverage = input("Would you like a drink, y or n? ")
if(beverage=="y"):
    beverageSelected=True
    beverage=input("s for $1.00, m for $1.75, l for $2.25, c for $2.63 ")
    print("you said",beverage,"drink")  #print(string,string,string)

if beverage=="s":
    total += 1.00
elif beverage=="m":
    total += 1.75
elif beverage=="l":
    total += 2.25
elif beverage=="c":
    total += 2.63

fries = input("Would you like french fries y or n? ")
if(fries=="y"):
    friesSelected=True
    fries = input("s for $1.00, m for $1.50, l for $2.00 ")
    print("you said",fries,"fries")

if fries=="s":
    total += 1.00
elif fries=="m":
    total += 1.50
elif fries=="l":
    fries=input("Would you like a child size fry instead for an addition $.38? (y or n) ")
    if (fries == "y"):
        total += 2.38
    else:
        total += 2

#if you do not convert input to int() it will be a squence or a string
ketchup=int(input("How many Ketchup packets would you like? "))*0.25
total+=ketchup
#but you could combine the top two lines into one

if(sandwichSelected and beverageSelected and friesSelected):        #and look for 2 true statements
    # if variable==true AND variable==true And varible==true
    total-=1

#print('Your order is a {0} sandwich, a {1} drink, a {2} fry, and {3} ketchup packet(s) \nfor a total of {4}'.format(sandwich,beverage,fries,ketchup))
#print('${:,.2f}'.format(total))

print('''
Your order is: 
    {0} sandwich,
    {1} drink,
    {2} fries,
    {3} packets
For a total of ${4}
'''.format(sandwich,beverage,fries,ketchup,total))