'''
Print 1 to n using Recursion

Input: n = 3
Output: [1 2 3 ]
Explanation: We have to print numbers from 1 to 3.

Input: n = 10
Output: [1 2 3 4 5 6 7 8 9 10]
Explanation: We have to print numbers from 1 to 10 .
'''

def printNum(n):
  if n == 0:
    return 0
  printNum(n-1)
  print(n, end=' ')
printNum(10)
