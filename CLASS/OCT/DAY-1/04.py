'''
Question: Functional List Transformation

Write a function process_numbers(numbers) that:

Takes a list of integers numbers.

Uses functional programming tools (map, filter, reduce from functools, and/or lambda).

Performs these operations in order:

Filters out all even numbers.

Squares each remaining number.

Calculates and returns the sum of these squared numbers.
'''

from functools import reduce

def process_numbers(numbers):
  filtered_list = list(filter(lambda num: num%2!=0, numbers))
  squared_list = list(map(lambda num: num*num, filtered_list))
  sum_list = reduce(lambda num1, num2: num1+num2, squared_list)
  return sum_list

length = int(input('Enter the number of digits you want to enter: '))
numbers = [int(input(f'Enter number {i+1}: ')) for i in range(length)]

print(process_numbers(numbers))