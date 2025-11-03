'''
Find Maximum and Minimum in a List

Input:

numbers = [12, 45, 7, 89, 34, 22]


Output:

Maximum: 89  
Minimum: 7
'''

numbers = [12, 45, 7, 89, 34, 22]

max = min = numbers[0]

for number in numbers:
  if number < min:
    min = number
  elif number >  max:
    max = number
print('Maximum Number:', max, 'Minimum Number:', min)