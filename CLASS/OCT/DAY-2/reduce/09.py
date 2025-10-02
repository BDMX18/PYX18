'''
Find the Most Frequent Element

Problem:
Given a list of elements, use reduce to find the element that appears the most times.
(Hint: You may need collections.Counter with reduce.)

Sample Input:

nums = [1, 3, 2, 1, 4, 1, 3, 3, 3]


Expected Output:

3
'''

from functools import reduce as r

nums = [1, 3, 2, 1, 4, 1, 3, 3, 3]

def count(c_dict, num):
  init = 1
  if num in c_dict:
    c_dict[num] = c_dict.get(num, 0) + 1
  else:
    c_dict[num] = init
  return c_dict

result = r(count, nums, {})
print(max(result.values()))

res = r(lambda acc, num : (acc.update({num: acc.get(num, 0)+1})) or acc, nums, {})
max_occ = max(res.values())
print(max_occ)

