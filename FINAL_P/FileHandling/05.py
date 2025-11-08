'''
Q5. Write Even and Odd Numbers into Separate Files

Problem Statement:
Given a file containing numbers (one per line), write a Python program that separates even and odd numbers into two new files: even.txt and odd.txt.

Sample File (numbers.txt):

12
45
78
23
56
89
90
'''

data = '''
12
45
78
23
56
89
90
'''

with open('numbers.txt', 'w') as FO:
  FO.write(data)

with open('numbers.txt', 'r') as FO:
  data = FO.read()
  str_num_list = data.split()
  num_list = []
  for num in str_num_list:
    num_list.append(int(num))

with open('even.txt', 'w') as FO:
  for num in num_list:
    if num % 2 == 0:
      FO.write(str(num)+'\n')

with open('odd.txt', 'w') as FO:
  for num in num_list:
    if num % 2 != 0:
      FO.writelines(str(num)+'\n')
      