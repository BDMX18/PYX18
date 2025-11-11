'''
Q1. Prime Number Checker

Write a program that checks whether a given number is prime using a for-else loop.
If the number has no divisors, print “Prime Number”, else print “Not Prime”.

Sample Input:

num = 29


Expected Output:

29 is a Prime Number
'''

# num = int(input('Enter A Number: '))
# if num > 1:
#   for div in range(2, num//2+1):
#     if num % div == 0:
#       print(num, 'is not a Prime Number')
#       break
#   else:
#     print(num, 'is a Prime Number')
# else:
#   print(num, 'is not a Prime Number')

num = int(input('Enter A Number: '))
if num > 1:
  div = 2
  while div <= num//2+1:
    if num % div == 0:
      print(num, 'is not a Prime Number')
      break
    div += 1
  else:
    print(num, 'is a Prime Number')
else:
  print(num, 'is not a Prime Number')
