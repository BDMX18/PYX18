'''
Average with Optional Rounding

Problem: Implement average(*nums, round_to=2) that returns mean rounded.

Input: average(10, 20, 30, round_to=1)

Output: 20.0
'''

from functools import reduce

def average(*nums, round_to = 2):
  result = reduce(lambda a, b: a+b, nums)
  average = result/len(nums)
  round_result = round(average, round_to)
  return round_result

print(average(10, 20, 30, round_to=1))