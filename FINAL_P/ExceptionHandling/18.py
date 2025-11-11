'''
Q1. File Reading with Exception Handling

Write a program to read the contents of a file.
Handle the following exceptions:

FileNotFoundError (if file doesn’t exist)

PermissionError (if file cannot be accessed)

Sample Data:
Try with filenames:

"data.txt" (existing)

"missing.txt" (non-existent)
'''

file_name = input('Enter the name of the file that you want to read: ')
try:
  FO = open(file_name, 'r')
  data = FO.read()
  print(data)
except FileNotFoundError as error:
  print(error)
except PermissionError as error:
  print(error)