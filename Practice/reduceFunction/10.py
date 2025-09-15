'''
10. Combine Numbers into a Single Integer

Question: Use reduce() to combine digits into a single integer.

Sample Data:
[1, 2, 3, 4]
Expected Output: 1234
'''

from functools import reduce as r
print(r(lambda a,b: int(str(a)+str(b)), [1, 2, 3, 4]))