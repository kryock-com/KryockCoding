import datetime as date
print("welcome to the guessing how old you are")


year = int(input("First Im going to ask you for the year you were born. "))
month = int(input("Then the month. "))
day = int(input("Then finally the day. "))


howOld = date.datetime.now().year - year - ((date.datetime.now().month, date.datetime.now().day) < (month, day))

print("You were born on the",day,"of the",month,"in the year",year,)
print("You are",howOld,"years old")





