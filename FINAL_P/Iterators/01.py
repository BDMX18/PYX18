'''
Q1. Create a Custom Iterator for Even Numbers

Problem Statement:
Write a Python class called EvenIterator that takes a list of integers and iterates only over the even numbers using the iterator protocol.
Implement the __iter__() and __next__() methods properly.

Sample Data:

numbers = [3, 6, 8, 11, 14, 17, 20]


Expected Behavior:
When you iterate using this class, it should yield: 6, 8, 14, 20
'''

# class EvenIterator:

#   def __init__(self, numbers):
#     self.numbers = numbers
#     self.index = 0
  
#   def __iter__(self):
#     return self
  
#   def __next__(self):
#     while self.index <= len(self.numbers):
#       num = self.numbers[self.index]
#       self.index += 1
#       if num % 2 == 0:
#         return num
#     raise StopIteration

numbers = [1,5,3,2,4,5,6,88,9,12,14,44]

# EIO = EvenIterator(numbers)

# for value in EIO:
#   print(value)


def evenGenerator(num_list):
  for num in num_list:
    if num % 2 == 0:
      yield num

EG = evenGenerator(numbers)

print(next(EG))
print(next(EG))
print(next(EG))
print(next(EG))