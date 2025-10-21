'''
Power of a Number
Implement a recursive function to calculate x^y without using the power operator.
'''

def recursive_exponent(num, power = 1):
  if power == 1:
    return num
  return num * recursive_exponent(num, power-1)

print(recursive_exponent(4, 3))