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
hex=(out[2:]) #get the first three char

for i in range(3):
     if(len(hex)%4==0):
          print(" ")
     else:
          hex = hex[:0] + "0" + hex[0:]

n=4
numlist=[]
for i in range(0,len(hex),n):
    numlist.append(hex[i:i+n])
print(numlist)
"""
HEXADEC        BINARY
  0             0000
  1             0001
  2             0010
  3             0011
  4             0100
  5             0101
  6             0110
  7             0111
  8             1000
  9             1001
  A             1010
  B             1011
  C             1100
  D             1101
  E             1110
  F             1111
"""
hexlist    = [ "0"  , "1"  , "2"  , "3"  , "4"  , "5"  , "6"  , "7"  , "8"  , "9"  , "A"  , "B"  , "C"  , "D"  , "E"  , "F"  ]
binarylist = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
for i in range(len(numlist)):
     numlist[i]=hexlist[binarylist.index(numlist[i])]

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data(numlist))