#Write a Python program to construct the following pattern, using a nested for loop.
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

#Write a python prograam to construct the following pattern
print("---------------------")
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")


#mario
rows = 8
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("# ", end="")
    print("")



#while lOOOOps
height=5    #num of rows
i=0 #the purpose of i is to iterate through the loop
while i<height: #run until we reach the height needed
    x=height-1  #helps print the num of spaces
    a=0         #helps print the num of #
    while x>=i: #prints the spaces
        print(" ",end="")
        x-=1    #with while loops you tell the loop to iterate
    while a<=i: #print the #
        print("#",end="")
        a+=1    #helps increment the while loop
    print("")   #moves to the new line
    i+=1        #iterates the entire while loop