#assumed 7% sale tax
def tax(taxAmount,subtotal):
    theTotalAmount = subtotal * (1 + taxAmount / 100)
    return theTotalAmount

def tip(tipAmount,subtotal):
    theTotalAmount = subtotal+tipAmount/100 *subtotal
    return theTotalAmount

def pizzaCost(size,sauceFromTheUser,listOfToppings):
    sizeList =      ["s","m","l","xl"]
    sizeCostList =  [ 3 , 4 , 5 ,  6 ]
    sauce = .50
    topping = .50
    totalCost = 0
    if size in sizeList:
        i = sizeList.index(size)    #finding the index of the size
        totalCost+=sizeCostList[i]  #pulling info
        #way below reduces lines 34 and 35 into i line
        #totalCost+=sizeCostList[sizeList.index(size)]
    if sauceFromTheUser !="no":
        totalCost+=sauce
    #added in topping cost
    totalCost+=len(listOfToppings)*.50
    #print(totalCost)
    return totalCost

def orderpizza():
    name=input("Whats the name of your pizza? ")
    size=input("What size of pizza would you like? ")
    crust=input("What type of crust? ")
    sauce=input("What is your sauce? ")
    listOfToppings=[]
    ui=input("Say done for no toppings or list the toppings you want? ")
    while(ui!="done"):
        listOfToppings.append(ui)
        ui=input("Say done for no toppings or list the toppings you want? ")
    print(f'''
        You ordered a {name} pizza
            the {size} size
            with {crust} crust
            with {sauce} sauce
            with these toppings:''')
    for i in listOfToppings:
        print("\t\t"+i)
    
    return (name,size,crust,sauce,listOfToppings)

"""
thePizzaIOrdered=orderpizza()
#calling to order a pizza
#   when you call to order a pizza, you and the othewr person pick up the phone
#   in Python that means say the name pick up your left     (
#   and the other person will pick up the          right    )
"""

def makingThePizza(name,size,crust,sauce,listOfToppings):
    pizza= (f'''
            the name {name}
            the size {size}
            the crust {crust}
            the sauce {sauce}
            the toppings {listOfToppings}''')
    return pizza

'''    
thePizza=makingThePizza(thePizzaIOrdered[0],thePizzaIOrdered[1],thePizzaIOrdered[2],thePizzaIOrdered[3],thePizzaIOrdered[4])
print(thePizza)
theTotalCostOfThePizza = pizzaCost(thePizzaIOrdered[1],thePizzaIOrdered[3],thePizzaIOrdered[4])
print(theTotalCostOfThePizza)
taxTotal=tax(7,theTotalCostOfThePizza)
tipTotal=tip(10,taxTotal)

print(taxTotal)
print(tipTotal)
'''

theOrder = []
thePizzas = []
ui = input("Welcome to Pizza the Hut, can I take your order? ")
while(ui != "no"):
    theOrder.append(orderpizza())
    ui = input("Do you want another Pizza?")
for i in range(len(theOrder)):
    thePizzas.append(makingThePizza(theOrder[i][0],theOrder[i][1],theOrder[i][2],theOrder[i][3],theOrder[i][4]))
#print(theOrder)
print(thePizzas)

totalCostOfPizzas=0
for i in range(len(theOrder)):
    totalCostOfPizzas += pizzaCost(theOrder[i][1],theOrder[i][3],theOrder[i][4])
print(totalCostOfPizzas)
taxTotal=tax(7,totalCostOfPizzas)
tipTotal=tip(10,taxTotal)
print('${:,.2f}'.format(taxTotal))
print('${:,.2f}'.format(tipTotal))



















#can you send me the git bash directions and visual studio code directions so that i can download them on my computer at home