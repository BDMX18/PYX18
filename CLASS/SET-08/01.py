'''
Q1. Word Frequency Counter (File Handling)

Write a Python program to read a text file and count how many times each word appears.

Sample Data (file: data.txt):

Python is fun and Python is powerful


Expected Output:

{'Python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}
'''

with open('one.txt', 'w+') as FO:
  ip_str = input('Enter A String To Add To The File: ')
  FO.write(ip_str)
  print(FO.tell())
  FO.seek(0)
  data = FO.read()
  data_list = data.split()
  occurance_dict = {}
  for word in data_list:
    if word not in occurance_dict:
      occurance_dict[word] = 1
    else:
      occurance_dict[word] += 1
  print(occurance_dict)

