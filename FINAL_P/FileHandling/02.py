'''
Q2. Copy Contents from One File to Another

Problem Statement:
Write a program to copy all contents from one text file to another file.
Make sure that the destination file is newly created and existing content (if any) is not overwritten accidentally.

Sample File (source.txt):

Learning Python is fun.
Practice makes perfect.
'''

with open('q2_1.txt', 'w+') as FO_1:
  FO_1.write('''Learning Python is fun.
Practice makes perfect.''')
  FO_1.seek(0)
  data = FO_1.read()

with open('q2_2.txt', 'w+') as FO_2:
  FO_2.write(data)
  FO_2.seek(0)
  data = FO_2.read()
  print(data)

