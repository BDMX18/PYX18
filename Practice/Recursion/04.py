'''
Fibonacci Sequence
Write a recursive function to return the nth Fibonacci number.
Input: 6 → Output: 8
'''

def fibonacci(count):
  if(count <= 0):
    return 0
  elif(count == 1):
    return 1
  return fibonacci(count-1) + fibonacci(count-2)
print(fibonacci(50))

# count = int(input('Count: '))
# first = int(input('Enter First Element: '))
# second = int(input('Enter Second Element: '))
# if count == 1:
#   print(first)
# elif count == 2:
#   print(second)
# else:
#   print(first, second, end=' ')
#   for i in range(count-2):
#     sum = first + second
#     print(sum, end=' ')
#     first, second = sum, first
  