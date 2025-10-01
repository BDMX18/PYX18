'''
Write a Python program that:

Takes a list of temperatures in Fahrenheit as input from the user (you can ask how many temperatures they want to enter).

Converts all temperatures to Celsius using a functional approach.

Filters out all temperatures below freezing point (0°C).

Returns the list of remaining temperatures rounded to 2 decimal places.

Requirements:

Use functional tools like map(), filter(), and lambda.

No explicit loops for processing (you can use loops for input collection).

Use function composition or chaining if you want.

Formula to convert Fahrenheit to Celsius:
'''


def temperatureConverter(num):
  temp_list = []
  for i in range(num):
    temp = int(input(f'Enter Tempreature {i+1} (*F): '))
    temp_list.append(temp)
  
  # Convert To Celcius: 
  celcius_list = list(map(lambda temp: (temp-32)*5/9, temp_list))

  # Filter Temperature Above Freezing (0*C)
  filter_temp = list(filter(lambda temp: temp > 0, celcius_list))

  # Round To 2 Decimal Places
  output_list = list(map(lambda temp: round(temp, 2), filter_temp))

  print(output_list)

num = int(input('Enter Number Of Tempreature: '))
temperatureConverter(num)