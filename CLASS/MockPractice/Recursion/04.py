'''
Count Digits in a Number
Count how many digits a given integer has using recursion.
'''

def recursive_count(num):
  if num < 10:
    return 1
  return 1 + recursive_count(num//10)

print(recursive_count(0))