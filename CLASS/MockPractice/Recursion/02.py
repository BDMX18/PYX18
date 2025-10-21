'''
Sum of Digits
Recursively find the sum of digits of a given number.
'''

def recursive_sum(num):
  if num == 0:
    return 0
  return num%10 + recursive_sum(num//10)

print(recursive_sum(123))