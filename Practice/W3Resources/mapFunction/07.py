'''
7. List Addition and Difference Map
Write a Python program to add two given lists and find the difference between them. Use the map() function.

Original lists:
[6, 5, 3, 9]
[0, 1, 7, 7]

Result:
[(6, 6), (6, 4), (10, -4), (16, 2)]
'''

def sumDiff(a, b):
  return a+b, a-b

print(list(map(sumDiff, [6, 5, 3, 9], [0, 1, 7, 7])))