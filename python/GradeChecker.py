grade=int(input("what grade did you get (%)-"))
if grade > 100:
  print('Input A Valid number, 0-100')
elif (grade >= 90) and (grade <= 100):
  print('A')
elif (grade >= 80) and (grade <= 89):
  print('B')
elif (grade >= 70) and (grade <= 79):
  print('C')
elif (grade >= 60) and (grade <= 69):
  print('D')
elif (grade >= 0) and (grade <= 59):
  print('F')
