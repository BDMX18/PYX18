'''
Q7. Remove Blank Lines from a File

Problem Statement:
Write a Python program that removes all blank lines from a given text file and writes the cleaned content to a new file.

Sample File (paragraph.txt):

Python is great.

It supports multiple programming paradigms.

File handling is simple in Python.
'''

data = '''Python is great.

It supports multiple programming paradigms.

File handling is simple in Python.'''

with open('paragraph.txt', 'w') as FO:
  FO.write(data)

with open('paragraph.txt', 'r') as FO:
  file_data = FO.readlines()

with open('paragraph_new.txt', 'w') as FO:
  for line in file_data:
    if line.strip():
      FO.write(line)
