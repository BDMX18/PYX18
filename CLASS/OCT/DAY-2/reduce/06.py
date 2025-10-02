'''
Sum of Digits of All Numbers

Problem:
Write a program that takes a list of numbers and uses reduce to compute the sum of all digits in all numbers.

Sample Input:

nums = [123, 45, 67]


Expected Output:

1+2+3+4+5+6+7 = 28
'''

from functools import reduce
nums = [123, 45, 67]

def sumDigits(acc, num):
  while num > 0:
    acc += num % 10
    num //= 10
  return acc

print(reduce(sumDigits, nums, 0))

# Using lambda function

result = reduce(lambda acc, num: acc + sum(map(int, str(num))), nums, 0)
print(result)