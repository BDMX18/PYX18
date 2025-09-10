#4. Factorial Using Recursion: Write a Python program to get the factorial of a non-negative integer using recursion.

def factrial(num):
  if num == 0:
    return 1
  return num * factrial(num-1)

print(factrial(5))