'''
Calculate power of a number:
Write a program to calculate 3 to the power of 4
Input: Base = 3, Exponent = 4
Expected Output = 81
'''

base = int(input('Enter The Base: '))
exp = int(input('Enter The Exponent: '))
count = 0
power = 1
while count < exp:
  power *= base
  count += 1
print(power)