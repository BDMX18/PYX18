'''
Power of a Number
Compute a^b (a raised to the power of b) using recursion.
'''

def power(a, b):
  if(b == 0):
    return 1
  return (a * power(a, b-1))

print(power(4,3))
