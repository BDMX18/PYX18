'''
Filter Only Integers

Problem: Implement filter_ints(**kwargs) → return dict of only int values.

Input: filter_ints(a=10, b="hello", c=20)

Output: {'a':10, 'c':20}
'''

def filter_ints(**kwargs):
  result = {k: v for k, v in kwargs.items() if isinstance(v, int)}
  return result



print(filter_ints(a=10, b='hello', c=20))