'''
1. Cubes Generator

Write a Python program that creates a generator function that yields cubes of numbers from 1 to n. Accept n from the user.
'''

def cube_generator(n):
  for num in range(1, n+1):
    yield num**3

gen = cube_generator(5)
print(next(gen))
print(next(gen))
# for value in gen:
#   print(value)