'''
Q5. Dictionary Key Lookup

Problem Statement:
Write a Python program to get a value from a dictionary using a key entered by the user.
Handle the exception if the key doesn’t exist.

Sample Data:

students = {'101': 'Alice', '102': 'Bob', '103': 'Charlie'}


Sample Input:

Enter student ID: 105


Expected Output:

Error: Key not found.
'''

students = {'101': 'Alice', '102': 'Bob', '103': 'Charlie'}

try:
  id = int(input('Enter Student ID: '))
  if id in students:
    print(students[id])
except KeyError as KE:
  print(KE)