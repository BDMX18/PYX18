# Write a Python program to create a new text file and write multiple lines of input taken from the user.

num = int(input('Enter The Number Of Lines You Want To Add To The File: '))
file_L = []
for i in range(num):
  str = input('Enter The Data: ')
  file_L.append(str + '\n')

with open('first.txt', 'w') as file:
  PO = file_L
  file.writelines(PO)
  print(PO)