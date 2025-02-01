'''#making sure the world is list is in it
numbersList = [] 
total = 0
user=eval(input("Please enter a number "))
while(user!="q"):
    numbersList.append(user)
    total+=user
    #iterator to stop infinite loop
    user=eval(input("Please enter a number "))


print("Sum: {}".format(total)) 
print("Ave: {}".format(total/len(numbersList)))
print("# of inputs: {}".format(len(numbersList)))
for i in numbersList:
    print (i) 
'''

numbersList = [] 
total = 0

print("Enter numbers to add to the list. Type 'q' to quit.")

while True:
    user_input = input("Please enter a number (or 'q' to quit): ")
    if user_input.lower() == "q":
        break
    try:
        user = int(user_input)
        numbersList.append(user)
        total += user
    except ValueError:
        print("Invalid input. Please enter a valid number or 'q' to quit.")

if numbersList:
    print("\nSummary:")
    print(f"Sum: {total}")
    print(f"Average: {total / len(numbersList):.2f}")
    print(f"Number of inputs: {len(numbersList)}")
    print("Numbers entered:", ", ".join(map(str, numbersList)))
else:
    print("No numbers were entered.")