import random
import string
import secrets

length = 7

digits = "1234567890"

lowLetters = "abcdefghijklmnopqrstuvwxyz"

upLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
symbols = "!@#$%^&*()"

password = ''.join(secrets.choice(digits + upLetter + symbols + lowLetters) for t in range(20))
def message():
    print("Hello, here is a password generator. ")
    print("Choose the length of your characters:")
    passGen()

def passGen():
    c = 0
    upper = int(input("How many capitalized letters you want? "))
    lower = int(input("How many lower cased letters you want? "))
    spec = int(input("How many symbols you want? "))
    num = int(input("How many numbers you want? "))
    c += upper + num + spec + lower
    if c < length:
        print('Your password is too short.')
        passGen()
    else:
        newPassword = ""
        for i in range(upper):
            newPassword += random.choice(upLetter)
        for x in range(spec):
            newPassword += random.choice(symbols)
        for y in range(num):
            newPassword += random.choice(digits)
        for z in range(lower):
            newPassword += random.choice(lowLetters)

        passWord = list(newPassword)
        shuff = random.shuffle(passWord)
        newPass = "".join(passWord)
        password = secrets.token_urlsafe(7)
        print(newPass)

message()