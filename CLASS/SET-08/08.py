'''
Q8. File Copy Program

Write a Python program to copy content from one text file to another.

Sample Files:

source.txt → “Python is great.”

destination.txt → empty before running

Expected Output (destination.txt content):

Python is great.
'''

with open('source.txt', 'w') as FFO:
  ip_str = input('Enter A String: ')
  FFO.write(ip_str)

with open('source.txt', 'r') as FFO:
  data = FFO.read()

with open('destination.txt', 'w+') as SFO:
  SFO.write(data)
  SFO.seek(0)
  copy = SFO.read()
  print('Copy:', copy)

