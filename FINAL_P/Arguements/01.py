'''
Sum of Variable-Length Numbers

Write a Python function sum_numbers() that accepts any number of numeric arguments and returns their total sum using *args.

Sample Data:

sum_numbers(10, 20, 30)
sum_numbers(5, 15, 25, 35, 45)
'''

def sum_numbers(*args):
  sum = 0
  for num in args:
    sum += num
  return sum

print(sum_numbers(10, 20, 30))
print(sum_numbers(5, 15, 25, 35, 45))