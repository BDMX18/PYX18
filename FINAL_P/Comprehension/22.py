'''
Q1. Enumerate + Conditioned Transformation

Problem:
Given a list of numbers, create a dictionary using dictionary comprehension and enumerate() where:

The key is the index

The value is square of the number if the index is even, otherwise cube

Sample Data:

nums = [2, 3, 4, 5, 6, 7]


Expected Output:

{0: 4, 1: 27, 2: 16, 3: 125, 4: 36, 5: 343}
'''

nums = [2, 3, 4, 5, 6, 7]

print({i:(num**2 if i%2==0 else num**3) for i, num in enumerate(nums)})