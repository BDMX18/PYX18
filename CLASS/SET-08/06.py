'''
Q6. Calculate Factorials Using Lambda and Map

Use lambda and map() to calculate factorials of numbers in a list.

Sample Data:

nums = [3, 5, 6]


Expected Output:

[6, 120, 720]
'''

from functools import reduce as r

nums = [3,5,6]

factorial = list(map(lambda x: r(lambda a, b: a*b, range(1, x+1)), nums))

print(factorial)