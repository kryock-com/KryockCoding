question=input("What do you want to convert to Celsius or Fahrenheit? ")
if question == ("celsius"):
  celsius = float(input("Enter temperature in celsius: "))
  fahrenheit = (celsius * 9/5) + 32
  print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
elif question == ("fahrenheit"):
  fahrenheit = float(input("Enter temperature in fahrenheit: "))
  celsius = (fahrenheit - 32) * 5/9
  print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))