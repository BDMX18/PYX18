'''
Replace Word in File:
Write a Python program to replace a specific word in a text file with another word.
'''

with open('text1.txt', 'w') as FO:
  FO.writelines('Python is easy to learn.\nPython is powerful.')

with open('text1.txt', 'r') as FO:
  data = FO.read()

new_data = data.replace('Python', 'Java')

with open('text1.txt', 'w') as FO:
  FO.writelines(new_data)



