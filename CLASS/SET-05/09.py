'''
Find the GCD (Greatest Common Divisor) of two numbers

Problem:
Find the greatest common divisor using loops (without math.gcd).

Example:

Input → a = 12, b = 18

Output → 6
'''

a = int(input())
b = int(input())
while b != 0:
  a, b = b, a % b
print(a)