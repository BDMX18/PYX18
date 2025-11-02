'''
Create and Write to File

Question:
Write a Python program to create a new text file called sample1.txt and write the following lines into it.

Sample Data (to write):

Python is fun.
File handling makes automation easy.
Practice makes perfect.
'''

with open('sample1.txt', 'w') as FO:
  FO.writelines('''Python is fun. \nFile handling makes automation easy. \nPractice makes perfect.''')

