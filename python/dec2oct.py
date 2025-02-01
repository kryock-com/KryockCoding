# 1 byte = 8 bits = 256 unique integers = highest value is 255

decimal = int(input("Give me a whole number: "))
checkList=[]

#this while loop generates the list to calculate the bin string
i=0
while decimal>=2**i:
     #insert will allow you to put where you want (location,value)
     checkList.insert(0,2**i)
     i+=1

#this loop calculates the bin string or converts int to binary
for i in range(len(checkList)):
     #if the 2**checkList[i] is less than or equal to our integer
     if decimal >= checkList[i]:
          decimal-=checkList[i]
          checkList[i]="1"
     else:
          checkList[i]="0"


#out put string
out="0b"
for b in checkList:
     out+=b
octal=(out[2:]) #get the first three char

for i in range(2):
     if(len(octal)%3==0):
          print(" ")
     else:
          octal = octal[:0] + "0" + octal[0:]

n=3
numlist=[]
for i in range(0,len(octal),n):
    numlist.append(octal[i:i+n])

"""
OCTAL          BINARY
  0             000
  1             001
  2             010
  3             011
  4             100
  5             101
  6             110
  7             111
"""
octallist =  [ "0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" ]
binarylist = ["000","001","010","011","100","101","110","111"]
for i in range(len(numlist)):
     numlist[i]=octallist[binarylist.index(numlist[i])]

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data(numlist))

