'''
2. Temperature Converter

Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

Expected Output :

60°C is 140 in Fahrenheit
45°F is 7 in Celsius
'''

choice = int(input('1.Celsius to Fahrenheit \n2.Fahrenheit to Celsius \n Enter Your Choice: '))
temp = float(input('Enter Tempreature: '))
if (choice == 1):
  print(f'Tempreature in Fahrenheit: {(9/5*temp)+32} F')
elif(choice == 2):
  print(f'Tempreature in Celsius: {round((temp-32)*5/9)} C')
else:
  print('Enter Valid Choice!')