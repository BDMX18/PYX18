# 1. Sum of List Using Recursion: Write a Python program to calculate the sum of a list of numbers using recursion.

def sumOfListElements(num_list):
  if len(num_list) == 0:
    return 0
  return sumOfListElements(num_list[1:]) + num_list[0]

print(sumOfListElements([1, 2, 3]))