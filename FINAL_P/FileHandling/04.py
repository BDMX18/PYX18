'''
Q4. Read File Line by Line and Display Line Numbers

Problem Statement:
Write a Python program that reads a text file line by line and prints each line along with its line number.

Sample File (lines.txt):

Hello, World!
Welcome to Python Programming.
Let's master file handling.
'''

data = '''Hello, World!
Welcome to Python Programming.
Let's master file handling.'''


with open('q4.txt', 'w') as FO:
  FO.write(data)

with open('q4.txt', 'r') as FO:
    line_number = 1
    while True:
      line = FO.readline()
      if not line:
        break
      print(f'{line_number}. {line}', end='')
      line_number += 1
  
        
       

