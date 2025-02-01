import random

fname = input("What is your first name? ")
lname = input("What is your last name? ")
email = input("What is your EVSC email? ")
password = input("And what is the password? ")

if ((fname in email) and (lname in email) and ("OpenS3@same" == password)):
    print("Welcome Home Sir")
else:
    print("HaHa Poor...Try again")

s1 = input("string1 ")
s2 = input ("string2 ")
#   [Start:End:Step]
s3 = s1[0:round(len(s2)/2)]+s2+s1[round(len(s2)/2):]

print (s3)

#0  -0 -0 -0 -0-0-0-0
#128-64-32-16-8-4-2-1
#             0 1 1 1
#             0+4+2+1 = 7
total=0         #instantiate the total variable
b=input("enter binary digits from 0000 to 1111 ")
if  b[0]=="1":
    total+=8
if b[1]=="1":
    total+=4
if b[2]=="1":
    total+=2
if b[3]=="1":
    total+=1
print(total)


print("""
        A        B       Middle Point
     (0, 0)   (2, 1)     {}
     (1, 4)   (4, 2)     (2.5, 3.0)
     (2, 7)   (6, 3)     (4.0, 5.0)
     (3, 9)   (10, 5)    (6.5, 7.0)
     (4, 11)  (12, 7)    (8.0, 9.0)
""".format("(1.0, 0.5)"))
#\n makes a new line

licensePlate=""
licensePlate+=chr(random.randint(65,90))        #DRY = Doesn't Repeat Yourself
licensePlate+=chr(random.randint(65,90))        #WET = no no no no no no no no
licensePlate+=chr(random.randint(65,90))
licensePlate+=str(random.randint(1000,9999))
#print(licensePlate)


#for each number in a range from 0 to 3:
for i in range(3):      #range(start,stop,step)
    licensePlate+=chr(random.randint(65,90))
for i in range(4):
    licensePlate+=str(random.randint(0,9))
print(licensePlate)
''''''