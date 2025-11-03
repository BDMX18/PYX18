'''
Function to Find Factorial

Input:

num = 5


Output:

Factorial of 5 = 120
'''

def factorial(num):
  fact = 1
  while num != 1:
    fact *= num
    num -= 1
  return fact

num = int(input('Enter A Number: '))
print('Factorial Of', num, 'Is', factorial(num))