# Sum of Digits of an Integer Using Recursion Write a Python program to get the sum of a non-negative integer using recursion.

def sumOfDigits(num):
  if num == 0:
    return 0
  return num%10 + sumOfDigits(num//10)

num = int(input('Enter A Number: '))
print(sumOfDigits(num))