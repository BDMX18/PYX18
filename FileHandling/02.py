'''
Write a Python program to read the contents of a file and display them line by line.
'''

with open('first.txt', 'r') as FO:
  PO = FO.read()
  print(PO)