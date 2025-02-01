
userOwe = input("What is the change owed: ")

owe = float(userOwe)

print ("Change owed : " + str(owe))

#Quarters
Quarter = int(owe/.25)
print("Quarters : " + str(Quarter))
owe = round(owe%0.25,2)
print(owe)

#Dimes
Dime = int(owe/.10)
print("Dimes : " + str(Dime))
owe = round(owe%0.10,2)
print(owe)

#Nickels
Nickel = int(owe/.05)  
print("Nickels : " + str(Nickel))
owe = round(owe%0.05,2)
print(owe)

#Pennies
Pennie = int(owe/.01)
print("Pennies : " + str(Pennie))
owe = round(owe%0.01,2)
print(owe)
