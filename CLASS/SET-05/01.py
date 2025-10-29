'''
Problem:
Calculate the factorial of a given number n.

Example:

Input → 5

Output → 120
'''

n = int(input('Enter A Number: '))
fact = 1
for i in range(1, n+1):
  fact *= i
print(fact)
