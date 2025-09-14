'''
Sum of Digits of a Number

Compute the sum of all digits in a number, e.g., 123 → 1 + 2 + 3 = 6.
'''

def sumOfNum(num):
  if num < 10:
    return num
  return num%10 + sumOfNum(num//10)
print(sumOfNum(1234))