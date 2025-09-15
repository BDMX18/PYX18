'''
6. Compute Factorial

Question: Use reduce() to compute the factorial of a number (e.g., 5!).

Sample Data:
Number: 5
Equivalent list: [1, 2, 3, 4, 5]
Expected Output: 120
'''

from functools import reduce as r

n = int(input('Enter A Number: '))
list = list()
for num in range(1, n+1):
  list.append(num)
print(r(lambda a,b: a*b, list))