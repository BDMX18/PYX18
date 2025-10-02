'''
Q3. Find Factorials using map and Recursion

Problem:
Write a Python program to calculate the factorial of each number in a list using functional programming. Use recursion for factorial calculation.

Sample Input:

nums = [3, 4, 5]


Expected Output:

[6, 24, 120]
'''


nums = [3, 4, 5]

def factorial(num):
  fact = 1
  for i in range(1, num+1):
    fact *= i
  return fact

result = list(map(factorial, nums))

print(result)