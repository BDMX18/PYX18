'''
You are given an integer n. Print numbers from n to 1 without the help of loops.

Examples:

Input: n = 5
Output: 5 4 3 2 1
Explanation: We have to print numbers from 5 to 1.

Input: n = 10
Output: 10 9 8 7 6 5 4 3 2 1
Explanation: We have to print numbers from 10 to 1.
'''

def printNum(n):
  if n == 1:
    return 1
  print(n, end=' ')
  printNum(n-1)
printNum(10)