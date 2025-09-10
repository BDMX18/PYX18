# 5. Fibonacci Sequence Using Recursion: Write a Python program to solve the Fibonacci sequence using recursion.

def fibonacci(count):
  if count == 1 or count == 2:
    return 1
  return fibonacci(count-1) + fibonacci(count-2)

count = int(input('Enter The Count: '))
print(fibonacci(count))


'''
first = int(input('Enter The First Number: '))
second = int(input('Enter The Second Number: '))
count = int(input('Enter The Count: '))
if(count == 1):
  print(first)
elif(count == 2):
  print(first, second)
else:
  print(first, '\n',second)
  for num in range(count-2):
    first, second = second, first+second
    print(second)
'''
