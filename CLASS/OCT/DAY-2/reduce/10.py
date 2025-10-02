'''
Q10. Running Cumulative Sum

Problem:
Use reduce to compute the running cumulative sum of a list.
(Note: Return a list, not just the final sum.)

Sample Input:

nums = [1, 2, 3, 4]


Expected Output:

[1, 3, 6, 10]
'''

nums = [1, 2, 3, 4]

from functools import reduce

def sumList(acc, num):
  if acc == []:
    acc.append(num)
  else:
    acc.append(acc[-1]+num)
  return acc

result = reduce(sumList, nums, [])
print(result)

result = reduce(lambda acc, num: (acc.append(num if not acc else acc[-1]+num)) or acc, nums, [])
print(result)