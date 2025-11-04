'''
Find the Maximum and Minimum

Write a function find_extremes() that accepts a variable number of integers using *args and prints both the maximum and minimum numbers.

Sample Data:

find_extremes(11, 4, 7, 9, 12, 2)
find_extremes(100, 50, 200, 10)
'''

def find_extremes(*args):
  max = min = args[0]
  for num in args:
    if num > max:
      max = num
    elif num < min:
      min = num
  result = f'Maximun: {max}, Minimum: {min}'
  return result

print(find_extremes(11, 4, 7, 9, 12, 2))
print(find_extremes(100, 50, 200, 10))