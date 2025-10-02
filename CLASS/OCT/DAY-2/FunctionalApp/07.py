'''
Sum of Digits (Recursive + Functional)

Problem:
Write a program that takes a list of numbers and returns the sum of digits of each number using map and recursion.

Sample Input:

nums = [123, 456, 789]


Expected Output:

[6, 15, 24]
'''

nums = [123, 456, 789]

def sumOfDigits(num):
  sum = 0
  while num > 0:
    rem = num % 10
    sum += rem
    num //= 10
  return sum

def recursiveSum(num):
  if num == 0:
    return 0
  return num % 10 + recursiveSum(num//10)

result = list(map(recursiveSum, nums))

print(result)