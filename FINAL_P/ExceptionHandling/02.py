'''
Q2. File Reading with Exception Handling

Problem Statement:
Write a Python program that reads data from a file named data.txt.
Handle exceptions if the file doesn’t exist or cannot be read.

Sample Data (data.txt):

Python is fun to learn.


Expected Output (if file is missing):

Error: File not found.
'''

FO = open('data.txt', 'w')
FO.write('Python is fun to learn')
FO.close()

try:
  FO = open('dat.txt', 'r')
  data = FO.read()
  print(data)
except FileNotFoundError as FNFE:
  print(FNFE)
