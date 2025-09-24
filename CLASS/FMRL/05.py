'''
6. filter() Interview Question

Q: Given a list of numbers, filter out all numbers that are perfect squares.

'''

def perfectSquare(num):
  i = 1
  while i*i <= num:
    if i*i == num:
      return True
    i += 1
  return False

print(list(filter(perfectSquare, [1, 2, 4, 5, 9, 10, 16, 20, 25, 30])))